from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"User '{username}' successfully created")
            return redirect('artists-home')
            
    else:
        form = UserRegistrationForm()

    data = {"form": form}
    return render(request, "register.html", data)
    


