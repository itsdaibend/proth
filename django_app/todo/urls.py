from django.urls import path

from .views import TodoDeleteView, TodoPageView, TodoUpdateStatusView


urlpatterns = [
    path('', TodoPageView, name='todos'),
    path('delete/<int:todo_id>', TodoDeleteView, name='todo_del'),
    path('update_status/<int:todo_id>/<int:status>', TodoUpdateStatusView, name='todo_status_upd'),
]