import time
import random
import csv
import asyncio
import logging
from asyncio import get_running_loop
from textual.widget import Widget
from textual.reactive import Reactive

async def sleep(sleep_for: float) -> None:
    """An asyncio sleep.

    On Windows this achieves a better granularity than asyncio.sleep

    Args:
        sleep_for (float): Seconds to sleep for.
    """    
    await get_running_loop().run_in_executor(None, time.sleep, sleep_for)

class ReactionTimeExperiment:
    def __init__(self, trial_number):
        self.trial_number = trial_number
        self.trials = []
        self.start_time = 0.0
        self.current_trial = 0

    async def run_trials(self, ui):
        for trial in range(self.trial_number):
            self.current_trial = trial + 1
            logging.debug(f"Starting trial {self.current_trial}")
            await sleep(random.uniform(1, 10))
            ui.message = "Press 'z' now!"
            self.start_time = time.time()
            ui.awaiting_keypress = True
            while ui.awaiting_keypress:
                await asyncio.sleep(0.1)  # Use asyncio.sleep for short intervals

        ui.message = "Experiment is over"
        self.print_results()

    def record_reaction_time(self, reaction_time):
        logging.debug(f"Reaction time recorded: {reaction_time}")
        self.trials.append((self.current_trial, reaction_time))

    def print_results(self):
        with open("reaction_times.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Trial", "Reaction Time (s)"])
            for trial in self.trials:
                writer.writerow(trial)
        
        with open("reaction_times.csv", "r") as csvfile:
            logging.debug(csvfile.read())