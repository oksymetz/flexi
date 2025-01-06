from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Draft, Material, Product

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/index.html', context=context)

@csrf_exempt
def configurator(request):
    context = {}
    """View function for login page of site."""
    if request.method == 'POST':

        standingHeight = 1
        sittingHeight = 1

        draft = Draft(
            body_height=request.POST.get("inputBodyHeight"),         # Body height
            stand_height=standingHeight,        # Stand height
            sitting_height=sittingHeight,       # Sitting height
            width=request.POST.get("width"),                 # Width
            length=request.POST.get("length"),
            material_id=1, # wood
            product_id=1, # table
            user_id=request.user.id,
        )
        draft.save()
        return render(request, 'product/draft_saved.html', context=context)


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/configurator.html', context=context)

def box(request):
    """View function for login page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/box.html', context=context)