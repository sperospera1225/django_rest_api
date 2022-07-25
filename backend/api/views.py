from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def api_post(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # save method create instance -> no way to use get_my_discount()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)



@api_view(["GET", "POST"])
def api_rest(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])

    return Response(data)

# Django Model
def api_product(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])

    # model instance (model_data)
    # turn a python dictionary
    # return JSON to my client
    return JsonResponse(data)
    # HttpResponse로 보내기 위해서는 복잡한 처리과정이 필요함


def api_home(request, *args, **kwargs):
    # request is an instance of http request class
    # JSON : request.body
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET) # <QueryDict: {'abc': ['123']}>
    data['headers'] = dict(request.headers) # Could not be automatically be converted into JSON -> enforce dictionary value
    data['content_type'] = request.content_type
    return JsonResponse(data)