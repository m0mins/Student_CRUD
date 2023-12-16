from django import forms
from studentProfileApp.models import Profile

class ProfileForm(forms.ModelForm):
    name=forms.CharField(label="Full Name",required=True)
    email=forms.EmailField(label="Email Address",required=True)
    su_id=forms.CharField(label="Student ID",required=True)
    phone=forms.CharField(label="Phone Number",required=True)
    class Meta:
        model=Profile
        fields=('name','email','su_id','department','phone','age','image','gender','religion','address')