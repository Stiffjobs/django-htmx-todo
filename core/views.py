from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods, require_POST

from core.forms import TodoForm
from core.models import Todo


# Create your views here.
@login_required
def index(request):
    context = {"todos": Todo.objects.filter(user=request.user), "form": TodoForm()}
    return render(request, "index.html", context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        # return partial template to htmx
        context = {"todo": todo}
        return render(request, "index.html#todoitem-partial", context)


@login_required
@require_POST
def toggle_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    context = {"todo": todo}
    return render(request, "index.html#todoitem-partial", context=context)


@login_required
@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response["HX-Trigger"] = "delete-todo"
    return response
