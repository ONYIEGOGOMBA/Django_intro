from django.shortcuts import render

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')

def classes(request):
    return render(request, 'students/classes.html')