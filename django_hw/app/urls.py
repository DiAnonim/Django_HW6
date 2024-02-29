from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('worker/<int:worker_id>/', worker, name='worker'),
    path('update/<int:worker_id>/', update, name='update'),
    path('delete/<int:worker_id>/', delete, name='delete'),
]
