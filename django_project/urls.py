from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from reporter import views as reporter_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', reporter_views.register, name='register'),
    path('profile/', reporter_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='reporter/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='reporter/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reporter/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reporter/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reporter/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reporter/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('', include('news.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
