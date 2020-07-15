"""Orbital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts import views as accounts_views
from survey import views as survey_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('accounts/', include('accounts.urls')),
#     path('admin/', admin.site.urls)
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('survey.urls')),
    url(r'^$',accounts_views.index,name='index'),
    url(r'^special/',accounts_views.special,name='special'),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^accounts/profile/',accounts_views.profile_view, name='profile'),
    url(r'^logout/$', accounts_views.user_logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
