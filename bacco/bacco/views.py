from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import MyModelPhoto
import os
from predict import predict

def my_endpoint(request):
    return HttpResponse("¡Hi world! This is baccos")


@csrf_exempt
def upload_photo(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']
        print(photo.name)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        photo_folder_path = os.path.join(current_directory, 'photos')
        if not os.path.exists(photo_folder_path):
            os.makedirs(photo_folder_path)
        photo_path = os.path.join(photo_folder_path, photo.name)
        with open(photo_path, 'wb') as destination:
            for chunk in photo.chunks():
                destination.write(chunk)

        beverage = predict(photo, photo_path)
        return JsonResponse({'message': beverage})
    else:
        return JsonResponse({'error': 'No se proporcionó ninguna foto en la solicitud'}, status=400)
