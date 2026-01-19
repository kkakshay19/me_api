from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    education = models.TextField()
    bio = models.TextField(blank=True)

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.JSONField(default=dict)
    skills = models.ManyToManyField(Skill, related_name="projects")

class SocialLinks(models.Model):
    github = models.URLField()
    linkedin = models.URLField()
    portfolio = models.URLField(blank=True)
