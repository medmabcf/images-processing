from django.shortcuts import render
from .forms import MyForm

import json
from django.http import HttpResponse

from django.shortcuts import render
from .forms import ImageForm
from django.http import JsonResponse
from django.views import View

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def image_upload_view(request):
    """Process images uploaded by users"""
    print(request)
    if request.method == 'POST':
        
            
        print(request)
        data = json.loads(request.body)
        startX = data['startX']
        startY = data['startY']
        endX = data['endX']
        endY = data['endY']



        

