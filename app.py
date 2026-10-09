
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#081426">
<meta name="description" content="The personal portfolio of a Class XI student interested in PCM, computer science, cricket and technology.">
<title>Tishtup Pyke | Student Portfolio</title>

<style>
:root {
    --bg: #081426;
    --bg2: #0d1c32;
    --card: rgba(20, 39, 65, 0.78);
    --text: #eef4ff;
    --muted: #aabbd3;
    --accent: #55b8ff;
    --accent2: #8c7bff;
    --border: rgba(255,255,255,0.11);
    --shadow: rgba(0,0,0,0.22);
}

body.light {
    --bg: #f2f6fc;
    --bg2: #e5edf9;
    --card: rgba(255,255,255,0.9);
    --text: #14233a;
    --muted: #586b85;
    --accent: #0879d1;
    --accent2: #6652db;
    --border: rgba(20,35,58,0.12);
    --shadow: rgba(27,51,85,0.09);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: "Segoe UI", Arial, sans-serif;
    background:
        radial-gradient(circle at 10% 5%, rgba(65,133,255,0.13), transparent 30%),
        radial-gradient(circle at 90% 25%, rgba(135,91,255,0.11), transparent 27%),
        var(--bg);
    color: var(--text);
    line-height: 1.7;
    transition: background 0.3s, color 0.3s;
}

a {
    color: inherit;
    text-decoration: none;
}

button {
    font: inherit;
}

nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    padding: 15px 7%;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(18px);
}

.logo {
    font-size: 1.2rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    white-space: nowrap;
}

.logo span {
    color: var(--accent);
}

.nav-links {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    align-items: center;
    gap: 17px;
}

.nav-links a {
    font-size: 0.88rem;
    color: var(--muted);
    transition: color 0.2s;
}

.nav-links a:hover {
    color: var(--accent);
}

.theme-btn {
    border: 1px solid var(--border);
    background: var(--card);
    color: var(--text);
    border-radius: 50%;
    width: 39px;
    height: 39px;
    cursor: pointer;
}

section {
    padding: 85px 8%;
    scroll-margin-top: 75px;
}

.hero {
    min-height: 88vh;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
}

.hero-content {
    max-width: 850px;
    position: relative;
    z-index: 1;
}

.eyebrow {
    display: inline-block;
    color: var(--accent);
    background: rgba(85,184,255,0.09);
    border: 1px solid rgba(85,184,255,0.24);
    padding: 6px 13px;
    border-radius: 30px;
    font-size: 0.85rem;
    margin-bottom: 22px;
}

h1 {
    font-size: clamp(2.7rem, 7vw, 5.3rem);
    line-height: 1.12;
    letter-spacing: -2px;
    margin-bottom: 20px;
}

.gradient-text {
    background: linear-gradient(100deg, #55b8ff, #9b8bff, #62e4d0);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero p {
    max-width: 650px;
    color: var(--muted);
    font-size: 1.1rem;
    margin-bottom: 25px;
}

.hero-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 25px;
}

.btn {
    display: inline-block;
    padding: 11px 19px;
    border-radius: 10px;
    background: linear-gradient(110deg, #168de0, #7061eb);
    color: white;
    font-weight: 700;
    border: none;
    cursor: pointer;
    transition: transform 0.2s, opacity 0.2s;
}

.btn:hover {
    transform: translateY(-3px);
    opacity: 0.92;
}

.btn.secondary {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
}

.hero-glow {
    position: absolute;
    width: 330px;
    height: 330px;
    right: 3%;
    top: 24%;
    border-radius: 50%;
    background: linear-gradient(135deg, #258bff, #7657e8);
    filter: blur(120px);
    opacity: 0.23;
    pointer-events: none;
}

.section-heading {
    text-align: center;
    margin-bottom: 40px;
}

.section-heading h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 9px;
}

.section-heading p {
    color: var(--muted);
    max-width: 700px;
    margin: auto;
}

.accent {
    color: var(--accent);
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 230px), 1fr));
    gap: 20px;
}

.card {
    padding: 25px;
    border: 1px solid var(--border);
    border-radius: 19px;
    background: var(--card);
    box-shadow: 0 12px 35px var(--shadow);
    backdrop-filter: blur(12px);
    transition: transform 0.25s, border-color 0.25s;
}

.card:hover {
    transform: translateY(-5px);
    border-color: rgba(85,184,255,0.45);
}

