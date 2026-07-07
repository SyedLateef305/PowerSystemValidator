from dataclasses import dataclass, field


@dataclass
class SinkBusIncrement:
    bus_number: int
    increment: float


@dataclass
class Sink:
    area: int
    option: int
    load_percent: int
    location: int
    load_type: int
    bus_count: int = 0
    bus_increments: list[SinkBusIncrement] = field(default_factory=list)