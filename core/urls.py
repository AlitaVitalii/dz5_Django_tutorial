"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from application.views import triangle
from polls import views
from polls.views import current_datetime, your_name

urlpatterns = [
    path('admin/', admin.site.urls),

    path('polls/', include('polls.urls')),

    path("current-datetime/", current_datetime, name='current-datetime'),
    path("your_name/", your_name, name='your-name'),
    path("triangle/", triangle, name='triangle-name'),

    # path('exampl/', views.MyView.as_view()),
    # path('exampl/', TemplateView.as_view(template_name='exampl.html')),
    path('exampl/', views.TemplateViewExample.as_view()),
    path('example/', include('example.urls')),

    path('bootstrap/', TemplateView.as_view(template_name='bootstrap.html'), name="bootstrap"),

]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
