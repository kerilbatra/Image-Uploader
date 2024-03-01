from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'home.html', {'img': img, 'form': form})
