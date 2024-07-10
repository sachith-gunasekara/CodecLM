from codeclm.helpers.metadata import get_metadata

class Encoder:
    instruction: str
    metadata: dict

    def __init__(self, instruction: str) -> None:
        self.instruction = instruction

    def generate_metadata(self) -> tuple:
        self.metadata = get_metadata(self.instruction)

        return self