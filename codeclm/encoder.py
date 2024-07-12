from dataclasses import dataclass

from codeclm.helpers.metadata import get_metadata

@dataclass
class Metadata:
    use_case: str
    skills: list


class Encoder:
    instruction: str
    metadata: dict

    def __init__(self, instruction: str) -> None:
        self.instruction = instruction

    def generate_metadata(self) -> tuple:
        self.metadata = get_metadata(self.instruction)

        return self.metadata
