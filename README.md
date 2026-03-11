Asteroids.

Asteroids is a small Python game featuring a player-controlled spaceship and numerous spawning objects such as ‘asteroids’, ‘ores’, and player shots. This guided project by boot.dev was designed to practise core software engineering skills, including object-oriented design, event-driven programming, and managing game state in Python using Pygame.

Key features:

The base project included:

•	Core game loop with delta time calculations for frame-rate independent movement, capped at 60 FPS to reduce CPU usage and maintain consistent game speed.
•	Movement system using the w,s,d,a keys and space bar.
•	Basic object interactions between the player’s shots and asteroids, as well as the player and asteroids.
•	Object spawning and ‘destruction’.

Personal additions made that enhance the base project:

•	Implemented a more realistic, inertia-based movement system, allowing the player to glide in short bursts, mimicking movement in space.
•	Added a basic scoring system with an endgame screen to provide feedback on player performance.
•	Created custom sound effects using Audacity for laser shots and asteroid destruction, with additional effects for score thresholds, enhancing engagement.
•	Introduced additional ‘ores’ that spawn when asteroids are destroyed, providing buffs or extra score.
•	Made aesthetic and colour improvements to enhance the visual experience.

Installation instructions:

This project is developed for Python 3.x using Pygame. It has been tested in Ubuntu on WSL and requires a virtual environment with Pygame installed. Running outside this environment may result in errors or missing functionality.

1. Clone or download the ‘Asteroids’ repository from GitHub.

2. Open a terminal in the top-level asteroids folder.

3. Create and activate a virtual environment in the terminal.

python3 -m venv venv
source venv/bin/activate

4. Install dependencies.

pip install -r requirements.txt

5. Run the game.

python3 main.py

6. To exit the virtual environment.

deactivate

Known issue:

•	Rapidly firing or holding down the shoot key may cause some sound effects to stop playing permanently until the game is restarted. This is due to limitations in Pygame’s audio mixer and how it handles multiple overlapping sounds. Note: Playing single shots slowly will allow all sound effects to be heard correctly.

Design choices:

•	Chose an inertia-based movement system for a more realistic and satisfying player experience.
•	Implemented a scoring system and endgame screen to reward player performance.
•	Custom sound effects and score-based audio feedback make gameplay more engaging.
•	Added ‘ores’ that spawn from destroyed asteroids, giving buffs or additional score.

Future improvements:

•	Considering finding a better way to implement sounds, to avoid the aforementioned issue with overlapping sounds.
•	Improving the UI to provide better information to the player on what certain ‘ores’ buff and what the score thresholds are.
•	May consider adding an ‘enemy’ spaceship for extra challenge.
