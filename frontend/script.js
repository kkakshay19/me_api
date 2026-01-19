// API configuration
const API_BASE_URL = '/api/';

// Utility function to fetch data from API
async function fetchData(endpoint) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        const data = await response.json();
        if (!response.ok) {
            // Return the error data from the API response
            return { error: data.message || data.error || `HTTP ${response.status}: ${response.statusText}`, ...data };
        }
        return data;
    } catch (error) {
        console.error('API Error:', error);
        return { error: error.message };
    }
}

// Display error message
function displayError(container, message) {
    container.innerHTML = `<div class="error">${message}</div>`;
}

// Display no results message
function displayNoResults(container, message = 'No results found') {
    container.innerHTML = `<p class="no-results">${message}</p>`;
}

// Load and display profile
async function loadProfile() {
    const container = document.getElementById('profile-content');
    const data = await fetchData('profile/');

    if (data.error) {
        displayError(container, `Failed to load profile: ${data.error}`);
        return;
    }

    // Assuming profile includes social links in the response
    // Note: Adjust based on actual API response structure
    container.innerHTML = `
        <div class="profile-item"><strong>Name:</strong> ${data.name || 'N/A'}</div>
        <div class="profile-item"><strong>Email:</strong> ${data.email || 'N/A'}</div>
        <div class="profile-item"><strong>Education:</strong> ${data.education || 'N/A'}</div>
        <div class="profile-item"><strong>Bio:</strong> ${data.bio || 'N/A'}</div>
        <div class="profile-item">
            <strong>Social Links:</strong>
            <div class="social-links">
                ${data.github ? `<a href="${data.github}" target="_blank">GitHub</a>` : ''}
                ${data.linkedin ? `<a href="${data.linkedin}" target="_blank">LinkedIn</a>` : ''}
                ${data.portfolio ? `<a href="${data.portfolio}" target="_blank">Portfolio</a>` : ''}
            </div>
        </div>
    `;
}

// Load and display all projects
async function loadProjects() {
    const container = document.getElementById('projects-content');
    const data = await fetchData('projects/');

    if (data.error) {
        displayError(container, `Failed to load projects: ${data.error}`);
        return;
    }

    if (!data || data.length === 0) {
        displayNoResults(container, 'No projects found');
        return;
    }

    container.innerHTML = data.map(project => `
        <div class="project-card">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="project-skills">
                ${project.skills ? project.skills.map(skill => `<span class="skill-tag">${skill.name}</span>`).join('') : ''}
            </div>
            <div class="project-links">
                ${project.links && project.links.github ? `<a href="${project.links.github}" target="_blank">GitHub</a>` : ''}
                ${project.links && project.links.demo ? `<a href="${project.links.demo}" target="_blank">Demo</a>` : ''}
            </div>
        </div>
    `).join('');
}

// Search projects by skill
async function searchProjectsBySkill() {
    const skillInput = document.getElementById('skill-input');
    const skill = skillInput.value.trim();
    const container = document.getElementById('skill-results');

    if (!skill) {
        displayNoResults(container, 'Please enter a skill name');
        return;
    }

    const data = await fetchData(`projects/?skill=${encodeURIComponent(skill)}`);

    if (data.error) {
        displayError(container, `Search failed: ${data.error}`);
        return;
    }

    if (!data || data.length === 0) {
        displayNoResults(container, `No projects found for skill: ${skill}`);
        return;
    }

    container.innerHTML = data.map(project => `
        <div class="project-card">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="project-skills">
                ${project.skills ? project.skills.map(skill => `<span class="skill-tag">${skill.name}</span>`).join('') : ''}
            </div>
            <div class="project-links">
                ${project.links && project.links.github ? `<a href="${project.links.github}" target="_blank">GitHub</a>` : ''}
                ${project.links && project.links.demo ? `<a href="${project.links.demo}" target="_blank">Demo</a>` : ''}
            </div>
        </div>
    `).join('');
}

// Global search
async function globalSearch() {
    const searchInput = document.getElementById('global-search-input');
    const query = searchInput.value.trim();
    const container = document.getElementById('global-results');

    if (!query) {
        displayNoResults(container, 'Please enter a search term');
        return;
    }

    // Show loading state
    container.innerHTML = '<p>Searching...</p>';

    const data = await fetchData(`search/?q=${encodeURIComponent(query)}`);

    if (data.error) {
        displayError(container, `Search failed: ${data.error}`);
        return;
    }

    let resultsHtml = '';

    // Display matched projects
    if (data.projects && Array.isArray(data.projects) && data.projects.length > 0) {
        resultsHtml += '<h3>Projects</h3>';
        resultsHtml += data.projects.map(project => `
            <div class="project-card">
                <h3>${project.title || 'Untitled Project'}</h3>
                <p>${project.description || 'No description available'}</p>
                <div class="project-skills">
                    ${project.skills && Array.isArray(project.skills) ? project.skills.map(skill => `<span class="skill-tag">${skill.name || skill}</span>`).join('') : ''}
                </div>
                <div class="project-links">
                    ${project.links && project.links.github ? `<a href="${project.links.github}" target="_blank">GitHub</a>` : ''}
                    ${project.links && project.links.demo ? `<a href="${project.links.demo}" target="_blank">Demo</a>` : ''}
                </div>
            </div>
        `).join('');
    }

    // Display matched skills
    if (data.skills && Array.isArray(data.skills) && data.skills.length > 0) {
        resultsHtml += '<h3>Skills</h3>';
        resultsHtml += '<div class="project-skills">';
        resultsHtml += data.skills.map(skill => `<span class="skill-tag">${skill.name || skill}</span>`).join('');
        resultsHtml += '</div>';
    }

    if (!resultsHtml) {
        displayNoResults(container, `No results found for: ${query}`);
        return;
    }

    container.innerHTML = resultsHtml;
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Load initial data
    loadProfile();
    loadProjects();

    // Skill search
    document.getElementById('skill-search-btn').addEventListener('click', searchProjectsBySkill);
    document.getElementById('skill-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            searchProjectsBySkill();
        }
    });

    // Global search
    document.getElementById('global-search-btn').addEventListener('click', globalSearch);
    document.getElementById('global-search-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            globalSearch();
        }
    });
});