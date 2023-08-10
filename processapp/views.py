from django.shortcuts import render
from .forms import MyForm

import json
from django.http import HttpResponse

from django.shortcuts import render
from .forms import ImageForm
from django.http import JsonResponse
from django.views import View
import cv2
from django.http import JsonResponse
from PIL import Image
from django.core.files.base import ContentFile
import numpy as np
from django.views.decorators.csrf import csrf_exempt
def image_upload_view(request):
    """Process images uploaded by users"""
    print("cecfvc",request)
    if request.method == 'POST':
        
        if 'title' in request.POST:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                           # Get the uploaded image from the form
                image = form.cleaned_data['image']

                
                # Read the image data into a NumPy array
                img_data = np.asarray(bytearray(image.read()), dtype=np.uint8)
                # Read the image data using cv2
                img = cv2.imdecode(img_data, cv2.IMREAD_UNCHANGED)

                # Resize the image
                scale=img.shape[0]/img.shape[1]
                new_width = 1000
                new_height = (int)(1000*scale)
                img_resized = cv2.resize(img, (new_width, new_height))
                # Encode the resized image as JPEG
                _, img_encoded = cv2.imencode('.jpg', img_resized)

                # Update the image field of the Image model instance
                instance = form.save(commit=False)
                instance.image.save(image.name, ContentFile(img_encoded.tobytes()), save=False)

                # Save the form data to the database
                instance.save()

                img_obj = form.instance
                
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
    elif request.method == 'GET':
        form = ImageForm()    
        return render(request, 'upload.html', {'form': form})






        

