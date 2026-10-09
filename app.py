
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0f172a">
<title>Tishtup | Student Portfolio</title>

<style>
:root {
    color-scheme: dark;
    --bg: #0f172a;
    --nav: rgba(15, 23, 42, 0.95);
    --card: #1e293b;
    --footer: #020617;
    --text: #f8fafc;
    --muted: #cbd5e1;
    --subtle: #94a3b8;
    --accent: #38bdf8;
    --border: #334155;
    --shadow: rgba(0, 0, 0, 0.25);
}

body.light {
    color-scheme: light;
    --bg: #f1f5f9;
    --nav: rgba(241, 245, 249, 0.96);
    --card: #ffffff;
    --footer: #e2e8f0;
    --text: #0f172a;
    --muted: #334155;
    --subtle: #475569;
    --accent: #0284c7;
    --border: #cbd5e1;
    --shadow: rgba(15, 23, 42, 0.10);
}

* {
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    transition: background 0.3s, color 0.3s;
}

nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    padding: 16px 6%;
    background: var(--nav);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
}

.logo {
    font-size: 24px;
    font-weight: bold;
    color: var(--accent);
}

.nav-links {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}

nav a {
    color: var(--muted);
    text-decoration: none;
    font-size: 14px;
}

nav a:hover {
    color: var(--accent);
}

#theme-toggle {
    border: 1px solid var(--border);
    background: var(--card);
    color: var(--text);
    border-radius: 25px;
    padding: 10px 14px;
    cursor: pointer;
    font-size: 14px;
    transition: transform 0.2s, border-color 0.2s;
}

#theme-toggle:hover {
    transform: translateY(-2px);
    border-color: var(--accent);
}

.hero {
    min-height: 88vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 75px 20px;
    position: relative;
    overflow: hidden;
}

.hero:before {
    content: "";
    position: absolute;
    width: 420px;
    height: 420px;
    background: var(--accent);
    opacity: 0.09;
    filter: blur(100px);
    border-radius: 50%;
    pointer-events: none;
}

.hero-content {
    position: relative;
    max-width: 900px;
    animation: fadeUp 0.8s ease;
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border: 1px solid var(--accent);
    border-radius: 30px;
    color: var(--accent);
    font-size: 13px;
    margin-bottom: 20px;
}

h1 {
    font-size: 64px;
    margin: 10px 0;
}

h1 span {
    color: var(--accent);
    animation: glow 2s infinite alternate;
}

p {
    line-height: 1.7;
}

.hero p {
    color: var(--muted);
    font-size: 18px;
}

.button {
    display: inline-block;
    margin-top: 20px;
    padding: 13px 25px;
    background: var(--accent);
    color: #ffffff;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    transition: transform 0.3s, box-shadow 0.3s;
}

.button:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px var(--shadow);
}

.info-container {
    margin-top: 40px;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 14px;
}

.info-box {
    background: var(--card);
    border: 1px solid var(--border);
    padding: 17px 22px;
    border-radius: 12px;
    transition: transform 0.3s;
}

.info-box:hover {
    transform: translateY(-5px);
}

section {
    padding: 80px 7%;
    text-align: center;
    scroll-margin-top: 85px;
}

section h2 {
    font-size: 35px;
    margin-bottom: 15px;
}

.section-text {
    color: var(--subtle);
    max-width: 700px;
    margin: auto;
}

.cards {
    margin-top: 38px;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 24px;
}

.card {
    width: 270px;
    padding: 28px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 15px;
    box-shadow: 0 8px 25px var(--shadow);
    transition: transform 0.3s, border-color 0.3s;
}

.card:hover {
    transform: translateY(-7px);
    border-color: var(--accent);
}

.card h3 {
    color: var(--accent);
}

.card p {
    color: var(--muted);
}

.contact-box {
    max-width: 850px;
    margin: 35px auto 0;
    background: var(--card);
    border: 1px solid var(--border);
    padding: 38px 25px;
    border-radius: 20px;
}

.contact-box h3 {
    font-size: 26px;
}

.contact-box p {
    color: var(--subtle);
}

.socials {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-top: 25px;
}

.social {
    display: inline-block;
    padding: 15px 22px;
    background: var(--bg);
    color: var(--text);
    text-decoration: none;
    border-radius: 10px;
    border: 1px solid var(--border);
    transition: transform 0.3s, border-color 0.3s;
}

.social:hover {
    transform: translateY(-4px);
    border-color: var(--accent);
}

.username {
    display: block;
    color: var(--subtle);
    font-size: 13px;
    margin-top: 6px;
}

