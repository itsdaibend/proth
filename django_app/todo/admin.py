from django.contrib import admin

from todo.models import Todo, TodoLabel

admin.site.register(Todo)
admin.site.register(TodoLabel)