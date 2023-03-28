from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from todo.forms import TodoCreationForm, TodoUpdateForm
from todo.models import Todo


class TodoPageView(View):
    context = {"page_title": "Todos"}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("sign_in")

        update_form = TodoUpdateForm()
        form = TodoCreationForm()

        self.context["form"] = form
        self.context["update_form"] = update_form
        self.context["todos"] = Todo.objects.filter(user=request.user).order_by(
            "created_at"
        )
        return render(request, "todo/todopage.html", self.context)

    def post(self, request, todo_id=None, status=None):
        if "Update" in request.POST:
            todo = get_object_or_404(Todo, id=todo_id)
            form = TodoUpdateForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()

            return redirect("todos")

        elif "Update_status" in request.POST:
            todo = Todo.objects.get(id=todo_id)
            if request.user == todo.user and status == 4:
                todo.status = status
                todo.is_completed = True
                todo.save()

            elif request.user == todo.user:
                todo.status = status
                todo.save()

            return redirect("todos")

        elif "Create" in request.POST:
            form = TodoCreationForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.save()

                return redirect("todos")

        elif "Delete" in request.POST:
            if request.method == "POST":
                todo = Todo.objects.get(id=todo_id)
                todo.delete()

                return redirect("todos")
