# Tank on Ice

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/marcinostaszewski/tank_on_ice.git
    cd tank_on_ice
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Starting the Game

1. Ensure the virtual environment is activated.
2. Run the game:
    ```sh
    python main.py
    ```

## Running the Watcher for Development

1. Ensure the virtual environment is activated.
2. Install `watchdog` if not already installed:
    ```sh
    pip install watchdog
    ```
3. Run the watcher:
    ```sh
    py ./watcher.py
    ```

This will automatically restart the game whenever a Python file is modified.