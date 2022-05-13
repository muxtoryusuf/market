from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = (
    # create user
    path('list', views.TradePointListView.as_view(), name="list"),
    path('visit/<int:pk>', views.TradePointCreateView.as_view(), name="list"),
)
