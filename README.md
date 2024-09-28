
# 🏴‍☠️ Pirate's Code: Battle for Booty 🏴‍☠️

## Overview
Welcome to **Pirate's Code: Battle for Booty**, a thrilling adventure that immerses you in the life of a pirate navigating the treacherous waters of the seven seas! This Python-based simulation leverages Object-Oriented Programming (OOP) principles to create a dynamic and engaging experience where players can build their fleets, engage in epic battles, and loot enemy ships for treasure.

## Features
- **🚢 Ship Customization**: Purchase and manage your very own ships, complete with a robust cargo hold for storing your plunder.
- **⚔️ Naval Combat**: Engage enemy ships in thrilling battles, using strategy and firepower to emerge victorious.
- **💰 Looting System**: After defeating enemy vessels, loot their cargo to enhance your inventory with valuable items.
- **🔧 Ship Maintenance**: Repair your ship using the treasures you acquire to keep it seaworthy for future adventures.
- **📦 Inventory Management**: Balance your resources between cannonballs, gold, and other plundered goods to ensure your success on the high seas.

## Classes

### 🏴‍☠️ Pirate
The **Pirate** class represents your character, allowing for actions such as purchasing ships, battling enemies, and looting treasure.

- **Attributes**:
  - `name`: The name of the pirate.
  - `inventory`: A collection of loot items.
  - `ship`: The pirate's current ship.

- **Key Methods**:
  - `purchase_ship(ship)`: Buy a ship and add it to the pirate's fleet.
  - `battle(enemy_ship)`: Engage in battle with an enemy ship.
  - `loot_ship(enemy_ship)`: Loot cargo from a defeated enemy ship.

### 🚢 Ship
The **Ship** class encapsulates the details of the pirate's vessel, including its condition and cargo.

- **Attributes**:
  - `name`: The name of the ship.
  - `damage_counter`: A counter tracking the ship's damage.
  - `cargo`: The items stored in the ship's hold.

- **Key Methods**:
  - `take_hit()`: Increase damage on the ship.
  - `repair_ship()`: Repair the ship if it is damaged.

### 💰 Loot
The **Loot** class represents the treasure and items that pirates can collect.

- **Attributes**:
  - `name`: The name of the loot item.
  - `description`: A brief description of the item.

- **Key Methods**:
  - `get_name()`: Retrieve the name of the loot.
  - `get_description()`: Retrieve the description of the loot.

## Getting Started

### Prerequisites
To run this project, you'll need:
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mridul-Learing-Unisa/Pirate-Battle-for-Booty.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Pirate-Battle-for-Booty
   ```

### Running the Game
Execute the main program to start your pirate adventure:
```bash
python main.py
```
### Example Gameplay
Once the game starts, you'll be introduced to your pirate character. Purchase a ship, engage in battles, and embark on a journey of loot and glory! Will you become the most feared pirate of the seas?


Set sail and enjoy your adventure in **Pirate's Code: Battle for Booty**! 🏴‍☠️💰
