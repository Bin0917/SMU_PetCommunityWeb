from django.shortcuts import render

# Create your views here.



def showstart(request):
    return render(request, 'account/start.html')