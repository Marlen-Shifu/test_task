from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *

router = DefaultRouter()


urlpatterns = [
    path('', workers),
    path('db-setup/', db_setup),
    path('list/', WorkerViewSet.as_view()),
    path('create/', WorkerCreateView.as_view()),
    path('update/<int:pk>/', WorkerUpdateView.as_view()),
    path('retrieve/<int:pk>/', WorkerRetrieveView.as_view()),
    path('destroy/<int:pk>/', WorkerDestroyView.as_view()),
    path('auth/', LoginPage.as_view()),
]

urlpatterns += router.urls