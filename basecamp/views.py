from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return redirect('/blog/')


def about_me(request):
    return render(
        request,
        'basecamp/about_me.html'
    )