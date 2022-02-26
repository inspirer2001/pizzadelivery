from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    # flavour=serializers.CharField(max_length=40)

    class Meta:
        model=Order 
        fields=['id','order_status', 'size', 'quantity']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_status=serializers.CharField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    placed_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    # flavour=serializers.CharField(max_length=40)

    class Meta:
        model=Order 
        fields=['id','order_status', 'size', 'quantity','placed_at','updated_at']
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=25)

    class Meta:
        model=Order
        fields=['order_status']