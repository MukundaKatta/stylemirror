"""Occasion-based dress code guidelines.

Provides detailed guidance for dressing appropriately across a wide range
of occasions, from casual everyday wear to white-tie galas.
"""

from stylemirror.models import Formality, OccasionType


# Comprehensive dress code information for each occasion type.
OCCASION_GUIDELINES: dict[OccasionType, dict] = {
    OccasionType.CASUAL_EVERYDAY: {
        "formality": Formality.CASUAL,
        "description": "Day-to-day wear for errands, casual outings, and relaxed settings.",
        "tip": "Prioritize comfort without sacrificing style. Well-fitted basics are key.",
        "essentials": [
            "Well-fitted jeans or chinos",
            "Quality t-shirts or casual button-downs",
            "Clean sneakers or loafers",
            "A versatile jacket (denim, bomber, or lightweight)",
        ],
        "colors": ["Neutral base with one accent color"],
        "avoid": [
            "Overly worn or damaged clothing",
            "Pajama-like pieces outside the home",
        ],
    },
    OccasionType.CASUAL_WEEKEND: {
        "formality": Formality.VERY_CASUAL,
        "description": "Relaxed weekend wear for leisure activities.",
        "tip": "Lean into comfort and personal expression. This is where your style shines.",
        "essentials": [
            "Comfortable jeans, shorts, or casual pants",
            "Graphic tees, henleys, or casual knits",
            "Sneakers, sandals, or casual boots",
        ],
        "colors": ["Anything goes; express your personality"],
        "avoid": ["Formal pieces that feel out of place"],
    },
    OccasionType.BUSINESS_CASUAL: {
        "formality": Formality.BUSINESS_CASUAL,
        "description": "Professional but relaxed office environment.",
        "tip": "Think polished but approachable. Blazers elevate any business casual look.",
        "essentials": [
            "Chinos or tailored trousers",
            "Collared shirts, blouses, or fine-knit sweaters",
            "Blazers or structured cardigans",
            "Loafers, oxfords, or polished flats",
        ],
        "colors": ["Navy, gray, white, earth tones with subtle accents"],
        "avoid": [
            "Jeans (unless dress code explicitly allows)",
            "Sneakers or flip-flops",
            "Visible logos or graphic tees",
        ],
    },
    OccasionType.BUSINESS_FORMAL: {
        "formality": Formality.BUSINESS_FORMAL,
        "description": "Traditional corporate or professional settings.",
        "tip": "Classic and conservative wins. Invest in tailoring.",
        "essentials": [
            "Tailored suit in navy, charcoal, or black",
            "Crisp dress shirt or structured blouse",
            "Leather dress shoes or heels",
            "Minimal, elegant accessories",
            "Tie or silk scarf for added polish",
        ],
        "colors": ["Navy, charcoal, black, white, subtle pinstripes"],
        "avoid": [
            "Bright or flashy colors",
            "Casual fabrics like denim or jersey",
            "Excessive jewelry",
        ],
    },
    OccasionType.DATE_NIGHT: {
        "formality": Formality.SMART_CASUAL,
        "description": "Romantic evening out; dinner, drinks, or entertainment.",
        "tip": "Look put-together but not overdressed. Wear something that makes you feel confident.",
        "essentials": [
            "Dark jeans or tailored trousers",
            "A flattering top or well-fitted shirt",
            "Stylish shoes (no worn-out sneakers)",
            "One statement accessory",
        ],
        "colors": ["Dark, rich tones; black, burgundy, deep blue, emerald"],
        "avoid": [
            "Overly casual athletic wear",
            "Anything you are not comfortable in",
        ],
    },
    OccasionType.COCKTAIL_PARTY: {
        "formality": Formality.SEMI_FORMAL,
        "description": "Evening social event; cocktail attire specified.",
        "tip": "A cocktail dress or a sharp suit. This is the time to make a statement.",
        "essentials": [
            "Cocktail dress (knee to midi length) or tailored suit",
            "Dressy heels or polished dress shoes",
            "Evening clutch or small bag",
            "Statement jewelry or a pocket square",
        ],
        "colors": ["Jewel tones, metallics, classic black, deep colors"],
        "avoid": [
            "Floor-length gowns (too formal)",
            "Casual day dresses",
            "Jeans in any form",
        ],
    },
    OccasionType.FORMAL_GALA: {
        "formality": Formality.FORMAL,
        "description": "Black-tie or formal evening event; gala, ball, or awards.",
        "tip": "Go all out. Floor-length gowns or a tuxedo. Elegance is the only rule.",
        "essentials": [
            "Floor-length gown or tuxedo",
            "Formal dress shoes or elegant heels",
            "Fine jewelry or cufflinks",
            "Evening bag or clutch",
        ],
        "colors": ["Black, navy, metallics, jewel tones, classic white"],
        "avoid": [
            "Short dresses (unless the invite specifies)",
            "Business suits",
            "Casual accessories",
        ],
    },
    OccasionType.WEDDING_GUEST: {
        "formality": Formality.SEMI_FORMAL,
        "description": "Attending a wedding as a guest.",
        "tip": "Dress to celebrate, not to upstage. Check the invitation for dress code hints.",
        "essentials": [
            "Midi or maxi dress, or a suit",
            "Dressy but comfortable shoes (you will be standing)",
            "Coordinated accessories",
        ],
        "colors": ["Pastels, florals, jewel tones, earth tones"],
        "avoid": [
            "White, ivory, or cream (reserved for the bride)",
            "All black (can read as funereal in some cultures)",
            "Anything too revealing or casual",
            "Overly flashy outfits that steal attention",
        ],
    },
    OccasionType.JOB_INTERVIEW: {
        "formality": Formality.BUSINESS_FORMAL,
        "description": "Professional job interview.",
        "tip": "Dress one level above the company's daily dress code. When in doubt, go more formal.",
        "essentials": [
            "Tailored suit or blazer with trousers/skirt",
            "Crisp, pressed shirt or blouse",
            "Polished, closed-toe shoes",
            "Minimal accessories",
            "A professional bag or portfolio",
        ],
        "colors": ["Navy, charcoal, black, white, subtle blue"],
        "avoid": [
            "Flashy patterns or colors",
            "Strong perfume or cologne",
            "Casual wear even if the company is casual",
            "Excessive jewelry or accessories",
        ],
    },
    OccasionType.OUTDOOR_EVENT: {
        "formality": Formality.CASUAL,
        "description": "Outdoor gatherings: picnics, festivals, garden parties.",
        "tip": "Layer for weather changes and prioritize comfort and mobility.",
        "essentials": [
            "Breathable fabrics (cotton, linen)",
            "Comfortable walking shoes",
            "Sun protection (hat, sunglasses)",
            "Layering pieces for temperature changes",
        ],
        "colors": ["Bright, seasonal colors; earth tones"],
        "avoid": [
            "Heels that will sink into grass",
            "Heavy or restrictive clothing",
            "Pieces you are afraid to get dirty",
        ],
    },
    OccasionType.BEACH: {
        "formality": Formality.VERY_CASUAL,
        "description": "Beach day or resort setting.",
        "tip": "Effortless and relaxed. A great cover-up transitions from sand to lunch.",
        "essentials": [
            "Swimwear with a stylish cover-up",
            "Sandals or espadrilles",
            "Sun hat and sunglasses",
            "Light, flowy layers",
        ],
        "colors": ["Bright, tropical, nautical, white"],
        "avoid": [
            "Heavy fabrics",
            "Dark, heat-absorbing colors in hot sun",
        ],
    },
    OccasionType.WORKOUT: {
        "formality": Formality.VERY_CASUAL,
        "description": "Exercise, gym, or active sports.",
        "tip": "Function first, but coordinated activewear boosts motivation.",
        "essentials": [
            "Moisture-wicking top and bottoms",
            "Supportive athletic shoes",
            "Sports bra or compression wear",
        ],
        "colors": ["Personal preference; matching sets look polished"],
        "avoid": [
            "Cotton that holds sweat",
            "Loose, flapping clothing around machines",
        ],
    },
    OccasionType.BRUNCH: {
        "formality": Formality.SMART_CASUAL,
        "description": "Late morning social meal; relaxed but put-together.",
        "tip": "Chic and comfortable. Think elevated casual; a sundress or nice jeans with a blouse.",
        "essentials": [
            "Sundress, nice blouse with jeans, or smart-casual separates",
            "Comfortable but stylish shoes",
            "Light accessories",
            "Sunglasses",
        ],
        "colors": ["Pastels, florals, light neutrals, soft brights"],
        "avoid": [
            "Overly formal or stiff looks",
            "Last night's outfit",
        ],
    },
}


