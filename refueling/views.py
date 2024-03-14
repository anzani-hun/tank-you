from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Refuel
from .serializers import RefuelSerializer


from django.contrib.auth.models import AnonymousUser
# Create your views here.

@api_view(['GET'])
def getRefuels(request):
    if not isinstance(request.user, AnonymousUser):
        refuels = Refuel.objects.filter(user = request.user).order_by('-refuel_date')
        serialized = RefuelSerializer(refuels, many = True)
        return Response(serialized.data)
    return Response({'message':'User is undefined.'})


@api_view(['GET'])
def getConsumption(request):
    if isinstance(request.user, AnonymousUser):
        return Response({'message':'User is undefined. - Nincs elég adat, azaz tankolás'})

    refuels = Refuel.objects.filter(user = request.user).order_by('-refuel_date')
    
    if len(refuels) < 2:
        return Response({'message':'Not enough data'})

    consumption = None
    last = refuels[0]
    before = refuels[1]

    distance = last.distance - before.distance
    
    consumption = (last.petrol_amount_litre/distance)*100
    
    return Response({'consumption': round(consumption, 1)})


from django.shortcuts import redirect

@api_view(['POST'])
def saveNewRefuel(request):

    refuel = Refuel()
    refuel.user = request.user
    refuel.distance = request.POST['distance']
    refuel.petrol_amount_litre = request.POST['petrol_amount_litre']
    refuel.refuel_date = request.POST['refuel_date']
    refuel.save()
    
    return redirect('index')


    