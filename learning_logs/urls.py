from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('create_entry/<int:topic_id>', views.create_entry, name='create_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]
