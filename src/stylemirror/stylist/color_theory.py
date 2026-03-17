"""Color theory engine for fashion color coordination.

Implements real color theory principles including the color wheel, complementary,
analogous, triadic, and split-complementary harmonies applied to fashion.
"""

from stylemirror.models import ColorHarmonyType, ColorPalette, Season

# Color wheel with 12 standard hues mapped to fashion-friendly color names.
# Positions are indexed 0-11 around the wheel (30-degree increments).
COLOR_WHEEL: list[str] = [
    "red",
    "red-orange",
    "orange",
    "yellow-orange",
    "yellow",
    "yellow-green",
    "green",
    "blue-green",
    "blue",
    "blue-violet",
    "violet",
    "red-violet",
]

# Mapping of common fashion color names to their nearest color-wheel position.
FASHION_COLOR_MAP: dict[str, int] = {
    "red": 0,
    "scarlet": 0,
    "crimson": 0,
    "cherry": 0,
    "coral": 1,
    "rust": 1,
    "terracotta": 1,
    "burnt orange": 2,
    "orange": 2,
    "tangerine": 2,
    "peach": 3,
    "apricot": 3,
    "amber": 3,
    "gold": 3,
    "mustard": 4,
    "yellow": 4,
    "lemon": 4,
    "chartreuse": 5,
    "lime": 5,
    "olive": 5,
    "sage": 5,
    "green": 6,
    "emerald": 6,
    "forest green": 6,
    "hunter green": 6,
    "mint": 6,
    "teal": 7,
    "turquoise": 7,
    "aqua": 7,
    "cyan": 7,
    "blue": 8,
    "navy": 8,
    "cobalt": 8,
    "royal blue": 8,
    "denim": 8,
    "sky blue": 8,
    "powder blue": 8,
    "indigo": 9,
    "periwinkle": 9,
    "violet": 10,
    "purple": 10,
    "plum": 10,
    "lavender": 10,
    "eggplant": 10,
    "magenta": 11,
    "fuchsia": 11,
    "mauve": 11,
    "burgundy": 11,
    "wine": 11,
    "berry": 11,
    "maroon": 0,
    "pink": 11,
    "blush": 11,
    "rose": 11,
    "hot pink": 11,
}

# Neutral colors that pair with everything and sit outside the color wheel.
NEUTRAL_COLORS: set[str] = {
    "black",
    "white",
    "gray",
    "grey",
    "charcoal",
    "ivory",
    "cream",
    "beige",
    "tan",
    "khaki",
    "taupe",
    "camel",
    "brown",
    "chocolate",
    "espresso",
    "cognac",
    "nude",
    "off-white",
    "ecru",
    "silver",
}

# Seasonal color palettes based on seasonal color analysis theory.
SEASONAL_PALETTES: dict[Season, list[str]] = {
    Season.SPRING: [
        "coral", "peach", "mint", "sky blue", "yellow", "lavender",
        "turquoise", "blush", "chartreuse", "cream",
    ],
    Season.SUMMER: [
        "white", "navy", "powder blue", "rose", "lavender", "sage",
        "mauve", "periwinkle", "soft yellow", "silver",
    ],
    Season.AUTUMN: [
        "burgundy", "rust", "mustard", "olive", "forest green", "burnt orange",
        "terracotta", "camel", "chocolate", "gold",
    ],
    Season.WINTER: [
        "black", "white", "red", "emerald", "royal blue", "cobalt",
        "purple", "fuchsia", "charcoal", "navy",
    ],
}

# Classic color combinations that are universally recognized in fashion.
CLASSIC_COMBINATIONS: list[tuple[str, str, str]] = [
    ("navy", "white", "Nautical classic"),
    ("black", "white", "Timeless monochrome"),
    ("camel", "white", "Elegant neutral"),
    ("navy", "burgundy", "Rich sophistication"),
    ("olive", "cream", "Earth-toned elegance"),
    ("gray", "blush", "Modern romance"),
    ("navy", "mustard", "Bold complementary"),
    ("emerald", "gold", "Luxe pairing"),
    ("burgundy", "camel", "Autumn warmth"),
    ("cobalt", "orange", "Dynamic contrast"),
]


