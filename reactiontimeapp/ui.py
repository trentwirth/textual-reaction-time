from textual.widget import Widget
from textual.widgets import Button
from textual import events

import logging

logging.basicConfig(level=logging.INFO)

class ReactionTimeUI(Widget):

    def compose(self):
        yield Button("Start", id="start_button")
        yield Button("z", id="z_button")
        yield Button("m", id="m_button")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start_button":
            logging.info("Start button pressed")

    async def on_key(self, event: events.Key) -> None:
        if event.key == "z":
            self.query_one("#z_button").press()
            logging.info("z pressed")
        elif event.key == "m":
            self.query_one("#m_button").press()
            logging.info("m pressed")