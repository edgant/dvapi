from django.shortcuts import render
from django.db.models import ProtectedError
from rest_framework import authentication, viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer


class DrugHasVaccinations(APIException):
    status_code = 400
    default_detail = 'Cannot delete. This drug has vaccinations associated.'
    default_code = 'bad_request'


class DrugViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Drugs.
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk=None):
        try:
            return super().destroy(request, pk)
        except ProtectedError:
            raise DrugHasVaccinations


class VaccinationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Vaccinations.
    """
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    permission_classes = [IsAuthenticated]
