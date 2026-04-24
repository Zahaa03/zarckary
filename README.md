# Zarckary Game

## Overview
Zarckary is a Python-based game that combines resource management, combat mechanics, and event handling. Players navigate through various challenges, managing resources like water bottles and engaging in battles.

## Features
- **Resource Management**: Manage water bottles with a simplified system where each bottle has a fixed value and fullness percentage.
- **Combat Mechanics**: Engage in battles using the `FIGHT` function.
- **Event Handling**: Dynamic events that challenge the player.
- **Save System**: Encrypted save files ensure progress is secure.

## Files
- **zarckary.py**: Core game logic.
- **zarckary_watcher.py**: Monitors game state.
- **zark.json**: Encrypted save file.
- **Zcryptv1.py**: Handles save file encryption/decryption.

## How to Play
1. **Setup**: Ensure Python 3.x is installed on your system.
2. **Run the Game**: Execute `zarckary.py` to start the game.
3. **Manage Resources**: Use the `drink` functionality to manage water bottles effectively.
4. **Engage in Combat**: Use the `FIGHT` function to battle enemies.
5. **Save Progress**: The game automatically saves progress in an encrypted file.

## Usage Instructions
- **Starting the Game**: Run the following command in your terminal:
  ```bash
  python zarckary.py
  ```
  If python zarckary.py does not work try:
  ```bash
  python3 zarckary.py
  ````

- **Drinking Water**: The `drink` functionality allows you to consume water bottles. Each bottle has a fixed value and fullness percentage.
- **Combat**: Use the `FIGHT` function to engage in battles. Ensure you have sufficient resources before entering combat.

## Debugging and Development
- **Testing**: Use `zarckary_watcher.py` to monitor the game state during development.
- **Encryption**: Modify `Zcryptv1.py` for custom encryption settings.
- **Save Files**: The `zark.json` file stores encrypted game progress.

## Requirements
- Python 3.x

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.