from rest_framework import serializers

from .models import Picture


class PictureSerializer(serializers.ModelSerializer):

    QR_Embedded_Image = serializers.SerializerMethodField()

    class Meta:

        model = Picture
        fields = ('Original_Image', 'QR_Embedded_Image', 'created_at',
                  'updated_at')

    def get_QR_Embedded_Image(self, request):
        Image_name = request.Original_Image
        return 'https://esp32cam.s3.amazonaws.com/media/' + 'embedded_' + str(Image_name)
