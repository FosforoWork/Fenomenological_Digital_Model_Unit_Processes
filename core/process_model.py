"""Modelos de apoyo para historico y snapshots de la sala de control."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ControlLog:
    """Registro en memoria de snapshots temporales de variables."""

    max_points: int = 1000
    _rows: list[dict] = field(default_factory=list)
    _start_time: datetime = field(default_factory=datetime.now)

    def append(self, row: dict) -> None:
        elapsed = (datetime.now() - self._start_time).total_seconds()
        row_with_time = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "elapsed_s": elapsed,
            **row,
        }
        self._rows.append(row_with_time)
        if len(self._rows) > self.max_points:
            self._rows = self._rows[-self.max_points :]

    @property
    def rows(self) -> list[dict]:
        """Acceso publico de solo lectura a las filas almacenadas."""
        return self._rows

    def __len__(self) -> int:
        return len(self._rows)

    def __bool__(self) -> bool:
        return bool(self._rows)

    def to_dataframe(self):
        # Mantenido por retrocompatibilidad si otros scripts lo llaman,
        # pero importado perezosamente para ahorrar tiempo de carga inicial.
        import pandas as pd
        if not self._rows:
            return pd.DataFrame()
        return pd.DataFrame(self._rows)


def build_snapshot(
    controls: dict,
    result: dict,
    equipment_specs: dict | None = None,
    capacity_limits: dict | None = None,
) -> dict:
    """Aplana controles y resultados por etapa para persistir en historico."""
    snapshot: dict = {}

    for key, value in controls.items():
        snapshot[f"ctrl_{key}"] = float(value)

    if equipment_specs:
        for key, value in equipment_specs.items():
            snapshot[f"eq_{key}"] = float(value)

    if capacity_limits:
        for key, value in capacity_limits.items():
            snapshot[f"limit_{key}"] = float(value)

    for stage_name, stage_data in result.items():
        if isinstance(stage_data, dict):
            for key, value in stage_data.items():
                if isinstance(value, (int, float)):
                    snapshot[f"{stage_name}_{key}"] = float(value)

    return snapshot
