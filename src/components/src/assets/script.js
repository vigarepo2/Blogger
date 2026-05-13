// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Dark Mode Logic
const themeToggle = document.getElementById('dark-toggle');
const htmlElement = document.documentElement;

// Check for saved preference
if (localStorage.getItem('theme') === 'dark' || 
    (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    htmlElement.classList.add('dark');
}

themeToggle.addEventListener('click', () => {
    if (htmlElement.classList.contains('dark')) {
        htmlElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    } else {
        htmlElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    }
});
