from django.shortcuts import redirect, render

# Create your views here.
def intro(request):
    return render(request,'view.html')