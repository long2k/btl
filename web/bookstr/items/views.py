from django.shortcuts import render,redirect
from .models import Item as item_model
# Create your views here.
def index(req):
    return render(req, 'items/home.html')
def addItem(req):
    return render(req, 'items/addItem.html')
def notFound(req):
    return render(req, 'items/error.html')
def listItem(req): 
    return render(req, 'items/listItem.html')
def saveData(req):
    if req.method == 'POST': 
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
        return redirect('/list/')
    else:
        return render(req, 'error.html')
        

        
