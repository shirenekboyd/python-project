# from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Contact
from .forms import ContactForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contacts')  # Redirect to the contact list view after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the project's index.")

# from django.shortcuts import render
# from .models import Contact

def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'reallysimplecrm/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect(reverse('contact_list'))
    else:
        form = ContactForm()

    return render(request, 'reallysimplecrm/contact_form.html', {'form': form})
