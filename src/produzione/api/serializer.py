from rest_framework import serializers
from produzione.models import Board, Order, Test, Verify, Smt



class OrderSerializer(serializers.ModelSerializer):

    created_at = serializers.SerializerMethodField()
    board_name= serializers.SerializerMethodField()
    customer= serializers.SerializerMethodField()
    order_verify = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_smt = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_test = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_shipping = serializers.SlugRelatedField(many=True, read_only=True, slug_field="uuid")


    class Meta:
        model = Order
        exclude = ["id", "updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B %Y")
    
    def get_board_name (self, instance):
        return instance.board.board_name
    def get_customer (self, instance):
        return instance.board.customer
    
    
    # def validate(self, data):

    #     return data

class BoardSerializer(serializers.ModelSerializer):

    order = OrderSerializer(many=True, read_only=True)
 
    class Meta:
        model = Board
        exclude = ["updated_at"]


class TestSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Test
        exclude = ["updated_at"]   

class VerifySerializer(serializers.ModelSerializer):
    
    order =  OrderSerializer(read_only=True)
    
    class Meta:
        model = Verify
        exclude = ["id", "updated_at"]

class SmtSerializer(serializers.ModelSerializer):

    order =  OrderSerializer(read_only=True)

    class Meta:
        model = Smt
        exclude = ["id", "updated_at"]

class BoardImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ("board_img",)