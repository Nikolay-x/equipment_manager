from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from em_asd.accounts.forms import UserCreateForm, UserEditForm

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm


'''
Username: Superuser1
Password: password
Usernames: Superuser2, Staffadmin1, Staffadmin2, Engineer1, Engineer2, User1, User2 
Other passwords: QwertAsdf
'''
