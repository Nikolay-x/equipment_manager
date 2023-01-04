from django.urls import path

from em_asd.accounts.views import UserDetailsView, favourites_list, \
    add_remove_favourites, SignUpView, SignInView, SignOutView, UserEditView, \
    UserDeleteView

urlpatterns = (
    path('profile/details/<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    path('profile/favourites/', favourites_list, name='favourites'),
    path('favourites/<int:pump_id>/', add_remove_favourites, name='add or remove favourites'),
    path('profile/signup/', SignUpView.as_view(), name='profile signup'),
    path('profile/signin/', SignInView.as_view(), name='profile signin'),
    path('profile/signout/', SignOutView.as_view(), name='profile signout'),
    path('profile/edit/<int:pk>/', UserEditView.as_view(), name='profile edit'),
    path('profile/delete/<int:pk>/', UserDeleteView.as_view(), name='profile delete'),
)
