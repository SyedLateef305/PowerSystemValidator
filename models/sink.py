from dataclasses import dataclass


@dataclass
class Sink:
    area: int
    option: int
    load_percent: int
    location: int
    load_type: int