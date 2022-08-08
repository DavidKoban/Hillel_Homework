from django.urls import path, include
from test_task.views import Order_View


urlpatterns = [
    path('', Order_View.as_view(),),
]
