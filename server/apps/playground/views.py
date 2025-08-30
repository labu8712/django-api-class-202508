from django.http import Http404
from rest_framework.decorators import api_view
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


class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=400)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "ok"}, status=201)


# GET /xxxxxx/items/<id> => 得到資料庫中指定的 Items


class ItemDetailView(APIView):
    def get_item(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, item_id):
        item = self.get_item(item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def delete(self, request, item_id):
        item = self.get_item(item_id)
        item.delete()
        return Response(status=204)

    def put(self, request, item_id):
        item = self.get_item(item_id)

        serializer = ItemSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
