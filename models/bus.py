from dataclasses import dataclass


@dataclass
class Bus:
    bus_id: int
    dummy_no: int
    zone_no: int
    base_voltage: float
    bus_name: str
    voltage: float
    angle: float
    pgen: float
    qgen: float
    pload: float
    qload: float
    qcomp: float
    island_no: int