class OccasionDresscode:
    """Provides dress code guidance for various occasions.

    Includes formality level, essential items, recommended colors,
    and what to avoid for each occasion type.
    """

    def __init__(self) -> None:
        self._guidelines = OCCASION_GUIDELINES

    def get_dresscode(self, occasion: OccasionType) -> dict | None:
        """Return the full dress code guide for an occasion."""
        return self._guidelines.get(occasion)

    def get_essentials(self, occasion: OccasionType) -> list[str]:
        """Return essential clothing items for an occasion."""
        guide = self._guidelines.get(occasion, {})
        return guide.get("essentials", [])

    def get_tip(self, occasion: OccasionType) -> str:
        """Return the key styling tip for an occasion."""
        guide = self._guidelines.get(occasion, {})
        return guide.get("tip", "")

    def get_avoid_list(self, occasion: OccasionType) -> list[str]:
        """Return what to avoid for an occasion."""
        guide = self._guidelines.get(occasion, {})
        return guide.get("avoid", [])

    def get_formality(self, occasion: OccasionType) -> Formality | None:
        """Return the expected formality level for an occasion."""
        guide = self._guidelines.get(occasion, {})
        return guide.get("formality")

    def recommended_colors(self, occasion: OccasionType) -> list[str]:
        """Return recommended color guidance for an occasion."""
        guide = self._guidelines.get(occasion, {})
        return guide.get("colors", [])

    def list_occasions(self) -> list[OccasionType]:
        """Return all supported occasion types."""
        return list(self._guidelines.keys())

    def summarize(self, occasion: OccasionType) -> str:
        """Return a formatted text summary of the dress code for an occasion."""
        guide = self._guidelines.get(occasion)
        if not guide:
            return f"No guidelines available for {occasion.value}."

        lines = [
            f"Occasion: {occasion.value.replace('_', ' ').title()}",
            f"Formality: {guide['formality'].value.replace('_', ' ').title()}",
            f"Description: {guide['description']}",
            f"Key Tip: {guide['tip']}",
            "",
            "Essentials:",
        ]
        for item in guide.get("essentials", []):
            lines.append(f"  - {item}")
        lines.append("")
        lines.append("Avoid:")
        for item in guide.get("avoid", []):
            lines.append(f"  - {item}")
        return "\n".join(lines)
