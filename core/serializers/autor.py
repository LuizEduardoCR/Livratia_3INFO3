from rest_framework.serializers import ModelSerializer

from core.models.autor import Autor


class AutorSerializer (ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
