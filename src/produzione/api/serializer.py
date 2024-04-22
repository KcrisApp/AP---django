from rest_framework import serializers
from rest_framework.serializers import BaseSerializer
from produzione.models import Welding, Board, Order, Test, Verify, Smt, Shipping, ProductionSteps



class OrderSerializer(serializers.ModelSerializer):

    # created_at = serializers.SerializerMethodField()
    board_name= serializers.SerializerMethodField()

    customer= serializers.SerializerMethodField()
    order_verify = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_smt = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_test = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_welding = serializers.SlugRelatedField(many=False, read_only=True, slug_field="uuid")
    order_shipping = serializers.SlugRelatedField(many=True, read_only=True, slug_field="uuid")




 
    
    
    class Meta:
        model = Order
        exclude = ["updated_at"]
    
    # def get_created_at(self, instance):
    #     return instance.created_at.strftime("%d/%m/%Y")
    
    def get_board_name (self, instance):
        return instance.board.board_name
    def get_customer (self, instance):
        return instance.board.customer

    

class OrderStatusSerializer(serializers.ModelSerializer):

    # created_at = serializers.SerializerMethodField()
    board_name= serializers.SerializerMethodField()
    customer= serializers.SerializerMethodField()

    order_verify = serializers.SlugRelatedField(many=False, read_only=True, slug_field="status")
    order_smt = serializers.SlugRelatedField(many=False, read_only=True, slug_field="status")
    order_test = serializers.SlugRelatedField(many=False, read_only=True, slug_field="status")
    order_welding = serializers.SlugRelatedField(many=False, read_only=True, slug_field="status")
   

    
    
    class Meta:
        model = Order
        exclude = ["updated_at","uuid",'order_quantity','order_process_note','order_serialnumber','order_customization','order_filetopographic','board','created_at','id']
    
    # def get_created_at(self, instance):
    #     return instance.created_at.strftime("%d/%m/%Y")
    
    def get_board_name (self, instance):
        return instance.board.board_name
    def get_customer (self, instance):
        return instance.board.customer

    
    
    


class OrderTopographicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("order_filetopographic",)
            



class BoardSerializer(serializers.ModelSerializer):

    order = OrderSerializer(many=True, read_only=True)
   

    class Meta:
        model = Board
        exclude = ["updated_at"]
    
  


class ProductionStepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductionSteps
        exclude = ["id", "updated_at"]

  

class TestSerializer(serializers.ModelSerializer):
    
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Test
        exclude = ["updated_at"]   
    
    def get_order_number (self, instance):
        return instance.order.order_number

class VerifySerializer(serializers.ModelSerializer):
    
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Verify
        exclude = ["id", "updated_at"]
    
    def get_order_number (self, instance):
        return instance.order.order_number

class SmtSerializer(serializers.ModelSerializer):

    order_number = serializers.SerializerMethodField()
   

    class Meta:
        model = Smt
        exclude = ["id", "updated_at"]
    
    def get_order_number (self, instance):
        return instance.order.order_number

class ShippingSerializer(serializers.ModelSerializer):

    # order = OrderSerializer(many=True)
    order_number = serializers.SerializerMethodField()
    order_quantity = serializers.SerializerMethodField()
    
    class Meta:
        model = Shipping
        exclude = ["updated_at"]
    
    def get_order_number (self, instance):
        return instance.order.order_number
    
    def get_order_quantity (self, instance):
            return instance.order.order_quantity
    


class WeldingSerializer(serializers.ModelSerializer):
    
    order_number = serializers.SerializerMethodField()

    class Meta:
        model = Welding
        exclude = ["id", "updated_at"]
    
    def get_order_number (self, instance):
        return instance.order.order_number
    



class BoardImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ("board_img",)
        
class BoardImagesBotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ("board_img_bot",)





# CREARE SERIALIZER FOGLIO DI PRODUZIONE
class ProductionDetailsSerializer(serializers.ModelSerializer):

    order_verify = SmtSerializer(many=False, read_only=True)
    order_shipping = ShippingSerializer(many=True, read_only=True)
    order_smt = SmtSerializer(many=False, read_only=True)
    order_verify = VerifySerializer(many=False, read_only=True)
    order_test = TestSerializer(many=False, read_only=True)
    board_name= serializers.SerializerMethodField()
    board_code= serializers.SerializerMethodField()


    class Meta:
        model = Order
        exclude = ["updated_at"]


    def get_board_name (self, instance):
            return instance.board.board_name
    def get_board_code (self, instance):
            return instance.board.board_code
    
