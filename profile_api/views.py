from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from .models import Profile, Skill, Project, WorkExperience, SocialLinks
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer, WorkExperienceSerializer, SocialLinksSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        if profile:
            social_links = SocialLinks.objects.first()
            data = ProfileSerializer(profile).data
            if social_links:
                data['github'] = social_links.github
                data['linkedin'] = social_links.linkedin
                data['portfolio'] = social_links.portfolio
            return Response(data)
        return Response({"message": "No profile found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        profile = Profile.objects.first()
        if profile:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "No profile found"}, status=status.HTTP_404_NOT_FOUND)

class ProjectsView(APIView):
    def get(self, request):
        skill_name = request.query_params.get('skill')
        if skill_name:
            projects = Project.objects.filter(skills__name__icontains=skill_name)
        else:
            projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class SkillsTopView(APIView):
    def get(self, request):
        skills = Skill.objects.annotate(project_count=Count('projects')).order_by('-project_count')
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"message": "Query parameter 'q' is required"}, status=status.HTTP_400_BAD_REQUEST)
        projects = Project.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(skills__name__icontains=query)
        ).distinct()
        skills = Skill.objects.filter(name__icontains=query)
        result = {
            "projects": ProjectSerializer(projects, many=True).data,
            "skills": SkillSerializer(skills, many=True).data
        }
        return Response(result)
