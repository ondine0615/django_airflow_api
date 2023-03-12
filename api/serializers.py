from rest_framework import serializers
from .models import KipoAdminRegBs

class KipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KipoAdminRegBs
        fields = ["registernumber",
                  "registerationdate",
                  "examinationdate",
                  "existduringdate",
                  "lapscause",
                  "lapsdate",
                  "applicationnumber",
                  "applicationdate",
                  "publicationnumber",
                  "publicationdate",
                  "internationregistrationnumber",
                  "internationregistrationdate",
                  "originalapplicationnumber",
                  "originalapplicationdate",
                  "classificationcode",
                  "inventiontitle",
                  "inventiontitleeng",
                  "claimcount",
                  "prioritycountry",
                  "prioritydate",
                  "prioritycount",
                  "id"]