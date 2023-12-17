from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from example.models import Product, Image


# Create your views here.


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 3
    # template_name = 'example_2'


def list_example(request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'example/product_list.html', {
        'page_obj': page_obj,
        "product_list": page_obj.object_list})


class ProductDeleteViews(generic.DeleteView):
    model = Product
    success_url = reverse_lazy("products")
    template_name = "example/product_delete.html"


def static_example_view(request):
    # return render(request, "exampstatic/examstatic.html")
    file = Image.objects.last()
    return render(request, "exampstatic/examstatic.html", {"file": file})
