# textual-reaction-time
 A reaction time app built on the Textual framework for Prof. Trent Wirth's PSYC 3010 Programming for Behavioral Scientists course. The purpose of the app is to construct a dual-choice reaction time task where participants (students) will react to X's and O's by pressing different keys. Their reaction time to the different letters, as well as their accuracy, will be saved locally to their machine in either a `.csv` or a `.txt` file. 

Target File Tree:
```text
reactiontimeapp/
├── reactiontimeapp/              # Main package folder
│   ├── __init__.py               # Makes the folder a package
│   ├── main.py                   # Main entry point and app orchestration
│   ├── ui.py                     # Handles Textual UI components and instructions
│   ├── reactions.py              # Logic for reaction time measurement and trials
│   ├── data_manager.py           # Functions for handling file paths and saving data
│   └── config.py                 # Configurations and constants, e.g., trial count
├── tests/                        # Folder for unit tests
│   ├── __init__.py
│   ├── test_reactions.py         # Tests for reaction timing logic
│   ├── test_data_manager.py      # Tests for data saving and file handling
│   └── test_ui.py                # Tests for UI components if needed
├── requirements.txt              # Required dependencies for the project
├── setup.py                      # Setup file for pip installation
└── README.md                     # Project description and instructions
```