"""Seasonal fashion trend tracking.

Provides awareness of current and recurring fashion trends organized
by season, with practical styling advice.
"""

from stylemirror.models import Season, StyleType


# Recurring and contemporary fashion trends organized by season.
SEASONAL_TRENDS: dict[Season, list[dict[str, str]]] = {
    Season.SPRING: [
        {
            "name": "Pastel Power",
            "description": "Soft lavender, mint, butter yellow, and blush dominate spring palettes.",
            "how_to_wear": "Pair pastel tops with neutral bottoms, or go tonal with a head-to-toe pastel look.",
        },
        {
            "name": "Floral Revival",
            "description": "Floral prints return each spring in fresh interpretations.",
            "how_to_wear": "Ground bold florals with solid-colored accessories. Midi dresses in floral print are a spring staple.",
        },
        {
            "name": "Light Layering",
            "description": "Transitional layering with lightweight jackets, cardigans, and scarves.",
            "how_to_wear": "Layer a linen blazer over a simple tee, or drape a light knit over a dress.",
        },
        {
            "name": "Sheer and Lightweight Fabrics",
            "description": "Organza, chiffon, and cotton voile for an airy feel.",
            "how_to_wear": "Use sheer pieces as overlays or layer with opaque basics underneath.",
        },
        {
            "name": "Relaxed Tailoring",
            "description": "Softly structured blazers, wide-leg trousers, and relaxed suiting.",
            "how_to_wear": "Pair an unstructured blazer with straight-leg pants and loafers for polished ease.",
        },
    ],
    Season.SUMMER: [
        {
            "name": "Linen Everything",
            "description": "Linen dominates summer for its breathability and relaxed aesthetic.",
            "how_to_wear": "Embrace the wrinkle. Linen sets (matching top and bottom) are effortlessly chic.",
        },
        {
            "name": "Bold Brights",
            "description": "Saturated colors like fuchsia, cobalt, and tangerine make summer pop.",
            "how_to_wear": "One bold piece per outfit; pair with neutrals to let the color shine.",
        },
        {
            "name": "Crochet and Knit",
            "description": "Handmade textures in tops, bags, and cover-ups.",
            "how_to_wear": "A crochet cover-up over swimwear, or a knit vest over a cotton dress.",
        },
        {
            "name": "Maxi Lengths",
            "description": "Floor-length skirts and dresses for an elegant summer silhouette.",
            "how_to_wear": "Pair a flowy maxi skirt with a fitted tank and flat sandals.",
        },
        {
            "name": "Tropical and Vacation Prints",
            "description": "Palm leaves, abstract tropicals, and resort-inspired motifs.",
            "how_to_wear": "Keep it to one printed piece and balance with solids.",
        },
    ],
    Season.AUTUMN: [
        {
            "name": "Rich Earth Tones",
            "description": "Burgundy, rust, olive, mustard, and chocolate define the autumn palette.",
            "how_to_wear": "Build outfits around a warm neutral base and accent with one rich tone.",
        },
        {
            "name": "Layering Mastery",
            "description": "The art of combining textures and lengths for warmth and style.",
            "how_to_wear": "Turtleneck under a blazer, topped with a scarf. Mix textures like knit, wool, and leather.",
        },
        {
            "name": "Leather and Suede",
            "description": "Leather jackets, suede boots, and leather accessories anchor fall wardrobes.",
            "how_to_wear": "A leather jacket is the ultimate fall investment piece. Suede boots complete any look.",
        },
        {
            "name": "Plaid and Checks",
            "description": "Timeless patterns in blazers, scarves, and trousers.",
            "how_to_wear": "One plaid piece per outfit. A plaid blazer with solid trousers is a classic pairing.",
        },
        {
            "name": "Oversized Knitwear",
            "description": "Chunky sweaters, long cardigans, and cozy knit accessories.",
            "how_to_wear": "Balance oversized tops with slimmer bottoms. Tuck the front of a chunky sweater for shape.",
        },
    ],
    Season.WINTER: [
        {
            "name": "Monochromatic Dressing",
            "description": "Head-to-toe single-color outfits in rich or neutral tones.",
            "how_to_wear": "Vary textures within the same color family for depth. All-black with mixed textures is eternally chic.",
        },
        {
            "name": "Statement Coats",
            "description": "The coat IS the outfit. Bold colors, patterns, or silhouettes.",
            "how_to_wear": "Invest in one statement coat; keep everything underneath simple.",
        },
        {
            "name": "Velvet and Luxe Textures",
            "description": "Velvet blazers, satin blouses, and cashmere knits for holiday elegance.",
            "how_to_wear": "One luxe texture per outfit. A velvet blazer elevates jeans instantly.",
        },
        {
            "name": "Dark Florals",
            "description": "Moody, dark-ground floral prints for winter romance.",
            "how_to_wear": "A dark floral dress with tights and boots transitions from day to evening.",
        },
        {
            "name": "Tailored Layers",
            "description": "Structured layering with blazers, vests, and coats over knitwear.",
            "how_to_wear": "Blazer over a fine-knit turtleneck, under a tailored coat. Each layer should be visible.",
        },
    ],
}

