from django.urls import path
from .views import FrutasView, FrutasCambios

urlpatterns = [
    path('', FrutasView.as_view()),
    path('/<int:pk>', FrutasCambios.as_view())
]