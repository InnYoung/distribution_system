from django.shortcuts import render, redirect
from django.http import HttpResponse
from tiger_distribution.models import Item

# Create your views here.
def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/id/')  
    items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})