.card h3 {
    margin: 8px 0 10px;
}

.card p {
    color: var(--muted);
    font-size: 0.96rem;
}

.card-icon {
    font-size: 2rem;
}

.tag {
    display: inline-block;
    padding: 4px 10px;
    border: 1px solid var(--border);
    border-radius: 20px;
    color: var(--accent);
    font-size: 0.78rem;
    margin: 10px 5px 0 0;
}

.about-box {
    max-width: 850px;
    margin: auto;
    text-align: center;
}

.about-box p {
    color: var(--muted);
    font-size: 1.05rem;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 15px;
    margin-top: 28px;
}

.stat {
    padding: 20px 12px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 15px;
}

.stat strong {
    display: block;
    color: var(--accent);
    font-size: 1.15rem;
}

.stat span {
    color: var(--muted);
    font-size: 0.88rem;
}

/* CRICKET ZONE */

.cricket-section {
    background: linear-gradient(180deg, transparent, rgba(20,55,100,0.12), transparent);
}

.mi-banner {
    padding: 35px;
    border-radius: 23px;
    border: 1px solid rgba(246,190,70,0.3);
    background:
        radial-gradient(circle at 85% 15%, rgba(246,190,70,0.16), transparent 30%),
        linear-gradient(120deg, #071b47, #0c3274, #071b47);
    color: #fff;
    margin-bottom: 28px;
}

.mi-banner h3 {
    font-size: clamp(1.6rem, 4vw, 2.4rem);
    color: #ffd36d;
    margin-bottom: 8px;
}

.mi-banner p {
    color: #e0eaff;
}

.mi-label {
    color: #ffd36d;
    font-size: 0.82rem;
    letter-spacing: 2px;
    font-weight: 800;
}

.player-art {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1649a4, #14203f);
    border: 1px solid rgba(255,211,109,0.45);
    color: #ffd36d;
    font-size: 1.25rem;
    font-weight: 900;
}

/* PLAYGROUND */

.playground-intro {
    margin-bottom: 26px;
}

.game-card {
    overflow: hidden;
}

.game-card .card-icon {
    margin-bottom: 5px;
}

.quiz-panel {
    margin-top: 25px;
    padding: clamp(20px, 4vw, 35px);
    border-radius: 22px;
    border: 1px solid var(--border);
    background: var(--card);
    box-shadow: 0 12px 35px var(--shadow);
}

.quiz-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 18px;
}

.quiz-score {
    color: var(--accent);
    font-weight: 800;
}

.quiz-categories {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 25px;
}

.category-btn {
    border: 1px solid var(--border);
    color: var(--text);
    background: transparent;
    padding: 8px 15px;
    border-radius: 30px;
    cursor: pointer;
}

