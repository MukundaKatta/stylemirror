"""Tests for wardrobe management."""

import json
from pathlib import Path

import pytest

from stylemirror.models import Formality, Garment, GarmentCategory, Season
from stylemirror.stylist.wardrobe import WardrobeManager


@pytest.fixture
def wardrobe():
    return WardrobeManager()


@pytest.fixture
def populated_wardrobe():
    wm = WardrobeManager()
    wm.add_garment(Garment(
        name="White T-Shirt", category=GarmentCategory.TOP, color="white",
        formality=Formality.CASUAL,
    ))
    wm.add_garment(Garment(
        name="Navy Blazer", category=GarmentCategory.OUTERWEAR, color="navy",
        formality=Formality.SMART_CASUAL,
    ))
    wm.add_garment(Garment(
        name="Dark Jeans", category=GarmentCategory.BOTTOM, color="indigo",
        formality=Formality.CASUAL,
    ))
    wm.add_garment(Garment(
        name="Black Dress Shoes", category=GarmentCategory.FOOTWEAR, color="black",
        formality=Formality.BUSINESS_FORMAL,
    ))
    wm.add_garment(Garment(
        name="Red Scarf", category=GarmentCategory.ACCESSORY, color="red",
        formality=Formality.CASUAL, favorite=True,
    ))
    return wm


class TestBasicOperations:
    def test_empty_wardrobe(self, wardrobe):
        assert wardrobe.count() == 0
        assert wardrobe.get_all() == []

    def test_add_garment(self, wardrobe):
        g = Garment(name="Shirt", category=GarmentCategory.TOP, color="blue")
        wardrobe.add_garment(g)
        assert wardrobe.count() == 1

    def test_remove_garment(self, populated_wardrobe):
        assert populated_wardrobe.remove_garment("White T-Shirt")
        assert populated_wardrobe.count() == 4

    def test_remove_nonexistent(self, wardrobe):
        assert not wardrobe.remove_garment("Ghost Shirt")

    def test_remove_case_insensitive(self, populated_wardrobe):
        assert populated_wardrobe.remove_garment("white t-shirt")
        assert populated_wardrobe.count() == 4


class TestFiltering:
    def test_by_category(self, populated_wardrobe):
        tops = populated_wardrobe.by_category(GarmentCategory.TOP)
        assert len(tops) == 1
        assert tops[0].name == "White T-Shirt"

    def test_by_color(self, populated_wardrobe):
        navy_items = populated_wardrobe.by_color("navy")
        assert len(navy_items) == 1

    def test_by_formality(self, populated_wardrobe):
        casual = populated_wardrobe.by_formality(Formality.CASUAL)
        assert len(casual) == 3

    def test_by_season(self, populated_wardrobe):
        # Default seasons include all seasons
        spring = populated_wardrobe.by_season(Season.SPRING)
        assert len(spring) == 5

    def test_favorites(self, populated_wardrobe):
        favs = populated_wardrobe.favorites()
        assert len(favs) == 1
        assert favs[0].name == "Red Scarf"

    def test_search(self, populated_wardrobe):
        results = populated_wardrobe.search("blazer")
        assert len(results) == 1
        assert results[0].name == "Navy Blazer"

    def test_search_by_color(self, populated_wardrobe):
        results = populated_wardrobe.search("navy")
        assert len(results) >= 1


class TestAnalytics:
    def test_color_distribution(self, populated_wardrobe):
        dist = populated_wardrobe.color_distribution()
        assert "white" in dist
        assert "navy" in dist

    def test_category_distribution(self, populated_wardrobe):
        dist = populated_wardrobe.category_distribution()
        assert "top" in dist
        assert "outerwear" in dist

    def test_formality_distribution(self, populated_wardrobe):
        dist = populated_wardrobe.formality_distribution()
        assert "casual" in dist
        assert dist["casual"] == 3

    def test_wardrobe_gaps_empty(self, wardrobe):
        gaps = wardrobe.wardrobe_gaps()
        assert len(gaps) > 0

    def test_wardrobe_gaps_populated(self, populated_wardrobe):
        gaps = populated_wardrobe.wardrobe_gaps()
        # Should have no missing essential categories
        category_gaps = [g for g in gaps if "Missing category" in g]
        assert len(category_gaps) == 0


class TestPersistence:
    def test_save_and_load(self, populated_wardrobe, tmp_path):
        filepath = tmp_path / "test_wardrobe.json"
        populated_wardrobe._storage_path = filepath
        populated_wardrobe.save()

        assert filepath.exists()
        data = json.loads(filepath.read_text())
        assert len(data) == 5

        # Load into a new wardrobe
        new_wm = WardrobeManager(storage_path=filepath)
        new_wm.load()
        assert new_wm.count() == 5
        assert new_wm.get_all()[0].name == "White T-Shirt"

    def test_load_nonexistent(self, wardrobe, tmp_path):
        wardrobe._storage_path = tmp_path / "nonexistent.json"
        wardrobe.load()  # Should not raise
        assert wardrobe.count() == 0
