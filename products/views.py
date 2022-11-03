from rest_framework.response import Response
from rest_framework.decorators import APIView, permission_classes
from .serializers import ProductSerializer, UpdateProductSerializer, HotSerializer, CreateHotSerializer
from rest_framework import status
from .models import Products, Hots
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


class CreateProduct(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            response = {
                "message": "Product created successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        product = Products.objects.all()
        serilizer = self.serializer_class(product, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class Get_Delete_Update_product(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    serializer_class = ProductSerializer
    serializer_update_class = UpdateProductSerializer

    def get(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
            serilizer = self.serializer_class(product, many=False)
            return Response(serilizer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={"Message": "This Product is not in the database"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        product = Products.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        product = Products.objects.get(id=pk)
        serializer = self.serializer_update_class(
            data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': "updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)


class Create_Get_Hot(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateHotSerializer
    serializer_hot = HotSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            response = {
                "message": "Product Created successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        hot = Hots.objects.all()
        serializer = self.serializer_hot(hot, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Update_Delete_Hot(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    serializer_class = HotSerializer

    def post(self, request, pk):
        hot = Hots.objects.get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=hot)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': "updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        hot = Hots.objects.get(id=pk)
        hot.delete()
        return Response(data={"Product Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
