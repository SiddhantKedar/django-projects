from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mumbai'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=be387b80ca91aa89f49e1f9ab6fa27a2'
    PARAMS = {'units': 'metric'}

    data = requests.get(url, PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()
    print(temp, day)
    return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon, 'temp': temp, 'day': day})