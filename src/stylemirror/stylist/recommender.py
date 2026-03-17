"""Outfit recommender engine.

Suggests outfits based on occasion, weather, body type, color preference,
and the user's existing wardrobe.
"""

from stylemirror.models import (
    BodyType,
    ColorHarmonyType,
    Formality,
    Garment,
    GarmentCategory,
    OccasionType,
    Outfit,
    Season,
    StyleProfile,
    Weather,
)
from stylemirror.fashion.occasions import OccasionDresscode
from stylemirror.stylist.body_type import BodyTypeAnalyzer
from stylemirror.stylist.color_theory import ColorHarmonyEngine
from stylemirror.stylist.wardrobe import WardrobeManager


# Mapping from weather to suitable seasons as a fallback heuristic.
WEATHER_SEASON_MAP: dict[Weather, list[Season]] = {
    Weather.HOT: [Season.SUMMER],
    Weather.WARM: [Season.SUMMER, Season.SPRING],
    Weather.MILD: [Season.SPRING, Season.AUTUMN],
    Weather.COOL: [Season.AUTUMN, Season.SPRING],
    Weather.COLD: [Season.WINTER, Season.AUTUMN],
    Weather.RAINY: [Season.AUTUMN, Season.SPRING],
    Weather.SNOWY: [Season.WINTER],
}

# Minimum formality required per occasion type.
OCCASION_FORMALITY: dict[OccasionType, Formality] = {
    OccasionType.CASUAL_EVERYDAY: Formality.CASUAL,
    OccasionType.CASUAL_WEEKEND: Formality.VERY_CASUAL,
    OccasionType.BUSINESS_CASUAL: Formality.BUSINESS_CASUAL,
    OccasionType.BUSINESS_FORMAL: Formality.BUSINESS_FORMAL,
    OccasionType.DATE_NIGHT: Formality.SMART_CASUAL,
    OccasionType.COCKTAIL_PARTY: Formality.SEMI_FORMAL,
    OccasionType.FORMAL_GALA: Formality.FORMAL,
    OccasionType.WEDDING_GUEST: Formality.SEMI_FORMAL,
    OccasionType.JOB_INTERVIEW: Formality.BUSINESS_FORMAL,
    OccasionType.OUTDOOR_EVENT: Formality.CASUAL,
    OccasionType.BEACH: Formality.VERY_CASUAL,
    OccasionType.WORKOUT: Formality.VERY_CASUAL,
    OccasionType.BRUNCH: Formality.SMART_CASUAL,
}

# Formality levels ordered for comparison.
FORMALITY_ORDER: list[Formality] = [
    Formality.VERY_CASUAL,
    Formality.CASUAL,
    Formality.SMART_CASUAL,
    Formality.BUSINESS_CASUAL,
    Formality.BUSINESS_FORMAL,
    Formality.SEMI_FORMAL,
    Formality.FORMAL,
    Formality.BLACK_TIE,
    Formality.WHITE_TIE,
]


def _formality_index(f: Formality) -> int:
    try:
        return FORMALITY_ORDER.index(f)
    except ValueError:
        return 0


