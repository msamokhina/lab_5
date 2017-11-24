# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

horsesObjects = []

for i in range(1, 20):
    horsesObjects.append({
        'id': i,
        'horseName': 'horseName' + str(i),
    })

def objectslist(request):
    return render(request, 'objectsList.html', {
        'horses': horsesObjects,
    })

def object(request, id):
    data = {
        'horse':{
            'id': id
        }
    }
    return render(request, 'object.html', data)