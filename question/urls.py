from django.urls import path

from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.questionDetail, name='detail'),
    path('results/<int:question_id>/', views.questionResults, name='results'),
    path('vote/<int:question_id>/', views.questionVote, name='vote'),
    path('resultsdata/<int:obj>/', views.resultsData, name='resultsdata'),
]