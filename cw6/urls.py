"""cw6 URL Configuration

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
from django.contrib import admin
from django.urls import path

from wa_v1.models import (HomeController,
                          TestController,
                          ProfileController,
                          SubjectController,
                          )

urlpatterns = [
    path("", HomeController().render_page, name='home'),
    path("test/", TestController.render_page, name="test"),
    path("select_profiles/", ProfileController.render_page, name='profiles'),
    path("select_subjects/", SubjectController.render_page, name='subjects'),

    path("convert", ProfileController.convert, name='profiles_convert'),
    path("convert", SubjectController.render_page, name='subjects_convert'),

    path("test_result", TestController().get_test_result, name="test_result"),

    path("test/advise", TestController().advise_he, name="advise_test"),
    path("test/dormitory_city", TestController().choose_city_dormitory, name="dorm_city"),
    path("select_profiles/advise", ProfileController().advise_he, name="advise_profiles"),
    path("select_subjects/advise", SubjectController().advise_he, name="advise_subjects"),


]
