from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Profile

@method_decorator(login_required, name="dispatch")
class home(ListView):
    model = Profile
    def get_queryset(self):
        return Profile.objects.filter(id = self.request.user.profile.id)


@method_decorator(login_required, name="dispatch")    
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ["phone_no", "dob", "profileimg"]
    def get_queryset(self):
        return Profile.objects.filter(id = self.request.user.profile.id)



