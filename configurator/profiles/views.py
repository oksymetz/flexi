from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User

from product.models import Draft, Material, Box
from profiles.models import Customer


# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {}
    if request.user.is_authenticated:
        name = User.get_full_name(request.user)
        address = Customer.objects.get(user=request.user.id).address
        print(name, address)
        context["name"] = name
        context["address"] = address
        return render(request, 'profiles/profile.html', context=context)

    # Redirect to login page if not authenticated
    return redirect("/profile/login")


@csrf_exempt
def login(request):
    """View function for login page of site."""
    context = {}
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/profile/")

    # Render the login page
    return render(request, 'profiles/login.html', context=context)


def log_out(request):
    """View function to log out a user."""
    if request.user.is_authenticated:
        logout(request)
    return redirect('/profile/')


@csrf_exempt
def signin(request):
    """View function for signin page of site."""
    context = {}
    if request.method == 'POST':
        username = request.POST["username"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("login")

        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        new_user = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=first_name,
            last_name=last_name,
        )
        new_user.save()
        messages.success(request, "Account created successfully!")

        address = request.POST["address"]
        customer = Customer.objects.create(user=new_user, address=address)
        customer.save()

        auth_login(request, new_user)
        return redirect("/profile/")

    # Render the signin page
    return render(request, 'profiles/signin.html', context=context)


def drafts(request):
    """View function for drafts page of site."""
    if request.user.is_authenticated:
        """Data from database for the tables"""
        drafts = Draft.objects.filter(user=request.user).order_by('-id')[:10]

        idx = [r['id'] for r in drafts.values()]
        bh = [r['body_height'] for r in drafts.values()]
        sth = [r['stand_height'] for r in drafts.values()]
        sh = [r['sitting_height'] for r in drafts.values()]
        w = [r['width'] for r in drafts.values()]
        l = [r['length'] for r in drafts.values()]
        mat = [Material.objects.get(id=r['material_id']) for r in drafts.values()]
        q = [r['quantity'] for r in drafts.values()]

        draft_items = zip(bh, sth, sh, w, l, mat, q)

        """Data from database for the boxes"""
        boxes = Box.objects.filter(user=request.user).order_by('-id')[:10]

        idx = [r['id'] for r in boxes.values()]
        bxh = [r['box_height'] for r in boxes.values()]
        bxl = [r['box_length'] for r in boxes.values()]
        bxd = [r['box_depth'] for r in boxes.values()]
        mat = [Material.objects.get(id=r['material_id']) for r in boxes.values()]
        q = [r['quantity'] for r in boxes.values()]

        box_items = zip( bxh, bxl, bxd, mat, q)

        """data for the template"""
        context = {'draft_items': draft_items, 'box_items': box_items}

        # Render the drafts page
        return render(request, 'profiles/drafts.html', context=context)
    else:
        return redirect("/profile/login")


def box(request):
    """View function for displaying box drafts."""
    if request.user.is_authenticated:
        boxes = Box.objects.filter(user=request.user).order_by('-id')[:10]

        idx = [r['id'] for r in boxes.values()]
        bh = [r['box_height'] for r in boxes.values()]
        sth = [r['box_length'] for r in boxes.values()]
        sh = [r['box_depth'] for r in boxes.values()]
        mat = [Material.objects.get(id=r['material_id']) for r in boxes.values()]
        q = [r['quantity'] for r in boxes.values()]

        box_items = zip( bh, sth, sh, mat, q)
        context = {'box_items': box_items}

        # Render the box drafts page
        return render(request, 'profiles/drafts.html', context=context)
    else:
        return redirect("/profile/login")
