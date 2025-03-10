"""
URL configuration for myPagePrj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=".env")

urlpatterns = [
    path('demoApp/', include('demoApp.urls')), # 배포용 데모 앱
    path('', include('resume.urls')), # 이력서 페이지
    path('blog/', include('blog.urls')), # blog 페이지
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    # path(env('DJANGO_PROD_ADMIN_PAGE_URL'), admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
