# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from plain import views
from django.contrib.auth import views as auth_views
from user.views import CustomPasswordResetView, CustomPasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), 
    path('', views.plain, name='plain'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
 
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
