"""Tests for the color theory engine."""

import pytest

from stylemirror.models import ColorHarmonyType, Season
from stylemirror.stylist.color_theory import (
    COLOR_WHEEL,
    ColorHarmonyEngine,
    FASHION_COLOR_MAP,
    NEUTRAL_COLORS,
)


@pytest.fixture
def engine():
    return ColorHarmonyEngine()


class TestColorWheel:
    def test_wheel_has_12_positions(self):
        assert len(COLOR_WHEEL) == 12

    def test_fashion_colors_mapped(self):
        assert "navy" in FASHION_COLOR_MAP
        assert "burgundy" in FASHION_COLOR_MAP
        assert "emerald" in FASHION_COLOR_MAP

    def test_neutrals_defined(self):
        assert "black" in NEUTRAL_COLORS
        assert "white" in NEUTRAL_COLORS
        assert "beige" in NEUTRAL_COLORS


class TestNeutralDetection:
    def test_black_is_neutral(self, engine):
        assert engine.is_neutral("black")

    def test_white_is_neutral(self, engine):
        assert engine.is_neutral("white")

    def test_navy_is_not_neutral(self, engine):
        assert not engine.is_neutral("navy")

    def test_case_insensitive(self, engine):
        assert engine.is_neutral("Black")
        assert engine.is_neutral("WHITE")


class TestComplementary:
    def test_red_complement_is_green(self, engine):
        result = engine.complementary("red")
        assert result == ["green"]

    def test_blue_complement_is_orange(self, engine):
        result = engine.complementary("blue")
        assert result == ["orange"]

    def test_navy_complement(self, engine):
        # navy maps to position 8 (blue), complement is position 2 (orange)
        result = engine.complementary("navy")
        assert result == ["orange"]

    def test_neutral_returns_empty(self, engine):
        result = engine.complementary("black")
        assert result == []


class TestAnalogous:
    def test_blue_analogous(self, engine):
        result = engine.analogous("blue")
        assert "blue-green" in result
        assert "blue-violet" in result
        assert len(result) == 2

    def test_red_analogous(self, engine):
        result = engine.analogous("red")
        assert "red-violet" in result
        assert "red-orange" in result


class TestTriadic:
    def test_red_triadic(self, engine):
        # red=0, triadic at 4 (yellow) and 8 (blue)
        result = engine.triadic("red")
        assert "yellow" in result
        assert "blue" in result

    def test_blue_triadic(self, engine):
        result = engine.triadic("blue")
        assert "red" in result or "yellow" in result


class TestSplitComplementary:
    def test_blue_split_complementary(self, engine):
        # blue=8, complement=2 (orange), split = 1 (red-orange) and 3 (yellow-orange)
        result = engine.split_complementary("blue")
        assert "red-orange" in result
        assert "yellow-orange" in result


class TestFindHarmonies:
    def test_returns_all_types_for_chromatic(self, engine):
        harmonies = engine.find_harmonies("navy")
        assert ColorHarmonyType.COMPLEMENTARY in harmonies
        assert ColorHarmonyType.ANALOGOUS in harmonies
        assert ColorHarmonyType.TRIADIC in harmonies
        assert ColorHarmonyType.SPLIT_COMPLEMENTARY in harmonies
        assert ColorHarmonyType.MONOCHROMATIC in harmonies

    def test_returns_neutral_for_neutral_color(self, engine):
        harmonies = engine.find_harmonies("black")
        assert ColorHarmonyType.NEUTRAL in harmonies
        assert len(harmonies) == 1


class TestEvaluateCombination:
    def test_all_neutrals_scores_high(self, engine):
        score, harmony, _ = engine.evaluate_combination(["black", "white", "gray"])
        assert score >= 7.0
        assert harmony == ColorHarmonyType.NEUTRAL

    def test_single_chromatic_with_neutral(self, engine):
        score, harmony, _ = engine.evaluate_combination(["navy", "white"])
        assert score >= 8.0

    def test_complementary_pair(self, engine):
        score, harmony, _ = engine.evaluate_combination(["red", "green"])
        assert score >= 8.0
        assert harmony == ColorHarmonyType.COMPLEMENTARY

    def test_empty_colors(self, engine):
        score, _, _ = engine.evaluate_combination([])
        assert score == 0.0

    def test_analogous_pair(self, engine):
        score, harmony, _ = engine.evaluate_combination(["blue", "blue-green"])
        assert harmony == ColorHarmonyType.ANALOGOUS


class TestBuildPalette:
    def test_build_complementary_palette(self, engine):
        palette = engine.build_palette("navy", ColorHarmonyType.COMPLEMENTARY)
        assert palette.primary == "navy"
        assert palette.secondary is not None
        assert palette.harmony_type == ColorHarmonyType.COMPLEMENTARY

    def test_build_palette_with_season(self, engine):
        palette = engine.build_palette("navy", season=Season.SUMMER)
        assert Season.SUMMER in palette.season_affinity


class TestSeasonalRecommendations:
    def test_spring_colors(self, engine):
        colors = engine.seasonal_recommendations(Season.SPRING)
        assert len(colors) > 0
        assert "coral" in colors or "mint" in colors

    def test_winter_colors(self, engine):
        colors = engine.seasonal_recommendations(Season.WINTER)
        assert "black" in colors or "red" in colors


class TestClassicCombinations:
    def test_has_classic_combos(self, engine):
        combos = engine.get_classic_combinations()
        assert len(combos) >= 5
        # Each is (color1, color2, description)
        assert all(len(c) == 3 for c in combos)
