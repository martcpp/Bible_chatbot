// Clean markdown content loader for production
async function loadMarkdownContent(filename, contentElementId, loadingElementId, errorElementId) {
    const loadingElement = document.getElementById(loadingElementId);
    const contentElement = document.getElementById(contentElementId);
    const errorElement = document.getElementById(errorElementId);

    try {
        const path = filename;
        const response = await fetch(path);
        
        if (!response.ok) {
            throw new Error(`Failed to load ${filename}: ${response.status} ${response.statusText}`);
        }
        
        const markdownText = await response.text();
        
        if (!markdownText.trim()) {
            throw new Error(`Markdown file ${filename} is empty`);
        }
        
        // Convert markdown to HTML
        const htmlContent = marked.parse(markdownText);
        
        // Hide loading message
        loadingElement.style.display = 'none';
        
        // Show content
        contentElement.innerHTML = htmlContent;
        contentElement.style.display = 'block';
        
        // Apply styling
        applyMarkdownStyles(contentElement);
        
    } catch (error) {
        console.error(`Error loading ${filename}:`, error);
        
        // Hide loading message and show error
        loadingElement.style.display = 'none';
        if (errorElement) {
            errorElement.style.display = 'block';
            errorElement.textContent = `Failed to load ${filename}`;
        }
    }
}

// Apply consistent styling to rendered markdown content
function applyMarkdownStyles(contentElement) {
    const headings = contentElement.querySelectorAll('h1, h2, h3, h4, h5, h6');
    headings.forEach(heading => {
        if (heading.tagName === 'H1') {
            heading.className = 'page-title';
        } else if (heading.tagName === 'H2') {
            heading.style.fontSize = '1.25rem';
            heading.style.fontWeight = '700';
            heading.style.margin = '1.5rem 0 0.75rem';
            heading.style.color = 'var(--primary)';
        }
    });

    const paragraphs = contentElement.querySelectorAll('p');
    paragraphs.forEach(p => {
        p.style.marginBottom = '0.75rem';
        p.style.color = 'var(--text-light)';
        p.style.lineHeight = '1.6';
    });

    const lists = contentElement.querySelectorAll('ul, ol');
    lists.forEach(list => {
        list.style.margin = '0.75rem 0';
        list.style.paddingLeft = '1.5rem';
    });

    const listItems = contentElement.querySelectorAll('li');
    listItems.forEach(li => {
        li.style.marginBottom = '0.5rem';
        li.style.color = 'var(--text-light)';
    });

    const codeElements = contentElement.querySelectorAll('code');
    codeElements.forEach(code => {
        code.style.background = '#f1f5f9';
        code.style.padding = '0.25rem 0.5rem';
        code.style.borderRadius = '4px';
        code.style.fontFamily = "'Monaco', 'Consolas', monospace";
        code.style.fontSize = '0.875rem';
    });

    const blockquotes = contentElement.querySelectorAll('blockquote');
    blockquotes.forEach(quote => {
        quote.style.borderLeft = '4px solid var(--primary)';
        quote.style.paddingLeft = '1rem';
        quote.style.margin = '1rem 0';
        quote.style.fontStyle = 'italic';
        quote.style.background = '#f8fafc';
        quote.style.padding = '1rem';
        quote.style.borderRadius = '0 8px 8px 0';
    });
}

// URL-based routing system
function initRouter() {
    const path = window.location.pathname;
    const page = path.substring(1) || 'home'; // Remove leading slash, default to 'home'
    
    // Valid pages
    const validPages = ['home', 'privacy', 'terms'];
    const currentPage = validPages.includes(page) ? page : 'home';
    
    showPage(currentPage);
}

function showPage(pageName) {
    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => {
        page.classList.remove('active');
    });

    // Show selected page
    const targetPage = document.getElementById(pageName);
    if (targetPage) {
        targetPage.classList.add('active');
    }

    // Load markdown content for privacy and terms pages
    if (pageName === 'privacy') {
        loadMarkdownContent('privacy.md', 'privacy-content', 'privacy-loading', 'privacy-error');
    } else if (pageName === 'terms') {
        loadMarkdownContent('TERMS.md', 'terms-content', 'terms-loading', 'terms-error');
    }

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Update URL without page reload (for SPA behavior)
    const newPath = pageName === 'home' ? '/' : '/' + pageName;
    if (window.location.pathname !== newPath) {
        history.pushState(null, '', newPath);
    }
}

// Handle browser back/forward buttons
window.addEventListener('popstate', function(event) {
    initRouter();
});

// Handle navigation clicks
document.addEventListener('click', function(e) {
    const link = e.target.closest('a[href^="/"]');
    if (link && !link.getAttribute('href').startsWith('http')) {
        e.preventDefault();
        const path = link.getAttribute('href');
        const page = path.substring(1) || 'home';
        showPage(page);
    }
});


window.addEventListener('load', function() {
    initRouter();
});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        if (this.getAttribute('href').startsWith('#features')) {
            e.preventDefault();
            const target = document.querySelector('#features');
            if (target && document.getElementById('home').classList.contains('active')) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(255, 255, 255, 0.98)';
        nav.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
    } else {
        nav.style.background = 'rgba(255, 255, 255, 0.95)';
        nav.style.boxShadow = 'none';
    }
});


const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

window.addEventListener('load', function() {
    const cards = document.querySelectorAll('.feature-card, .tech-item');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});