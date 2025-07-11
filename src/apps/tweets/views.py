from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tweet


@login_required
def home(request):
    tweets = Tweet.objects.all()
    context = {
        'tweets': tweets
    }
    return render(request, 'tweets/pages/home.html', context)
