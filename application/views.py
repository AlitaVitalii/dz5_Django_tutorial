from django.shortcuts import render

from .forms import TriangleForm


def triangle(request):
    if request.GET:
        form = TriangleForm(request.GET)
        if form.is_valid():
            cat1 = form.cleaned_data['cathetus1']
            cat2 = form.cleaned_data['cathetus2']
            gip = round((cat1**2 + cat2**2)**0.5, 2)
            return render(request, 'triangle.html', {'form': form, 'gip': gip})

    else:
        form = TriangleForm()

    return render(request, 'triangle.html', {'form': form})
