from django.shortcuts import render
from rest_framework import viewsets

from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer


class DrugViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Drugs.
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class VaccinationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Vaccinations.
    """
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
