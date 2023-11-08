from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.

class edit_profile(View):
    def get(self,request,username):
        user = get_object_or_404(User,username=username)
        profile_form = ProfileEditForm(data=request.POST)
        user_form = UserEditForm(data=request.POST)
        context = {
            "profile_form":profile_form,
            "user_form":user_form,
        }
        return render(request,"account/edit_profile.html",context)
    def post(self,request,username):
        user = get_object_or_404(User,username=username)
        user_form = UserEditForm(data=request.POST)
        profile_form = ProfileEditForm(data=request.POST)
        if(user_form.is_valid() and profile_form.is_valid()):
            ucd = user_form.cleaned_data
            fcd = profile_form.cleaned_data
            auth = User.objects.filter(username=ucd["username"])
            if auth.exists():
                return redirect('edit_profile' ,username)
            else:
                if ucd["username"] == "":
                    print("empty field")
                else:
                    user.username = ucd["username"]
                user.first_name = ucd["first_name"]
                user.last_name = ucd["last_name"]
                user.save()
                profile = Profile(
                    user = user,
                    date_of_birth = fcd["date_of_birth"],
                    image = fcd["image"],
                    ).save();
                user.profile = profile
                user.save()
                return redirect("dashboard")
        return HttpResponse("")
def landing(request):
    
    return render(request,"account/landing.html")
    
@login_required
def dashboard(request):
    
    return render(request,"account/dashboard.html")
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit = False)
            user.set_password(cd["password"])
            user.save();
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        form = UserRegistrationForm();
    context = {
        "form":form,
    }
    return render(request,'account/register.html',context)