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

<title>Tishtup | Student Portfolio</title>

<style>

* {
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0f172a;
    color: white;
}

/* NAVBAR */

nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    padding: 18px 8%;
    background: rgba(15, 23, 42, 0.95);
    border-bottom: 1px solid #1e293b;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 24px;
    font-weight: bold;
    color: #38bdf8;
}

nav a {
    color: #cbd5e1;
    text-decoration: none;
    margin-left: 20px;
    font-size: 15px;
}

nav a:hover {
    color: #38bdf8;
}

/* HERO */

.hero {
    min-height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 80px 20px;
    position: relative;
    overflow: hidden;
}

.hero:before {
    content: "";
    position: absolute;
    width: 500px;
    height: 500px;
    background: #38bdf8;
    opacity: 0.08;
    filter: blur(100px);
    border-radius: 50%;
}

.hero-content {
    position: relative;
    max-width: 900px;
    animation: fadeUp 1s ease;
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border: 1px solid #38bdf8;
    border-radius: 30px;
    color: #38bdf8;
    font-size: 13px;
    margin-bottom: 20px;
}

h1 {
    font-size: 64px;
    margin: 10px 0;
}

h1 span {
    color: #38bdf8;
    animation: glow 2s infinite alternate;
}

.hero p {
    color: #cbd5e1;
    font-size: 19px;
    line-height: 1.7;
}

.button {
    display: inline-block;
    margin-top: 25px;
    padding: 13px 25px;
    background: #38bdf8;
    color: #0f172a;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    transition: 0.3s;
}

.button:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(56,189,248,0.3);
}

/* INFO BOXES */

.info-container {
    margin-top: 45px;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 15px;
}

.info-box {
    background: #1e293b;
    padding: 18px 25px;
    border-radius: 12px;
    min-width: 150px;
    transition: 0.3s;
}

.info-box:hover {
    transform: translateY(-6px);
}

/* SECTIONS */

section {
    padding: 90px 8%;
    text-align: center;
}

section h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.section-text {
    color: #94a3b8;
    max-width: 700px;
    margin: auto;
    line-height: 1.7;
}

/* CARDS */

.cards {
    margin-top: 40px;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 25px;
}

.card {
    width: 270px;
    padding: 30px;
    background: #1e293b;
    border-radius: 15px;
    transition: 0.3s;
    border: 1px solid transparent;
}

.card:hover {
    transform: translateY(-8px);
    border-color: #38bdf8;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
}

.card h3 {
    color: #38bdf8;
}

.card p {
    color: #cbd5e1;
    line-height: 1.6;
}

/* CONTACT */

.contact-box {
    max-width: 850px;
    margin: 40px auto 0;
    background: #1e293b;
    padding: 45px 30px;
    border-radius: 20px;
    border: 1px solid #334155;
}

.contact-box h3 {
    font-size: 28px;
    margin-top: 0;
}

.contact-box p {
    color: #94a3b8;
    line-height: 1.7;
}

.socials {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 18px;
    margin-top: 30px;
}

.social {
    display: inline-block;
    padding: 15px 22px;
    background: #0f172a;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    border: 1px solid #334155;
    transition: 0.3s;
}

.social:hover {
    transform: translateY(-5px);
    border-color: #38bdf8;
    color: #38bdf8;
}

.username {
    color: #94a3b8;
    font-size: 13px;
    display: block;
    margin-top: 5px;
}

/* FOOTER */

footer {
    padding: 30px;
    text-align: center;
    background: #020617;
    color: #64748b;
}

/* ANIMATIONS */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes glow {
    from {
        text-shadow: 0 0 5px #38bdf8;
    }

    to {
        text-shadow: 0 0 25px #38bdf8;
    }
}

/* MOBILE */

@media (max-width: 700px) {

    nav {
        padding: 15px 5%;
    }

    nav a {
        margin-left: 8px;
        font-size: 12px;
    }

    h1 {
        font-size: 45px;
    }

    section {
        padding: 70px 5%;
    }

    .hero {
        min-height: 85vh;
    }

}

</style>

</head>

<body>

<nav>

<div class="logo">Tishtup.</div>

<div>
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#interests">Interests</a>
<a href="#projects">Projects</a>
<a href="#contact">Contact</a>
</div>

</nav>


<!-- HERO -->

<section class="hero">

<div class="hero-content">

<div class="badge">
CLASS XI - PCM - COMPUTER SCIENCE
</div>

<h1>
Hi, I'm <span>Tishtup</span>.
</h1>

<p>
Student | Learner | Future Developer
</p>

<p>
I am a Class XI student passionate about learning,
technology, programming and building new things.
</p>

<a href="#about" class="button">
Explore My Portfolio
</a>

<div class="info-container">

<div class="info-box">
Physics
</div>

<div class="info-box">
Chemistry
</div>

<div class="info-box">
Mathematics
</div>

<div class="info-box">
Computer Science
</div>

</div>

</div>

</section>


<!-- ABOUT -->

<section id="about">

<h2>About Me</h2>

<p class="section-text">
I am a Class XI student studying PCM and Computer Science.
I am currently learning Python, programming and web development.
My goal is to keep improving my skills and build interesting projects.
</p>

</section>


<!-- SKILLS -->

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


<!-- INTERESTS -->

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


<!-- PROJECTS -->

<section id="projects">

<h2>My Projects</h2>

<p class="section-text">
Some of the things I am building while learning programming.
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


<!-- CONTACT -->

<section id="contact">

<h2>Let's Connect</h2>

<p class="section-text">
Want to see what I am building or follow my journey?
Connect with me here.
</p>

<div class="contact-box">

<h3>Connect with Tishtup</h3>

<p>
You can find my work and updates on the platforms below.
</p>

<div class="socials">

<a class="social"
href="https://github.com/pyketishtup-sketch"
target="_blank">

💻 GitHub

<span class="username">
pyketishtup-sketch
</span>

</a>

<a class="social"
href="#"
onclick="alert('Instagram username: tishtup.*.1845.*.pyke'); return false;">

📸 Instagram

<span class="username">
tishtup.*.1845.*.pyke
</span>

</a>

</div>

</div>

</section>


<!-- FOOTER -->

<footer>

<p>
© 2026 Tishtup. Built with Python & Flask.
</p>

</footer>

</body>
</html>
"""

app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
