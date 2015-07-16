from django.conf.urls import url

from .views import CheeseListView, CheeseDetailView, CheeseCreateView, CheeseUpdateView, CheeseDeleteView


urlpatterns = [
    # List and detail views
    url(r'^$', CheeseListView.as_view(), name='list_cheeses'),
    url(r'^/(?P<pk>[0-9]+)$', CheeseDetailView.as_view(), name='view_cheese'),

    # # Create, update, delete
    url(r'^/new$', CheeseCreateView.as_view(), name='new_cheese'),
    url(r'^/(?P<pk>[0-9]+)/edit$', CheeseUpdateView.as_view(), name='edit_cheese'),
    url(r'^/(?P<pk>[0-9]+)/delete$', CheeseDeleteView.as_view(), name='delete_cheese'),
]
