from django.shortcuts import render

# Create your views here.
def plain(request):
    return render(request, "index.html")
