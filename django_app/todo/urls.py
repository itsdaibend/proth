from django.urls import path

from .views import TodoPageView

urlpatterns = [
    path("", TodoPageView.as_view(), name="todos"),
    path("delete/<int:todo_id>", TodoPageView.as_view(), name="todos"),
    path(
        "update_status/<int:todo_id>/<int:status>", TodoPageView.as_view(), name="todos"
    ),
    path("update/<int:todo_id>", TodoPageView.as_view(), name="todos"),
]
