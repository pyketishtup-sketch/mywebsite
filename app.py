from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<html>
<head>

<title>Tishtup - Student Portfolio</title>

<style>

body {
    margin: 0;
    font-family: Arial;
    background-color: #0f172a;
    color: white;
    text-align: center;
}

header {
    padding: 30px;
    background-color: #111827;
}

h1 {
    font-size: 50px;
    margin: 20px;
}

h1 span {
    color: #38bdf8;
}

p {
    color: #cbd5e1;
    font-size: 18px;
}

.button {
    display: inline-block;
    margin-top: 20px;
    padding: 12px 25px;
    background-color: #38bdf8;
    color: #0f172a;
    text-decoration: none;
    border-radius: 8px;
}

section {
    padding: 60px 20px;
}

.card {
    display: inline-block;
    width: 250px;
    margin: 15px;
    padding: 25px;
    background-color: #1e293b;
    border-radius: 12px;
}

footer {
    padding: 20px;
    background-color: #111827;
}

</style>

</head>

<body>

<header>
<h2>Tishtup.</h2>
</header>

<section>

<p>CLASS XI - PCM - COMPUTER SCIENCE</p>

<h1>Hi, I'm <span>Tishtup</span>.</h1>

<p>Student | Learner | Future Developer</p>

<a class="button" href="#about">Explore My Website</a>

</section>

<section id="about">

<h2>About Me</h2>

<p>
I am a Class XI student studying PCM and Computer Science.
I am learning Python, programming and web development.
</p>

<div class="card">
<h2>Studies</h2>
<p>Physics, Chemistry and Mathematics</p>
</div>

<div class="card">
<h2>Programming</h2>
<p>Learning Python and Flask</p>
</div>

<div class="card">
<h2>Projects</h2>
<p>Building my own websites and programs</p>
</div>

</section>

<footer>
<p>My Student Portfolio - Built with Python and Flask</p>
</footer>

</body>
</html>
"""

app.run()