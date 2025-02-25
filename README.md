# Pong Game

This project is a classic implementation of the Pong game using Python's `turtle` module. It's a two-player game where each player controls a paddle to hit the ball back and forth.

## Features

- **Two-Player Mode**: Player A uses the 'W' and 'S' keys to move their paddle up and down, while Player B uses the 'Up' and 'Down' arrow keys.
- **Score Tracking**: The game keeps track of each player's score, displayed at the top of the screen.
- **Ball Dynamics**: The ball resets to the center after a point is scored and moves in the direction of the player who scored.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/singhvibhanshu/Pong-Game.git
   cd Pong-Game
   ```

2. **Install Dependencies**:

   Ensure you have Python installed on your system. This game uses the `turtle` module, which is included in the Python Standard Library.

## Usage

1. **Run the Game**:

   Execute the `main.py` file:

   ```bash
   python main.py
   ```

2. **Controls**:

   - **Player A**:
     - Move Up: Press 'W'
     - Move Down: Press 'S'
   - **Player B**:
     - Move Up: Press 'Up Arrow'
     - Move Down: Press 'Down Arrow'

3. **Gameplay**:

   - Each time the ball passes a paddle, the opposing player scores a point.
   - The game continues indefinitely, allowing players to compete for the highest score.

## Notes

- Ensure your Python environment is set up correctly to run the `turtle` module.
- The game window can be closed by clicking the close button on the window.

---