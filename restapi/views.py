from django.http import HttpResponse
from .decoraters import controller_api
from .models import DriverLocation,Driver
import math, json


def grab_nearbyCabs(location):
    R = 6373.0
    lat1 = math.radians(location[0])
    lon1 = math.radians(location[1])
    availiable_cabs =[]
    for cab in DriverLocation.objects.all():        
        lat2 = math.radians(cab.lat)
        lon2 = math.radians(cab.long)
        dlon = lon2 - lon1
        dlat = lat2 - lat1  
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        if round(distance) <= 4:
            availiable_cabs.append(cab)
    return  availiable_cabs       
            
            

def index(requests):
    return HttpResponse("Hello, world. You're at Rest.")
    
@controller_api   
def driver(request):
    
    if request.method == 'POST':
        postdata = json.loads(request.body)
        name = postdata.get('name')
        email = postdata.get('email')
        phone = postdata.get('phone_number')
        liscence = postdata.get('license_number')
        carNumber = postdata.get('car_number')
        newdriver = Driver.objects.create(name=name, email=email,phone=phone, liscence=liscence , carNumber=carNumber)
        data = {"id":newdriver.id,  
                "name": newdriver.name,
                "email":newdriver.email, 
                "phone_number":newdriver.phone, 
                "license_number": newdriver.liscence ,
                "car_number": newdriver.carNumber}
        return HttpResponse(json.dumps(data), content_type="application/json", status=201) 


@controller_api 
def driverLocation(request,id):
    if request.method == 'POST':
        driver = Driver.objects.filter(pk= id).first()
        if not driver:
            raise ValueError
        postdata = json.loads(request.body)
        lat = postdata.get("latitude")
        long = postdata.get("longitude")
        location = DriverLocation.objects.create(lat=lat, long=long, driver=driver)
        data = {"status": "success"}
        return HttpResponse(json.dumps(data), content_type="application/json", status=202)
        
        
@controller_api        
def passengers(request):
    if request.method == 'POST':
        postdata = json.loads(request.body)
        lat = postdata.get("latitude")
        long = postdata.get("longitude")
        cabs = grab_nearbyCabs((lat,long))
        if not cabs:
            data = { "message": "No cabs available!"}
        else:            
            available_cabs = [{"name": cab.driver.name,
                               "car_number": cab.driver.carNumber,
                               "phone_number":cab.driver.phone} for cab in cabs]
            data = {"available_cabs":available_cabs}
        
        return HttpResponse(json.dumps(data), content_type="application/json", status=200)
        
        
     
        
        