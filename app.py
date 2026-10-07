from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Tishtup | Student Portfolio</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background: #0b1120;
            color: white;
            line-height: 1.6;
        }

        nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(11, 17, 32, 0.95);
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #1e293b;
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
            color: #38bdf8;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            margin-left: 25px;
            font-size: 15px;
        }

        nav a:hover {
            color: #38bdf8;
        }

        .hero {
            min-height: 90vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px 20px;
            background:
                radial-gradient(circle at top, #172554 0%, #0b1120 55%);
        }

        .hero small {
            color: #38bdf8;
            font-size: 16px;
            letter-spacing: 2px;
        }

        .hero h1 {
            font-size: 65px;
            margin: 15px 0;
        }

        .hero h1 span {
            color: #38bdf8;
        }

        .hero p {
            color: #94a3b8;
            font-size: 20px;
            max-width: 650px;
            margin: auto;
        }

        .button {
            display: inline-block;
            margin-top: 30px;
            padding: 13px 28px;
            background: #38bdf8;
            color: #07111f;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: 0.3s;
        }

        .button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(56, 189, 248, 0.25);
        }

        section {
            padding: 90px 8%;
            text-align: center;
        }

        .section-title {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .section-text {
            color: #94a3b8;
            max-width: 700px;
            margin: 0 auto 45px;
        }

        .cards {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
        }

        .card {
            width: 280px;
            padding: 30px;
            background: #111827;
            border: 1px solid #1e293b;
            border-radius: 15px;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
            border-color: #38bdf8;
        }

        .card h3 {
            color: #38bdf8;
            margin-bottom: 12px;
            font-size: 22px;
        }

        .card p {
            color: #94a3b8;
        }

        .skills {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 30px;
        }

        .skill {
            padding: 10px 18px;
            background: #172033;
            border: 1px solid #263449;
            border-radius: 20px;
            color: #cbd5e1;
        }

        .contact {
            background: #111827;
        }

        footer {
            padding: 25px;
            text-align: center;
            color: #64748b;
            background: #070b14;
        }

        @media (max-width: 700px) {
            nav {
                padding: 15px 5%;
            }

            nav a {
                margin-left: 10px;
                font-size: 13px;
            }

            .hero h1 {
                font-size: 45px;
            }

            .hero p {
                font-size: 17px;
            }

            section {
                padding: 65px 5%;
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
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</nav>


<section class="hero">

    <div>
        <small>CLASS XI - PCM - COMPUTER SCIENCE</small>

        <h1>Hi, I'm <span>Tishtup.</span></h1>

        <p>
            Student, learner and aspiring developer.
            Currently exploring Python, programming and web development.
        </p>

        <a class="button" href="#about">Explore My Portfolio</a>
    </div>

</section>


<section id="about">

    <h2 class="section-title">About Me</h2>

    <p class="section-text">
        I am a Class XI student studying Physics, Chemistry,
        Mathematics and Computer Science. I enjoy learning
        technology and building things with code.
    </p>

    <div class="cards">

        <div class="card">
            <h3>Education</h3>
            <p>Class XI student with a focus on PCM and Computer Science.</p>
        </div>

        <div class="card">
            <h3>Programming</h3>
            <p>Currently learning Python, Flask, HTML and CSS.</p>
        </div>

        <div class="card">
            <h3>Goal</h3>
            <p>Keep learning, build useful projects and become a better developer.</p>
        </div>

    </div>

</section>


<section id="skills">

    <h2 class="section-title">My Skills</h2>

    <p class="section-text">
        Technologies and subjects I am currently learning.
    </p>

    <div class="skills">

        <div class="skill">Python</div>
        <div class="skill">Flask</div>
        <div class="skill">HTML</div>
        <div class="skill">CSS</div>
        <div class="skill">Java</div>
        <div class="skill">Physics</div>
        <div class="skill">Chemistry</div>
        <div class="skill">Mathematics</div>

    </div>

</section>


<section id="projects">

    <h2 class="section-title">My Projects</h2>

    <p class="section-text">
        Things I have built and things I am working on.
    </p>

    <div class="cards">

        <div class="card">
            <h3>Student Portfolio</h3>
            <p>This website, built using Python and Flask.</p>
        </div>

        <div class="card">
            <h3>Python Programs</h3>
            <p>Small programs and experiments created while learning Python.</p>
        </div>

        <div class="card">
            <h3>Future Projects</h3>
            <p>More interesting projects are coming soon.</p>
        </div>

    </div>

</section>


<section class="contact" id="contact">

    <h2 class="section-title">Let's Connect</h2>

    <p class="section-text">
        Thanks for visiting my portfolio.
        More projects and updates will be added here soon.
    </p>

    <a class="button" href="#">Back to Top</a>

</section>


<footer>
    Tishtup - Student Portfolio | Built with Python and Flask
</footer>

</body>
</html>
"""

app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 5000)))
