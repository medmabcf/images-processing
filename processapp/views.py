from django.shortcuts import render
from .forms import MyForm




from django.shortcuts import render
from .forms import ImageForm

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            print(img_obj)
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()    
        return render(request, 'upload.html', {'form': form})
