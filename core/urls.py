from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.shortcuts import redirect

# View simples para interceptar o login do admin
def oidc_admin_login_redirect(request):
    return redirect('oidc_authentication_init')

urlpatterns = [
    # ESSA LINHA DEVE VIR ANTES DO admin.site.urls!
    path('admin/login/', oidc_admin_login_redirect, name='admin_login_redirect'),
    
    path('admin/', admin.site.urls),
    path('oidc/', include('mozilla_django_oidc.urls')),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)