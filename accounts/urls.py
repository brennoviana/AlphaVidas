from django.urls import path
from .views import UserLoginView, UserRegisterView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
