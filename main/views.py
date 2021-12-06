import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import CarForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>Information about author</h4>")


def equipment(request):
    file = 'medical_equipment/main/files/equipment.json'
    with open(file) as outfile:
        data = outfile.readlines()
    return HttpResponse(data, content_type="application/json")


def add_equipment(request):
    # if request.method == 'POST':  # data sent by user
    #     form = CarForm(request.POST)
    #     print('post now')
    #     if form.is_valid():
    #         form.save()  # this will save Car info to database
    #         return HttpResponse('Car added to database')
    # else:  # display empty form

    if request.method == 'GET':
        return render(request, 'main/add_equipment.html', {'car_form': CarForm()})
    else:
        data = {"id": request.POST.get('id'),
                "description": {
                    "id": request.POST.get('description_id'),
                    "name": request.POST.get('description_name'),
                    "brand": request.POST.get('description_brand'),
                    "model": request.POST.get('description_model'),
                    "manufacturer": {
                        "id": request.POST.get('description_manufacturer_id'),
                        "name": request.POST.get('description_manufacturer_name'),
                        "country": request.POST.get('description_manufacturer_country')
                    },
                    "category": {
                        "id": request.POST.get('description_category_id'),
                        "code": request.POST.get('description_category_code'),
                        "name": request.POST.get('description_category_name')
                    },
                },
                "serial": request.POST.get('serial'),
                "inventory": request.POST.get('inventory'),
                "date": request.POST.get('date'),
                "storage": {
                    "building": request.POST.get('storage_building'),
                    "room": request.POST.get('storage_room')
                },
                "condition": {
                    "id": request.POST.get('condition_id'),
                    "works": request.POST.get('condition_works'),
                    "location": request.POST.get('condition_location')
                }
                }
        print(json.dumps(data))
        with open('medical_equipment/main/files/data.json', 'w') as f:
            json.dump(data, f)
        return HttpResponse("Оборудование успешно добавлено")