.category-btn.active {
    background: linear-gradient(110deg, #168de0, #7061eb);
    color: white;
    border-color: transparent;
}

.progress-track {
    width: 100%;
    height: 7px;
    background: var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin: 14px 0 25px;
}

.progress-fill {
    width: 0;
    height: 100%;
    background: linear-gradient(90deg, #55b8ff, #8c7bff);
    transition: width 0.25s;
}

.question-text {
    font-size: clamp(1.15rem, 3vw, 1.55rem);
    margin-bottom: 20px;
}

.answers {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.answer-btn {
    width: 100%;
    padding: 13px 15px;
    text-align: left;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 12px;
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s;
}

.answer-btn:hover:not(:disabled) {
    border-color: var(--accent);
    background: rgba(85,184,255,0.07);
}

.answer-btn:disabled {
    cursor: default;
    opacity: 0.92;
}

.answer-btn.correct {
    border-color: #28b981;
    background: rgba(40,185,129,0.12);
}

.answer-btn.wrong {
    border-color: #ee7777;
    background: rgba(238,119,119,0.12);
}

.feedback {
    min-height: 30px;
    margin: 18px 0 12px;
    font-weight: 700;
}

.feedback.good {
    color: #28b981;
}

.feedback.bad {
    color: #ee7777;
}

.quiz-actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    margin-top: 12px;
}

.quiz-result {
    text-align: center;
    padding: 25px 5px;
}

.result-score {
    font-size: clamp(2.7rem, 7vw, 4.5rem);
    font-weight: 900;
    color: var(--accent);
    margin: 12px 0;
}

.hidden {
    display: none !important;
}

.project-note {
    font-size: 0.85rem;
    color: var(--muted);
    margin-top: 10px;
}

.contact-card a {
    color: var(--accent);
    overflow-wrap: anywhere;
}

footer {
    padding: 28px 8%;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--muted);
}

.reveal {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.65s ease, transform 0.65s ease;
}

.reveal.visible {
    opacity: 1;
    transform: translateY(0);
}

@media (max-width: 850px) {
    nav {
        align-items: flex-start;
        flex-wrap: wrap;
        padding: 13px 5%;
    }

    .nav-links {
        justify-content: flex-start;
        gap: 12px;
    }

    section {
        padding: 65px 6%;
    }

    .hero {
        min-height: 75vh;
    }
}

@media (max-width: 550px) {
    .nav-links {
        gap: 9px 13px;
    }

    .nav-links a {
        font-size: 0.82rem;
    }

    .answers {
        grid-template-columns: 1fr;
    }

    .mi-banner {
        padding: 25px 20px;
    }

    .card {
        padding: 21px;
    }

    h1 {
        letter-spacing: -1px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
    }
}
</style>
</head>

<body>

<nav>
    <a href="#home" class="logo">TP<span>.</span></a>

    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#interests">Interests</a>
        <a href="#cricket">Cricket</a>
        <a href="#playground">Playground</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
        <button class="theme-btn" id="themeToggle" aria-label="Toggle light and dark theme">☀️</button>
    </div>
</nav>

<!-- HERO -->

<section class="hero" id="home">
    <div class="hero-glow"></div>

    <div class="hero-content reveal">
        <span class="eyebrow">CLASS XI · PCM · COMPUTER SCIENCE</span>

        <h1>Hi, I'm <span class="gradient-text">Tishtup Pyke.</span></h1>

        <p>
            Student. Learner. Future Developer.
            Exploring science, solving problems, learning to code,
            and enjoying the game of cricket.
        </p>

        <div class="hero-buttons">
            <a href="#projects" class="btn">Explore My Work ↗</a>
            <a href="#playground" class="btn secondary">Enter Playground 🎮</a>
        </div>
    </div>
</section>

<!-- ABOUT -->

<section id="about">
    <div class="section-heading reveal">
        <span class="eyebrow">A LITTLE ABOUT ME</span>
        <h2>More Than <span class="gradient-text">Just a Student</span></h2>
        <p>Learning, experimenting and building something new every day.</p>
    </div>

    <div class="about-box reveal">
        <p>
            I'm a Class XI student studying Physics, Chemistry and Mathematics,
            with a growing interest in computer science and web development.
            I enjoy understanding how things work, trying new ideas and
            improving my skills step by step.
        </p>

        <div class="stat-grid">
            <div class="stat">
                <strong>Class XI</strong>
                <span>Student Life</span>
            </div>
            <div class="stat">
                <strong>PCM</strong>
                <span>Science Stream</span>
            </div>
            <div class="stat">
                <strong>Python</strong>
                <span>Learning to Code</span>
            </div>
            <div class="stat">
                <strong>Cricket 🏏</strong>
                <span>A Childhood Passion</span>
            </div>
        </div>
    </div>
</section>

<!-- SKILLS -->

<section id="skills">
    <div class="section-heading reveal">
        <span class="eyebrow">WHAT I'M EXPLORING</span>
        <h2>My <span class="gradient-text">Skills</span></h2>
        <p>Skills grow through curiosity, practice and consistency.</p>
    </div>

    <div class="grid">
        <article class="card reveal">
            <div class="card-icon">🐍</div>
            <h3>Python</h3>
            <p>Learning programming fundamentals and creating small applications.</p>
            <span class="tag">Programming</span>
        </article>

        <article class="card reveal">
            <div class="card-icon">🌐</div>
            <h3>Web Development</h3>
            <p>Building a personal website with Flask, HTML, CSS and JavaScript.</p>
            <span class="tag">Flask</span>
            <span class="tag">HTML & CSS</span>
        </article>

        <article class="card reveal">
            <div class="card-icon">🧩</div>
            <h3>Problem Solving</h3>
            <p>Practising mathematical reasoning and breaking challenging problems into steps.</p>
            <span class="tag">Logic</span>
            <span class="tag">Mathematics</span>
        </article>
    </div>
</section>

<!-- INTERESTS -->

<section id="interests">
    <div class="section-heading reveal">
        <span class="eyebrow">LIFE OUTSIDE THE CLASSROOM</span>
        <h2>Beyond <span class="gradient-text">Academics</span></h2>
        <p>Things that keep me curious and motivated.</p>
    </div>

    <div class="grid">
        <article class="card reveal">
            <div class="card-icon">🏏</div>
            <h3>Cricket</h3>
            <p>A sport I have loved since childhood. Cricket is one of my biggest passions.</p>
        </article>

        <article class="card reveal">
            <div class="card-icon">💻</div>
            <h3>Technology</h3>
            <p>Exploring websites, programming and the technology behind everyday things.</p>
        </article>

        <article class="card reveal">
            <div class="card-icon">📚</div>
            <h3>Learning</h3>
            <p>Discovering new concepts and getting better through practice and experience.</p>
        </article>
    </div>
</section>

<!-- CRICKET ZONE -->

<section class="cricket-section" id="cricket">
    <div class="section-heading reveal">
        <span class="eyebrow">MY FAVOURITE GAME</span>
        <h2>The <span class="gradient-text">Cricket Zone</span></h2>
        <p>Big matches, unforgettable players and a passion for cricket.</p>
    </div>

    <div class="mi-banner reveal">
        <div class="mi-label">MY FAVOURITE IPL TEAM</div>
        <h3>🔵 Mumbai Indians</h3>
        <p>
            Blue and gold, big moments and memories that make the IPL special.
            Mumbai Indians have a special place in my cricket fandom.
        </p>
        <p class="project-note">
            A fan-made tribute, not an official team website.
        </p>
    </div>

    <div class="grid">
        <article class="card reveal">
            <div class="player-art">RS</div>
            <h3>Rohit Sharma</h3>
            <p>Known for elegant batting, big scores and leadership.</p>
            <span class="tag">Hitman</span>
        </article>

        <article class="card reveal">
            <div class="player-art">VK</div>
            <h3>Virat Kohli</h3>
            <p>A celebrated batter known for intensity and chasing targets.</p>
            <span class="tag">Chase Master</span>
        </article>

        <article class="card reveal">
            <div class="player-art">JB</div>
            <h3>Jasprit Bumrah</h3>
            <p>An outstanding fast bowler known for accuracy and difficult overs.</p>
            <span class="tag">Yorker Specialist</span>
        </article>

        <article class="card reveal">
            <div class="player-art">HP</div>
            <h3>Hardik Pandya</h3>
            <p>An all-rounder who contributes with both bat and ball.</p>
            <span class="tag">All-Rounder</span>
        </article>
    </div>
</section>

<!-- INTERACTIVE PLAYGROUND -->

<section id="playground">
    <div class="section-heading reveal">
        <span class="eyebrow">YOUR TURN TO PLAY</span>
        <h2>Welcome to the <span class="gradient-text">Playground</span> 🎮</h2>
        <p>
            Take a break and challenge yourself with science, general knowledge
            and cricket trivia. Pick a category, earn points and try again!
        </p>
    </div>

    <div class="grid playground-intro">
        <article class="card game-card reveal">
            <div class="card-icon">🧪</div>
            <h3>Science Challenge</h3>
            <p>Test your knowledge of Physics, Chemistry and basic science.</p>
        </article>

        <article class="card game-card reveal">
            <div class="card-icon">🌍</div>
            <h3>General Knowledge</h3>
            <p>Answer questions about the world, space and everyday knowledge.</p>
        </article>

        <article class="card game-card reveal">
            <div class="card-icon">🏏</div>
            <h3>Cricket Challenge</h3>
            <p>Take on cricket questions about rules, players and the game.</p>
        </article>
    </div>

    <div class="quiz-panel reveal">
        <div class="quiz-top">
            <div>
                <h3>Quiz Arena</h3>
                <p style="color:var(--muted)">Choose a category and start playing.</p>
            </div>
            <div class="quiz-score" id="totalPoints">⭐ Points: 0</div>
        </div>

        <div class="quiz-categories" role="group" aria-label="Quiz categories">
            <button class="category-btn active" data-category="science">🧪 Science</button>
            <button class="category-btn" data-category="general">🌍 General Knowledge</button>
            <button class="category-btn" data-category="cricket">🏏 Cricket</button>
        </div>

        <div id="quizGame">
            <div class="quiz-top">
                <span id="questionCount">Question 1</span>
                <span class="quiz-score" id="roundScore">Score: 0</span>
            </div>

            <div class="progress-track">
                <div class="progress-fill" id="progressFill"></div>
            </div>

            <h3 class="question-text" id="questionText">Loading question...</h3>

            <div class="answers" id="answerOptions"></div>

            <div class="feedback" id="feedback" aria-live="polite"></div>

            <div class="quiz-actions">
                <button class="btn hidden" id="nextQuestion">Next Question →</button>
                <button class="btn secondary" id="restartQuiz">Restart Quiz ↻</button>
            </div>
        </div>

        <div id="quizResult" class="quiz-result hidden" aria-live="polite">
            <div class="card-icon">🏆</div>
            <h3 id="resultHeading">Challenge Complete!</h3>
            <div class="result-score" id="resultScore">0/5</div>
            <p id="resultMessage"></p>
            <p class="project-note" id="pointsEarned"></p>
            <div style="margin-top:20px">
                <button class="btn" id="playAgain">Play Again ↻</button>
            </div>
        </div>
    </div>

    <p class="project-note" style="text-align:center">
        Your points are saved in this browser on this device.
        They are not shared with a server or other visitors.
    </p>
</section>

<!-- PROJECTS -->

<section id="projects">
    <div class="section-heading reveal">
        <span class="eyebrow">THINGS I'M BUILDING</span>
        <h2>My <span class="gradient-text">Projects</span></h2>
        <p>Small steps today, bigger ideas for tomorrow.</p>
    </div>

    <div class="grid">
        <article class="card reveal">
            <div class="card-icon">🖥️</div>
            <h3>Personal Portfolio</h3>
            <p>This website introduces my interests, skills, projects and interactive activities.</p>
            <span class="tag">Flask</span>
            <span class="tag">Web Design</span>
        </article>

        <article class="card reveal">
            <div class="card-icon">⚙️</div>
            <h3>Python Experiments</h3>
            <p>Small programming exercises to strengthen my understanding of coding.</p>
            <span class="tag">Python</span>
        </article>

        <article class="card reveal">
            <div class="card-icon">🚀</div>
            <h3>Future Projects</h3>
            <p>More ideas, experiments and useful projects as I continue learning.</p>
            <span class="tag">Coming Soon</span>
        </article>
    </div>
</section>

<!-- CONTACT -->

<section id="contact">
    <div class="section-heading reveal">
        <span class="eyebrow">LET'S CONNECT</span>
        <h2>Find Me <span class="gradient-text">Online</span></h2>
        <p>Check out my coding work and social profile.</p>
    </div>

    <div class="grid">
        <article class="card contact-card reveal">
            <div class="card-icon">🐙</div>
            <h3>GitHub</h3>
            <p>Explore my repositories and coding projects.</p>
            <p style="margin-top:14px">
                <a href="https://github.com/pyketishtup-sketch"
                   target="_blank" rel="noopener noreferrer">
                    @pyketishtup-sketch ↗
                </a>
            </p>
        </article>

        <article class="card contact-card reveal">
            <div class="card-icon">📸</div>
            <h3>Instagram</h3>
            <p>Find my Instagram profile.</p>
            <p style="margin-top:14px">
                <span class="accent">tishtup._.1845._.pyke</span>
            </p>
        </article>
    </div>
</section>

<footer>
    <p>Designed with curiosity and built while learning. 💙</p>
    <p>© <span id="year"></span> Tishtup Pyke · Keep Learning. Keep Building.</p>
</footer>

<script>
/* THEME TOGGLE */

const themeToggle = document.getElementById("themeToggle");

function setTheme(theme) {
    document.body.classList.toggle("light", theme === "light");
    themeToggle.textContent = theme === "light" ? "🌙" : "☀️";
    themeToggle.setAttribute(
        "aria-label",
        theme === "light" ? "Switch to dark theme" : "Switch to light theme"
    );
}

let savedTheme = "dark";

try {
    savedTheme = localStorage.getItem("tishtup-theme") || "dark";
} catch (error) {
    savedTheme = "dark";
}

setTheme(savedTheme);

themeToggle.addEventListener("click", function () {
    const newTheme = document.body.classList.contains("light") ? "dark" : "light";
    setTheme(newTheme);

    try {
        localStorage.setItem("tishtup-theme", newTheme);
    } catch (error) {
        // Theme still works for this page even if storage is unavailable.
    }
});


/* FOOTER YEAR */

document.getElementById("year").textContent = new Date().getFullYear();


/* SCROLL REVEAL */

const revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.08 });

