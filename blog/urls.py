from django.urls import path , include
from . import views



urlpatterns = [
    path('',views.Home.as_view()),
    path('myblog/',views.MyBlog.as_view()),
    path('addblog/',views.CreateBlog.as_view(success_url="/blog")),
    path('editblog/<int:pk>',views.UpdateBlog.as_view(success_url="/blog")),
    path('<int:pk>', views.BlogDetail.as_view()),
]
