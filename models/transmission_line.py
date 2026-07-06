from dataclasses import dataclass


@dataclass
class TransmissionLine:
    status: int
    circuits: int
    from_bus: int
    to_bus: int
    resistance: float
    reactance: float
    charging: float