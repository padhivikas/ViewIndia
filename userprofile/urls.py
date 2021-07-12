from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home.as_view()),
    path('edit/<int:pk>',views.ProfileUpdate.as_view(success_url="/profile")),
    
]
