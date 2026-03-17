"""Tests for fashion modules: occasions, trends, and styles."""

import pytest

from stylemirror.models import Formality, OccasionType, Season, StyleType
from stylemirror.fashion.occasions import OccasionDresscode
from stylemirror.fashion.trends import TrendTracker
from stylemirror.fashion.styles import StyleProfileGuide


class TestOccasionDresscode:
    @pytest.fixture
    def guide(self):
        return OccasionDresscode()

    def test_all_occasions_have_guidelines(self, guide):
        for occasion in OccasionType:
            dresscode = guide.get_dresscode(occasion)
            assert dresscode is not None, f"No guidelines for {occasion.value}"

    def test_get_essentials(self, guide):
        essentials = guide.get_essentials(OccasionType.JOB_INTERVIEW)
        assert len(essentials) > 0
        assert any("suit" in e.lower() or "blazer" in e.lower() for e in essentials)

    def test_get_tip(self, guide):
        tip = guide.get_tip(OccasionType.DATE_NIGHT)
        assert len(tip) > 0

    def test_get_formality(self, guide):
        formality = guide.get_formality(OccasionType.FORMAL_GALA)
        assert formality == Formality.FORMAL

    def test_wedding_avoid_white(self, guide):
        avoid = guide.get_avoid_list(OccasionType.WEDDING_GUEST)
        assert any("white" in a.lower() for a in avoid)

    def test_list_occasions(self, guide):
        occasions = guide.list_occasions()
        assert len(occasions) >= 10

    def test_summarize(self, guide):
        summary = guide.summarize(OccasionType.BUSINESS_CASUAL)
        assert "Occasion:" in summary
        assert "Formality:" in summary
        assert "Essentials:" in summary

    def test_recommended_colors(self, guide):
        colors = guide.recommended_colors(OccasionType.BUSINESS_FORMAL)
        assert len(colors) > 0


class TestTrendTracker:
    @pytest.fixture
    def tracker(self):
        return TrendTracker()

    def test_all_seasons_have_trends(self, tracker):
        for season in Season:
            trends = tracker.get_trends(season)
            assert len(trends) >= 3

    def test_trend_structure(self, tracker):
        trends = tracker.get_trends(Season.SPRING)
        for trend in trends:
            assert "name" in trend
            assert "description" in trend
            assert "how_to_wear" in trend

    def test_get_trend_names(self, tracker):
        names = tracker.get_trend_names(Season.AUTUMN)
        assert len(names) >= 3
        assert all(isinstance(n, str) for n in names)

    def test_style_advice(self, tracker):
        for style in StyleType:
            advice = tracker.get_style_advice(style)
            assert len(advice) > 0

    def test_search_trends(self, tracker):
        results = tracker.search_trends("linen")
        assert len(results) >= 1
        assert any("linen" in r.get("name", "").lower() or "linen" in r.get("description", "").lower()
                    for r in results)

    def test_summarize_season(self, tracker):
        summary = tracker.summarize_season(Season.WINTER)
        assert "Winter" in summary
        assert len(summary) > 100


class TestStyleProfileGuide:
    @pytest.fixture
    def guide(self):
        return StyleProfileGuide()

    def test_all_styles_have_profiles(self, guide):
        for style in StyleType:
            profile = guide.get_profile(style)
            assert profile is not None

    def test_profile_structure(self, guide):
        for style in StyleType:
            p = guide.get_profile(style)
            assert "motto" in p
            assert "description" in p
            assert "key_colors" in p
            assert "signature_pieces" in p
            assert "fabrics" in p
            assert "rules" in p

    def test_get_motto(self, guide):
        motto = guide.get_motto(StyleType.MINIMALIST)
        assert "less" in motto.lower()

    def test_get_signature_pieces(self, guide):
        pieces = guide.get_signature_pieces(StyleType.CLASSIC)
        assert len(pieces) >= 5
        assert any("blazer" in p.lower() for p in pieces)

    def test_get_key_colors(self, guide):
        colors = guide.get_key_colors(StyleType.BOHEMIAN)
        assert len(colors) >= 3

    def test_get_rules(self, guide):
        rules = guide.get_rules(StyleType.STREETWEAR)
        assert len(rules) >= 3

    def test_list_styles(self, guide):
        styles = guide.list_styles()
        assert len(styles) >= 5

    def test_summarize(self, guide):
        summary = guide.summarize(StyleType.PREPPY)
        assert "Preppy" in summary
        assert "Signature Pieces:" in summary
        assert "Style Rules:" in summary
