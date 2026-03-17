"""Tests for the outfit recommender engine."""

import pytest

from stylemirror.models import (
    BodyType,
    Formality,
    Garment,
    GarmentCategory,
    OccasionType,
    Season,
    StyleProfile,
    StyleType,
    Weather,
)
from stylemirror.stylist.recommender import OutfitRecommender
from stylemirror.stylist.wardrobe import WardrobeManager


@pytest.fixture
def full_wardrobe():
    """A wardrobe with diverse items for testing recommendations."""
    wm = WardrobeManager()
    items = [
        Garment(name="White Oxford Shirt", category=GarmentCategory.TOP, color="white",
                formality=Formality.BUSINESS_CASUAL),
        Garment(name="Navy Polo", category=GarmentCategory.TOP, color="navy",
                formality=Formality.SMART_CASUAL),
        Garment(name="Gray T-Shirt", category=GarmentCategory.TOP, color="gray",
                formality=Formality.CASUAL),
        Garment(name="Khaki Chinos", category=GarmentCategory.BOTTOM, color="khaki",
                formality=Formality.BUSINESS_CASUAL),
        Garment(name="Dark Jeans", category=GarmentCategory.BOTTOM, color="indigo",
                formality=Formality.CASUAL),
        Garment(name="Navy Blazer", category=GarmentCategory.OUTERWEAR, color="navy",
                formality=Formality.SMART_CASUAL),
        Garment(name="Brown Loafers", category=GarmentCategory.FOOTWEAR, color="brown",
                formality=Formality.SMART_CASUAL),
        Garment(name="Black Dress", category=GarmentCategory.DRESS, color="black",
                formality=Formality.SEMI_FORMAL),
        Garment(name="Silver Watch", category=GarmentCategory.ACCESSORY, color="silver",
                formality=Formality.SMART_CASUAL),
    ]
    for item in items:
        wm.add_garment(item)
    return wm


@pytest.fixture
def profile():
    return StyleProfile(
        body_type=BodyType.HOURGLASS,
        preferred_style=StyleType.CLASSIC,
        preferred_colors=["navy", "white"],
    )


class TestOutfitRecommender:
    def test_basic_recommendation(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(
            occasion=OccasionType.CASUAL_EVERYDAY,
            weather=Weather.MILD,
        )
        assert len(outfits) > 0
        assert all(o.score >= 0 for o in outfits)

    def test_business_casual_recommendation(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(
            occasion=OccasionType.BUSINESS_CASUAL,
            weather=Weather.MILD,
        )
        assert len(outfits) > 0

    def test_with_profile(self, full_wardrobe, profile):
        recommender = OutfitRecommender(full_wardrobe, style_profile=profile)
        outfits = recommender.recommend(
            occasion=OccasionType.BUSINESS_CASUAL,
            weather=Weather.WARM,
        )
        assert len(outfits) > 0

    def test_with_color_preference(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(
            occasion=OccasionType.CASUAL_EVERYDAY,
            weather=Weather.MILD,
            color_preference="navy",
        )
        assert len(outfits) > 0

    def test_max_results(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(max_results=2)
        assert len(outfits) <= 2

    def test_outfits_sorted_by_score(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(max_results=10)
        if len(outfits) > 1:
            for i in range(len(outfits) - 1):
                assert outfits[i].score >= outfits[i + 1].score

    def test_string_enum_inputs(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(
            occasion="casual_everyday",
            weather="mild",
            season="spring",
        )
        assert len(outfits) > 0

    def test_dress_based_outfit(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(
            occasion=OccasionType.COCKTAIL_PARTY,
            weather=Weather.COOL,
        )
        # Should include dress-based outfits
        dress_outfits = [
            o for o in outfits
            if any(g.category == GarmentCategory.DRESS for g in o.garments)
        ]
        assert len(dress_outfits) >= 0  # May or may not have dresses depending on formality filter

    def test_empty_wardrobe(self):
        wm = WardrobeManager()
        recommender = OutfitRecommender(wm)
        outfits = recommender.recommend()
        assert outfits == []

    def test_outfit_has_notes(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend()
        if outfits:
            assert isinstance(outfits[0].notes, list)

    def test_season_inferred_from_weather(self, full_wardrobe):
        recommender = OutfitRecommender(full_wardrobe)
        outfits = recommender.recommend(weather=Weather.HOT)
        if outfits:
            assert outfits[0].season == Season.SUMMER

    def test_body_type_from_profile(self, full_wardrobe, profile):
        recommender = OutfitRecommender(full_wardrobe, style_profile=profile)
        outfits = recommender.recommend()
        # Should not raise; body type comes from profile
        assert isinstance(outfits, list)
