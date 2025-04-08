# filepath: octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = [
            {"email": "student1@example.com", "name": "Alice", "age": 16, "team": "Team A"},
            {"email": "student2@example.com", "name": "Bob", "age": 17, "team": "Team B"},
        ]
        for user in users:
            User.objects.create(**user)

        # Populate teams
        teams = [
            {"name": "Team A", "members": ["student1@example.com"]},
            {"name": "Team B", "members": ["student2@example.com"]},
        ]
        for team in teams:
            Team.objects.create(**team)

        # Populate activities
        activities = [
            {"user_email": "student1@example.com", "activity_type": "Running", "duration_minutes": 30, "date": "2025-04-01"},
            {"user_email": "student2@example.com", "activity_type": "Cycling", "duration_minutes": 45, "date": "2025-04-02"},
        ]
        for activity in activities:
            Activity.objects.create(**activity)

        # Populate leaderboard
        leaderboard = [
            {"team": "Team A", "total_points": 100},
            {"team": "Team B", "total_points": 80},
        ]
        for entry in leaderboard:
            Leaderboard.objects.create(**entry)

        # Populate workouts
        workouts = [
            {"workout_name": "Morning Run", "description": "A 5km run to start the day", "difficulty": "Intermediate"},
            {"workout_name": "Evening Yoga", "description": "Relaxing yoga session", "difficulty": "Beginner"},
        ]
        for workout in workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))