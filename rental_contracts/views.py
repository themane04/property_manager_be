from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rental_contracts.models import RentalContract
from rental_contracts.serliazer import RentalContractSerializer
from rental_units.models import RentalUnit
from tenants.models import Tenant


class RentalContractListCreateView(APIView):
    def get(self, request):
        try:
            contracts = RentalContract.objects()
            serializer = RentalContractSerializer(contracts, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def post(self, request):
        serializer = RentalContractSerializer(data=request.data)
        if serializer.is_valid():
            try:
                RentalUnit.objects.get(id=serializer.validated_data["rental_unit"])
                Tenant.objects.get(id=serializer.validated_data["tenant"])

                contract = RentalContract(
                    tenant=serializer.validated_data["tenant"],
                    rental_unit=serializer.validated_data["rental_unit"],
                    start_of_contract=serializer.validated_data["start_of_contract"],
                    end_of_contract=serializer.validated_data["end_of_contract"],
                    rent=serializer.validated_data["rent"],
                    deposit=serializer.validated_data["deposit"],
                    status=serializer.validated_data["status"]
                )
                contract.save()

                return Response(RentalContractSerializer(contract).data, status=status.HTTP_201_CREATED)

            except (RentalUnit.DoesNotExist, Tenant.DoesNotExist):
                return Response({"error": "Tenant or Rental Unit not found"},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalContractDetailView(APIView):
    def get_object(self, pk):
        try:
            return RentalContract.objects.get(id=pk)
        except RentalContract.DoesNotExist:
            return None

    def get(self, request, pk):
        contract = self.get_object(pk)
        if contract is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RentalContractSerializer(contract)
        return Response(serializer.data)

    def patch(self, request, pk):
        contract = self.get_object(pk)
        if contract is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for attr, value in request.data.items():
            setattr(contract, attr, value)
        contract.save()
        return Response(RentalContractSerializer(contract).data)

    def delete(self, request, pk):
        contract = self.get_object(pk)
        if contract is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
