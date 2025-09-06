from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ItemDetailView(GenericAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_url_kwarg = "item_id"

    def get(self, request, item_id):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def delete(self, request, item_id):
        item = self.get_object()
        item.delete()
        return Response(status=204)

    def put(self, request, item_id):
        item = self.get_object()

        serializer = self.get_serializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, item_id):
        item = self.get_object()

        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
