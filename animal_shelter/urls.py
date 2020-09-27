from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import AnimalViewSetReadOnly, MyModelViewSet

app_name = "animals"

urlpatterns = [path('', views.animals_list_view, name='animals_list'),
               path('<int:pk>/', views.animal_detail_view, name='animal_detail'),
               path('new/', views.new_animal_view, name='new_animal'),
               path('<int:pk>/edit/', views.edit_animal_view, name='edit_animal'),
               ]
router = DefaultRouter()
router.register(r'api', AnimalViewSetReadOnly)
router.register(r'detail', MyModelViewSet)
urlpatterns += router.urls
