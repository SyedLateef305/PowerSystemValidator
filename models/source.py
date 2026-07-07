from dataclasses import dataclass, field


@dataclass
class SourceBusIncrement:
    bus_number: int
    increment: float


@dataclass
class Source:
    area: int
    option: int
    location: int
    load_percent: int
    contribution: float
    bus_count: int = 0
    bus_increments: list[SourceBusIncrement] = field(default_factory=list)