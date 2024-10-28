import logging
import time
from textual.widget import Widget
from textual.reactive import Reactive
from textual.widgets import Button
from textual.events import Key
from reactiontimeapp.utilities.parameters import TRIAL_NUMBER
from reactiontimeapp.experiment import ReactionTimeExperiment

class ReactionTimeUI(Widget):
    message: Reactive[str] = Reactive("Press the start button to begin the reaction time test.")
    experiment: ReactionTimeExperiment = ReactionTimeExperiment(TRIAL_NUMBER)
    awaiting_keypress: Reactive[bool] = Reactive(False)

    def compose(self):
        yield Button("Start", id="start_button")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start_button":
            logging.debug("Start button pressed")
            self.message = "Get ready..."
            await self.experiment.run_trials(self)

    async def on_key(self, event: Key) -> None:
        logging.debug(f"Key pressed: {event.key}")
        if self.awaiting_keypress and event.key == "z":
            reaction_time = time.time() - self.experiment.start_time
            self.experiment.record_reaction_time(reaction_time)
            self.message = "Get ready for the next trial..."
            self.awaiting_keypress = False