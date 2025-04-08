from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField()

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    total_points = models.IntegerField()

class Workout(models.Model):
    workout_name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)