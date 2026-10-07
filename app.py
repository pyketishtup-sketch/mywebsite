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
            0% {
                text-shadow: 0 0 5px #38bdf8;
            }

            50% {
                text-shadow: 0 0 25px #38bdf8;
            }

            100% {
                text-shadow: 0 0 5px #38bdf8;
            }
        }

        @keyframes floatGlow {
            0%, 100% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-25px);
            }
        }


        /* NAVIGATION */

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
            transition: 0.3s;
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

            padding: 70px 20px;

            background:
                radial-gradient(
                    circle at 50% 20%,
                    #172554 0%,
                    #0b1120 55%
                );

            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: "";

            position: absolute;

            width: 350px;
            height: 350px;

            border-radius: 50%;

            background: #38bdf8;

            opacity: 0.08;

            filter: blur(80px);

            animation: floatGlow 5s ease-in-out infinite;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero small {
            display: inline-block;

            color: #38bdf8;

            font-size: 14px;

            letter-spacing: 3px;

            padding: 8px 15px;

            border: 1px solid #1e7494;

            border-radius: 20px;

            background: #0f2030;

            animation: fadeUp 1s ease;
        }

        .hero h1 {
            font-size: 70px;

            margin: 22px 0 10px;

            animation: fadeUp 1.2s ease;
        }

        .hero h1 span {
            color: #38bdf8;

            animation: glow 2s infinite;
        }

        .hero p {
            color: #94a3b8;

            font-size: 20px;

            max-width: 650px;

            margin: auto;

            animation: fadeUp 1.4s ease;
        }

        .hero-info {
            display: flex;

            justify-content: center;

            flex-wrap: wrap;

            gap: 15px;

            margin-top: 30px;

            animation: fadeUp 1.5s ease;
        }

        .info-box {
            padding: 12px 20px;

            background: #111827;

            border: 1px solid #263449;

            border-radius: 10px;

            color: #cbd5e1;

            transition: 0.3s;
        }

        .info-box:hover {
            transform: translateY(-5px);

            border-color: #38bdf8;

            box-shadow:
                0 8px 25px rgba(56, 189, 248, 0.12);
        }


        /* BUTTON */

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

            animation: fadeUp 1.6s ease;
        }

        .button:hover {
            transform: translateY(-4px);

            box-shadow:
                0 10px 30px rgba(56, 189, 248, 0.25);
        }


        /* SECTIONS */

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


        /* CARDS */

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

            box-shadow:
                0 15px 35px rgba(0, 0, 0, 0.3);
        }

        .card h3 {
            color: #38bdf8;

            margin-bottom: 12px;

            font-size: 22px;
        }

        .card p {
            color: #94a3b8;
        }


        /* SKILLS */

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

            transition: 0.3s;
        }

        .skill:hover {
            color: #38bdf8;

            border-color: #38bdf8;

            transform: translateY(-3px);
        }


        /* INTERESTS */

        .interests {
            background: #0f172a;
        }

        .interest-card {
            width: 300px;

            padding: 35px 25px;

            background: #111827;

            border: 1px solid #1e293b;

            border-radius: 18px;

            transition: 0.3s;
        }

        .interest-card:hover {
            transform: translateY(-10px);

            border-color: #38bdf8;

            box-shadow:
                0 15px 35px rgba(56, 189, 248, 0.12);
        }

        .interest-icon {
            font-size: 45px;

            margin-bottom: 15px;
        }

        .interest-card h3 {
            color: #38bdf8;

            font-size: 23px;

            margin-bottom: 10px;
        }

        .interest-card p {
            color: #94a3b8;
        }


        /* CONTACT */

        .contact {
            background: #111827;
        }


        /* FOOTER */

        footer {
            padding: 25px;

            text-align: center;

            color: #64748b;

            background: #070b14;
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

            .hero {
                min-height: 85vh;
            }

            .hero h1 {
                font-size: 45px;
            }

            .hero p {
                font-size: 17px;
            }

            .hero small {
                font-size: 11px;

                letter-spacing: 2px;
            }

            section {
                padding: 65px 5%;
            }

            .section-title {
                font-size: 30px;
            }

        }

    </style>

</head>


