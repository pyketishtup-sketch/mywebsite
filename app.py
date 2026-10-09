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
<meta name="description" content="Tishtup Pyke's student portfolio featuring cricket, science quizzes and interactive challenges.">
<title>Tishtup Pyke | Portfolio & Quiz Arena</title>

<style>
:root {
    --bg:#081426; --bg2:#10223c; --card:rgba(20,39,65,.85);
    --text:#eef4ff; --muted:#aabbd3; --accent:#55b8ff;
    --accent2:#8c7bff; --border:rgba(255,255,255,.12);
}
body.light {
    --bg:#f2f6fc; --bg2:#e5edf9; --card:rgba(255,255,255,.93);
    --text:#14233a; --muted:#586b85; --accent:#0879d1;
    --accent2:#6652db; --border:rgba(20,35,58,.13);
}
* {box-sizing:border-box;margin:0;padding:0;scroll-behavior:smooth}
body {
    font-family:"Segoe UI",Arial,sans-serif;color:var(--text);
    background:radial-gradient(circle at 10% 5%,rgba(65,133,255,.13),transparent 30%),var(--bg);
    line-height:1.7;transition:background .3s,color .3s;
}
a {color:inherit;text-decoration:none}
button,input {font:inherit}
nav {
    position:sticky;top:0;z-index:1000;padding:14px 6%;
    display:flex;justify-content:space-between;align-items:center;gap:15px;
    background:var(--bg);border-bottom:1px solid var(--border);
}
.logo {font-size:1.25rem;font-weight:900;white-space:nowrap}
.logo span,.accent {color:var(--accent)}
.nav-links {display:flex;flex-wrap:wrap;justify-content:flex-end;gap:13px;align-items:center}
.nav-links a {font-size:.85rem;color:var(--muted)}
.nav-links a:hover {color:var(--accent)}
.theme-btn {
    width:38px;height:38px;border-radius:50%;cursor:pointer;
    background:var(--card);color:var(--text);border:1px solid var(--border)
}
section {padding:75px 8%;scroll-margin-top:75px}
.hero {min-height:82vh;display:flex;align-items:center;position:relative;overflow:hidden}
.hero-content {max-width:850px;position:relative;z-index:1}
.eyebrow {
    display:inline-block;color:var(--accent);background:rgba(85,184,255,.09);
    border:1px solid rgba(85,184,255,.25);padding:5px 13px;
    border-radius:30px;font-size:.83rem;margin-bottom:20px
}
h1 {font-size:clamp(2.7rem,7vw,5rem);line-height:1.12;letter-spacing:-2px;margin-bottom:20px}
.gradient-text {
    background:linear-gradient(100deg,#55b8ff,#9b8bff,#62e4d0);
    -webkit-background-clip:text;background-clip:text;color:transparent
}
.hero p {max-width:650px;color:var(--muted);font-size:1.1rem;margin-bottom:24px}
.hero-glow {
    position:absolute;right:4%;top:25%;width:300px;height:300px;border-radius:50%;
    background:linear-gradient(135deg,#258bff,#7657e8);filter:blur(120px);opacity:.25
}
.hero-buttons,.actions {display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}
.btn {
    display:inline-block;padding:11px 18px;border:0;border-radius:10px;
    background:linear-gradient(110deg,#168de0,#7061eb);color:white;
    font-weight:700;cursor:pointer;transition:transform .2s
}
.btn:hover {transform:translateY(-2px)}
.btn.secondary {background:transparent;border:1px solid var(--border);color:var(--text)}
.section-heading {text-align:center;margin-bottom:35px}
.section-heading h2 {font-size:clamp(2rem,4vw,3rem);margin-bottom:8px}
.section-heading p {color:var(--muted);max-width:700px;margin:auto}
.grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:19px}
.card {
    padding:24px;border:1px solid var(--border);border-radius:18px;
    background:var(--card);box-shadow:0 12px 35px rgba(0,0,0,.09);
    transition:transform .25s,border-color .25s
}
.card:hover {transform:translateY(-4px);border-color:var(--accent)}
.card h3 {margin:8px 0}
.card p {color:var(--muted);font-size:.96rem}
.card-icon {font-size:2rem}
.tag {
    display:inline-block;padding:3px 9px;margin:8px 4px 0 0;
    border:1px solid var(--border);border-radius:20px;color:var(--accent);font-size:.78rem
}
.about-box {max-width:850px;margin:auto;text-align:center}
.about-box p {color:var(--muted)}
.stat-grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:14px;margin-top:25px}
.stat {padding:18px 10px;background:var(--card);border:1px solid var(--border);border-radius:14px}
.stat strong {display:block;color:var(--accent)}
.stat span {font-size:.85rem;color:var(--muted)}
.mi-banner {
    padding:32px;border-radius:22px;border:1px solid rgba(246,190,70,.3);
    background:radial-gradient(circle at 85% 15%,rgba(246,190,70,.16),transparent 30%),linear-gradient(120deg,#071b47,#0c3274,#071b47);
    color:white;margin-bottom:25px
}
.mi-banner h3 {font-size:clamp(1.7rem,4vw,2.4rem);color:#ffd36d}
.mi-banner p {color:#e0eaff}
.mi-label {color:#ffd36d;font-size:.8rem;letter-spacing:2px;font-weight:800}
.player-art {
    display:flex;align-items:center;justify-content:center;width:65px;height:65px;
    border-radius:18px;background:linear-gradient(135deg,#1649a4,#14203f);
    border:1px solid rgba(255,211,109,.45);color:#ffd36d;font-weight:900;font-size:1.3rem
}
.quiz-panel {margin-top:24px;padding:clamp(18px,4vw,32px);border:1px solid var(--border);border-radius:22px;background:var(--card)}
.quiz-top {display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:16px}
.quiz-score {font-weight:800;color:var(--accent)}
.categories {display:flex;flex-wrap:wrap;gap:9px;margin:20px 0}
.category-btn {
    padding:8px 13px;border-radius:25px;border:1px solid var(--border);
    background:transparent;color:var(--text);cursor:pointer
}
.category-btn.active {background:linear-gradient(110deg,#168de0,#7061eb);color:white;border-color:transparent}
.progress-track {height:7px;background:var(--border);border-radius:10px;overflow:hidden;margin:14px 0 22px}
.progress-fill {height:100%;width:0;background:linear-gradient(90deg,#55b8ff,#8c7bff);transition:width .25s}
.question-text {font-size:clamp(1.1rem,3vw,1.5rem);margin-bottom:18px}
.answers {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:11px}
.answer-btn {
    padding:12px;text-align:left;border-radius:11px;border:1px solid var(--border);
    background:transparent;color:var(--text);cursor:pointer
}
.answer-btn:hover:not(:disabled) {border-color:var(--accent)}
.answer-btn:disabled {cursor:default;opacity:.95}
.answer-btn.correct {border-color:#28b981;background:rgba(40,185,129,.12)}
.answer-btn.wrong {border-color:#ee7777;background:rgba(238,119,119,.12)}
.feedback {min-height:28px;margin:15px 0;font-weight:700}
.feedback.good {color:#28b981}.feedback.bad {color:#ee7777}
.hidden {display:none!important}
.result {text-align:center;padding:22px 5px}
.result-score {font-size:clamp(2.7rem,7vw,4.3rem);font-weight:900;color:var(--accent)}
.muted {color:var(--muted);font-size:.9rem}
.daily-box {
    padding:25px;border-radius:19px;border:1px solid rgba(246,190,70,.35);
    background:linear-gradient(120deg,rgba(13,45,89,.8),rgba(49,36,86,.8));color:white
}
.daily-box h3 {color:#ffd36d;font-size:1.5rem}
.daily-box p {color:#e0eaff}
.daily-box .answer-btn {color:white;border-color:rgba(255,255,255,.25)}
.daily-box .answer-btn:hover:not(:disabled) {background:rgba(255,255,255,.1)}
.daily-status {margin-top:12px;font-weight:700;min-height:28px}
.name-input {
    width:100%;max-width:320px;padding:10px 12px;border:1px solid var(--border);
    border-radius:9px;background:var(--bg);color:var(--text);margin:12px 0
}
.table-wrap {overflow-x:auto;margin-top:16px}
table {width:100%;border-collapse:collapse;min-width:280px}
th,td {padding:10px;text-align:left;border-bottom:1px solid var(--border)}
th {color:var(--accent)}
footer {padding:25px 8%;border-top:1px solid var(--border);text-align:center;color:var(--muted)}
.reveal {opacity:0;transform:translateY(15px);transition:opacity .6s,transform .6s}
.reveal.visible {opacity:1;transform:translateY(0)}
.project-note {font-size:.83rem;color:var(--muted);margin-top:10px}
.contact-card a {color:var(--accent);overflow-wrap:anywhere}
@media(max-width:800px) {
    nav {flex-wrap:wrap;padding:13px 5%}
    .nav-links {justify-content:flex-start;gap:10px}
    section {padding:60px 6%}
}
@media(max-width:550px) {
    .nav-links {gap:8px 12px}
    .nav-links a {font-size:.8rem}
    .answers {grid-template-columns:1fr}
    .mi-banner {padding:23px}
    h1 {letter-spacing:-1px}
}
@media(prefers-reduced-motion:reduce) {
    *,*::before,*::after {scroll-behavior:auto!important;transition-duration:.01ms!important}
}
</style>
</head>
<body>

<nav>
    <a href="#home" class="logo">TP<span>.</span></a>
    <div class="nav-links">
        <a href="#about">About</a><a href="#skills">Skills</a>
        <a href="#interests">Interests</a><a href="#cricket">Cricket</a>
        <a href="#playground">Playground</a><a href="#learn">Learn</a><a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
        <button class="theme-btn" id="themeToggle" aria-label="Toggle theme">☀️</button>
    </div>
</nav>

<section class="hero" id="home">
    <div class="hero-glow"></div>
    <div class="hero-content reveal">
        <span class="eyebrow">CLASS XI · PCM · COMPUTER SCIENCE</span>
        <h1>Hi, I'm <span class="gradient-text">Tishtup Pyke.</span></h1>
        <p>Student. Learner. Future Developer. Exploring science, coding, problem-solving and the game of cricket.</p>
        <div class="hero-buttons">
            <a class="btn" href="#projects">Explore My Work ↗</a>
            <a class="btn secondary" href="#playground">Play a Quiz 🎮</a>
        </div>
    </div>
</section>

<section id="about">
    <div class="section-heading reveal">
        <span class="eyebrow">A LITTLE ABOUT ME</span>
        <h2>More Than <span class="gradient-text">Just a Student</span></h2>
        <p>Learning, experimenting and building something new every day.</p>
    </div>
    <div class="about-box reveal">
        <p>I'm a Class XI student studying Physics, Chemistry and Mathematics, with an interest in computer science and web development. I enjoy understanding how things work, trying new ideas and improving my skills.</p>
        <div class="stat-grid">
            <div class="stat"><strong>Class XI</strong><span>Student Life</span></div>
            <div class="stat"><strong>PCM</strong><span>Science Stream</span></div>
            <div class="stat"><strong>Python</strong><span>Learning to Code</span></div>
            <div class="stat"><strong>Cricket 🏏</strong><span>Childhood Passion</span></div>
        </div>
    </div>
</section>

<section id="skills">
    <div class="section-heading reveal"><span class="eyebrow">WHAT I'M EXPLORING</span><h2>My <span class="gradient-text">Skills</span></h2><p>Skills grow through curiosity, practice and consistency.</p></div>
    <div class="grid">
        <article class="card reveal"><div class="card-icon">🐍</div><h3>Python</h3><p>Learning programming fundamentals and creating small applications.</p><span class="tag">Programming</span></article>
        <article class="card reveal"><div class="card-icon">🌐</div><h3>Web Development</h3><p>Building websites with Flask, HTML, CSS and JavaScript.</p><span class="tag">Flask</span><span class="tag">Web Design</span></article>
        <article class="card reveal"><div class="card-icon">🧩</div><h3>Problem Solving</h3><p>Practising mathematical reasoning and logical thinking.</p><span class="tag">Logic</span></article>
    </div>
</section>

<section id="interests">
    <div class="section-heading reveal"><span class="eyebrow">LIFE OUTSIDE THE CLASSROOM</span><h2>Beyond <span class="gradient-text">Academics</span></h2></div>
    <div class="grid">
        <article class="card reveal"><div class="card-icon">🏏</div><h3>Cricket</h3><p>A sport I have loved since childhood and one of my biggest passions.</p></article>
        <article class="card reveal"><div class="card-icon">💻</div><h3>Technology</h3><p>Exploring websites, programming and everyday technology.</p></article>
        <article class="card reveal"><div class="card-icon">📚</div><h3>Learning</h3><p>Discovering new concepts and improving through practice.</p></article>
    </div>
</section>

<section id="cricket">
    <div class="section-heading reveal"><span class="eyebrow">MY FAVOURITE GAME</span><h2>The <span class="gradient-text">Cricket Zone</span></h2><p>Big matches, unforgettable players and a passion for cricket.</p></div>
    <div class="mi-banner reveal">
        <div class="mi-label">MY FAVOURITE IPL TEAM</div><h3>🔵 Mumbai Indians</h3>
        <p>Blue and gold, big moments and memories that make the IPL special.</p>
        <p class="project-note">Fan-made tribute. Not an official team website.</p>
    </div>
    <div class="grid">
        <article class="card reveal"><div class="player-art">RS</div><h3>Rohit Sharma</h3><p>Known for elegant batting, big scores and leadership.</p><span class="tag">Hitman</span></article>
        <article class="card reveal"><div class="player-art">VK</div><h3>Virat Kohli</h3><p>A celebrated batter known for intensity and chasing targets.</p><span class="tag">Chase Master</span></article>
        <article class="card reveal"><div class="player-art">JB</div><h3>Jasprit Bumrah</h3><p>A fast bowler known for accuracy and difficult overs.</p><span class="tag">Bowling</span></article>
        <article class="card reveal"><div class="player-art">HP</div><h3>Hardik Pandya</h3><p>An all-rounder who contributes with both bat and ball.</p><span class="tag">All-Rounder</span></article>
    </div>
</section>

<section id="playground">
    <div class="section-heading reveal">
        <span class="eyebrow">YOUR TURN TO PLAY</span>
        <h2>Welcome to the <span class="gradient-text">Playground</span> 🎮</h2>
        <p>Try a daily cricket question, earn quiz points and share your score with friends.</p>
    </div>

    <!-- DAILY CHALLENGE -->
    <div class="daily-box reveal">
        <div class="mi-label">TODAY'S CHALLENGE</div>
        <h3>🏏 Daily Cricket Question</h3>
        <p id="dailyDate"></p>
        <h3 id="dailyQuestion" style="color:white;font-size:1.2rem;margin-top:14px">Loading question...</h3>
        <div class="answers" id="dailyAnswers" style="margin-top:16px"></div>
        <div class="daily-status" id="dailyStatus" aria-live="polite"></div>
        <p class="project-note">One attempt per day in this browser. Clearing browser data may reset it.</p>
    </div>

    <!-- MAIN QUIZ -->
    <div class="quiz-panel reveal">
        <div class="quiz-top">
            <div><h3>Quiz Arena</h3><p class="muted">Choose a category and start playing.</p></div>
            <div class="quiz-score" id="totalPoints">⭐ Points: 0</div>
        </div>
        <div class="categories">
            <button class="category-btn active" data-category="science">🧪 Science</button>
            <button class="category-btn" data-category="general">🌍 General Knowledge</button>
            <button class="category-btn" data-category="cricket">🏏 Cricket</button>
        </div>
        <div id="quizGame">
            <div class="quiz-top"><span id="questionCount">Question 1</span><span class="quiz-score" id="roundScore">Score: 0</span></div>
            <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
            <h3 class="question-text" id="questionText">Loading question...</h3>
            <div class="answers" id="answerOptions"></div>
            <div class="feedback" id="feedback" aria-live="polite"></div>
            <div class="actions">
                <button class="btn hidden" id="nextQuestion">Next Question →</button>
                <button class="btn secondary" id="restartQuiz">Restart Quiz ↻</button>
            </div>
        </div>
        <div id="quizResult" class="result hidden" aria-live="polite">
            <div class="card-icon">🏆</div><h3 id="resultHeading">Challenge Complete!</h3>
            <div class="result-score" id="resultScore">0/5</div>
            <p id="resultMessage"></p><p class="muted" id="pointsEarned"></p>
            <input class="name-input" id="playerName" maxlength="20" placeholder="Enter a nickname for the leaderboard" aria-label="Leaderboard nickname">
            <div class="actions" style="justify-content:center">
                <button class="btn" id="saveScore">Save Local Score</button>
                <button class="btn secondary" id="shareScore">Share My Score ↗</button>
                <button class="btn secondary" id="playAgain">Play Again ↻</button>
            </div>
            <p class="project-note" id="shareStatus" aria-live="polite"></p>
        </div>
    </div>

    <!-- LOCAL LEADERBOARD -->
    <div class="quiz-panel reveal">
        <div class="quiz-top">
            <div><h3>🏆 Local Leaderboard</h3><p class="muted">Your saved scores on this browser.</p></div>
            <button class="btn secondary" id="clearLeaderboard">Clear Scores</button>
        </div>
        <div class="table-wrap">
            <table>
                <thead><tr><th>#</th><th>Player</th><th>Category</th><th>Score</th></tr></thead>
                <tbody id="leaderboardBody"></tbody>
            </table>
        </div>
        <p class="project-note">This is a local leaderboard, not a global ranking. Other visitors cannot see your saved scores.</p>
    </div>
</section>

<section id="learn">
    <div class="section-heading reveal">
        <span class="eyebrow">LEARN SOMETHING NEW</span>
        <h2>Quick <span class="gradient-text">Learning Corner</span></h2>
        <p>Short explanations to make each visit useful, whether you love cricket or science.</p>
    </div>
    <div class="grid">
        <article class="card reveal">
            <div class="card-icon">⚡</div>
            <h3>Science Bite: Power</h3>
            <p>Power is the rate at which work is done. In SI units, power is measured in watts (W).</p>
            <span class="tag">Physics</span>
        </article>
        <article class="card reveal">
            <div class="card-icon">🏏</div>
            <h3>Cricket Bite: The Over</h3>
            <p>A standard over contains six legal deliveries. Wides and no-balls do not count as legal balls in the over.</p>
            <span class="tag">Cricket Rules</span>
        </article>
        <article class="card reveal">
            <div class="card-icon">🧠</div>
            <h3>Quiz Tip: Learn the Why</h3>
            <p>After answering a question, read the explanation. Understanding why an answer is correct helps you remember it longer.</p>
            <span class="tag">Study Skills</span>
        </article>
    </div>
    <p class="project-note" style="text-align:center;margin-top:18px">This is student-made educational content for learning and practice.</p>
</section>

<section id="projects">
    <div class="section-heading reveal"><span class="eyebrow">THINGS I'M BUILDING</span><h2>My <span class="gradient-text">Projects</span></h2></div>
    <div class="grid">
        <article class="card reveal"><div class="card-icon">🖥️</div><h3>Personal Portfolio</h3><p>A website introducing my interests, skills and interactive activities.</p><span class="tag">Flask</span></article>
        <article class="card reveal"><div class="card-icon">⚙️</div><h3>Python Experiments</h3><p>Small programming exercises to strengthen my coding skills.</p><span class="tag">Python</span></article>
        <article class="card reveal"><div class="card-icon">🚀</div><h3>Future Projects</h3><p>More ideas and useful projects as I continue learning.</p><span class="tag">Coming Soon</span></article>
    </div>
</section>

<section id="contact">
    <div class="section-heading reveal"><span class="eyebrow">LET'S CONNECT</span><h2>Find Me <span class="gradient-text">Online</span></h2><p>Check out my coding work and social profile.</p></div>
    <div class="grid">
        <article class="card contact-card reveal"><div class="card-icon">🐙</div><h3>GitHub</h3><p>Explore my repositories and projects.</p><p style="margin-top:14px"><a href="https://github.com/pyketishtup-sketch" target="_blank" rel="noopener noreferrer">@pyketishtup-sketch ↗</a></p></article>
        <article class="card contact-card reveal"><div class="card-icon">📸</div><h3>Instagram</h3><p>My Instagram username:</p><p class="accent" style="margin-top:14px">tishtup._.1845._.pyke</p></article>
    </div>
</section>

<footer>
    <p>Designed with curiosity and built while learning. 💙</p>
    <p>© <span id="year"></span> Tishtup Pyke · Keep Learning. Keep Building.</p>
    <p style="margin-top:8px"><a href="/about">About</a> · <a href="/privacy">Privacy Policy</a> · <a href="/contact">Contact</a></p>
</footer>

<script>
/* THEME */
const themeToggle = document.getElementById("themeToggle");
function setTheme(theme) {
    document.body.classList.toggle("light", theme === "light");
    themeToggle.textContent = theme === "light" ? "🌙" : "☀️";
}
let savedTheme = "dark";
try { savedTheme = localStorage.getItem("tishtup-theme") || "dark"; } catch(e) {}
setTheme(savedTheme);
themeToggle.addEventListener("click", function() {
    const next = document.body.classList.contains("light") ? "dark" : "light";
    setTheme(next);
    try { localStorage.setItem("tishtup-theme", next); } catch(e) {}
});

/* FOOTER AND ANIMATIONS */
document.getElementById("year").textContent = new Date().getFullYear();
if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {threshold:0.08});
    document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
} else {
    document.querySelectorAll(".reveal").forEach(el => el.classList.add("visible"));
}

/* QUESTION BANK */
const quizData = {
    science: [
        {q:"What is the SI unit of force?",o:["Joule","Newton","Watt","Pascal"],a:1,e:"Force is measured in newtons (N)."},
        {q:"Which particle has a negative electric charge?",o:["Proton","Neutron","Electron","Nucleus"],a:2,e:"An electron carries a negative electric charge."},
        {q:"What is the chemical formula of water?",o:["CO₂","H₂O","O₂","NaCl"],a:1,e:"A water molecule contains two hydrogen atoms and one oxygen atom."},
        {q:"Which quantity is measured in watts?",o:["Power","Energy","Force","Momentum"],a:0,e:"The watt is the SI unit of power."},
        {q:"What is the approximate speed of light in vacuum?",o:["3 × 10⁶ m/s","3 × 10⁸ m/s","3 × 10⁴ m/s","3 × 10¹⁰ m/s"],a:1,e:"The speed of light is approximately 3 × 10⁸ m/s."}
    ],
    general: [
        {q:"Which planet is known as the Red Planet?",o:["Venus","Jupiter","Mars","Mercury"],a:2,e:"Mars appears reddish because of iron oxide on its surface."},
        {q:"What is the capital of India?",o:["Mumbai","New Delhi","Kolkata","Chennai"],a:1,e:"New Delhi is the capital of India."},
        {q:"How many sides does a hexagon have?",o:["Five","Six","Seven","Eight"],a:1,e:"A hexagon has six sides."},
        {q:"Which is the largest ocean on Earth?",o:["Atlantic","Indian","Arctic","Pacific"],a:3,e:"The Pacific Ocean is the largest ocean."},
        {q:"Which instrument measures temperature?",o:["Barometer","Thermometer","Ammeter","Hygrometer"],a:1,e:"A thermometer measures temperature."}
    ],
    cricket: [
        {q:"How many players from one team are on the field in a standard cricket match?",o:["9","10","11","12"],a:2,e:"A standard cricket team has eleven players on the field."},
        {q:"How many legal deliveries are there in a standard over?",o:["Four","Five","Six","Eight"],a:2,e:"A standard over consists of six legal deliveries."},
        {q:"What does LBW stand for?",o:["Long Ball Wide","Leg Before Wicket","Last Batting Wicket","Line Before Wicket"],a:1,e:"LBW stands for Leg Before Wicket."},
        {q:"How many runs is a boundary worth when the ball reaches it along the ground?",o:["Two","Three","Four","Six"],a:2,e:"A boundary reached along the ground scores four runs."},
        {q:"Which is a type of dismissal in cricket?",o:["Checkmate","Offside","Bowled","Touchdown"],a:2,e:"Bowled is a dismissal in cricket."}
    ]
};

/* SAFE LOCAL STORAGE HELPERS */
function readJSON(key, fallback) {
    try {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : fallback;
    } catch(e) { return fallback; }
}
function writeJSON(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch(e) {}
}
let totalPoints = 0;
try { totalPoints = Number(localStorage.getItem("tishtup-quiz-points")) || 0; } catch(e) {}

function updatePoints() {
    document.getElementById("totalPoints").textContent = "⭐ Points: " + totalPoints;
}
function awardPoints(points) {
    totalPoints += points;
    try { localStorage.setItem("tishtup-quiz-points", String(totalPoints)); } catch(e) {}
    updatePoints();
}

/* QUIZ ENGINE */
let category = "science", index = 0, score = 0, roundPoints = 0, answered = false;
const $ = id => document.getElementById(id);

function startQuiz(nextCategory) {
    category = nextCategory || category;
    index = 0; score = 0; roundPoints = 0; answered = false;
    document.querySelectorAll(".category-btn").forEach(btn =>
        btn.classList.toggle("active", btn.dataset.category === category)
    );
    $("quizGame").classList.remove("hidden");
    $("quizResult").classList.add("hidden");
    renderQuestion();
}
function renderQuestion() {
    const questions = quizData[category];
    if (index >= questions.length) { finishQuiz(); return; }
    const q = questions[index];
    answered = false;
    $("questionCount").textContent = "Question " + (index + 1) + " of " + questions.length;
    $("roundScore").textContent = "Score: " + score;
    $("progressFill").style.width = (index / questions.length * 100) + "%";
    $("questionText").textContent = q.q;
    $("answerOptions").innerHTML = "";
    $("feedback").textContent = "";
    $("feedback").className = "feedback";
    $("nextQuestion").classList.add("hidden");

    q.o.forEach((option, i) => {
        const btn = document.createElement("button");
        btn.className = "answer-btn";
        btn.textContent = String.fromCharCode(65 + i) + ". " + option;
        btn.addEventListener("click", () => chooseAnswer(i, btn));
        $("answerOptions").appendChild(btn);
    });
}
function chooseAnswer(choice, selected) {
    if (answered) return;
    answered = true;
    const q = quizData[category][index];
    const buttons = $("answerOptions").querySelectorAll("button");
    buttons.forEach(btn => btn.disabled = true);
    buttons[q.a].classList.add("correct");

    if (choice === q.a) {
        score++; roundPoints += 10;
        $("feedback").textContent = "Correct! +10 points. " + q.e;
        $("feedback").className = "feedback good";
    } else {
        selected.classList.add("wrong");
        $("feedback").textContent = "Not quite. " + q.e;
        $("feedback").className = "feedback bad";
    }
    $("roundScore").textContent = "Score: " + score;
    $("progressFill").style.width = ((index + 1) / quizData[category].length * 100) + "%";
    $("nextQuestion").textContent = index === quizData[category].length - 1 ? "See Results 🏆" : "Next Question →";
    $("nextQuestion").classList.remove("hidden");
}
function finishQuiz() {
    $("quizGame").classList.add("hidden");
    $("quizResult").classList.remove("hidden");
    awardPoints(roundPoints);
    const total = quizData[category].length;
    const percent = Math.round(score / total * 100);
    $("resultScore").textContent = score + "/" + total;
    $("resultHeading").textContent = percent === 100 ? "Perfect Score! 🏆" : percent >= 60 ? "Well Played! 🎉" : "Keep Practising! 💪";
    $("resultMessage").textContent = "You answered " + score + " out of " + total + " questions correctly (" + percent + "%).";
    $("pointsEarned").textContent = "You earned " + roundPoints + " points this round. Total points: " + totalPoints + ".";
    $("shareStatus").textContent = "";
}
document.querySelectorAll(".category-btn").forEach(btn =>
    btn.addEventListener("click", () => startQuiz(btn.dataset.category))
);
$("nextQuestion").addEventListener("click", () => {
    if (answered) { index++; renderQuestion(); }
});
$("restartQuiz").addEventListener("click", () => startQuiz(category));
$("playAgain").addEventListener("click", () => startQuiz(category));

/* SHARE SCORE */
function scoreMessage() {
    return "I scored " + score + "/" + quizData[category].length +
        " in the " + category.toUpperCase() + " Quiz on Tishtup's Quiz Arena! 🏆 Can you beat my score?";
}
async function shareCurrentScore() {
    const message = scoreMessage();
    try {
        if (navigator.share) {
            await navigator.share({title:"My Quiz Score", text:message, url:window.location.href});
            $("shareStatus").textContent = "Thanks for sharing your challenge!";
        } else if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(message + " " + window.location.href);
            $("shareStatus").textContent = "Score and website link copied. Share it with your friends!";
        } else {
            window.prompt("Copy your score and share it with friends:", message + " " + window.location.href);
        }
    } catch(e) {
        if (e.name !== "AbortError") $("shareStatus").textContent = "Sharing was unavailable. You can copy your score manually.";
    }
}
$("shareScore").addEventListener("click", shareCurrentScore);

/* LOCAL LEADERBOARD */
function renderLeaderboard() {
    const rows = readJSON("tishtup-local-leaderboard", []);
    const body = $("leaderboardBody");
    body.innerHTML = "";
    if (!rows.length) {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 4; td.textContent = "No saved scores yet. Finish a quiz to add your first score.";
        tr.appendChild(td); body.appendChild(tr); return;
    }
    rows.slice().sort((a,b) => b.score - a.score).slice(0,10).forEach((row,i) => {
        const tr = document.createElement("tr");
        [String(i+1), row.name, row.category, row.score + "/" + row.total].forEach(value => {
            const td = document.createElement("td"); td.textContent = value; tr.appendChild(td);
        });
        body.appendChild(tr);
    });
}
$("saveScore").addEventListener("click", () => {
    const name = $("playerName").value.trim().slice(0,20) || "Player";
    const rows = readJSON("tishtup-local-leaderboard", []);
    rows.push({name:name, category:category, score:score, total:quizData[category].length, date:new Date().toISOString()});
    writeJSON("tishtup-local-leaderboard", rows.slice(-50));
    renderLeaderboard();
    $("shareStatus").textContent = "Your score has been saved in this browser.";
});
$("clearLeaderboard").addEventListener("click", () => {
    if (confirm("Clear all scores saved in this browser?")) {
        writeJSON("tishtup-local-leaderboard", []);
        renderLeaderboard();
    }
});
renderLeaderboard();
updatePoints();
startQuiz("science");

/* DAILY CRICKET CHALLENGE */
const dailyQuestions = [
    {q:"How many legal balls are there in a standard over?",o:["4","5","6","8"],a:2,e:"A standard over has six legal deliveries."},
    {q:"What does LBW stand for?",o:["Leg Before Wicket","Long Ball Wide","Last Batting Wicket","Line Before Wicket"],a:0,e:"LBW means Leg Before Wicket."},
    {q:"How many players are in a standard cricket team?",o:["9","10","11","12"],a:2,e:"A standard team has eleven players."},
    {q:"How many runs does a batter score for a six?",o:["4","5","6","7"],a:2,e:"A six is awarded when the ball clears the boundary without bouncing."},
    {q:"Which player is known as the Hitman?",o:["Virat Kohli","Rohit Sharma","Jasprit Bumrah","Hardik Pandya"],a:1,e:"Rohit Sharma is popularly known as the Hitman."},
    {q:"What is the term for taking three wickets with three consecutive deliveries?",o:["Hat-trick","Triple play","Powerplay","Maiden"],a:0,e:"Three wickets in three consecutive deliveries is a hat-trick."},
    {q:"Which equipment does a batter use to hit the ball?",o:["Racket","Bat","Club","Stick"],a:1,e:"A batter uses a cricket bat."}
];

function localDateKey() {
    const d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth()+1).padStart(2,"0") + "-" + String(d.getDate()).padStart(2,"0");
}
function dailyQuestionForToday() {
    const key = localDateKey();
    let hash = 0;
    for (let i=0;i<key.length;i++) hash = (hash * 31 + key.charCodeAt(i)) >>> 0;
    return dailyQuestions[hash % dailyQuestions.length];
}
function initDailyChallenge() {
    const key = localDateKey();
    const q = dailyQuestionForToday();
    $("dailyDate").textContent = "Date: " + key + " · One daily question";
    $("dailyQuestion").textContent = q.q;
    const answers = $("dailyAnswers");
    answers.innerHTML = "";
    const saved = readJSON("tishtup-daily-result", null);

    if (saved && saved.date === key) {
        q.o.forEach((option,i) => {
            const btn = document.createElement("button");
            btn.className = "answer-btn" + (i === q.a ? " correct" : "");
            btn.textContent = String.fromCharCode(65+i) + ". " + option;
            btn.disabled = true;
            answers.appendChild(btn);
        });
        $("dailyStatus").textContent = saved.correct
            ? "You already completed today's challenge! Correct answer — well played! ⭐"
            : "Today's attempt is complete. " + q.e;
        return;
    }

    q.o.forEach((option,i) => {
        const btn = document.createElement("button");
        btn.className = "answer-btn";
        btn.textContent = String.fromCharCode(65+i) + ". " + option;
        btn.addEventListener("click", () => {
            answers.querySelectorAll("button").forEach(b => b.disabled = true);
            answers.children[q.a].classList.add("correct");
            const correct = i === q.a;
            if (!correct) btn.classList.add("wrong");
            if (correct) awardPoints(10);
            writeJSON("tishtup-daily-result", {date:key, correct:correct});
            $("dailyStatus").textContent = correct
                ? "Correct! +10 points. " + q.e
                : "Good try! " + q.e;
        });
        answers.appendChild(btn);
    });
}
initDailyChallenge();
</script>
</body>
</html>
"""


# These pages provide site information and are linked from the homepage footer.
def info_page(title, body):
    template = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#081426">
<title>PAGE_TITLE | Tishtup Pyke</title>
<style>
:root{--bg:#081426;--card:#142741;--text:#eef4ff;--muted:#aabbd3;--accent:#55b8ff;--border:rgba(255,255,255,.12)}
*{box-sizing:border-box}
body{margin:0;padding:28px 18px;font-family:"Segoe UI",Arial,sans-serif;background:radial-gradient(circle at 10% 5%,rgba(65,133,255,.13),transparent 30%),var(--bg);color:var(--text);line-height:1.75}
main{max-width:850px;margin:25px auto;padding:clamp(22px,5vw,42px);border:1px solid var(--border);border-radius:20px;background:var(--card)}
h1{line-height:1.2;font-size:clamp(2rem,6vw,3.2rem);margin-top:0}
h2{margin-top:26px;color:var(--accent)}
p,li{color:var(--muted)}
a{color:var(--accent)}
.home{display:inline-block;margin-bottom:24px;text-decoration:none;border:1px solid var(--border);padding:8px 13px;border-radius:9px}
footer{max-width:850px;margin:20px auto;text-align:center;color:var(--muted);font-size:.9rem}
</style>
</head>
<body>
<main>
<a class="home" href="/">← Back to homepage</a>
<h1>PAGE_TITLE</h1>
BODY_CONTENT
</main>
<footer>Student portfolio and learning project · <a href="/">Home</a> · <a href="/privacy">Privacy</a> · <a href="/contact">Contact</a></footer>
</body>
</html>
"""
    return template.replace("PAGE_TITLE", title).replace("BODY_CONTENT", body)


@app.route("/about")
def about_page():
    return info_page(
        "About",
        """
        <p>Hi, I'm Tishtup Pyke, a Class XI student studying Physics, Chemistry and Mathematics. I'm learning Python and web development and building this website as a personal project.</p>
        <h2>What you'll find here</h2>
        <ul>
          <li>Interactive science, general knowledge and cricket quizzes.</li>
          <li>A daily cricket question and explanations after answers.</li>
          <li>Short learning notes and information about my coding interests.</li>
        </ul>
        <h2>Why I built this website</h2>
        <p>I wanted a place to practise coding, share my interests and make learning a little more interactive. The website is a work in progress, so content and features may change as I learn.</p>
        <p>This is an independent student project and is not affiliated with any cricket team or governing body.</p>
        """
    )


@app.route("/privacy")
def privacy_page():
    return info_page(
        "Privacy Policy",
        """
        <p><strong>Last updated: 9 October 2026</strong></p>
        <p>This is a personal student portfolio and quiz website. This page explains the basic data handling used by the current version of the site.</p>
        <h2>Information stored in your browser</h2>
        <p>The quiz features use your browser's local storage to remember your theme preference, total quiz points, saved local leaderboard scores, and whether you have answered the daily challenge. This information is stored on your device/browser and is not sent to this site's Flask app as part of those features. Clearing browser data may remove it.</p>
        <p>If you enter a nickname for the local leaderboard, it is saved in that browser only. Do not enter sensitive or private information as a nickname.</p>
        <h2>Technical information</h2>
        <p>This site is hosted using Render. The hosting provider may process technical information such as request and server logs to operate, secure and maintain the service. Check Render's current privacy information for details about its processing.</p>
        <h2>Sharing features</h2>
        <p>If you choose to use the score-sharing button, your device may open its own sharing interface or copy text to your clipboard. You decide whether and where to share it.</p>
        <h2>Advertising and third-party services</h2>
        <p>This version of the site does not intentionally include advertising scripts or an advertising network. If ads, analytics, contact forms, or other third-party services are added later, this policy should be updated to explain their data practices before those features are used.</p>
        <h2>Children and personal information</h2>
        <p>Please do not submit sensitive personal information through this website. There is no contact form on this site; the contact page links to external profiles instead.</p>
        <h2>Changes</h2>
        <p>This policy may be updated when the website's features change. The date at the top will be revised when meaningful changes are made.</p>
        """
    )


@app.route("/contact")
def contact_page():
    return info_page(
        "Contact",
        """
        <p>Thanks for visiting my website. If you want to see my coding work or reach my public profile, use one of the links below.</p>
        <h2>GitHub</h2>
        <p><a href="https://github.com/pyketishtup-sketch" target="_blank" rel="noopener noreferrer">github.com/pyketishtup-sketch ↗</a></p>
        <h2>Instagram</h2>
        <p>Username: <strong>tishtup._.1845._.pyke</strong></p>
        <p>For your privacy, avoid sharing passwords, financial information, your home address, or other sensitive details online.</p>
        <p><a href="/">Return to the homepage →</a></p>
        """
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
