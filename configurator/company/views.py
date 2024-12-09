from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'company/index.html', context=context)

# Create your views here.
def about(request):
    """View function for about us page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'company/about.html', context=context)