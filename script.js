// Theme Toggling Functionality
const themeToggleBtn = document.getElementById('theme-toggle');
const currentTheme = localStorage.getItem('theme') || 'light';

document.documentElement.setAttribute('data-theme', currentTheme);
updateThemeButtonText(currentTheme);

themeToggleBtn.addEventListener('click', () => {
    let newTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeButtonText(newTheme);
});

function updateThemeButtonText(theme) {
    themeToggleBtn.textContent = theme === 'light' ? '🌙' : '☀️';
}

// Media Preview functionality
document.addEventListener('DOMContentLoaded', function() {
    const downloadButtons = document.querySelectorAll('.download-btn');
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const mediaType = this.closest('.media-card').querySelector('h3').textContent;
            alert(`🔒 This ${mediaType.includes('Video') ? 'video' : mediaType.includes('PDF') ? 'PDF' : 'image'} content is available after enrollment. Payment integration coming soon!`);
        });
    });
    
    // Smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});


// Auth functionality
document.addEventListener('DOMContentLoaded', function() {
    // Auth tabs functionality
    const authTabs = document.querySelectorAll('.auth-tab');
    const authForms = document.querySelectorAll('.auth-form-content');
    
    if (authTabs.length > 0) {
        authTabs.forEach(tab => {
            tab.addEventListener('click', function() {
                const tabName = this.getAttribute('data-tab');
                
                // Update active tab
                authTabs.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                
                // Show corresponding form
                authForms.forEach(form => {
                    form.classList.remove('active');
                    if (form.id === `${tabName}-form`) {
                        form.classList.add('active');
                    }
                });
            });
        });
    }
    
    // Password strength indicator
    const passwordInput = document.getElementById('signup-password');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const strengthBar = document.querySelector('.strength-bar');
            const strengthText = document.querySelector('.strength-text');
            const password = this.value;
            
            let strength = 0;
            if (password.length >= 8) strength++;
            if (password.match(/[a-z]/)) strength++;
            if (password.match(/[A-Z]/)) strength++;
            if (password.match(/[0-9]/)) strength++;
            if (password.match(/[^a-zA-Z0-9]/)) strength++;
            
            const width = (strength / 5) * 100;
            strengthBar.style.width = `${width}%`;
            
            if (strength <= 2) {
                strengthBar.style.background = '#ff4757';
                strengthText.textContent = 'Weak';
            } else if (strength <= 4) {
                strengthBar.style.background = '#ffa502';
                strengthText.textContent = 'Medium';
            } else {
                strengthBar.style.background = '#2ed573';
                strengthText.textContent = 'Strong';
            }
        });
    }
    
    // Form submission
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('🔒 Login functionality will be implemented with backend integration');
        });
    }
    
    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const password = document.getElementById('signup-password').value;
            const confirm = document.getElementById('signup-confirm').value;
            
            if (password !== confirm) {
                alert('❌ Passwords do not match!');
                return;
            }
            
            alert('✅ Account creation functionality will be implemented with backend integration');
        });
    }
    
    // XSS Lab functionality
    const testButton = document.querySelector('.submit-btn');
    if (testButton) {
        testButton.addEventListener('click', function() {
            alert('🔒 XSS payload testing will be implemented with proper sandboxing');
        });
    }
});
