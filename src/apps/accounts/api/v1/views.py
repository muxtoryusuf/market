from rest_framework import permissions
from apps.accounts.models import TradePoint
from apps.core.services import CustomResponse, CustomApiView, CustomListView
from .serializers import TradePointSerializer, VisitCreateSerializer


class TradePointListView(CustomListView):
    """
     GET: http://127.0.0.1:3333/api/market/v1/list?phone=+78001234567
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = TradePointSerializer

    def get_queryset(self):
        query_params = self.request.query_params.get('phone', None)
        if query_params:
            qs = TradePoint.objects.filter(user__phone_number=query_params)
            if not qs.exists():
                phone = f"+{query_params.replace(' ', '')}"
                qs = TradePoint.objects.filter(user__phone_number=phone)
            return qs
        else:
            return None


class TradePointCreateView(CustomApiView):
    """
    GET: http://127.0.0.1:3333/api/market/v1/list?phone=+78001234567
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = VisitCreateSerializer
    schema = None

    def post(self, request, pk):
        data = request.data
        try:
            market = TradePoint.objects.get(id=pk)
            data["market"] = market.id
            serializer = VisitCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = {"pk": serializer.instance.id, "date": serializer.instance.created_at}
                return self.success_response(results=data)
        except Exception as e:
            self.code = CustomResponse.CODE_3
            self.error_message = CustomResponse.MSG_3
            self.exception = e.args
            return self.error_response()
