from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 
from django.shortcuts import render
import os
import pandas as pd
import numpy as np
# Create your views here.

os.chdir(r"C:\Users\suraj\Downloads")
os.getcwd()
os.listdir()
df = pd.read_csv('covid_data_filter.csv', encoding='utf-8', na_values=None, error_bad_lines=False)

# df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv', encoding='utf-8', na_values=None, error_bad_lines=False)
df = df.sort_values(by='total_vaccinations', ascending=False)
df.continent = df.continent.str.replace(' ','_')
df.location = df.location.str.replace(' ','_')

def Index(request):
    Country_vacc = {}

    for country in df['location'].unique():    #Create Country_vacc dict for all countery & Total vaccine
        df1 = df[['location', 'date', 'total_vaccinations']][df['location'] == country]
        df1 = int(df1['total_vaccinations'].fillna(0).max())
        Country_vacc[country] = df1

    conti_name = list(df['continent'].unique()[1:])

    context_for_continent = {}

    for i in conti_name:
        temp = Country_vacc.get(i)
        context_for_continent[i] = temp

    Africa = context_for_continent.get('Africa')
    Asia = context_for_continent.get('Asia')
    Europe = context_for_continent.get('Europe')
    Oceania = context_for_continent.get('Oceania')
    South_America = context_for_continent.get('South_America')
    North_America = context_for_continent.get('North_America')

    for i in conti_name:  #deletion 
        del Country_vacc[i]
    del Country_vacc["World"]
    
    #Now Creating lable1 = Unique_country names and data1 = Total_Vaccine count for graph Country map
    Unique_country_names = []  #contain Unique_country names
    Total_Vaccine_count = []   #contain Total_Vaccine count

    for i, j in Country_vacc.items():
        Unique_country_names.append(i)
        Total_Vaccine_count.append(j)
        
    Total_Vaccine_sum_leftside_graph = sum(Total_Vaccine_count)   #Total in infacted in All over World   
    
    #for True condition 
    ShowMap = 'True'  #this is for display using true/false condition display in this section graph model
    
    context = {'North_America': North_America,'Asia': Asia,'Europe': Europe,'South_America': South_America,'Africa': Africa,'Oceania': Oceania,'Unique_country_names': Unique_country_names, 'Total_Vaccine_count': Total_Vaccine_count, 'Total_Vaccine_sum_leftside_graph': Total_Vaccine_sum_leftside_graph, 'ShowMap':ShowMap}
    
    return render(request, 'index.html', context)

def SingleCountry(request):
    Country_vacc = {}

    for country in df['location'].unique():    #Create Country_vacc dict for all countery & Total vaccine
        df1 = df[['location', 'date', 'total_vaccinations']][df['location'] == country]
        df1 = int(df1['total_vaccinations'].fillna(0).max())
        Country_vacc[country] = df1

    conti_name = list(df['continent'].unique()[1:])

    for i in conti_name:  #deletion 
        del Country_vacc[i]
    del Country_vacc["World"]
    
    #Now Creating lable1 = Unique_country names and data1 = Total_Vaccine count for graph Country map
    Unique_country_names = []  #contain Unique_country names
    Total_Vaccine_count = []   #contain Total_Vaccine count

    for i, j in Country_vacc.items():
        Unique_country_names.append(i)
        Total_Vaccine_count.append(j)
         
    Total_Vaccine_sum_leftside_graph = sum(Total_Vaccine_count)   #Total in infacted in All over World
    
    Country = request.POST.get('countryName')
    total_count_Contry_vacine = Country_vacc.get(Country)
    df2 = df[['date', 'total_vaccinations','people_fully_vaccinated','new_cases','new_deaths']][df['location'] == Country]
    df2 = df2[:30]         #Filter 30 days dataset
    df2 = df2.sort_values(by='total_vaccinations', ascending=True)  
    Date_for_graph = df2['date'].to_list()  #data-column to list
    temp1 = df2['total_vaccinations'].fillna(0).to_list()  #data-column to list
    temp2 = df2['people_fully_vaccinated'].fillna(0).to_list()
    temp3 = df2['new_cases'].fillna(0).to_list() 
    temp4 = df2['new_deaths'].fillna(0).to_list() 

    #Converting float to int 

    total_vaccinations = []
    for item1 in temp1:
        total_vaccinations.append(int(item1))
               
    people_fully_vaccinated = []
    for item2 in temp2:
        people_fully_vaccinated.append(int(item2))   
        
    new_cases = []
    for item3 in temp3:
        new_cases.append(int(item3))
        
    new_deaths = []
    for item4 in temp4:
        new_deaths.append(int(item4))

    total_vaccinations_sum = sum(total_vaccinations)      #sum of total_vaccinations
    people_fully_vaccinated_sum = sum(people_fully_vaccinated)      #sum of people_fully_vaccinated

    new_cases_sum = sum(new_cases)
    new_deaths_sum = sum(new_deaths)

    #for True condition 
    ShowMap = 'False'  #this is for display using true/false condition display in this section graph model
    
    context = {'total_count_Contry_vacine':total_count_Contry_vacine,'Unique_country_names': Unique_country_names, 'Total_Vaccine_count': Total_Vaccine_count, 'Total_Vaccine_sum_leftside_graph': Total_Vaccine_sum_leftside_graph, 'total_vaccinations_sum':total_vaccinations_sum,'new_cases_sum':new_cases_sum,'new_deaths_sum':new_deaths_sum,'people_fully_vaccinated':people_fully_vaccinated,'Date_for_graph': Date_for_graph, 'total_vaccinations': total_vaccinations, 'people_fully_vaccinated_sum':people_fully_vaccinated_sum,'new_cases':new_cases,'new_deaths':new_deaths,'Country':Country,'ShowMap':ShowMap}
    
    return render(request, 'new.html', context)