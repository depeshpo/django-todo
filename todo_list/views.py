from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request, ("Item has been added to the list successfully!"))
            return render(request, 'index.html', {'all_items': all_items})

    else:
        all_items = List.objects.all()
        return render(request, 'index.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted successfully!'))
    return redirect('index')


def make_completed(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('index')


def make_uncompleted(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Item successfully! ')
            return redirect('index')

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
