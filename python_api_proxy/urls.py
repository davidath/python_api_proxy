from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    #Events with subscription
    #Route: /events-with-subscription/<event_id>
    #Input:  ID of the event that we need info on
    #Output: JSON Response popullated with event details and event subscriptions

    url(r'^events-with-subscription/(?P<event_id>\w+)',views.event_sub,name='event_sub'),
)