# Style-specific trend adaptations.
STYLE_TREND_NOTES: dict[StyleType, str] = {
    StyleType.MINIMALIST: (
        "Focus on clean lines and quality fabrics. Adopt trends through subtle details "
        "like a slightly oversized silhouette or a muted version of a trendy color."
    ),
    StyleType.CLASSIC: (
        "Incorporate trends selectively through accessories or one statement piece. "
        "Your foundation of timeless pieces is your strength."
    ),
    StyleType.BOHEMIAN: (
        "Embrace flowing fabrics, layered jewelry, and earthy tones. Crochet, "
        "fringe, and artisanal details align naturally with boho style."
    ),
    StyleType.STREETWEAR: (
        "Mix high and low. Graphic pieces, oversized silhouettes, and sneaker culture "
        "are your playground. Stay current with drops and collaborations."
    ),
    StyleType.PREPPY: (
        "Layer with intent: collared shirts under sweaters, blazers over everything. "
        "Adopt trends through color and pattern while keeping the structured foundation."
    ),
    StyleType.ROMANTIC: (
        "Lace, ruffles, soft fabrics, and floral prints are your constants. "
        "Trends in sheer fabrics and feminine details fit naturally."
    ),
    StyleType.EDGY: (
        "Leather, hardware, dark palettes, and unexpected combinations. "
        "Adopt trends through deconstruction and contrast."
    ),
    StyleType.ATHLEISURE: (
        "Technical fabrics meet style. Matching sets, sleek sneakers, and "
        "performance-inspired pieces that work beyond the gym."
    ),
}


class TrendTracker:
    """Track and recommend seasonal fashion trends.

    Provides current trend information organized by season, with practical
    styling advice and style-specific interpretations.
    """

    def __init__(self) -> None:
        self._trends = SEASONAL_TRENDS
        self._style_notes = STYLE_TREND_NOTES

    def get_trends(self, season: Season) -> list[dict[str, str]]:
        """Return all trends for a given season."""
        return self._trends.get(season, [])

    def get_trend_names(self, season: Season) -> list[str]:
        """Return just the trend names for a season."""
        return [t["name"] for t in self._trends.get(season, [])]

    def get_style_advice(self, style: StyleType) -> str:
        """Return trend adaptation advice for a style archetype."""
        return self._style_notes.get(style, "Express your unique style with confidence.")

    def search_trends(self, keyword: str) -> list[dict[str, str | Season]]:
        """Search trends across all seasons by keyword."""
        results: list[dict[str, str | Season]] = []
        keyword_lower = keyword.lower()
        for season, trends in self._trends.items():
            for trend in trends:
                searchable = f"{trend['name']} {trend['description']}".lower()
                if keyword_lower in searchable:
                    results.append({**trend, "season": season})
        return results

    def summarize_season(self, season: Season) -> str:
        """Return a formatted summary of trends for a season."""
        trends = self._trends.get(season, [])
        if not trends:
            return f"No trend data for {season.value}."

        lines = [f"Fashion Trends for {season.value.title()}:", ""]
        for i, trend in enumerate(trends, 1):
            lines.append(f"{i}. {trend['name']}")
            lines.append(f"   {trend['description']}")
            lines.append(f"   How to wear: {trend['how_to_wear']}")
            lines.append("")
        return "\n".join(lines)