class OutfitRecommender:
    """Recommend outfits from a wardrobe based on multiple criteria.

    Considers occasion dress codes, weather/season appropriateness,
    body type guidelines, color harmony, and personal style preferences.
    """

    def __init__(
        self,
        wardrobe: WardrobeManager,
        style_profile: StyleProfile | None = None,
    ) -> None:
        self.wardrobe = wardrobe
        self.profile = style_profile
        self.color_engine = ColorHarmonyEngine()
        self.body_analyzer = BodyTypeAnalyzer()
        self.occasion_guide = OccasionDresscode()

    # ------------------------------------------------------------------
    # Main recommendation entry point
    # ------------------------------------------------------------------

    def recommend(
        self,
        occasion: OccasionType | str = OccasionType.CASUAL_EVERYDAY,
        weather: Weather | str = Weather.MILD,
        season: Season | str | None = None,
        body_type: BodyType | str | None = None,
        color_preference: str | None = None,
        max_results: int = 5,
    ) -> list[Outfit]:
        """Generate outfit recommendations.

        Parameters
        ----------
        occasion : OccasionType or str
            The event or context for the outfit.
        weather : Weather or str
            Current weather conditions.
        season : Season or str, optional
            Current season; inferred from weather if omitted.
        body_type : BodyType or str, optional
            Body type for tailored advice; falls back to profile.
        color_preference : str, optional
            A preferred base color to build around.
        max_results : int
            Maximum number of outfits to return.

        Returns
        -------
        list[Outfit]
            Scored and sorted outfit suggestions.
        """
        # Normalize enum inputs
        if isinstance(occasion, str):
            occasion = OccasionType(occasion)
        if isinstance(weather, str):
            weather = Weather(weather)
        if isinstance(season, str):
            season = Season(season)
        if isinstance(body_type, str):
            body_type = BodyType(body_type)

        # Infer season from weather if not provided
        if season is None:
            season = WEATHER_SEASON_MAP.get(weather, [Season.SPRING])[0]

        # Use profile body type as fallback
        if body_type is None and self.profile:
            body_type = self.profile.body_type

        # Determine required formality
        min_formality = OCCASION_FORMALITY.get(occasion, Formality.CASUAL)

        # Filter wardrobe
        candidates = self._filter_candidates(weather, season, min_formality)

        # Build outfit combinations
        outfits = self._build_outfits(
            candidates, occasion, season, min_formality, body_type, color_preference
        )

        # Sort by score descending
        outfits.sort(key=lambda o: o.score, reverse=True)
        return outfits[:max_results]

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _filter_candidates(
        self, weather: Weather, season: Season, min_formality: Formality
    ) -> list[Garment]:
        """Pre-filter wardrobe to season-appropriate, sufficiently formal items."""
        min_idx = _formality_index(min_formality)
        candidates: list[Garment] = []
        for g in self.wardrobe.get_all():
            # Season check
            if season not in g.seasons:
                continue
            # Formality: allow items at or one level below the minimum
            g_idx = _formality_index(g.formality)
            if g_idx < min_idx - 1:
                continue
            candidates.append(g)
        return candidates

    def _build_outfits(
        self,
        candidates: list[Garment],
        occasion: OccasionType,
        season: Season,
        formality: Formality,
        body_type: BodyType | None,
        color_preference: str | None,
    ) -> list[Outfit]:
        """Build and score outfit combinations from candidate garments."""
        tops = [g for g in candidates if g.category == GarmentCategory.TOP]
        bottoms = [g for g in candidates if g.category == GarmentCategory.BOTTOM]
        dresses = [g for g in candidates if g.category == GarmentCategory.DRESS]
        outerwear = [g for g in candidates if g.category == GarmentCategory.OUTERWEAR]
        footwear = [g for g in candidates if g.category == GarmentCategory.FOOTWEAR]
        accessories = [g for g in candidates if g.category == GarmentCategory.ACCESSORY]

        outfits: list[Outfit] = []

        # Strategy 1: Top + Bottom combinations
        for top in tops:
            for bottom in bottoms:
                garments = [top, bottom]
                # Optionally add outerwear
                if outerwear:
                    garments.append(outerwear[0])
                # Optionally add footwear
                if footwear:
                    garments.append(footwear[0])
                # Optionally add accessory
                if accessories:
                    garments.append(accessories[0])

                outfit = self._score_outfit(
                    garments, occasion, season, formality, body_type, color_preference
                )
                outfits.append(outfit)

        # Strategy 2: Dress-based outfits
        for dress in dresses:
            garments = [dress]
            if outerwear:
                garments.append(outerwear[0])
            if footwear:
                garments.append(footwear[0])
            if accessories:
                garments.append(accessories[0])

            outfit = self._score_outfit(
                garments, occasion, season, formality, body_type, color_preference
            )
            outfits.append(outfit)

        return outfits

    def _score_outfit(
        self,
        garments: list[Garment],
        occasion: OccasionType,
        season: Season,
        formality: Formality,
        body_type: BodyType | None,
        color_preference: str | None,
    ) -> Outfit:
        """Create and score a single outfit combination."""
        score = 5.0  # Base score
        notes: list[str] = []

        # --- Color harmony scoring ---
        colors = [g.color for g in garments]
        color_score, harmony_type, color_note = self.color_engine.evaluate_combination(colors)
        score += (color_score - 5.0) * 0.3  # Weight color at 30%
        notes.append(color_note)

        # Bonus for matching color preference
        if color_preference:
            if any(g.color.lower() == color_preference.lower() for g in garments):
                score += 0.5
                notes.append(f"Includes preferred color: {color_preference}.")

        # --- Body type scoring ---
        if body_type:
            for g in garments:
                bt_score, bt_note = self.body_analyzer.score_garment_fit(
                    body_type, g.name
                )
                score += (bt_score - 5.0) * 0.1
                if bt_score >= 8.0 or bt_score <= 4.0:
                    notes.append(bt_note)

        # --- Formality alignment ---
        formality_indices = [_formality_index(g.formality) for g in garments]
        avg_formality = sum(formality_indices) / len(formality_indices) if formality_indices else 0
        target_idx = _formality_index(formality)
        formality_diff = abs(avg_formality - target_idx)
        if formality_diff <= 0.5:
            score += 1.0
            notes.append("Formality level is well matched to the occasion.")
        elif formality_diff <= 1.5:
            score += 0.3
        else:
            score -= 0.5
            notes.append("Formality may not match the occasion well.")

        # --- Occasion-specific advice ---
        occasion_info = self.occasion_guide.get_dresscode(occasion)
        if occasion_info:
            notes.append(f"Occasion tip: {occasion_info.get('tip', '')}")

        # Clamp score
        score = max(0.0, min(10.0, score))

        # Build outfit name
        garment_names = [g.name for g in garments[:3]]
        outfit_name = " + ".join(garment_names)
        if len(garments) > 3:
            outfit_name += f" + {len(garments) - 3} more"

        return Outfit(
            name=outfit_name,
            garments=garments,
            occasion=occasion,
            formality=formality,
            season=season,
            color_harmony=harmony_type,
            score=round(score, 1),
            notes=notes,
        )
