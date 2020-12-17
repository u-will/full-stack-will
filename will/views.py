from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Will
from django.urls import reverse_lazy
# Create your views here.

class WillListView(ListView):
  template_name = 'will-list.html'
  model = Will

class WillDetailView(DetailView):
  template_name = 'will-detail.html'
  model = Will

class WillCreateView(CreateView):
  template_name = 'will-create.html'
  model = Will
  fields = ['name', 'purchaser', 'description']

class WillUpdateView(UpdateView):
  template_name = 'will-update.html'
  model = Will
  fields = ['name', 'description']
  
class WillDeleteView(DeleteView):
  template_name = 'will-delete.html'
  model = Will
  success_url = reverse_lazy('will_list')