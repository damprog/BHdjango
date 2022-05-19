from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from BeHealthyApp.models import Packages, Users, Recipes, Feedback
from BeHealthyApp.serializers import PackageSerializer, UserSerializer, RecipeSerializer, FeedbackSerializer

from django.core.files.storage import default_storage


# Create your views here.

# Package
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
        

# User
@csrf_exempt
def userApi(request, id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(UserId=user_data['UserId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.")

    elif request.method=='DELETE':
        user=Users.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


# Recipe
@csrf_exempt
def recipeApi(request, id=0):
    if request.method=='GET':
        recipes = Recipes.objects.all()
        recipes_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)
    
    elif request.method=='POST':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        recipe_data = JSONParser().parse(request)
        recipe = Recipes.objects.get(RecipeId=recipe_data['RecipeId'])
        recipe_serializer = RecipeSerializer(recipe, data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.")

    elif request.method=='DELETE':
        recipe=Recipes.objects.get(RecipeId=id)
        recipe.delete()
        return JsonResponse("Deleted Successfully!", safe=False)



# Feedback
@csrf_exempt
def feedbackApi(request, id=0):
    if request.method=='GET':
        feedback = Feedback.objects.all()
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False)
    
    elif request.method=='POST':
        feedback_data = JSONParser().parse(request)
        feedback_serializer = FeedbackSerializer(data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method=='PUT':
        feedback_data = JSONParser().parse(request)
        feedback = Feedback.objects.get(FeedbackId=feedback_data['FeedbackId'])
        feedback_serializer = FeedbackSerializer(feedback, data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        feedback=Feedback.objects.get(FeedbackId=id)
        feedback.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

# Photo
@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)