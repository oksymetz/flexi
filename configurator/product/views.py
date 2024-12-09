from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/index.html', context=context)

def configurator(request):
    """View function for login page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/configurator.html', context=context)

def box(request):
    """View function for login page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/box.html', context=context)