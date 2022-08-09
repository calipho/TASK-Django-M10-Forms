from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import StoreItemForm

from stores import models


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def create_store_item(request: HttpRequest) -> HttpResponse:
    form = StoreItemForm()
    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Item created")
    context = {
        "form": form,
    }
    return render(request, "create_store_item.html", context)


def update_store_item(request: HttpRequest, item_id: int) -> HttpResponse:
    store_item: models.StoreItem = models.StoreItem.objects.get(id=item_id)
    form = StoreItemForm(request.POST or None, instance=store_item)
    if form.is_valid():
        form.save()
        return HttpResponse("Item updated")
    context = {
        "form": form,
        "store_item": store_item,
    }
    return render(request, "update_store_item.html", context)


def delete_store_item(request: HttpRequest, item_id: int) -> HttpResponse:
    try:
        store_item = models.StoreItem.objects.get(id=item_id)
    except models.StoreItem.DoesNotExist:
        raise Http404("Item does not exist")
    store_item.delete()
    return HttpResponse("Item deleted")
