from django.db import models

# Create your models here.
class Packages(models.Model):
    PackageId = models.AutoField(primary_key=True)
    PackageName = models.CharField(max_length=100)
    Price = models.FloatField()

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100, null=False)
    Admin = models.BooleanField(null=False)
    PhotoFileName = models.CharField(max_length=100)
    Package = models.ForeignKey(Packages, on_delete=models.CASCADE)

class Recipes(models.Model):
    RecipeId = models.AutoField(primary_key=True)
    RecipeName = models.CharField(max_length=50, null=False)
    Category = models.CharField(max_length=50)
    VotesQuantity = models.FloatField()
    AverageOpinion = models.FloatField()
    Description = models.CharField(max_length=300)
    Ingredients = models.CharField(max_length=300)
    PhotoFileName = models.CharField(max_length=100)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)

class Feedback(models.Model):
    FeedbackId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(Users, on_delete=models.CASCADE)
    Email = models.CharField(max_length=100)

