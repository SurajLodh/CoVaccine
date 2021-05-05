from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
#implement
import pandas as pd
import numpy as np
import json
import os
from json import dumps

# Create your views here.

class PersonView(APIView):

    def get(self, request, format=None):
        os.chdir(r"C:\Users\suraj\Downloads")
        os.getcwd()
        os.listdir()
        df = pd.read_csv('covid_data_filter.csv', encoding='utf-8', na_values=None, error_bad_lines=False)

        # df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv', encoding='utf-8', na_values=None, error_bad_lines=False)
        df = df.sort_values(by='total_vaccinations', ascending=False).fillna(0)
        df.continent = df.continent.str.replace(' ','_')
        df.location = df.location.str.replace(' ','_')
       
        conti_name = list(df['continent'].unique()[1:])

        conti = {}
        for i in conti_name:
            df2 = df[df['continent'] == i][['date', 'total_vaccinations','people_fully_vaccinated']]
            df2 = df2[:30]
            df2 = df2.sort_values(by='total_vaccinations', ascending=True)
            df2.set_index("date", inplace = True)
            result = df2.to_json(orient='table')
            parsed_result = json.loads(result)
            data2 = parsed_result['data']
            conti[i] = data2

        return Response(conti) 