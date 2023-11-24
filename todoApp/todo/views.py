from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoItem
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo/todo_list.html'

class TodoCreateView(CreateView):
    model = TodoItem
    fields = ['title','description' 'completed']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ['title', 'completed']
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
    


# Similarly, define UpdateView and DeleteView

