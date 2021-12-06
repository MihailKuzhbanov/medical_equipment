import json
from os import listdir, path

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import EquipmentForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>Information about author</h4>")


def equipment(request):
    file_path = 'main/files'
    files = listdir(file_path)
    return render(request, 'main/equipment.html', {'files' : files})


def saved(request):
    data_file = 'main/files/equipment.json'
    with open(data_file) as outfile:
        data = outfile.readlines()
    return HttpResponse(data, content_type="application/json")


def reports(request):
    path = request.GET.get('filename')
    filepath = 'main/files/' + path
    with open(filepath) as outfile:
        data = outfile.readlines()
    return HttpResponse(data, content_type="application/json")


def add_equipment(request):
    if request.method == 'GET':
        return render(request, 'main/add_equipment.html', {'equipment_form': EquipmentForm()})
    else:
        counter = 0
        filename = "main/files/equipment{}.json"
        while path.isfile(filename.format(counter)):
            counter += 1
        filename = filename.format(counter)
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
        with open(filename, 'w') as f:
            json.dump(data, f)

        return HttpResponse("Оборудование успешно добавлено")


