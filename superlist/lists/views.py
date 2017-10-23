from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from lists.models import Item


def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text','')
    item.save()
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request,'home.html', {'new_item_text':item.text})


