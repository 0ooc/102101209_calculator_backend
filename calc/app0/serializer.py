from rest_framework import serializers
from app0.models import Calculations
# 继承自serializers.ModelSerializer
class CalculationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculations  # 指定要依据的模型类
        fields = '__all__'    # 设置全部字段自动生成
