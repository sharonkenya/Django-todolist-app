from django.shortcuts import render
# In your app's views.py file

from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def edit_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')

# Create your views here.
