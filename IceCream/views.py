from django.shortcuts import render

from IceCream.forms import IceCreamForm


# Create your views here.
def create_ice_cream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = IceCreamForm()
    return render(request, 'index.html', {'form': form})