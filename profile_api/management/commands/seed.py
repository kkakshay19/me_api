from django.core.management.base import BaseCommand
from profile_api.models import Profile, Skill, Project, WorkExperience, SocialLinks
from datetime import date

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        WorkExperience.objects.all().delete()
        SocialLinks.objects.all().delete()

        # Create Profile
        profile = Profile.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            education="Bachelor of Science in Computer Science",
            bio="Experienced software engineer with a passion for building scalable web applications."
        )

        # Create Skills
        python = Skill.objects.create(name="Python")
        django = Skill.objects.create(name="Django")
        postgresql = Skill.objects.create(name="PostgreSQL")
        javascript = Skill.objects.create(name="JavaScript")
        react = Skill.objects.create(name="React")

        # Create Projects
        project1 = Project.objects.create(
            title="E-commerce Platform",
            description="A full-stack e-commerce platform built with Django and React.",
            links={"github": "https://github.com/johndoe/ecommerce", "demo": "https://ecommerce-demo.com"}
        )
        project1.skills.add(python, django, postgresql, javascript, react)

        project2 = Project.objects.create(
            title="Task Management App",
            description="A simple task management application using Django REST Framework.",
            links={"github": "https://github.com/johndoe/taskapp"}
        )
        project2.skills.add(python, django, postgresql)

        project3 = Project.objects.create(
            title="Portfolio Website",
            description="Personal portfolio website built with React and hosted on GitHub Pages.",
            links={"github": "https://github.com/johndoe/portfolio", "demo": "https://johndoe.github.io/portfolio"}
        )
        project3.skills.add(javascript, react)

        # Create Work Experience
        WorkExperience.objects.create(
            company="Tech Corp",
            role="Senior Software Engineer",
            description="Developed and maintained web applications using Python and Django.",
            start_date=date(2020, 1, 1),
            end_date=None
        )

        WorkExperience.objects.create(
            company="Startup Inc",
            role="Full Stack Developer",
            description="Built responsive web apps with React and Node.js.",
            start_date=date(2018, 6, 1),
            end_date=date(2019, 12, 31)
        )

        # Create Social Links
        SocialLinks.objects.create(
            github="https://github.com/johndoe",
            linkedin="https://linkedin.com/in/johndoe",
            portfolio="https://johndoe.com"
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))