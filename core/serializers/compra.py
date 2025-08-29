from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade', 'total')
        depth = 1


from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError, # novo
)

class ItensCompraCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro', 'quantidade')

    def validate(self, item):
        if item['quantidade'] > item['livro'].quantidade:
            raise ValidationError('Quantidade de itens maior do que a quantidade em estoque.')
        return item


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.e-mail', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'itens')
       

        
