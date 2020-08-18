from django.shortcuts import render
from rest_framework import authentication, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer


class DrugViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Drugs.
    """
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    permission_classes = [IsAuthenticated]


class VaccinationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Vaccinations.
    """
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    permission_classes = [IsAuthenticated]