<body>


    <!-- NAVIGATION -->

    <nav>

        <div class="logo">
            Tishtup.
        </div>

        <div>

            <a href="#about">About</a>

            <a href="#skills">Skills</a>

            <a href="#projects">Projects</a>

            <a href="#interests">Interests</a>

            <a href="#contact">Contact</a>

        </div>

    </nav>


    <!-- HERO -->

    <section class="hero">

        <div class="hero-content">

            <small>
                CLASS XI - PCM - COMPUTER SCIENCE
            </small>

            <h1>
                Hi, I'm <span>Tishtup.</span>
            </h1>

            <p>
                Student, learner and aspiring developer.
                I am exploring programming, web development
                and technology one project at a time.
            </p>


            <div class="hero-info">

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


            <a class="button" href="#about">
                Explore My Portfolio
            </a>

        </div>

    </section>


    <!-- ABOUT -->

    <section id="about">

        <h2 class="section-title">
            About Me
        </h2>

        <p class="section-text">
            I am a Class XI student studying Physics,
            Chemistry, Mathematics and Computer Science.
            I enjoy learning technology and building
            things with code.
        </p>


        <div class="cards">


            <div class="card">

                <h3>
                    Education
                </h3>

                <p>
                    Class XI student with a focus on
                    PCM and Computer Science.
                </p>

            </div>


            <div class="card">

                <h3>
                    Programming
                </h3>

                <p>
                    Currently learning Python,
                    Flask, HTML and CSS.
                </p>

            </div>


            <div class="card">

                <h3>
                    Goal
                </h3>

                <p>
                    Keep learning, build useful projects
                    and become a better developer.
                </p>

            </div>


        </div>

    </section>


    <!-- SKILLS -->

    <section id="skills">

        <h2 class="section-title">
            My Skills
        </h2>

        <p class="section-text">
            Technologies and subjects I am currently learning.
        </p>


        <div class="skills">

            <div class="skill">
                Python
            </div>

            <div class="skill">
                Flask
            </div>

            <div class="skill">
                HTML
            </div>

            <div class="skill">
                CSS
            </div>

            <div class="skill">
                Java
            </div>

            <div class="skill">
                Physics
            </div>

            <div class="skill">
                Chemistry
            </div>

            <div class="skill">
                Mathematics
            </div>

        </div>

    </section>


    <!-- PROJECTS -->

    <section id="projects">

        <h2 class="section-title">
            My Projects
        </h2>

        <p class="section-text">
            Things I have built and things I am working on.
        </p>


        <div class="cards">


            <div class="card">

                <h3>
                    Student Portfolio
                </h3>

                <p>
                    This website, built using
                    Python and Flask.
                </p>

            </div>


            <div class="card">

                <h3>
                    Python Programs
                </h3>

                <p>
                    Small programs and experiments
                    created while learning Python.
                </p>

            </div>


            <div class="card">

                <h3>
                    Future Projects
                </h3>

                <p>
                    More interesting projects
                    are coming soon.
                </p>

            </div>


        </div>

    </section>


    <!-- BEYOND ACADEMICS -->

    <section class="interests" id="interests">

        <h2 class="section-title">
            Beyond Academics
        </h2>

        <p class="section-text">
            The things I enjoy outside my studies
            and programming.
        </p>


        <div class="cards">


            <div class="interest-card">

                <div class="interest-icon">
                    Cricket
                </div>

                <h3>
                    Cricket
                </h3>

                <p>
                    A sport I have loved since childhood.
                    Cricket is one of my biggest passions.
                </p>

            </div>


            <div class="interest-card">

                <div class="interest-icon">
                    Tech
                </div>

                <h3>
                    Technology
                </h3>

                <p>
                    I enjoy exploring computers,
                    programming and new technology.
                </p>

            </div>


            <div class="interest-card">

                <div class="interest-icon">
                    Learning
                </div>

                <h3>
                    Learning
                </h3>

                <p>
                    I like learning new things and
                    improving my skills step by step.
                </p>

            </div>


        </div>

    </section>


    <!-- CONTACT -->

    <section class="contact" id="contact">

        <h2 class="section-title">
            Let's Connect
        </h2>

        <p class="section-text">
            Thanks for visiting my portfolio.
            More projects and updates will be
            added here soon.
        </p>

        <a class="button" href="#">
            Back to Top
        </a>

    </section>


    <!-- FOOTER -->

    <footer>

        Tishtup - Student Portfolio |
        Built with Python and Flask

    </footer>


</body>

</html>
"""


app.run(
    host="0.0.0.0",
    port=int(__import__("os").environ.get("PORT", 5000))
)
