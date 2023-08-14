from django.shortcuts import render
from .forms import MyForm
from django.conf import settings
import os
import supervision as sv
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
            
                form.save()

                img_obj = form.instance
                
                return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
            else:
                form = ImageForm()    
                return render(request, 'upload.html', {'form': form})
        else :
            data = json.loads(request.body)
            # Process the data and create the objects to return
            xyxy =  data['cord']
            url =  data['path']
          
           
            
               
                
                
        

            
            IMAGE_PATH=os.path.join(settings.MEDIA_ROOT, url[url.find('a')+2:])
            print(IMAGE_PATH)
          
          
            
            box = np.array([
            xyxy['Xmin'],
            xyxy['Ymin'],
            xyxy['Xmax'],
            xyxy['Ymax']
            ])
            CHECKPOINT_PATH="C:/Users/21653/Desktop/imageprocessing/models/sam_vit_h_4b8939.pth"
            MODEL_TYPE = "vit_h"
            print(box)
            from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
            sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH)
            mask_predictor = SamPredictor(sam)
           
            

            image_bgr = cv2.imread(IMAGE_PATH)
            image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

            mask_predictor.set_image(image_rgb)

            masks, scores, logits = mask_predictor.predict(
                box=box,
                multimask_output=True
            )
            original_image=cv2.imread(IMAGE_PATH)
            
            img=np.zeros(original_image.shape)
            img[:,:,:]=[255,255,255]
            img[masks[2,:,:]]=original_image[masks[2,:,:]]
            cv2.imwrite("C:/Users/21653/Desktop/imageprocessing/models/test1.jpg",img)
            
            

            
            return JsonResponse({'status': 'success'})
            
            # Process the submitted data here

            
    elif request.method == 'GET':
        form = ImageForm()    
        return render(request, 'upload.html', {'form': form})






        

