from django.urls import path
from Accounts import views

# SET THE NAMESPACE!
app_name = 'Accounts'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/<int:pk>', views.index, name='profile'),
    # path('accounts/profile/', views.index, name='profile'),
    # path('user_login/',views.user_login,name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
]
