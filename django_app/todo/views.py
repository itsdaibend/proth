from django.shortcuts import redirect, render

from todo.forms import TodoCreationForm
from todo.models import Todo

def TodoPageView(request):
    form = TodoCreationForm()
    if request.method == 'POST':
            form = TodoCreationForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                return redirect('todos')

    queryset = Todo.objects.filter(user=request.user).order_by('created_at')

    context = {'page_title': 'Todos', 'todos': queryset, 'form': form}
    return render(request, 'todo/todopage.html', context)

def TodoDeleteView(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        todo.delete()

        return redirect('todos')

def TodoUpdateStatusView(request, todo_id, status):
    todo = Todo.objects.get(id=todo_id)

    if request.user == todo.user:
        todo.status = status
        todo.save()
    
    return redirect('todos')