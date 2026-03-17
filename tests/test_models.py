"""Tests for pydantic models."""

import pytest
from pydantic import ValidationError

from stylemirror.models import (
    BodyType,
    ColorHarmonyType,
    ColorPalette,
    Formality,
    Garment,
    GarmentCategory,
    OccasionType,
    Outfit,
    Season,
    StyleProfile,
    StyleType,
)


class TestGarment:
    def test_create_basic_garment(self):
        g = Garment(name="White T-Shirt", category=GarmentCategory.TOP, color="white")
        assert g.name == "White T-Shirt"
        assert g.category == GarmentCategory.TOP
        assert g.color == "white"
        assert g.formality == Formality.CASUAL  # default
        assert g.favorite is False

    def test_create_full_garment(self):
        g = Garment(
            name="Navy Blazer",
            category=GarmentCategory.OUTERWEAR,
            color="navy",
            secondary_color="gold",
            formality=Formality.SMART_CASUAL,
            seasons=[Season.SPRING, Season.AUTUMN],
            material="wool",
            brand="Brooks Brothers",
            tags=["workwear", "essential"],
            favorite=True,
        )
        assert g.secondary_color == "gold"
        assert g.material == "wool"
        assert g.brand == "Brooks Brothers"
        assert Season.SPRING in g.seasons
        assert "workwear" in g.tags
        assert g.favorite is True

    def test_garment_requires_name(self):
        with pytest.raises(ValidationError):
            Garment(category=GarmentCategory.TOP, color="white")

    def test_garment_serialization(self):
        g = Garment(name="Test", category=GarmentCategory.TOP, color="red")
        data = g.model_dump()
        assert data["name"] == "Test"
        restored = Garment.model_validate(data)
        assert restored.name == "Test"


class TestOutfit:
    def test_create_outfit(self):
        top = Garment(name="Shirt", category=GarmentCategory.TOP, color="white")
        bottom = Garment(name="Chinos", category=GarmentCategory.BOTTOM, color="khaki")
        outfit = Outfit(
            name="Casual Friday",
            garments=[top, bottom],
            occasion=OccasionType.BUSINESS_CASUAL,
            formality=Formality.BUSINESS_CASUAL,
            season=Season.SPRING,
            score=7.5,
        )
        assert len(outfit.garments) == 2
        assert outfit.score == 7.5

    def test_outfit_score_bounds(self):
        top = Garment(name="Shirt", category=GarmentCategory.TOP, color="white")
        with pytest.raises(ValidationError):
            Outfit(
                name="Bad",
                garments=[top],
                occasion=OccasionType.CASUAL_EVERYDAY,
                formality=Formality.CASUAL,
                season=Season.SUMMER,
                score=11.0,
            )


class TestStyleProfile:
    def test_create_profile(self):
        profile = StyleProfile(
            body_type=BodyType.HOURGLASS,
            preferred_style=StyleType.CLASSIC,
            preferred_colors=["navy", "white"],
        )
        assert profile.body_type == BodyType.HOURGLASS
        assert profile.preferred_style == StyleType.CLASSIC
        assert "navy" in profile.preferred_colors


class TestColorPalette:
    def test_create_palette(self):
        palette = ColorPalette(
            name="Ocean",
            primary="navy",
            secondary="turquoise",
            accent="coral",
            harmony_type=ColorHarmonyType.COMPLEMENTARY,
        )
        assert palette.primary == "navy"
        assert palette.accent == "coral"


class TestEnums:
    def test_all_body_types(self):
        assert len(BodyType) >= 9

    def test_all_style_types(self):
        assert len(StyleType) >= 5

    def test_all_occasion_types(self):
        assert len(OccasionType) >= 10

    def test_formality_ordering(self):
        assert Formality.VERY_CASUAL != Formality.FORMAL
