from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Blog , Contact
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from .serializer import BlogSerializer , UserSerializer , ContactSerializer
from .pagination import BlogPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

class Home(ListView):
    model = Blog
    def get_queryset(self):
        if ( Blog.objects.filter(status = 'publish') ):
            return Blog.objects.filter(status = 'publish')

class MyBlog(ListView):
    model = Blog
    def get_queryset(self):
        if ( Blog.objects.filter(user = self.request.user) ):
            return Blog.objects.filter(user = self.request.user)
            

class BlogDetail(DetailView):
    model=Blog
    def get_queryset(self):
        if self.request.user.is_authenticated:
            previouspath = self.request.META.get('HTTP_REFERER')
            if previouspath == 'http://localhost:8000/blog/myblog/':
                return Blog.objects.filter(user = self.request.user)
            else:
                return Blog.objects.filter(status = 'publish')
        else:
            return Blog.objects.filter(status = 'publish')



@method_decorator(login_required, name="dispatch")
class CreateBlog(CreateView):
    model = Blog
    fields = ["title", "content","status","img"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class UpdateBlog(UpdateView):
    model = Blog
    fields = ["title", "content","status","img"]
    def get_queryset(self):
        if ( Blog.objects.filter(user = self.request.user) ):
            return Blog.objects.filter(user = self.request.user)
     


class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    http_method_names = ['get']

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post', 'head']

