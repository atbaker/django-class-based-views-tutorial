from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Cheese

def home(request):
    """A sample function-based view"""
    context = {}

    # Do some view logic - for example:
    context['foo'] = 'bar'

    return render_to_response('index.html', context)

class CheeseListView(ListView):
    """Shows users a list of cheeses"""

    model = Cheese

class CheeseDetailView(DetailView):
    """Shows users a single cheese"""

    model = Cheese

class CheeseCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new cheese"""

    model = Cheese
    fields = ['name', 'price', 'quantity']
    success_message = 'Cheese successfully created.'


class CheeseUpdateView(SuccessMessageMixin, UpdateView):
    """Powers a form to edit existing cheeses"""

    model = Cheese
    fields = ['name', 'price', 'quantity']
    success_message = 'Cheese successfully updated.'


class CheeseDeleteView(DeleteView):
    """Prompts users to confirm deletion of an cheese"""

    model = Cheese
    success_url = reverse_lazy('list_cheeses')
