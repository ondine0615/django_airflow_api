from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import KipoAdminRegBs
from .serializers import KipoSerializer
# Create your views here.


class KipoListApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        kp = KipoAdminRegBs.objects.all()
        serializer= KipoSerializer(kp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            "registernumber" : request.data.get("registernumber"),
            "registerationdate" : request.data.get("registerationdate"),
                  "examinationdate" : request.data.get("examinationdate"),
                  "existduringdate" : request.data.get("existduringdate"),
                  "lapscause":request.data.get("lapscause"),
                  "lapsdate":request.data.get("lapsdate"),
                  "applicationnumber":request.data.get("applicationnumber"),
                  "applicationdate":request.data.get("applicationdate"),
                  "publicationnumber":request.data.get("publicationnumber"),
                  "publicationdate":request.data.get("publicationdate"),
                  "internationregistrationnumber":request.data.get("internationregistrationnumber"),
                  "internationregistrationdate":request.data.get("internationregistrationdate"),
                  "originalapplicationnumber":request.data.get("originalapplicationnumber"),
                  "originalapplicationdate":request.data.get("originalapplicationdate"),
                  "classificationcode":request.data.get("classificationcode"),
                  "inventiontitle":request.data.get("inventiontitle"),
                  "inventiontitleeng":request.data.get("inventiontitleeng"),
                  "claimcount":request.data.get("claimcount"),
                  "prioritycountry":request.data.get("prioritycountry"),
                  "prioritydate":request.data.get("prioritydate"),
                  "prioritycount":request.data.get("prioritycount"),
                  "id":request.data.get("id")
                }
        serializer=KipoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
