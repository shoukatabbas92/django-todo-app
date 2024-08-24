from django.shortcuts import render,redirect
from .models import Todo 

# Create your views here.


def todo_list(request):
    todos = Todo.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title,description=description)

    return redirect('todo_list')

def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

def edit_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    
    todo.edit()

