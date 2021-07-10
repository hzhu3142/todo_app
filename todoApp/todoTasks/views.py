from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoTem

# Create your views here.
def todoView(request):
    all_todo_items = ToDoTem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})


def addTodo(request):

    #create a new todo all_todo_items
    new_item = ToDoTem(content = request.POST['content'])

    #save
    new_item.save()

    #redirect the browser to '/todo/'
    return HttpResponseRedirect('/todoTasks/')

def deleteTodo(request, todo_id):
    item_to_delete = ToDoTem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todoTasks/')
