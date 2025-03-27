from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payments.models import Payment
from payments.serializer import PaymentSerializer


class PaymentListCreateView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            payment = Payment(**serializer.validated_data)
            payment.save()
            return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Payment.objects.get(id=pk)
        except Payment.DoesNotExist:
            return None

    def get(self, request, pk):
        payment = self.get_object(pk)
        if payment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def patch(self, request, pk):
        payment = self.get_object(pk)
        if payment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            setattr(payment, attr, value)
        payment.save()
        return Response(PaymentSerializer(payment).data)

    def delete(self, request, pk):
        payment = self.get_object(pk)
        if payment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
