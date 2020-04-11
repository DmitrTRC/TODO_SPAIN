from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm, MainTodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo_list = Todo.objects.order_by('complete')
    # form = TodoForm()
    form = MainTodoForm()

    content = {
        'todo_list': todo_list,
        'form': form
    }

    return render(request, 'todo/index.html', content)


@require_POST
def add_todo(request):
    form = MainTodoForm(request.POST)
    if form.is_valid():
        new_todo = form.save()

    return redirect('index')


def delete_complete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def uncomplete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()

    return redirect('index')