document.querySelectorAll(".reveal").forEach(function (element) {
    revealObserver.observe(element);
});


/* QUIZ QUESTION BANK */

const quizData = {
    science: [
        {
            q: "What is the SI unit of force?",
            options: ["Joule", "Newton", "Watt", "Pascal"],
            answer: 1,
            explanation: "Force is measured in newtons (N)."
        },
        {
            q: "Which particle has a negative electric charge?",
            options: ["Proton", "Neutron", "Electron", "Nucleus"],
            answer: 2,
            explanation: "An electron carries a negative electric charge."
        },
        {
            q: "What is the chemical formula of water?",
            options: ["CO₂", "H₂O", "O₂", "NaCl"],
            answer: 1,
            explanation: "A water molecule contains two hydrogen atoms and one oxygen atom."
        },
        {
            q: "Which quantity is measured in watts?",
            options: ["Power", "Energy", "Force", "Momentum"],
            answer: 0,
            explanation: "The watt is the SI unit of power."
        },
        {
            q: "What is the approximate speed of light in vacuum?",
            options: [
                "3 × 10⁶ m/s",
                "3 × 10⁸ m/s",
                "3 × 10⁴ m/s",
                "3 × 10¹⁰ m/s"
            ],
            answer: 1,
            explanation: "The speed of light in vacuum is approximately 3 × 10⁸ m/s."
        }
    ],

    general: [
        {
            q: "Which planet is known as the Red Planet?",
            options: ["Venus", "Jupiter", "Mars", "Mercury"],
            answer: 2,
            explanation: "Mars appears reddish because of iron oxide on its surface."
        },
        {
            q: "What is the capital of India?",
            options: ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
            answer: 1,
            explanation: "New Delhi is the capital of India."
        },
        {
            q: "How many sides does a hexagon have?",
            options: ["Five", "Six", "Seven", "Eight"],
            answer: 1,
            explanation: "A hexagon has six sides."
        },
        {
            q: "Which is the largest ocean on Earth?",
            options: ["Atlantic", "Indian", "Arctic", "Pacific"],
            answer: 3,
            explanation: "The Pacific Ocean is the largest ocean on Earth."
        },
        {
            q: "Which instrument is used to measure temperature?",
            options: ["Barometer", "Thermometer", "Ammeter", "Hygrometer"],
            answer: 1,
            explanation: "A thermometer is used to measure temperature."
        }
    ],

    cricket: [
        {
            q: "How many players from one team are on the field in a standard cricket match?",
            options: ["9", "10", "11", "12"],
            answer: 2,
            explanation: "A standard cricket team has eleven players on the field."
        },
        {
            q: "How many legal deliveries are there in a standard over?",
            options: ["Four", "Five", "Six", "Eight"],
            answer: 2,
            explanation: "A standard over consists of six legal deliveries."
        },
        {
            q: "What does LBW stand for?",
            options: [
                "Long Ball Wide",
                "Leg Before Wicket",
                "Last Batting Wicket",
                "Line Before Wicket"
            ],
            answer: 1,
            explanation: "LBW stands for Leg Before Wicket."
        },
        {
            q: "How many runs does a batter normally score for a boundary hit along the ground?",
            options: ["Two", "Three", "Four", "Six"],
            answer: 2,
            explanation: "A boundary reached along the ground scores four runs."
        },
        {
            q: "Which of these is a type of dismissal in cricket?",
            options: ["Checkmate", "Offside", "Bowled", "Touchdown"],
            answer: 2,
            explanation: "Bowled is a dismissal in which the ball hits the stumps and dislodges the bails."
        }
    ]
};


