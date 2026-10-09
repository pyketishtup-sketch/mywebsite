
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
    <meta name="theme-color" content="#0b1020">
    <meta name="description" content="Tishtup Pyke's personal portfolio featuring programming, technology, cricket and Mumbai Indians.">
    <title>Tishtup Pyke | Student Portfolio</title>

    <style>
        :root {
            color-scheme: dark;
            --bg: #0b1020;
            --nav: rgba(11, 16, 32, .88);
            --card: rgba(23, 33, 57, .82);
            --text: #f8fafc;
            --muted: #cbd5e1;
            --subtle: #94a3b8;
            --accent: #38bdf8;
            --accent2: #a78bfa;
            --border: rgba(148, 163, 184, .19);
            --shadow: rgba(0, 0, 0, .28);
            --footer: #070b16;
            --mi-blue: #3b82f6;
            --mi-gold: #fbbf24;
        }

        body.light {
            color-scheme: light;
            --bg: #f4f7ff;
            --nav: rgba(244, 247, 255, .90);
            --card: rgba(255, 255, 255, .86);
            --text: #111827;
            --muted: #334155;
            --subtle: #64748b;
            --accent: #0369a1;
            --accent2: #7c3aed;
            --border: rgba(71, 85, 105, .18);
            --shadow: rgba(30, 41, 59, .10);
            --footer: #e5ebf7;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(ellipse at 10% 5%, rgba(56,189,248,.10), transparent 35%),
                radial-gradient(ellipse at 90% 25%, rgba(167,139,250,.12), transparent 35%),
                var(--bg);
            color: var(--text);
            line-height: 1.7;
            overflow-x: hidden;
            transition: background-color .3s, color .3s;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        button {
            font: inherit;
        }

        .container {
            width: 90%;
            max-width: 1120px;
            margin: auto;
        }

        /* Navigation */

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: var(--nav);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--border);
        }

        .nav-inner {
            min-height: 74px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
        }

        .logo {
            font-size: 1.4rem;
            font-weight: 900;
            letter-spacing: -1px;
            white-space: nowrap;
        }

        .logo span {
            color: var(--accent);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .nav-links a {
            color: var(--muted);
            font-size: .89rem;
            transition: color .2s;
        }

        .nav-links a:hover {
            color: var(--accent);
        }

        #theme-toggle {
            border: 1px solid var(--border);
            background: var(--card);
            color: var(--text);
            padding: 9px 12px;
            border-radius: 30px;
            cursor: pointer;
            white-space: nowrap;
            transition: transform .2s, border-color .2s;
        }

        #theme-toggle:hover {
            transform: translateY(-2px);
            border-color: var(--accent);
        }

        /* Hero */

        .hero {
            min-height: 82vh;
            display: flex;
            align-items: center;
            position: relative;
            padding: 95px 0 80px;
            isolation: isolate;
        }

        .hero::before,
        .hero::after {
            content: "";
            position: absolute;
            width: 280px;
            height: 280px;
            border-radius: 50%;
            filter: blur(85px);
            opacity: .22;
            z-index: -1;
            pointer-events: none;
            animation: floatGlow 8s ease-in-out infinite alternate;
        }

        .hero::before {
            background: #0ea5e9;
            top: 8%;
            right: 12%;
        }

        .hero::after {
            background: #8b5cf6;
            bottom: 4%;
            right: 35%;
            animation-delay: -4s;
        }

        .hero-content {
            max-width: 820px;
            animation: fadeUp .9s ease both;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            color: var(--accent);
            font-size: .83rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .eyebrow::before {
            content: "";
            width: 26px;
            height: 2px;
            background: var(--accent);
            border-radius: 5px;
        }

        .hero h1 {
            font-size: clamp(3rem, 8vw, 6rem);
            line-height: 1.08;
            letter-spacing: -3px;
            margin: 22px 0 15px;
        }

        .gradient-text {
            color: var(--accent);
            background: linear-gradient(100deg, var(--accent), var(--accent2));
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero h2 {
            color: var(--muted);
            font-size: clamp(1.15rem, 3vw, 1.65rem);
            font-weight: 500;
            margin-bottom: 18px;
        }

        .hero-description {
            max-width: 680px;
            color: var(--subtle);
            font-size: 1.05rem;
        }

        .hero-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-top: 30px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 21px;
            border-radius: 10px;
            font-weight: 750;
            border: 1px solid var(--border);
            transition: transform .25s, box-shadow .25s, border-color .25s;
        }

        .btn:hover {
            transform: translateY(-4px);
        }

        .btn-primary {
            background: linear-gradient(110deg, #0ea5e9, #818cf8);
            color: #07111f;
            border-color: transparent;
            box-shadow: 0 8px 28px rgba(14,165,233,.18);
        }

        .btn-primary:hover {
            box-shadow: 0 12px 35px rgba(14,165,233,.30);
        }

        .btn-secondary {
            background: var(--card);
            color: var(--text);
        }

        .subject-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 34px;
        }

        .subject {
            padding: 7px 13px;
            font-size: .88rem;
            color: var(--muted);
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 30px;
            backdrop-filter: blur(8px);
        }

        /* General sections */

        section {
            padding: 82px 0;
            scroll-margin-top: 80px;
        }

        .section-heading {
            text-align: center;
            margin-bottom: 42px;
        }

        .section-heading h2 {
            font-size: clamp(2rem, 5vw, 2.8rem);
            line-height: 1.2;
            margin-bottom: 10px;
            letter-spacing: -1px;
        }

        .section-heading p {
            color: var(--subtle);
        }

        .section-heading h2 span {
            color: var(--accent);
        }

        /* About */

        .glass-panel {
            max-width: 850px;
            margin: auto;
            padding: 32px;
            border: 1px solid var(--border);
            border-radius: 20px;
            background: var(--card);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            box-shadow: 0 18px 45px var(--shadow);
        }

        .glass-panel p {
            color: var(--muted);
            margin-bottom: 15px;
        }

        .glass-panel p:last-child {
            margin-bottom: 0;
        }

        /* Cards */

        .cards {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 22px;
        }

        .card {
            position: relative;
            overflow: hidden;
            padding: 27px;
            border-radius: 18px;
            border: 1px solid var(--border);
            background: var(--card);
            box-shadow: 0 12px 30px var(--shadow);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            transition:
                transform .28s ease,
                border-color .28s ease,
                box-shadow .28s ease,
                background .3s ease;
        }

        .card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent);
            opacity: 0;
            transition: opacity .28s;
        }

        .card:hover {
            transform: translateY(-7px);
            border-color: var(--accent);
            box-shadow: 0 18px 38px var(--shadow);
        }

        .card:hover::before {
            opacity: 1;
        }

        .card-icon {
            width: 54px;
            height: 54px;
            display: grid;
            place-items: center;
            border-radius: 15px;
            margin-bottom: 18px;
            font-size: 1.8rem;
            background: linear-gradient(135deg, rgba(56,189,248,.14), rgba(167,139,250,.17));
            border: 1px solid var(--border);
        }

        .card h3 {
            font-size: 1.2rem;
            margin-bottom: 10px;
        }

        .card p {
            color: var(--subtle);
            font-size: .96rem;
        }

        .card-link {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            margin-top: 18px;
            color: var(--accent);
            font-weight: 750;
            overflow-wrap: anywhere;
            transition: gap .2s;
        }

        .card-link:hover {
            gap: 11px;
        }

        .project-label {
            display: inline-block;
            color: var(--accent);
            background: rgba(56,189,248,.09);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 4px 10px;
            margin-bottom: 14px;
            font-size: .76rem;
            font-weight: 750;
        }

        /* Cricket Zone */

        .cricket-section {
            position: relative;
            isolation: isolate;
        }

        .cricket-section::before {
            content: "";
            position: absolute;
            inset: 12% 0;
            z-index: -1;
            pointer-events: none;
            background:
                radial-gradient(ellipse at 15% 35%, rgba(37,99,235,.15), transparent 40%),
                radial-gradient(ellipse at 85% 65%, rgba(251,191,36,.08), transparent 38%);
        }

        .mi-banner {
            position: relative;
            overflow: hidden;
            margin-bottom: 38px;
            padding: clamp(28px, 5vw, 48px);
            border-radius: 24px;
            border: 1px solid rgba(96,165,250,.35);
            background:
                radial-gradient(ellipse at 85% 15%, rgba(96,165,250,.28), transparent 40%),
                linear-gradient(125deg, #071b49, #123e86 55%, #0b1b3e);
            box-shadow: 0 18px 50px rgba(0, 0, 0, .20);
            color: #f8fafc;
        }

        .mi-banner::after {
            content: "MI";
            position: absolute;
            right: 5%;
            top: 50%;
            transform: translateY(-50%) rotate(-8deg);
            font-size: clamp(6rem, 20vw, 13rem);
            line-height: 1;
            font-weight: 1000;
            letter-spacing: -12px;
            color: rgba(255,255,255,.055);
            pointer-events: none;
        }

        .mi-banner-content {
            position: relative;
            z-index: 1;
            max-width: 670px;
        }

        .mi-kicker {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: #fbbf24;
            font-size: .8rem;
            letter-spacing: 2px;
            font-weight: 900;
            text-transform: uppercase;
        }

        .mi-banner h3 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            line-height: 1.15;
            margin: 14px 0;
            letter-spacing: -1px;
        }

        .mi-banner p {
            color: #dbeafe;
            max-width: 560px;
        }

        .mi-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 23px;
        }

        .mi-badge {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,.20);
            background: rgba(255,255,255,.08);
            font-size: .84rem;
            color: #f8fafc;
        }

        .cricket-subheading {
            margin: 30px 0 22px;
            font-size: 1.35rem;
            letter-spacing: -.3px;
        }

        .player-card {
            padding: 0;
        }

        .player-art {
            position: relative;
            height: 175px;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            background:
                radial-gradient(circle at 50% 40%, rgba(255,255,255,.20), transparent 35%),
                linear-gradient(135deg, var(--player-color), #10182d);
        }

        .player-art::before,
        .player-art::after {
            content: "";
            position: absolute;
            border: 1px solid rgba(255,255,255,.13);
            border-radius: 50%;
            width: 180px;
            height: 180px;
        }

        .player-art::after {
            width: 130px;
            height: 130px;
        }

        .player-initials {
            position: relative;
            z-index: 1;
            font-size: 3.7rem;
            font-weight: 1000;
            letter-spacing: -3px;
            color: rgba(255,255,255,.96);
            text-shadow: 0 8px 30px rgba(0,0,0,.24);
        }

        .player-number {
            position: absolute;
            top: 12px;
            right: 14px;
            z-index: 1;
            color: rgba(255,255,255,.85);
            font-weight: 800;
            font-size: .82rem;
        }

        .player-info {
            padding: 22px;
        }

        .player-role {
            display: inline-block;
            margin: 0 0 9px;
            padding: 4px 9px;
            color: var(--accent);
            background: rgba(56,189,248,.09);
            border: 1px solid var(--border);
            border-radius: 20px;
            font-size: .75rem;
            font-weight: 800;
        }

        .player-info h4 {
            font-size: 1.18rem;
            margin-bottom: 7px;
        }

        .player-info p {
            color: var(--subtle);
            font-size: .91rem;
        }

        .cricket-note {
            margin-top: 24px;
            color: var(--subtle);
            font-size: .85rem;
            text-align: center;
        }

        /* Contact */

        .contact-intro {
            max-width: 650px;
            margin: 0 auto 32px;
            color: var(--subtle);
            text-align: center;
        }

        /* Scroll reveal */

        .reveal {
            opacity: 0;
            transform: translateY(22px);
            transition: opacity .65s ease, transform .65s ease;
        }

        .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

        footer {
            padding: 28px 0;
            text-align: center;
            color: var(--subtle);
            background: var(--footer);
            border-top: 1px solid var(--border);
        }

        footer strong {
            color: var(--accent);
        }

        footer p + p {
            margin-top: 5px;
            font-size: .85rem;
        }

        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(24px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes floatGlow {
            from {
                transform: translate(0, 0) scale(1);
            }
            to {
                transform: translate(-25px, 20px) scale(1.12);
            }
        }

        @media (max-width: 900px) {
            .nav-inner {
                padding: 13px 0;
                flex-wrap: wrap;
            }

            .nav-links {
                order: 3;
                width: 100%;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px 15px;
            }

            .cards {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .hero {
                min-height: 72vh;
            }
        }

        @media (max-width: 560px) {
            .container {
                width: 92%;
            }

            .logo {
                font-size: 1.2rem;
            }

            #theme-toggle {
                font-size: .82rem;
                padding: 8px 10px;
            }

            .nav-links {
                gap: 9px 13px;
            }

            .nav-links a {
                font-size: .83rem;
            }

            .hero {
                padding: 70px 0;
            }

            .hero h1 {
                letter-spacing: -1.7px;
            }

            section {
                padding: 60px 0;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .glass-panel {
                padding: 23px;
            }

            .mi-banner {
                padding: 25px;
            }

            .player-art {
                height: 155px;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *,
            *::before,
            *::after {
                scroll-behavior: auto !important;
                animation: none !important;
                transition: none !important;
            }

            .reveal {
                opacity: 1;
                transform: none;
            }
        }
    </style>
</head>

<body>
    <nav>
        <div class="container nav-inner">
            <a href="#home" class="logo">TISHTUP<span>.</span></a>

            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#interests">Interests</a>
                <a href="#cricket">Cricket</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>

            <button id="theme-toggle" type="button"
                aria-label="Switch to light mode" aria-pressed="false">
                ☀️ Light mode
            </button>
        </div>
    </nav>

    <main>
        <!-- Hero -->
        <section class="hero" id="home">
            <div class="container">
                <div class="hero-content">
                    <p class="eyebrow">Student portfolio</p>

                    <h1>Hi, I'm<br><span class="gradient-text">Tishtup Pyke.</span></h1>

                    <h2>Student · Learner · Future Developer</h2>

                    <p class="hero-description">
                        Exploring the world of technology, programming,
                        science, and new ideas. This is where my learning
                        journey meets creativity.
                    </p>

                    <div class="hero-buttons">
                        <a href="#projects" class="btn btn-primary">
                            Explore My Work ↗
                        </a>
                        <a href="#contact" class="btn btn-secondary">
                            Let's Connect
                        </a>
                    </div>

                    <div class="subject-list">
                        <span class="subject">⚛️ Physics</span>
                        <span class="subject">🧪 Chemistry</span>
                        <span class="subject">📐 Mathematics</span>
                        <span class="subject">💻 Computer Science</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- About -->
        <section id="about">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>About <span>Me</span></h2>
                    <p>A little about the person behind the screen.</p>
                </div>

                <div class="glass-panel reveal">
                    <p>
                        Hello! I'm Tishtup Pyke, a Class XI student studying
                        Physics, Chemistry, and Mathematics, along with
                        Computer Science.
                    </p>
                    <p>
                        I enjoy solving problems, understanding how things
                        work, exploring technology, and learning programming.
                        I'm developing my skills through practice and
                        personal projects like this website.
                    </p>
                    <p>
                        Beyond academics, cricket has a special place in my
                        life. I also enjoy discovering new technologies and
                        challenging myself to learn something new.
                    </p>
                </div>
            </div>
        </section>

        <!-- Skills -->
        <section id="skills">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>My <span>Skills</span></h2>
                    <p>Learning, practising, and improving every day.</p>
                </div>

                <div class="cards">
                    <article class="card reveal">
                        <div class="card-icon">🐍</div>
                        <h3>Python</h3>
                        <p>
                            Learning Python fundamentals and building a
                            foundation in programming.
                        </p>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">🌐</div>
                        <h3>Web Development</h3>
                        <p>
                            Exploring Flask, HTML, CSS, and JavaScript
                            to create interactive websites.
                        </p>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">🧠</div>
                        <h3>Problem Solving</h3>
                        <p>
                            Strengthening logical thinking through
                            mathematics, science, and coding.
                        </p>
                    </article>
                </div>
            </div>
        </section>

        <!-- Interests -->
        <section id="interests">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>Beyond <span>Academics</span></h2>
                    <p>What keeps me curious and inspired.</p>
                </div>

                <div class="cards">
                    <article class="card reveal">
                        <div class="card-icon">🏏</div>
                        <h3>Cricket</h3>
                        <p>
                            A sport I've loved since childhood.
                            Cricket is one of my biggest passions.
                        </p>
                        <a class="card-link" href="#cricket">Enter Cricket Zone ↗</a>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">💻</div>
                        <h3>Technology</h3>
                        <p>
                            Exploring computers, software, websites,
                            and the technology shaping our world.
                        </p>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">🚀</div>
                        <h3>Learning</h3>
                        <p>
                            Discovering new concepts, improving my
                            skills, and taking on fresh challenges.
                        </p>
                    </article>
                </div>
            </div>
        </section>

        <!-- Premium Cricket Zone -->
        <section id="cricket" class="cricket-section">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>The <span>Cricket Zone</span></h2>
                    <p>A little space dedicated to the game I love. 🏏</p>
                </div>

                <div class="mi-banner reveal">
                    <div class="mi-banner-content">
                        <span class="mi-kicker">💙 My Favourite IPL Team</span>
                        <h3>Mumbai Indians</h3>
                        <p>
                            Blue and gold, unforgettable cricket memories,
                            and a team that makes every match exciting.
                            Mumbai Indians will always have a special place
                            in my cricket world.
                        </p>

                        <div class="mi-badges">
                            <span class="mi-badge">🔵 One Family</span>
                            <span class="mi-badge">🏏 Cricket Passion</span>
                            <span class="mi-badge">💛 Blue & Gold</span>
                        </div>
                    </div>
                </div>

                <div class="section-heading reveal">
                    <h2>Players I <span>Admire</span></h2>
                    <p>Four names that make cricket even more exciting.</p>
                </div>

                <div class="cards">
                    <article class="card player-card reveal">
                        <div class="player-art"
                            style="--player-color:#1746a2;">
                            <span class="player-number">01</span>
                            <span class="player-initials">RS</span>
                        </div>
                        <div class="player-info">
                            <span class="player-role">BATTER</span>
                            <h4>Rohit Sharma</h4>
                            <p>
                                Known for elegant stroke play, effortless
                                timing, and memorable big scores. A key
                                favourite in my cricket zone.
                            </p>
                        </div>
                    </article>

                    <article class="card player-card reveal">
                        <div class="player-art"
                            style="--player-color:#7c2d12;">
                            <span class="player-number">02</span>
                            <span class="player-initials">VK</span>
                        </div>
                        <div class="player-info">
                            <span class="player-role">BATTER</span>
                            <h4>Virat Kohli</h4>
                            <p>
                                Famous for intensity, consistency, and
                                chasing challenging targets. A player
                                admired by cricket fans everywhere.
                            </p>
                        </div>
                    </article>

                    <article class="card player-card reveal">
                        <div class="player-art"
                            style="--player-color:#075985;">
                            <span class="player-number">03</span>
                            <span class="player-initials">JB</span>
                        </div>
                        <div class="player-info">
                            <span class="player-role">FAST BOWLER</span>
                            <h4>Jasprit Bumrah</h4>
                            <p>
                                Recognised for a distinctive bowling
                                action, precision, and exceptional
                                control in high-pressure overs.
                            </p>
                        </div>
                    </article>

                    <article class="card player-card reveal">
                        <div class="player-art"
                            style="--player-color:#9a3412;">
                            <span class="player-number">04</span>
                            <span class="player-initials">HP</span>
                        </div>
                        <div class="player-info">
                            <span class="player-role">ALL-ROUNDER</span>
                            <h4>Hardik Pandya</h4>
                            <p>
                                An explosive batter and seam-bowling
                                all-rounder known for bringing energy
                                and power to the game.
                            </p>
                        </div>
                    </article>
                </div>

                <p class="cricket-note reveal">
                    A fan-made personal section. Player cards use
                    stylised initials rather than official player photos
                    or team logos.
                </p>
            </div>
        </section>

        <!-- Projects -->
        <section id="projects">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>Featured <span>Projects</span></h2>
                    <p>Small steps today. Bigger ideas tomorrow.</p>
                </div>

                <div class="cards">
                    <article class="card reveal">
                        <span class="project-label">01 · WEB DEVELOPMENT</span>
                        <div class="card-icon">🖥️</div>
                        <h3>Personal Portfolio</h3>
                        <p>
                            A responsive personal website built with Flask,
                            HTML, CSS, and JavaScript, featuring a theme
                            switcher and animated design.
                        </p>
                        <a class="card-link" href="#home">Explore this site ↗</a>
                    </article>

                    <article class="card reveal">
                        <span class="project-label">02 · PROGRAMMING</span>
                        <div class="card-icon">⚙️</div>
                        <h3>Python Experiments</h3>
                        <p>
                            A growing collection of programming exercises
                            and experiments created while learning Python.
                        </p>
                        <a class="card-link"
                           href="https://github.com/pyketishtup-sketch"
                           target="_blank" rel="noopener noreferrer">
                            Visit GitHub ↗
                        </a>
                    </article>

                    <article class="card reveal">
                        <span class="project-label">03 · COMING SOON</span>
                        <div class="card-icon">✨</div>
                        <h3>Future Projects</h3>
                        <p>
                            More ideas, experiments, and useful projects
                            will be added as I continue learning.
                        </p>
                        <a class="card-link" href="#contact">Stay connected ↗</a>
                    </article>
                </div>
            </div>
        </section>

        <!-- Contact -->
        <section id="contact">
            <div class="container">
                <div class="section-heading reveal">
                    <h2>Let's <span>Connect</span></h2>
                    <p>Thanks for taking the time to visit.</p>
                </div>

                <p class="contact-intro reveal">
                    Follow my learning journey and explore the projects
                    I'm working on.
                </p>

                <div class="cards">
                    <article class="card reveal">
                        <div class="card-icon">🐙</div>
                        <h3>GitHub</h3>
                        <p>Explore my code and programming experiments.</p>
                        <a class="card-link"
                           href="https://github.com/pyketishtup-sketch"
                           target="_blank" rel="noopener noreferrer">
                            @pyketishtup-sketch ↗
                        </a>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">📸</div>
                        <h3>Instagram</h3>
                        <p>Find me on Instagram using my username.</p>
                        <p class="card-link">tishtup._.1845._.pyke</p>
                    </article>

                    <article class="card reveal">
                        <div class="card-icon">🌟</div>
                        <h3>Keep Growing</h3>
                        <p>
                            Every new skill starts with curiosity and
                            a willingness to learn.
                        </p>
                        <a class="card-link" href="#home">Back to top ↑</a>
                    </article>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>Designed with curiosity by <strong>Tishtup Pyke</strong> 💙</p>
            <p>Student Portfolio · Class XI · Keep learning.</p>
        </div>
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
                    isLight ? "#f4f7ff" : "#0b1020"
                );
            }

            let savedTheme = "dark";

            try {
                savedTheme = localStorage.getItem("tishtup-theme") || "dark";
            } catch (error) {
                savedTheme = "dark";
            }

            if (savedTheme !== "light" && savedTheme !== "dark") {
                savedTheme = "dark";
            }

            applyTheme(savedTheme);

            button.addEventListener("click", function () {
                const nextTheme =
                    document.body.classList.contains("light")
                        ? "dark"
                        : "light";

                applyTheme(nextTheme);

                try {
                    localStorage.setItem("tishtup-theme", nextTheme);
                } catch (error) {
                    // Theme switching still works if storage is unavailable.
                }
            });

            const revealElements = document.querySelectorAll(".reveal");

            if ("IntersectionObserver" in window) {
                const observer = new IntersectionObserver(
                    function (entries, currentObserver) {
                        entries.forEach(function (entry) {
                            if (entry.isIntersecting) {
                                entry.target.classList.add("visible");
                                currentObserver.unobserve(entry.target);
                            }
                        });
                    },
                    { threshold: 0.12 }
                );

                revealElements.forEach(function (element) {
                    observer.observe(element);
                });
            } else {
                revealElements.forEach(function (element) {
                    element.classList.add("visible");
                });
            }
        })();
    </script>
</body>
</html>
    """


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
