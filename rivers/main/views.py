from django.shortcuts import render, redirect
from .models import Item
from .forms import AdItem

def create_ad(request):
    if request.method == 'POST':
        form = AdItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')  # Перенаправление на список объявлений после создания
    else:
        form = AdItem()
    return render(request, 'main/ad_item.html', {'form': form})

def index(request):
    Item_list = Item.objects.order_by('-pub_date')[:5]
    context = {'Item_list': Item_list}
    return render(request, 'main/index.html', context)
