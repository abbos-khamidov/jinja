from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
# Create your views here.
def contacts(request):
    return render(request, 'contacts.html')
# Create your views here.
def about(request):
    return render(request, 'about.html')