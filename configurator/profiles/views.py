from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profiles/index.html', context=context)

def login(request):
    """View function for login page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profiles/login.html', context=context)

def signin(request):
    """View function for signin page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profiles/signin.html', context=context)