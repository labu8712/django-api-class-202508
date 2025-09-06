from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,  # 負責處理建立 (POST)
    DestroyModelMixin,  # 負責處理刪除 (DELETE)
    ListModelMixin,  # 負責列表 (GET)
    RetrieveModelMixin,  # 負責單一物件存取 (GET)
    UpdateModelMixin,  # 負責更新 (PUT, PATCH)
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from server.apps.playground.models import Item
from server.apps.playground.serializers import ItemSerializer


@api_view(["GET", "POST"])
def hello(request):
    if request.method == "GET":
        message = "Hello World by GET method"
    else:
        message = "Hello World by POST method"

    return Response({"message": message})


class HiView(APIView):
    def _build_message(self, method):
        return f"Hihi with {method} method"

    def get(self, request):
        return Response({"message": self._build_message("GET")})

    def post(self, request):
        return Response({"message": self._build_message("POST")})


# GET /xxxxxx/items => 得到資料庫中所有的 Items


class ItemListView(ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


# GET /xxxxxx/items/<id> => 得到資料庫中指定的 Items

## 版本一
# class ItemDetailView(
#     RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView
# ):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()
#     lookup_url_kwarg = "item_id"

#     def get(self, request, item_id):
#         return self.retrieve(request, item_id)

#     def delete(self, request, item_id):
#         return self.destroy(request, item_id)

#     def put(self, request, item_id):
#         return self.update(request, item_id)

#     def patch(self, request, item_id):
#         return self.partial_update(request, item_id)


## 版本二
class ItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_url_kwarg = "item_id"


## ========== ViewSet ==========


class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
