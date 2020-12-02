from django.contrib import admin
from Accounts.models import UserProfileInfo, User,Skill,Experience,Work

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Work)