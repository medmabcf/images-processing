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
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        if 'title' in request.POST:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
            
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                print(img_obj)
                return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
            else:
                form = ImageForm()    
                return render(request, 'upload.html', {'form': form})
        else :
            data = json.loads(request.body)
            startX = data['startX']
            startY = data['startY']
            endX = data['endX']
            endY = data['endY']

            # Process the submitted data here

            return JsonResponse({'status': 'success'})
        

