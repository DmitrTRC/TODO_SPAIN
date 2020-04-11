from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo_list = Todo.objects.order_by('complete')
    form = TodoForm()

    content = {
        'todo_list': todo_list,
        'form': form
    }

    return render(request, 'todo/index.html', content)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=form.clean_data['text'], complete=False)
        new_todo.save()

    print(request.POST.get('text', 'UNDEFINED!'))
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
