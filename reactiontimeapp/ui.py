
from textual.widget import Widget
from textual.widgets import Button 

class ReactionTimeUI(Widget):

    def compose(self):
        yield Button("Start", id="start_button")
    