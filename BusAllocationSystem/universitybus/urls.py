from django.urls import path
from .views import BusView, BusViewRUD

urlpatterns = [
    path('bus/', BusView.as_view()),
    path('bus/<int:pk>/', BusViewRUD.as_view())
]