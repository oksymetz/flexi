from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Draft, Material, Product, Box


# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/index.html', context=context)


@csrf_exempt
def manually(request):
    context = {}
    """View function for login page of site."""
    if request.method == 'POST':
        draft = Draft(
            stand_height=request.POST.get("manualDeskHeight"),  # Stand height
            sitting_height=request.POST.get("manualDeskHeight"),  # Sitting height
            width=request.POST.get("manualDeskDepth"),  # Width
            length=request.POST.get("manualDeskLength"),
            body_height=None,
            material_id=1,  # wood
            product_id=1,  # table
            user_id=request.user.id,
            quantity=request.POST.get("quantity"),

        )
        draft.save()
        return render(request, 'product/draft_saved.html', context=context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/configurator.html', context=context)


@csrf_exempt
def configurator(request):
    context = {}
    if request.user.is_authenticated:
        """View function for login page of site."""
        if request.method == 'POST':
            body_height = float(request.POST.get("inputBodyHeight"))
            standingHeight = 0.125 * 5 * body_height
            sittingHeight = 0.125 * 3.5 * body_height

            draft = Draft(
                body_height=float(request.POST.get("inputBodyHeight")),  # Body height
                stand_height=standingHeight,  # Stand height
                sitting_height=sittingHeight,  # Sitting height
                width=request.POST.get("depth"),  # Width
                length=request.POST.get("length"),
                material_id=1,  # wood
                product_id=1,  # table
                user_id=request.user.id,
                quantity=request.POST.get("quantity"),
            )
            draft.save()
            return render(request, 'product/draft_saved.html', context=context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/configurator.html', context=context)


@csrf_exempt
def box(request):
    context = {}
    if request.user.is_authenticated:
        """View function for login page of site."""
        if request.method == 'POST':
            box = Box(
                box_height=request.POST.get("box_height"),  # Sitting height
                box_length=request.POST.get("box_length"),  # Width
                box_depth=request.POST.get("box_depth"),
                material_id=1,  # wood
                product_id=2,  # table
                user_id=request.user.id,
                quantity=request.POST.get("quantity"),
            )
            box.save()
            return render(request, 'product/draft_saved.html', context=context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'product/box.html', context=context)
