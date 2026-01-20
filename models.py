from dataclasses import dataclass

@dataclass
class Prompt:
    name: str
    version: int
    content: str