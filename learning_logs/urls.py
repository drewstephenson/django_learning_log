"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views  # tells python to import the views module from the same directory as the current urls.py file.

app_name = 'learning_logs'

# List of URL pages that can be requested from the learning_logs app.
urlpatterns = [
    # Home page
    path('', views.index, name='index'),  # when the URL requested is the base URL, call the index() view function.

    # Page for showing all the topics
    path('topics/', views.topics, name='topics'),

    # More detailed page for a single page.
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # takes topic's id number, calls topic()

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]
