from rest_framework import generics
from rest_framework.response import Response
from .paginations import CustomPagination


class RequestController:

    def __init__(self, request=None):
        self.request = request

    def get_language(self):
        """
        Public method
        @return: request headers language
        """
        return self.__check_language()

    def __check_language(self):
        """Private method"""
        header = self.request.headers
        if 'Accept-Language' in header:
            lang = header['Accept-Language'][:2]
        else:
            lang = 'ru'
        return lang


class ResponseController(RequestController):
    code = 0
    success_message: dict = {"en": "OK", "ru": "ОК"}
    error_message: dict = {"en": "", "ru": ""}
    error_text: dict = {"en": "", "ru": ""}
    exception: tuple = ""

    def success_response(self, *args, **kwargs):
        lang = self.get_language()
        msg_by_language = self.success_message.get(lang)
        response = {'success': True, 'code': self.code, 'message': msg_by_language}
        if kwargs:
            response.update({key: kwargs[key] for key in kwargs})
        return Response(response)

    def error_response(self):
        lang = self.get_language()
        error_by_language = self.error_text.get(lang)
        try:
            message_by_language = self.error_message.get(lang) % error_by_language
        except TypeError:
            message_by_language = self.error_message.get(lang)
        response = {'success': False, 'code': self.code, 'message': message_by_language}
        if self.exception:
            response['debug'] = self.exception
        return Response(response)


class CustomApiView(ResponseController, generics.GenericAPIView):
    pass


class CustomRetrieveView(ResponseController, generics.RetrieveAPIView):
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            return self.success_response(result=serializer.data)
        except Exception as e:
            self.code = CustomResponse.CODE_4
            self.error_message = CustomResponse.MSG_4
            self.exception = e.args
            return self.error_response()


class CustomListView(ResponseController, generics.ListAPIView, CustomPagination):
    error_text = {"en": "Trade point", "ru": "Торговая точка"}

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        if qs:
            result = self.paginated_queryset(qs, request)
            serializer = self.serializer_class(result, many=True)
            response = self.paginated_response(data=serializer.data)
            return Response(response)
        else:
            self.code = CustomResponse.CODE_4
            self.error_message = CustomResponse.MSG_4
            return self.error_response()


class CustomResponse:

    CODE_0 = 0
    MSG_0 = {"en": "OK", "ru": "ОК"}

    CODE_3 = 3
    MSG_3 = {"en": "invalid data", "ru": "неверные данные"}

    CODE_4 = 4
    MSG_4 = {"en": "%s not found!", "ru": "%s не найден!"}

    CODE_6 = 6
    MSG_6 = {"en": "%s invalid value(s)", "ru": "%s недопустимый формат значения"}
