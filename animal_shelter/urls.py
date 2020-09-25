from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import AnimalViewSet


app_name = "animals"

urlpatterns = [path('', views.animals_list_view, name='animals_list'),
               path('<int:pk>/', views.animal_detail_view, name='animal_detail'),
               path('new/', views.new_animal_view, name='new_animal'), ]

router = DefaultRouter()
router.register(r'api', AnimalViewSet, basename='api')
urlpatterns += router.urls