/* QUIZ STATE */

let currentCategory = "science";
let questionIndex = 0;
let roundScore = 0;
let answered = false;
let roundPoints = 0;
let totalPoints = 0;

try {
    totalPoints = Number(localStorage.getItem("tishtup-quiz-points")) || 0;
} catch (error) {
    totalPoints = 0;
}

const questionText = document.getElementById("questionText");
const answerOptions = document.getElementById("answerOptions");
const feedback = document.getElementById("feedback");
const questionCount = document.getElementById("questionCount");
const roundScoreDisplay = document.getElementById("roundScore");
const progressFill = document.getElementById("progressFill");
const nextButton = document.getElementById("nextQuestion");
const restartButton = document.getElementById("restartQuiz");
const quizGame = document.getElementById("quizGame");
const quizResult = document.getElementById("quizResult");


function updateTotalPoints() {
    document.getElementById("totalPoints").textContent =
        "⭐ Points: " + totalPoints;
}


function saveTotalPoints() {
    try {
        localStorage.setItem("tishtup-quiz-points", String(totalPoints));
    } catch (error) {
        // The quiz remains playable if browser storage is unavailable.
    }
}


function renderQuestion() {
    const questions = quizData[currentCategory];

    if (questionIndex >= questions.length) {
        finishQuiz();
        return;
    }

    const question = questions[questionIndex];
    answered = false;

    questionCount.textContent =
        "Question " + (questionIndex + 1) + " of " + questions.length;

    roundScoreDisplay.textContent = "Score: " + roundScore;
    progressFill.style.width =
        (questionIndex / questions.length * 100) + "%";

    questionText.textContent = question.q;
    answerOptions.innerHTML = "";
    feedback.textContent = "";
    feedback.className = "feedback";
    nextButton.classList.add("hidden");

    question.options.forEach(function (option, index) {
        const button = document.createElement("button");
        button.className = "answer-btn";
        button.textContent = String.fromCharCode(65 + index) + ". " + option;

        button.addEventListener("click", function () {
            chooseAnswer(index, button);
        });

        answerOptions.appendChild(button);
    });
}


