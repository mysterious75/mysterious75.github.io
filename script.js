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
