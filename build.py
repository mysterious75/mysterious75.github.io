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
            <a href="/{course['page_name']}/" class="btn-primary">Learn More</a>
        </div>
        """
    
    homepage_content = f"""
    <section class="hero">
        <h1>Master Cybersecurity</h1>
        <p class="lead">Professional, in-depth courses for aspiring ethical hackers and security professionals.</p>
    </section>

    <section id="courses">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 2rem;">Our Courses</h2>
            <div class="course-grid">
                {course_cards_html}
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
    print("Building SecuriLearn website...")
    
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

    print("Build complete! Your static site is ready.")

if __name__ == "__main__":
    main()

