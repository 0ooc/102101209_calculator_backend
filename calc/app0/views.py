from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CalculationsSerializer
from .models import Calculations
# Create your views here.

@api_view(['GET'])
def huode(request):
    print(request)
    ten = Calculations.objects.order_by('-id')[:10]  #取最新的10个历史记录
    serializer2 = CalculationsSerializer(ten, many=True)
    out={"data":serializer2.data}
    return Response(out)

@api_view(['POST'])
def shangchuan(request):
        print(request)
        serializer =CalculationsSerializer(data=request.data)  #将要被反序列化的数据request.data传入data参数
        if serializer.is_valid():  #数据验证
            serializer.save()     #保存数据
        return Response({"answer": "history"}, status=200)

