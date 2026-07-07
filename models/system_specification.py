from dataclasses import dataclass


@dataclass
class SystemSpecification:
    max_bus_id: int
    total_buses: int
    total_two_wdg: int
    total_three_wdg: int
    total_lines: int
    total_series_reactors: int
    total_series_capacitors: int
    total_bus_couplers: int
    total_shunt_reactors: int
    total_shunt_capacitors: int
    total_motors: int

    total_generators: int
    total_loads: int
    total_filters: int
    total_hvdc: int

    island_count: int = 0
    zones: int = 0
    print_option: int = 0
    plot_option: int = 0
    base_mva: float = 100.0
    frequency: float = 50.0