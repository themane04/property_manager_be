from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from features.models import Feature
from features.serlializer import FeatureSerializer


class FeatureListCreateView(APIView):
    def get(self, request):
        features = Feature.objects.all()
        if not features:
            return Response({"message": "No features found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeatureSerializer(features, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeatureSerializer(data=request.data)
        if serializer.is_valid():
            feature = Feature(**serializer.validated_data)
            feature.save()
            return Response(FeatureSerializer(feature).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeatureDetailView(APIView):
    def get_object(self, pk):
        try:
            return Feature.objects.get(id=pk)
        except Feature.DoesNotExist:
            return None

    def get(self, request, pk):
        feature = self.get_object(pk)
        if feature is None:
            return Response({"message": "Feature not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = FeatureSerializer(feature)
        return Response(serializer.data)

    def patch(self, request, pk):
        feature = self.get_object(pk)
        if feature is None:
            return Response({"message": "Feature not found."}, status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            if attr != 'id':
                setattr(feature, attr, value)
        feature.save()
        return Response(FeatureSerializer(feature).data)

    def delete(self, request, pk):
        feature = self.get_object(pk)
        if feature is None:
            return Response({"message": "Feature not found."}, status=status.HTTP_404_NOT_FOUND)
        feature.delete()
        return Response({"message": "Feature deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
