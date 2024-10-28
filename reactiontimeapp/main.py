import sys
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from textual.app import App
from textual.widgets import Header, Footer
from reactiontimeapp.ui import ReactionTimeUI

class ReactionTimeApp(App):
    title = "Reaction Time App"
    css_path = "styles.css"

    def compose(self):
        yield Header()
        yield ReactionTimeUI()
        yield Footer()

if __name__ == "__main__":
    ReactionTimeApp().run()