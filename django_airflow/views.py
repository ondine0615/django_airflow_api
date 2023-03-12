from django.shortcuts import render
from django_airflow.models import KipoAdminRegBs
import pandas as pd

def main_view(request):
    kp=KipoAdminRegBs.objects.all().values()
    data=pd.DataFrame(kp)
    context={'df':data.to_html(justify='center')}
    return render(request, 'template/main.html',context)

