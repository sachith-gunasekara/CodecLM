from helpers.generate import f_s

class Encoder:

    def __init__(self, instruction: str) -> None:
        self.instruction = instruction

    def generate_metadata(self) -> tuple:
        