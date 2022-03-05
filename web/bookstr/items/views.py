from django.shortcuts import render,redirect
from .models import Item as item_model
# Create your views here.
def index(req):
    Items = item_model.objects.all()
    return render(req, "items/home.html", {'Items': Items})
    
def addItem(req):
    return render(req, 'items/addItem.html')
def notFound(req):
    return render(req, 'items/error.html')
def saveData(req):
    if req.method == 'POST': 
        print(req.POST)
        name_book = req.POST['name_book']
        type_book = req.POST['type_book']
        author = req.POST['author']
        price = req.POST['price']
        description = req.POST['description']
        status = req.POST['status']
        new_item = item_model.objects.create(
            name_book = name_book,
            type_book = type_book,
            author = author,
            price = price,
            description = description,
            status = status,
        )
        new_item.save()
        return render(req, 'items/addItem.html')
    else:
        return render(req, 'items/error.html')


        

        
