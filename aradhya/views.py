from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def interninspot(request):
    return render(request, 'interninspot.html')

def dermascan(request):
    return render(request, 'dermascan.html')