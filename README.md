# Me-API Playground

A Django REST API backend with a minimal frontend for showcasing a personal candidate profile, including skills, projects, work experience, and social links.

## Overview

This project demonstrates a simple yet complete backend API built with Django and Django REST Framework, using MySQL as the database. It includes CRUD operations for profile data, project listings with skill filtering, skill popularity ranking, and search functionality across projects and skills. A minimal HTML/JS frontend is provided to interact with the APIs.

## Architecture

- **Backend**: Django 6.0.1 with Django REST Framework
- **Database**: MySQL
- **Frontend**: Plain HTML + JavaScript (no frameworks)
- **CORS**: Enabled for frontend-backend communication

### Database Schema

- **Profile**: Stores personal information (name, email, education, bio)
- **Skill**: Unique skills (e.g., Python, Django)
- **Project**: Projects with descriptions, links, and associated skills (many-to-many)
- **WorkExperience**: Professional experience (company, role, dates, description)
- **SocialLinks**: Social media and portfolio links

## Local Setup

### Prerequisites

- Python 3.8+
- MySQL
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd me-api-playground/me_api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
    - Create a database named `me_api_db`
    - Update `settings.py` with your MySQL credentials if different

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Seed the database:
   ```bash
   python manage.py seed
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

8. Open the frontend:
   - Open `frontend/index.html` in your browser
   - Ensure the backend is running on `http://localhost:8000`
   - The frontend will automatically load profile and projects data
   - Use the search sections to filter projects by skill or search globally

## API Endpoints

### Health Check
- **GET** `/api/health/`
  - Returns: `{"status": "ok"}`

### Profile
- **GET** `/api/profile/`
  - Returns the profile data
- **POST** `/api/profile/`
  - Creates a new profile
- **PUT** `/api/profile/`
  - Updates the existing profile

### Projects
- **GET** `/api/projects/`
  - Returns all projects
- **GET** `/api/projects/?skill=<skill_name>`
  - Returns projects filtered by skill

### Skills
- **GET** `/api/skills/top/`
  - Returns skills sorted by project count (descending)

### Search
- **GET** `/api/search/?q=<query>`
  - Searches across project titles, descriptions, skills

### Example API Calls

```bash
# Health check
curl http://localhost:8000/api/health/

# Get profile
curl http://localhost:8000/api/profile/

# Get all projects
curl http://localhost:8000/api/projects/

# Get projects with Python skill
curl "http://localhost:8000/api/projects/?skill=Python"

# Get top skills
curl http://localhost:8000/api/skills/top/

# Search for "Django"
curl "http://localhost:8000/api/search/?q=Django"
```

## Seeding the Database

Run the seed command to populate the database with sample data:

```bash
python manage.py seed
```

This creates a sample profile for "John Doe", several skills, projects, work experience, and social links.

## Known Limitations

- Assumes a single profile (first object returned)
- No authentication or authorization
- Frontend is basic and not responsive
- Search is case-insensitive but simple (no advanced querying)
- No pagination on list endpoints
- Hardcoded database credentials in settings.py

## Resume Link

For a full resume, visit: [Placeholder - Add your resume link here]

## Contributing

This is a demonstration project. Feel free to fork and extend with additional features like authentication, pagination, or a more advanced frontend.