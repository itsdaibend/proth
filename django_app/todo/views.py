from django.shortcuts import get_object_or_404, redirect, render

from todo.forms import TodoCreationForm, TodoUpdateForm
from todo.models import Todo

def TodoPageView(request):
    update_form = TodoUpdateForm()
    form = TodoCreationForm()
    if request.method == 'POST':
            form = TodoCreationForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.save()
                return redirect('todos')

    queryset = Todo.objects.filter(user=request.user).order_by('created_at')

    context = {'page_title': 'Todos', 'todos': queryset, 'form': form, 'update_form': update_form}
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

def TodoUpdateView(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    form = TodoUpdateForm(request.POST or None, instance = todo)

    if form.is_valid():
        form.save()

    return redirect('todos')