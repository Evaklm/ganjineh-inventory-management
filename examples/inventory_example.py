"""Synthetic inventory-position example for the Ganjineh portfolio.

This standalone example illustrates domain calculations only. It contains no
production source, customer information, database access, or deployment logic.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class InventoryPosition:
    physical: int
    reserved: int
    incoming: int = 0

    def __post_init__(self) -> None:
        if min(self.physical, self.reserved, self.incoming) < 0:
            raise ValueError("inventory quantities must be non-negative")

    @property
    def available(self) -> int:
        return max(0, self.physical - self.reserved)

    @property
    def shortage(self) -> int:
        return max(0, self.reserved - self.physical)

    @property
    def projected_available(self) -> int:
        return max(0, self.physical + self.incoming - self.reserved)


if __name__ == "__main__":
    sample = InventoryPosition(physical=18, reserved=23, incoming=12)
    print(
        {
            "available": sample.available,
            "shortage": sample.shortage,
            "projected_available": sample.projected_available,
        }
    )

