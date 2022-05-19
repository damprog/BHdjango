from rest_framework import serializers
from BeHealthyApp.models import Packages, Users, Recipes, Feedback

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ( 'PackageId',
                    'PackageName',
                    'Price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ( 'UserId',
                    'UserName',
                    'Password',
                    'Admin',
                    'PhotoFileName',
                    'Package')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ( 'RecipeId',
                    'RecipeName',
                    'Category',
                    'VotesQuantity',
                    'AverageOpinion',
                    'Description',
                    'Ingredients',
                    'PhotoFileName',
                    'UserId')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ( 'FeedbackId',
                    'UserId',
                    'Email',
                    'Content')