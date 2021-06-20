from django.urls import path
from .views import createReadTodoFunction,individualTodoFunction
from .views import CreateReadToDoClass,IndividualToDoClass
from .views import ToDoMixins

app_name = "todo"

urlpatterns = [
    path("function/todo",createReadTodoFunction),
    path("function/todo/<int:id>",individualTodoFunction),
    path("class/todo",CreateReadToDoClass.as_view()),
    path("class/todo/<int:id>",IndividualToDoClass.as_view()),
    path("mixins/todo",ToDoMixins.as_view()),
    path("mixins/todo/<int:id>",ToDoMixins.as_view())
]