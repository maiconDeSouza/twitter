from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def logout(request):
    return render(request, 'accounts/logged_out.html')