class ColorHarmonyEngine:
    """Engine for analyzing and recommending color harmonies in fashion.

    Uses real color theory (12-point color wheel) to determine complementary,
    analogous, triadic, and split-complementary color pairings, translated
    into practical fashion color names.
    """

    def __init__(self) -> None:
        self._wheel = COLOR_WHEEL
        self._fashion_map = FASHION_COLOR_MAP
        self._neutrals = NEUTRAL_COLORS

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def is_neutral(self, color: str) -> bool:
        """Check whether a color is considered neutral."""
        return color.lower() in self._neutrals

    def wheel_position(self, color: str) -> int | None:
        """Return the 0-11 wheel position for a fashion color, or None if neutral/unknown."""
        return self._fashion_map.get(color.lower())

    # ------------------------------------------------------------------
    # Core harmony calculations
    # ------------------------------------------------------------------

    def complementary(self, color: str) -> list[str]:
        """Return the complementary color (opposite on the wheel).

        Complementary colors create maximum contrast and visual interest.
        In fashion, this pairing is bold and eye-catching: e.g. blue + orange,
        red + green (in muted tones like burgundy + sage).
        """
        pos = self.wheel_position(color)
        if pos is None:
            return []
        comp_pos = (pos + 6) % 12
        return [self._wheel[comp_pos]]

    def analogous(self, color: str) -> list[str]:
        """Return analogous colors (adjacent on the wheel).

        Analogous palettes feel harmonious and cohesive.  They are easy to
        wear and create a sophisticated tonal look: e.g. blue, blue-green,
        green.
        """
        pos = self.wheel_position(color)
        if pos is None:
            return []
        return [
            self._wheel[(pos - 1) % 12],
            self._wheel[(pos + 1) % 12],
        ]

    def triadic(self, color: str) -> list[str]:
        """Return triadic colors (evenly spaced 120 degrees apart).

        Triadic palettes are vibrant and balanced.  In fashion, one color
        typically dominates while the other two serve as accents:
        e.g. red + yellow + blue.
        """
        pos = self.wheel_position(color)
        if pos is None:
            return []
        return [
            self._wheel[(pos + 4) % 12],
            self._wheel[(pos + 8) % 12],
        ]

    def split_complementary(self, color: str) -> list[str]:
        """Return split-complementary colors.

        Instead of the direct complement, uses the two colors adjacent to the
        complement.  Offers strong contrast with less tension than pure
        complementary: e.g. blue -> yellow-orange + red-orange.
        """
        pos = self.wheel_position(color)
        if pos is None:
            return []
        comp_pos = (pos + 6) % 12
        return [
            self._wheel[(comp_pos - 1) % 12],
            self._wheel[(comp_pos + 1) % 12],
        ]

    def monochromatic(self, color: str) -> list[str]:
        """Suggest monochromatic variations (same hue family).

        Returns the color itself as the anchoring hue, plus any fashion
        synonyms mapped to the same wheel position.
        """
        pos = self.wheel_position(color)
        if pos is None:
            return [color.lower()]
        return [
            name
            for name, p in self._fashion_map.items()
            if p == pos and name != color.lower()
        ]

    # ------------------------------------------------------------------
    # High-level API
    # ------------------------------------------------------------------

    def find_harmonies(self, color: str) -> dict[ColorHarmonyType, list[str]]:
        """Return all harmony types for a given color."""
        result: dict[ColorHarmonyType, list[str]] = {}
        if self.is_neutral(color):
            result[ColorHarmonyType.NEUTRAL] = sorted(self._neutrals - {color.lower()})
            return result

        result[ColorHarmonyType.COMPLEMENTARY] = self.complementary(color)
        result[ColorHarmonyType.ANALOGOUS] = self.analogous(color)
        result[ColorHarmonyType.TRIADIC] = self.triadic(color)
        result[ColorHarmonyType.SPLIT_COMPLEMENTARY] = self.split_complementary(color)
        result[ColorHarmonyType.MONOCHROMATIC] = self.monochromatic(color)
        return result

    def evaluate_combination(self, colors: list[str]) -> tuple[float, ColorHarmonyType | None, str]:
        """Evaluate how well a set of colors work together.

        Returns (score 0-10, detected harmony type or None, explanation).
        """
        if not colors:
            return 0.0, None, "No colors provided."

        lower = [c.lower() for c in colors]
        chromatic = [c for c in lower if not self.is_neutral(c)]
        neutrals = [c for c in lower if self.is_neutral(c)]

        # All neutrals is always safe
        if not chromatic:
            return 8.0, ColorHarmonyType.NEUTRAL, (
                "All-neutral palette. Safe and versatile; consider adding one accent color "
                "for visual interest."
            )

        if len(chromatic) == 1:
            base = 8.5
            explanation = f"Single chromatic color ({chromatic[0]}) anchored with neutrals. "
            if neutrals:
                explanation += "Clean, polished look."
                base = 9.0
            else:
                explanation += "Consider adding a neutral for balance."
            return base, ColorHarmonyType.MONOCHROMATIC, explanation

        # Check for recognized harmonies between the first two chromatic colors
        pos_a = self.wheel_position(chromatic[0])
        pos_b = self.wheel_position(chromatic[1])
        if pos_a is None or pos_b is None:
            return 5.0, None, "Unable to map one or more colors to the color wheel."

        diff = (pos_b - pos_a) % 12

        if diff == 6:
            return 9.0, ColorHarmonyType.COMPLEMENTARY, (
                f"Complementary pairing ({chromatic[0]} + {chromatic[1]}). "
                "Bold contrast that draws the eye. Balance with a neutral."
            )
        if diff in (1, 11):
            return 8.5, ColorHarmonyType.ANALOGOUS, (
                f"Analogous pairing ({chromatic[0]} + {chromatic[1]}). "
                "Harmonious and easy to wear."
            )
        if diff in (4, 8):
            return 8.5, ColorHarmonyType.TRIADIC, (
                f"Triadic relationship detected ({chromatic[0]} + {chromatic[1]}). "
                "Vibrant; let one color dominate and use the other as an accent."
            )
        if diff in (5, 7):
            return 8.0, ColorHarmonyType.SPLIT_COMPLEMENTARY, (
                f"Split-complementary pairing ({chromatic[0]} + {chromatic[1]}). "
                "Strong contrast with less visual tension than pure complementary."
            )
        if diff in (2, 10):
            return 7.0, ColorHarmonyType.ANALOGOUS, (
                f"Extended analogous pairing ({chromatic[0]} + {chromatic[1]}). "
                "Works well but ensure enough contrast in value (light vs dark)."
            )
        if diff in (3, 9):
            return 6.5, None, (
                f"Square relationship ({chromatic[0]} + {chromatic[1]}). "
                "Can work if tones are balanced; add a neutral anchor."
            )

        return 5.5, None, "Unusual color combination. Could be creative or clashing."

    def build_palette(
        self,
        base_color: str,
        harmony: ColorHarmonyType = ColorHarmonyType.COMPLEMENTARY,
        season: Season | None = None,
    ) -> ColorPalette:
        """Build a complete fashion color palette from a base color and harmony type."""
        harmonies_map = {
            ColorHarmonyType.COMPLEMENTARY: self.complementary,
            ColorHarmonyType.ANALOGOUS: self.analogous,
            ColorHarmonyType.TRIADIC: self.triadic,
            ColorHarmonyType.SPLIT_COMPLEMENTARY: self.split_complementary,
            ColorHarmonyType.MONOCHROMATIC: self.monochromatic,
        }

        fn = harmonies_map.get(harmony)
        results = fn(base_color) if fn else []

        secondary = results[0] if results else "gray"
        accent = results[1] if len(results) > 1 else None

        season_affinity: list[Season] = []
        if season:
            season_affinity = [season]
        else:
            for s, palette_colors in SEASONAL_PALETTES.items():
                if base_color.lower() in [c.lower() for c in palette_colors]:
                    season_affinity.append(s)

        return ColorPalette(
            name=f"{base_color.title()} {harmony.value.replace('_', ' ').title()}",
            primary=base_color.lower(),
            secondary=secondary,
            accent=accent,
            neutral="white" if base_color.lower() not in {"white", "cream", "ivory"} else "charcoal",
            harmony_type=harmony,
            season_affinity=season_affinity,
        )

    def seasonal_recommendations(self, season: Season) -> list[str]:
        """Return recommended colors for a given season."""
        return SEASONAL_PALETTES.get(season, [])

    def get_classic_combinations(self) -> list[tuple[str, str, str]]:
        """Return list of classic fashion color combinations with descriptions."""
        return list(CLASSIC_COMBINATIONS)
