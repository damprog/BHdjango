from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from BeHealthyApp.models import Packages, Users, Recipes, Feedback
from BeHealthyApp.serializers import PackageSerializer, UserSerializer, RecipeSerializer, FeedbackSerializer


# Create your views here.
@csrf_exempt
def packageApi(request, id=0):
    if request.method=='GET':
        packages = Packages.objects.all()
        packages_serializer = PackageSerializer(packages, many=True)
        return JsonResponse(packages_serializer.data, safe=False)
    
    elif request.method=='POST':
        package_data = JSONParser().parse(request)
        package_serializer = PackageSerializer(data=package_data)
        if package_serializer.is_valid():
            package_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        package_data = JSONParser().parse(request)
        package = Packages.objects.get(PackageId=package_data['PackageId'])
        package_serializer = PackageSerializer(package, data=package_data)
        if package_serializer.is_valid():
            package_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.")

    elif request.method=='DELETE':
        package=Packages.objects.get(PackageId=id)
        package.delete()
        return JsonResponse("Deleted Successfully!", safe=False)
        