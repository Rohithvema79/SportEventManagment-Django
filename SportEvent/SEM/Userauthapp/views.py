from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'Userauthapp/register.html', {'form': form, 'mode': 'signup'})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('')  # Redirect to the homepage
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = SignInForm()
    return render(request, 'Userauthapp/login.html', {'form': form, 'mode': 'signin'})
def projecthomepage(request):
    return render(request, 'Userauthapp/homepage.html')