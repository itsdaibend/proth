from django.shortcuts import render

from todo.models import Todo

def HomePageView(request):
    todo = Todo.objects.filter(user=request.user, status=2)

    context = {'page_title': 'Home', 'todos': todo}
    return render(request, 'home_page.html', context)