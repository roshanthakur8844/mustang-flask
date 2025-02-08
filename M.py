from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mustang 1969 | Classic Legend</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            background: black;
            color: white;
            overflow: hidden;
        }

        .hero {
            padding: 50px;
            background: url('https://github.com/your-profile/images/mustang.jpg') no-repeat center;
            background-size: cover;
            height: 100vh; /* Full height */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        h1 {
            font-size: 3rem;
            text-shadow: 0 0 15px red;
        }

        .btn {
            padding: 12px 25px;
            background: red;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: 0.3s;
            font-size: 1.2rem;
            margin: 10px;
        }

        .btn:hover {
            background: yellow;
            color: black;
            transform: scale(1.1);
            box-shadow: 0 0 20px red;
        }

        .gallery img {
            width: 300px;
            margin: 10px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 0px 10px red;
        }

        .gallery img:hover {
            transform: scale(1.1);
            filter: brightness(1.2);
        }

        /* Full-screen smoke effect */
        #smoke {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: url('https://raw.githubusercontent.com/roshanthakur8844/Car/refs/heads/main/output-onlinegiftools.gif') no-repeat center;
            background-size: cover;
            opacity: 0;
            transition: opacity 1s ease-in-out;
            pointer-events: none;
        }
        
        /* Flash effect */
        .flash {
            background: red !important;
            transition: background 0.2s ease-in-out;
        }
    </style>
</head>
<body>

    <!-- Hero Section -->
    <div class="hero">
        <h1>Mustang 1969 - The Classic Beast</h1>
        <p>Power | Speed | Legacy</p>
        <a href="#" class="btn" onclick="startEngine()">Start Engine</a>
        <a href="#" class="btn" onclick="playRaceSound()">Race Mode</a>
    </div>

    <!-- Full-Screen Smoke Effect -->
    <div id="smoke"></div>

    <!-- Image Gallery -->
    <section class="gallery">
        <h2>Gallery</h2>
        <img src="https://raw.githubusercontent.com/roshanthakur8844/Car/refs/heads/main/RDT_20250208_192932973783823961050948-removebg-preview.png" alt="Mustang 1969">
        <img src="https://raw.githubusercontent.com/roshanthakur8844/Car/refs/heads/main/rear-of-the-year-69-mustang-gill-billington-removebg-preview.png" alt="Mustang View">
    </section>

    <!-- JavaScript for Interactivity -->
    <script>
        let raceAudio = null;

        function startEngine() {
            let audio = new Audio("https://raw.githubusercontent.com/roshanthakur8844/Car/main/videoplayback%20(1).m4a");
            document.body.classList.add("flash");
            setTimeout(() => {
                document.body.classList.remove("flash");
                setTimeout(() => {
                    let engineAudio = new Audio("https://github.com/your-profile/sounds/mustang-engine.mp3");
                    engineAudio.play();
                }, 1000);
            }, 500);
            audio.play();
            showSmoke();
        }

        function playRaceSound() {
            if (raceAudio === null || raceAudio.ended) {
                raceAudio = new Audio("https://raw.githubusercontent.com/roshanthakur8844/Car/main/EXTREME%20revving%20of%20Ford%20Mustang%20GT.mp3");
                raceAudio.play();
                showSmoke();
            }
        }

        function stopRaceSound() {
            if (raceAudio) {
                raceAudio.pause();
                raceAudio.currentTime = 0;
            }
        }

        function showSmoke() {
            let smoke = document.getElementById("smoke");
            smoke.style.opacity = "1";
            setTimeout(() => { smoke.style.opacity = "0"; }, 4000);
        }

        document.addEventListener("keydown", function(event) {
            if (event.key === "R" || event.key === "r") {
                playRaceSound();
            }
            if (event.key === "S" || event.key === "s") {
                stopRaceSound();
            }
        });
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)