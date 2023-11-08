
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileEditForm(forms.Form):
    bio = forms.CharField(widget=(forms.Textarea),required=False)
    date_of_birth = forms.DateField(required=False)
    image = forms.ImageField(required=False)
    
class UserEditForm(forms.Form):
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    
# with this user can create account in your site
class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"}))
    password2 = forms.CharField(label="comfirm mpassword",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"comfirm password"}))
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control","placeholder":"enter username"})
        self.fields["email"].widget.attrs.update({"class":"form-control","placeholder":"enter your email"})
        self.fields["first_name"].widget.attrs.update({"class":"form-control","placeholder":"enter your first name"})
        self.fields["last_name"].widget.attrs.update({"class":"form-control","placeholder":"enter your last name"})
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("password are not match")
        return cd["password"]