function chooseAnswer(selectedIndex, selectedButton) {
    if (answered) return;

    answered = true;

    const question = quizData[currentCategory][questionIndex];
    const allButtons = answerOptions.querySelectorAll(".answer-btn");

    allButtons.forEach(function (button) {
        button.disabled = true;
    });

    allButtons[question.answer].classList.add("correct");

    if (selectedIndex === question.answer) {
        roundScore += 1;
        roundPoints += 10;
        feedback.textContent = "Correct! +10 points. " + question.explanation;
        feedback.className = "feedback good";
    } else {
        selectedButton.classList.add("wrong");
        feedback.textContent = "Not quite. " + question.explanation;
        feedback.className = "feedback bad";
    }

    roundScoreDisplay.textContent = "Score: " + roundScore;
    progressFill.style.width =
        ((questionIndex + 1) / quizData[currentCategory].length * 100) + "%";

    nextButton.textContent =
        questionIndex === quizData[currentCategory].length - 1
        ? "See Results 🏆"
        : "Next Question →";

    nextButton.classList.remove("hidden");
}


function finishQuiz() {
    quizGame.classList.add("hidden");
    quizResult.classList.remove("hidden");

    totalPoints += roundPoints;
    saveTotalPoints();
    updateTotalPoints();

    const totalQuestions = quizData[currentCategory].length;
    const percentage = Math.round((roundScore / totalQuestions) * 100);

    document.getElementById("resultScore").textContent =
        roundScore + "/" + totalQuestions;

    document.getElementById("resultHeading").textContent =
        percentage === 100 ? "Perfect Score! 🏆" :
        percentage >= 60 ? "Well Played! 🎉" :
        "Keep Practising! 💪";

    document.getElementById("resultMessage").textContent =
        "You answered " + roundScore + " out of " + totalQuestions +
        " questions correctly (" + percentage + "%).";

    document.getElementById("pointsEarned").textContent =
        "You earned " + roundPoints +
        " points this round. Your total points are " + totalPoints + ".";
}


function startQuiz(category) {
    currentCategory = category;
    questionIndex = 0;
    roundScore = 0;
    roundPoints = 0;
    answered = false;

    document.querySelectorAll(".category-btn").forEach(function (button) {
        button.classList.toggle(
            "active",
            button.dataset.category === category
        );
    });

    quizGame.classList.remove("hidden");
    quizResult.classList.add("hidden");

    renderQuestion();
}


document.querySelectorAll(".category-btn").forEach(function (button) {
    button.addEventListener("click", function () {
        startQuiz(button.dataset.category);
    });
});


nextButton.addEventListener("click", function () {
    if (!answered) return;

    questionIndex += 1;
    renderQuestion();
});


restartButton.addEventListener("click", function () {
    startQuiz(currentCategory);
});


document.getElementById("playAgain").addEventListener("click", function () {
    startQuiz(currentCategory);
});


updateTotalPoints();
startQuiz("science");
</script>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
