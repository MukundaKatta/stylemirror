"""Wardrobe management for tracking owned clothing items."""

import json
from pathlib import Path

from stylemirror.models import Formality, Garment, GarmentCategory, Season


class WardrobeManager:
    """Manage a personal wardrobe of clothing items.

    Supports adding, removing, searching, and filtering garments by
    category, color, formality, and season.
    """

    def __init__(self, storage_path: Path | None = None) -> None:
        self._garments: list[Garment] = []
        self._storage_path = storage_path or Path("wardrobe.json")

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self) -> None:
        """Save the wardrobe to a JSON file."""
        data = [g.model_dump(mode="json") for g in self._garments]
        self._storage_path.write_text(json.dumps(data, indent=2))

    def load(self) -> None:
        """Load the wardrobe from a JSON file."""
        if self._storage_path.exists():
            data = json.loads(self._storage_path.read_text())
            self._garments = [Garment.model_validate(item) for item in data]

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add_garment(self, garment: Garment) -> None:
        """Add a garment to the wardrobe."""
        self._garments.append(garment)

    def remove_garment(self, name: str) -> bool:
        """Remove a garment by name.  Returns True if found and removed."""
        for i, g in enumerate(self._garments):
            if g.name.lower() == name.lower():
                self._garments.pop(i)
                return True
        return False

    def get_all(self) -> list[Garment]:
        """Return all garments."""
        return list(self._garments)

    def count(self) -> int:
        """Return the total number of garments."""
        return len(self._garments)

    # ------------------------------------------------------------------
    # Filtering
    # ------------------------------------------------------------------

    def by_category(self, category: GarmentCategory) -> list[Garment]:
        """Filter garments by category."""
        return [g for g in self._garments if g.category == category]

    def by_color(self, color: str) -> list[Garment]:
        """Filter garments by primary or secondary color."""
        color_lower = color.lower()
        return [
            g
            for g in self._garments
            if g.color.lower() == color_lower
            or (g.secondary_color and g.secondary_color.lower() == color_lower)
        ]

    def by_formality(self, formality: Formality) -> list[Garment]:
        """Filter garments by formality level."""
        return [g for g in self._garments if g.formality == formality]

    def by_season(self, season: Season) -> list[Garment]:
        """Filter garments suitable for a season."""
        return [g for g in self._garments if season in g.seasons]

    def by_tag(self, tag: str) -> list[Garment]:
        """Filter garments by a custom tag."""
        tag_lower = tag.lower()
        return [g for g in self._garments if tag_lower in [t.lower() for t in g.tags]]

    def favorites(self) -> list[Garment]:
        """Return favorite garments."""
        return [g for g in self._garments if g.favorite]

    def search(self, query: str) -> list[Garment]:
        """Search garments by name, color, material, brand, or tags."""
        q = query.lower()
        results: list[Garment] = []
        for g in self._garments:
            searchable = " ".join(
                [
                    g.name,
                    g.color,
                    g.secondary_color or "",
                    g.material or "",
                    g.brand or "",
                ]
                + g.tags
            ).lower()
            if q in searchable:
                results.append(g)
        return results

    # ------------------------------------------------------------------
    # Analytics
    # ------------------------------------------------------------------

    def color_distribution(self) -> dict[str, int]:
        """Return a count of garments per primary color."""
        dist: dict[str, int] = {}
        for g in self._garments:
            key = g.color.lower()
            dist[key] = dist.get(key, 0) + 1
        return dict(sorted(dist.items(), key=lambda x: x[1], reverse=True))

    def category_distribution(self) -> dict[str, int]:
        """Return a count of garments per category."""
        dist: dict[str, int] = {}
        for g in self._garments:
            key = g.category.value
            dist[key] = dist.get(key, 0) + 1
        return dict(sorted(dist.items(), key=lambda x: x[1], reverse=True))

    def formality_distribution(self) -> dict[str, int]:
        """Return a count of garments per formality level."""
        dist: dict[str, int] = {}
        for g in self._garments:
            key = g.formality.value
            dist[key] = dist.get(key, 0) + 1
        return dict(sorted(dist.items(), key=lambda x: x[1], reverse=True))

    def wardrobe_gaps(self) -> list[str]:
        """Identify missing categories or formality levels in the wardrobe."""
        gaps: list[str] = []
        present_categories = {g.category for g in self._garments}
        essential = {
            GarmentCategory.TOP,
            GarmentCategory.BOTTOM,
            GarmentCategory.FOOTWEAR,
            GarmentCategory.OUTERWEAR,
        }
        for cat in essential:
            if cat not in present_categories:
                gaps.append(f"Missing category: {cat.value}")

        present_formality = {g.formality for g in self._garments}
        key_formalities = {Formality.CASUAL, Formality.SMART_CASUAL, Formality.BUSINESS_CASUAL}
        for f in key_formalities:
            if f not in present_formality:
                gaps.append(f"No items at formality level: {f.value}")

        colors = self.color_distribution()
        if len(colors) < 3:
            gaps.append("Limited color variety; consider expanding your palette.")

        return gaps
