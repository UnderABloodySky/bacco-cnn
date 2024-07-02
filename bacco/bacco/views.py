from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import MyModelPhoto
import os
from .predict import predict

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
        return JsonResponse({'message': beverage}, status=200)
    else:
        return JsonResponse({'error': 'No se proporcionó ninguna foto en la solicitud'}, status=400)



@csrf_exempt
def upload_photo_for_retrain(request):
    if request.method == 'POST' and request.FILES.get('photo') and request.POST.get('beverage'):
        photo = request.FILES['photo']
        beverage = request.POST['beverage']
        current_directory = os.path.dirname(os.path.abspath(__file__))
        photo_folder_path = os.path.join(current_directory, 'retrain')
        final_path = f'{photo_folder_path}/{beverage}'
        if not os.path.exists(final_path):
            os.makedirs(final_path)
        photo_path = os.path.join(final_path, photo.name)
        with open(photo_path, 'wb') as destination:
            for chunk in photo.chunks():
                destination.write(chunk)

        return JsonResponse({'message': "OK"}, status=200)
    else:
        return JsonResponse({'error': 'No se proporcionó ninguna foto en la solicitud o nombre de la bebida'}, status=400)