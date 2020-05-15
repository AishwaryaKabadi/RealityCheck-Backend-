from django.shortcuts import render
from rest_framework import viewsets
from .models import Picture
from .serializers import PictureSerializer
#from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from base64 import b64decode
from .utils import upload_files_to_s3


class PictureView(viewsets.ModelViewSet):
    print('hey 1')
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class UploadImage(APIView):
    """ Used to Upload image
    """   

    def post(self, request):
        """ Will create image from base64 and upload to server

        Arguments:
            request {[json]} -- Base 64 image

        Returns:
            [type] -- Json response with status 200
        """
        list_of_keys = list(request.data.keys())
        
        base_64_string = list_of_keys[1].replace('base64,', '')
        print("heu 3")
        with open("image.jpeg", "wb") as f:
            f.write(b64decode(base_64_string))

        image_url = upload_files_to_s3("image.jpeg")
        print(image_url)

        image_obj = Picture.objects.create(title=image_url, images=image_url)

        serializer = PictureSerializer(image_obj)
        return JsonResponse(serializer.data, status=200)