footer {
    padding: 25px;
    text-align: center;
    background: var(--footer);
    color: var(--subtle);
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glow {
    from {
        text-shadow: 0 0 5px var(--accent);
    }
    to {
        text-shadow: 0 0 22px var(--accent);
    }
}

@media (max-width: 700px) {
    nav {
        justify-content: center;
        padding: 15px 4%;
    }

    .nav-links {
        gap: 12px;
    }

    nav a {
        font-size: 12px;
    }

    h1 {
        font-size: 43px;
    }

    section {
        padding: 65px 5%;
    }

    .hero {
        min-height: 80vh;
    }

    .card {
        width: 100%;
        max-width: 340px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        scroll-behavior: auto !important;
        animation: none !important;
        transition: none !important;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">Tishtup.</div>

    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#interests">Interests</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>

        <button id="theme-toggle" type="button"
                aria-label="Switch to light mode"
                aria-pressed="false">
            ☀️ Light mode
        </button>
    </div>
</nav>

<section class="hero">
    <div class="hero-content">
        <div class="badge">
            CLASS XI - PCM - COMPUTER SCIENCE
        </div>

        <h1>Hi, I'm <span>Tishtup</span>.</h1>

        <p>Student | Learner | Future Developer</p>

        <p>
            I enjoy learning, exploring technology,
            programming and building new things.
        </p>

        <a href="#about" class="button">
            Explore My Portfolio
        </a>

        <div class="info-container">
            <div class="info-box">Physics</div>
            <div class="info-box">Chemistry</div>
            <div class="info-box">Mathematics</div>
            <div class="info-box">Computer Science</div>
        </div>
    </div>
</section>

<section id="about">
    <h2>About Me</h2>
    <p class="section-text">
        I am a Class XI student studying PCM and Computer Science.
        I am learning Python, programming and web development.
        My goal is to keep improving my skills and build interesting projects.
    </p>
</section>

<section id="skills">
    <h2>My Skills</h2>
    <p class="section-text">
        Things I am currently learning and improving.
    </p>

    <div class="cards">
        <div class="card">
            <h3>Python</h3>
            <p>
                Learning programming fundamentals and building small applications.
            </p>
        </div>

        <div class="card">
            <h3>Flask</h3>
            <p>
                Learning how Python can be used to create real websites.
            </p>
        </div>

        <div class="card">
            <h3>Problem Solving</h3>
            <p>
                Working on Physics, Chemistry and Mathematics problems.
            </p>
        </div>
    </div>
</section>

<section id="interests">
    <h2>Beyond Academics</h2>
    <p class="section-text">
        The things I enjoy outside my regular studies.
    </p>

    <div class="cards">
        <div class="card">
            <h3>Cricket</h3>
            <p>
                A sport I have loved since childhood.
                Cricket is one of my biggest passions.
            </p>
        </div>

        <div class="card">
            <h3>Technology</h3>
            <p>
                I enjoy exploring computers, programming and new technology.
            </p>
        </div>

        <div class="card">
            <h3>Learning</h3>
            <p>
                I like learning new things and improving my skills step by step.
            </p>
        </div>
    </div>
</section>

<section id="projects">
    <h2>My Projects</h2>
    <p class="section-text">
        Some things I am building while learning programming.
    </p>

    <div class="cards">
        <div class="card">
            <h3>My Portfolio</h3>
            <p>
                This website was built using Python and Flask.
            </p>
        </div>

        <div class="card">
            <h3>Python Programs</h3>
            <p>
                Small programs and experiments created while learning Python.
            </p>
        </div>

        <div class="card">
            <h3>Future Projects</h3>
            <p>
                More interesting projects coming soon.
            </p>
        </div>
    </div>
</section>

<section id="contact">
    <h2>Let's Connect</h2>
    <p class="section-text">
        Follow my journey and explore my work.
    </p>

    <div class="contact-box">
        <h3>Connect with Tishtup</h3>
        <p>
            You can find my work and updates on these platforms.
        </p>

        <div class="socials">
            <a class="social"
               href="https://github.com/pyketishtup-sketch"
               target="_blank"
               rel="noopener noreferrer">
                💻 GitHub
                <span class="username">pyketishtup-sketch</span>
            </a>

            <a class="social"
               href="#contact"
               onclick="return false;">
                📸 Instagram
                <span class="username">tishtup.*.1845.*.pyke</span>
            </a>
        </div>
    </div>
</section>

<footer>
    <p>© 2026 Tishtup. Built with Python &amp; Flask.</p>
</footer>

<script>
(function () {
    const button = document.getElementById("theme-toggle");
    const metaTheme = document.querySelector(
        'meta[name="theme-color"]'
    );

    function applyTheme(theme) {
        const isLight = theme === "light";

        document.body.classList.toggle("light", isLight);

        button.textContent = isLight
            ? "🌙 Dark mode"
            : "☀️ Light mode";

        button.setAttribute(
            "aria-label",
            isLight ? "Switch to dark mode" : "Switch to light mode"
        );

        button.setAttribute("aria-pressed", String(isLight));

        metaTheme.setAttribute(
            "content",
            isLight ? "#f1f5f9" : "#0f172a"
        );
    }

    let savedTheme = "dark";

    try {
        savedTheme = localStorage.getItem("tishtup-theme") || "dark";
    } catch (error) {
        savedTheme = "dark";
    }

    applyTheme(savedTheme);

    button.addEventListener("click", function () {
        const newTheme = document.body.classList.contains("light")
            ? "dark"
            : "light";

        applyTheme(newTheme);

        try {
            localStorage.setItem("tishtup-theme", newTheme);
        } catch (error) {
            // Theme switching still works without browser storage.
        }
    });
})();
</script>

</body>
</html>
"""

app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
