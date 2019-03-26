"""markdojo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from hello.views import greeting
from todos.views import todoView, addTodo, deleteTodo
from survey.views import surveyView, addSurvey, deleteSurvey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hiya/', greeting),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('survey/', surveyView),
    path('addSurvey/', addSurvey),
    path('deleteSurvey/<int:survey_id>/', deleteSurvey),
]
