"""Tests for body type analysis."""

import pytest

from stylemirror.models import BodyType, GarmentCategory
from stylemirror.stylist.body_type import BodyTypeAnalyzer, BODY_TYPE_GUIDELINES


@pytest.fixture
def analyzer():
    return BodyTypeAnalyzer()


class TestBodyTypeGuidelines:
    def test_all_body_types_have_guidelines(self):
        for bt in BodyType:
            assert bt in BODY_TYPE_GUIDELINES

    def test_guidelines_have_required_fields(self):
        for bt, g in BODY_TYPE_GUIDELINES.items():
            assert g.description
            assert g.goal
            assert len(g.best_tops) > 0
            assert len(g.best_bottoms) > 0
            assert len(g.best_dresses) > 0
            assert len(g.best_outerwear) > 0
            assert len(g.tips) > 0
            assert len(g.avoid) > 0


class TestBodyTypeAnalyzer:
    def test_get_guidelines(self, analyzer):
        g = analyzer.get_guidelines(BodyType.HOURGLASS)
        assert "waist" in g.goal.lower()

    def test_recommend_tops(self, analyzer):
        recs = analyzer.recommend_categories(BodyType.PEAR, GarmentCategory.TOP)
        assert len(recs) > 0

    def test_recommend_bottoms(self, analyzer):
        recs = analyzer.recommend_categories(BodyType.APPLE, GarmentCategory.BOTTOM)
        assert len(recs) > 0

    def test_recommend_unknown_category(self, analyzer):
        recs = analyzer.recommend_categories(BodyType.HOURGLASS, GarmentCategory.ACCESSORY)
        assert recs == []

    def test_get_tips(self, analyzer):
        tips = analyzer.get_tips(BodyType.RECTANGLE)
        assert len(tips) > 0
        assert all(isinstance(t, str) for t in tips)

    def test_get_avoid_list(self, analyzer):
        avoid = analyzer.get_avoid_list(BodyType.INVERTED_TRIANGLE)
        assert len(avoid) > 0

    def test_score_garment_good_match(self, analyzer):
        score, note = analyzer.score_garment_fit(BodyType.HOURGLASS, "Wrap dress")
        assert score >= 7.0

    def test_score_garment_bad_match(self, analyzer):
        score, note = analyzer.score_garment_fit(BodyType.PEAR, "Pleated skirt")
        assert score <= 5.0

    def test_score_garment_neutral(self, analyzer):
        score, note = analyzer.score_garment_fit(BodyType.HOURGLASS, "Generic item")
        assert 4.0 <= score <= 8.0

    def test_summarize(self, analyzer):
        summary = analyzer.summarize(BodyType.PETITE)
        assert "Petite" in summary
        assert "Tips:" in summary
        assert "Avoid:" in summary

    def test_all_body_types_summarize(self, analyzer):
        for bt in BodyType:
            summary = analyzer.summarize(bt)
            assert len(summary) > 50
