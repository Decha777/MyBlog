from django import forms
from django.contrib.auth.models import User
from Accounts.models import UserProfileInfo,Work,Experience,Skill

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'username','placeholder': 'Enter Username',}),
            'email' : forms.EmailInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'email','placeholder': 'Enter Email',}),
            'password' : forms.PasswordInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'password','placeholder': 'Enter Password',}),
            # 'Confirm' : forms.PasswordInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'password2','placeholder': 'Confirm Password',}),
        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)
        widgets = {

            # 'birth_date': forms.TextInput(attrs = {'class': ' form w-full h-6/12 mt-2 ', 'name':'title','placeholder': 'Enter Title',}),
            # 'job': forms.TextInput(attrs ={ 'class': 'form-control user_website'}),
            # 'portfolio_site': forms.URLInput(attrs ={ 'class': 'form-control user_website'}),
            'profile_pic' : forms.FileInput(attrs ={'class': ' form w-full h-6/12 mt-2 ',}),
            
        }

class Skill(forms.ModelForm):
    class Meta():
        model = Skill
        fields = ('skill_name', 'skill_value')
        widgets = {
            'skill_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'skill_value': forms.NumberInput(attrs= {'class': 'form-control'}),
        }
class Experience(forms.ModelForm):
    class Meta():
        model = Experience
        fields = ('experience_name', 'decription','start_date','end_date')
        widgets = {
            'experience_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'decription': forms.Textarea(attrs= {'class': 'form-control'}),
            'start_date': forms.TextInput(attrs= {'class': 'form-control'}),
            'end_date': forms.TextInput(attrs= {'class': 'form-control'}),

        }
        
class Work(forms.ModelForm):
    class Meta():
        model = Work
        fields = ('work_name', 'decription','link')
        widgets = {
            'work_name': forms.TextInput(attrs= {'class': 'form-control'}),
            'decription': forms.Textarea(attrs= {'class': 'form-control'}),
            'link': forms.URLInput(attrs= {'class': 'form-control'}),

        }
