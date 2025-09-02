import yaml
import os
import shutil

def load_template(template_name):
    try:
        with open(f'templates/{template_name}', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Template '{template_name}' not found.")
        exit(1)

def load_courses():
    try:
        with open('courses/courses.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Error: 'courses/courses.yaml' file not found.")
        exit(1)

def render_homepage(courses):
    base_template = load_template('base.html')
    
    course_cards_html = ""
    for course in courses:
        course_cards_html += f"""
        <div class="course-card">
            <div class="course-icon">{course['icon']}</div>
            <h3>{course['title']}</h3>
            <p>{course['description']}</p>
            <a href="/{course['page_name']}/" class="btn-primary">Access Course Content</a>
        </div>
        """
    
    homepage_content = f"""
    <section class="hero">
        <h1>Master Cybersecurity</h1>
        <p class="lead">Professional courses with video tutorials, PDF resources, and reference materials for aspiring ethical hackers.</p>
    </section>

    <section id="courses">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 2rem;">Available Courses</h2>
            <div class="course-grid">
                {course_cards_html}
            </div>
        </div>
    </section>
    
    <section style="padding: 4rem 2rem; text-align: center; background: var(--bg-secondary);">
        <div class="container">
            <h2>What's Included in Each Course?</h2>
            <div class="media-grid" style="margin-top: 3rem;">
                <div class="media-card">
                    <h3>🎬 Video Tutorials</h3>
                    <p>Step-by-step video demonstrations of techniques and tools.</p>
                </div>
                <div class="media-card">
                    <h3>📚 PDF Guides</h3>
                    <p>Comprehensive documentation and cheatsheets for reference.</p>
                </div>
                <div class="media-card">
                    <h3>🖼️ Visual References</h3>
                    <p>Screenshots, diagrams, and reference images.</p>
                </div>
            </div>
        </div>
    </section>
    """
    
    return base_template.replace("{{ content }}", homepage_content)

def render_course_page(course):
    base_template = load_template('base.html')
    course_template = load_template('course.html')
    
    course_content = course_template
    for key, value in course.items():
        placeholder = "{{ " + key + " }}"
        course_content = course_content.replace(placeholder, str(value))
    
    full_page = base_template.replace("{{ content }}", course_content)
    return full_page

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    print("Building SecuriLearn website with media support...")
    
    courses = load_courses()
    
    homepage_html = render_homepage(courses)
    with open('index.html', 'w') as file:
        file.write(homepage_html)
    print("✓ Generated index.html")
    
    for course in courses:
        course_dir = course['page_name']
        ensure_directory(course_dir)
        
        course_html = render_course_page(course)
        with open(f'{course_dir}/index.html', 'w') as file:
            file.write(course_html)
        print(f"✓ Generated {course_dir}/index.html")
    
    # Create assets directories if they don't exist
    for asset_type in ['videos', 'images', 'pdfs', 'icons']:
        ensure_directory(f'assets/{asset_type}')
    
    print("Build complete! Your media-ready website is ready.")
    print("You can now add your files to:")
    print("  - assets/videos/    for video files")
    print("  - assets/images/    for image files") 
    print("  - assets/pdfs/      for PDF files")
    print("  - assets/icons/     for icon files")

if __name__ == "__main__":
    main()

# ... existing code ...

def render_auth_page():
    base_template = load_template('base.html')
    auth_template = load_template('auth.html')
    return base_template.replace("{{ content }}", auth_template)

def render_xss_labs_page():
    try:
        with open('xss-labs/index.html', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "XSS Labs page not found"

def main():
    print("Building SecuriLearn website with new features...")
    
    courses = load_courses()
    
    # Render main pages
    homepage_html = render_homepage(courses)
    with open('index.html', 'w') as file:
        file.write(homepage_html)
    print("✓ Generated index.html")
    
    # Render auth page
    auth_html = render_auth_page()
    ensure_directory('auth')
    with open('auth/index.html', 'w') as file:
        file.write(auth_html)
    print("✓ Generated auth/index.html")
    
    # Render XSS labs page
    ensure_directory('xss-labs')
    xss_labs_html = render_xss_labs_page()
    with open('xss-labs/index.html', 'w') as file:
        file.write(xss_labs_html)
    print("✓ Generated xss-labs/index.html")
    
    # Render course pages
    for course in courses:
        course_dir = course['page_name']
        ensure_directory(course_dir)
        
        course_html = render_course_page(course)
        with open(f'{course_dir}/index.html', 'w') as file:
            file.write(course_html)
        print(f"✓ Generated {course_dir}/index.html")
    
    print("Build complete! New features added:")
    print("  - Auth system (Signup/Login)")
    print("  - XSS Learning Labs")
    print("  - Spelling corrections")

# ... rest of the code ...
