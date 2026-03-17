"""Body type analysis with real fashion dressing guidelines.

Guidelines are based on widely accepted fashion styling principles that
help create balanced silhouettes and highlight one's best features.
"""

from dataclasses import dataclass

from stylemirror.models import BodyType, GarmentCategory


@dataclass(frozen=True)
class BodyTypeGuidelines:
    """Styling guidelines for a specific body type."""

    description: str
    goal: str
    best_tops: list[str]
    best_bottoms: list[str]
    best_dresses: list[str]
    best_outerwear: list[str]
    patterns_and_prints: list[str]
    fabrics: list[str]
    avoid: list[str]
    tips: list[str]


# Comprehensive, real-world dressing guidelines per body type.
BODY_TYPE_GUIDELINES: dict[BodyType, BodyTypeGuidelines] = {
    BodyType.HOURGLASS: BodyTypeGuidelines(
        description="Balanced shoulders and hips with a defined waist.",
        goal="Highlight the natural waist and maintain proportional balance.",
        best_tops=[
            "Wrap tops", "V-necklines", "Fitted blouses",
            "Scoop necks", "Peplum tops",
        ],
        best_bottoms=[
            "High-waisted trousers", "Pencil skirts", "Straight-leg jeans",
            "A-line skirts", "Bootcut jeans",
        ],
        best_dresses=[
            "Wrap dresses", "Fit-and-flare", "Bodycon",
            "Belted shirt dresses", "A-line dresses",
        ],
        best_outerwear=[
            "Belted trench coats", "Fitted blazers", "Tailored jackets",
            "Wrap coats",
        ],
        patterns_and_prints=[
            "Vertical stripes at the center", "Balanced all-over prints",
            "Defined waistline patterns",
        ],
        fabrics=[
            "Structured knits", "Medium-weight fabrics",
            "Fabrics with some drape",
        ],
        avoid=[
            "Shapeless, boxy silhouettes", "Overly stiff fabrics",
            "Empire waists that hide the natural waist",
            "Very high necklines that shorten the torso",
        ],
        tips=[
            "Always define the waist with belts, tucks, or tailoring.",
            "Match volume on top with volume on the bottom.",
            "V-necks and wrap styles are your best friends.",
        ],
    ),
    BodyType.PEAR: BodyTypeGuidelines(
        description="Hips wider than shoulders; weight carried in lower body.",
        goal="Draw attention upward and balance the upper and lower body.",
        best_tops=[
            "Boat necks", "Off-the-shoulder tops", "Embellished necklines",
            "Structured shoulders", "Statement sleeves",
        ],
        best_bottoms=[
            "Dark-wash straight-leg jeans", "A-line skirts",
            "Wide-leg trousers", "Bootcut pants",
        ],
        best_dresses=[
            "A-line dresses", "Fit-and-flare", "Empire waist dresses",
            "Wrap dresses with a flared skirt",
        ],
        best_outerwear=[
            "Cropped jackets", "Structured blazers with shoulder detail",
            "Pea coats", "Double-breasted jackets",
        ],
        patterns_and_prints=[
            "Detailed prints on top, solid on bottom",
            "Horizontal stripes on top only",
            "Dark, solid colors for bottoms",
        ],
        fabrics=[
            "Structured fabrics for tops", "Fluid fabrics for bottoms",
            "Avoid clingy materials on the lower half",
        ],
        avoid=[
            "Skinny jeans without a long top", "Pleated skirts",
            "Light-colored, tight bottoms", "Ankle straps that shorten legs",
        ],
        tips=[
            "Create visual interest above the waist with color, pattern, and accessories.",
            "Dark-colored bottoms with a brighter or detailed top create balance.",
            "A-line and bootcut silhouettes skim the hips gracefully.",
        ],
    ),
    BodyType.APPLE: BodyTypeGuidelines(
        description="Weight carried around the midsection with slimmer legs and arms.",
        goal="Elongate the torso and draw attention to legs and decolletage.",
        best_tops=[
            "V-neck tops", "Wrap tops", "Empire waist tops",
            "Tunics", "Open cardigans over fitted tanks",
        ],
        best_bottoms=[
            "Straight-leg pants", "Bootcut jeans",
            "Mid-rise trousers with stretch", "Slim ankle pants",
        ],
        best_dresses=[
            "Empire waist dresses", "Wrap dresses", "Shift dresses",
            "A-line with a defined bust",
        ],
        best_outerwear=[
            "Long cardigans", "Open-front blazers", "Waterfall jackets",
            "Single-breasted coats",
        ],
        patterns_and_prints=[
            "Vertical lines and panels", "Monochromatic outfits",
            "Prints above the bust or below the hip",
        ],
        fabrics=[
            "Structured but not stiff", "Draping jersey",
            "Avoid clingy midsection fabrics",
        ],
        avoid=[
            "Belts at the natural waist", "Crop tops",
            "Boxy, shapeless tops that add bulk",
            "Turtlenecks without a long necklace",
        ],
        tips=[
            "V-necks elongate the torso beautifully.",
            "Show off your legs; they are often your best asset.",
            "Monochromatic dressing creates a long, lean line.",
        ],
    ),
    BodyType.RECTANGLE: BodyTypeGuidelines(
        description="Shoulders, waist, and hips roughly the same width; athletic build.",
        goal="Create the illusion of curves and waist definition.",
        best_tops=[
            "Peplum tops", "Wrap tops", "Ruffled blouses",
            "Off-the-shoulder styles", "Layered tops",
        ],
        best_bottoms=[
            "Flared jeans", "Pleated trousers", "Skirts with volume",
            "Paperbag-waist pants",
        ],
        best_dresses=[
            "Fit-and-flare", "Wrap dresses", "Belted shirt dresses",
            "Ruched bodycon", "Tiered dresses",
        ],
        best_outerwear=[
            "Belted jackets", "Cropped jackets", "Peplum blazers",
            "Trench coats with a cinched waist",
        ],
        patterns_and_prints=[
            "Color blocking to create dimension",
            "Patterns that create visual curves",
            "Diagonal lines",
        ],
        fabrics=[
            "Textured fabrics for dimension", "Soft, drapy materials",
            "Fabrics with some body",
        ],
        avoid=[
            "Straight, column-like silhouettes without waist detail",
            "Very boxy, oversized tops with straight-leg bottoms",
            "Minimalist outfits with no visual interest at the waist",
        ],
        tips=[
            "Use belts to create waist definition.",
            "Layering adds dimension and visual curves.",
            "Color blocking can create an hourglass illusion.",
        ],
    ),
    BodyType.INVERTED_TRIANGLE: BodyTypeGuidelines(
        description="Broad shoulders with narrower hips; strong upper body.",
        goal="Balance the upper body by adding volume to the lower half.",
        best_tops=[
            "V-necks", "Scoop necks", "Simple, fitted tops",
            "Raglan sleeves", "Halter necks (for a narrowing effect)",
        ],
        best_bottoms=[
            "Wide-leg trousers", "Flared skirts", "A-line skirts",
            "Cargo pants", "Pleated wide-leg pants",
        ],
        best_dresses=[
            "A-line dresses", "Fit-and-flare with a full skirt",
            "Wrap dresses", "Drop-waist dresses",
        ],
        best_outerwear=[
            "Cocoon coats", "Collarless jackets", "Single-breasted blazers",
            "Hip-length cardigans",
        ],
        patterns_and_prints=[
            "Simple, dark tops with printed bottoms",
            "Avoid horizontal stripes on top",
            "Wide stripes or bold prints on lower half",
        ],
        fabrics=[
            "Soft, unstructured fabrics on top",
            "Stiffer, voluminous fabrics on the bottom",
        ],
        avoid=[
            "Shoulder pads", "Boat necks", "Puffy sleeves",
            "Double-breasted jackets",
            "Heavy embellishments on the upper body",
        ],
        tips=[
            "Keep the top half simple and direct attention downward.",
            "Full skirts and wide-leg pants balance broad shoulders.",
            "V-necks narrow the shoulder line visually.",
        ],
    ),
    BodyType.ATHLETIC: BodyTypeGuidelines(
        description="Muscular, well-defined build with minimal waist definition.",
        goal="Soften angles and create waist definition; add feminine or relaxed touches.",
        best_tops=[
            "Off-the-shoulder tops", "Draped blouses", "Wrap tops",
            "Feminine ruffled tops", "Cowl necks",
        ],
        best_bottoms=[
            "Flared jeans", "Wide-leg trousers", "Pleated skirts",
            "Paperbag-waist pants",
        ],
        best_dresses=[
            "Wrap dresses", "Fit-and-flare", "Ruched dresses",
            "Draped dresses",
        ],
        best_outerwear=[
            "Belted coats", "Soft blazers", "Waterfall jackets",
            "Draped cardigans",
        ],
        patterns_and_prints=[
            "Flowing, organic prints", "Soft florals",
            "Curved patterns over geometric",
        ],
        fabrics=[
            "Soft jersey", "Silk and satin", "Chiffon",
            "Drapy materials that move with the body",
        ],
        avoid=[
            "Very structured, boxy pieces", "Overly tight athleisure for non-workout",
            "Stiff, heavy fabrics that emphasize broadness",
        ],
        tips=[
            "Draped fabrics soften a muscular silhouette.",
            "Belts at the waist create feminine curves.",
            "Mix structured and soft pieces for balance.",
        ],
    ),
    BodyType.PETITE: BodyTypeGuidelines(
        description="Shorter stature (typically under 5'4\" / 163 cm).",
        goal="Elongate the frame and create a proportional, streamlined silhouette.",
        best_tops=[
            "Fitted tops", "V-necks", "Cropped jackets",
            "Vertical details", "Monochrome tops matching bottoms",
        ],
        best_bottoms=[
            "High-waisted pants", "Slim-fit trousers", "Ankle-length pants",
            "Mini to knee-length skirts",
        ],
        best_dresses=[
            "Above-the-knee dresses", "Fit-and-flare",
            "Wrap dresses (petite sizing)", "Column dresses",
        ],
        best_outerwear=[
            "Cropped jackets", "Fitted blazers", "Short trench coats",
            "Tailored coats hitting mid-thigh",
        ],
        patterns_and_prints=[
            "Small-scale prints", "Vertical stripes",
            "Tone-on-tone patterns", "Avoid oversized motifs",
        ],
        fabrics=[
            "Lightweight, non-bulky fabrics",
            "Tailored materials", "Avoid heavy, stiff fabrics",
        ],
        avoid=[
            "Oversized, baggy clothing", "Maxi dresses that overwhelm",
            "Very wide-leg pants", "Large, chunky accessories",
            "Horizontal stripes that widen the frame",
        ],
        tips=[
            "Monochromatic dressing elongates the body.",
            "High-waisted bottoms visually lengthen the legs.",
            "Pointed-toe shoes add height.",
            "Tailoring is your best investment.",
        ],
    ),
    BodyType.TALL: BodyTypeGuidelines(
        description="Taller stature (typically over 5'8\" / 173 cm).",
        goal="Celebrate height while creating proportion and visual interest.",
        best_tops=[
            "Layered looks", "Belted tops", "Crop tops with high-waisted pants",
            "Wide necklines", "Horizontal details",
        ],
        best_bottoms=[
            "Wide-leg trousers", "Culottes", "Midi and maxi skirts",
            "Boyfriend jeans", "Full-length pants",
        ],
        best_dresses=[
            "Maxi dresses", "Midi dresses", "Shirt dresses",
            "Tiered dresses", "Color-blocked dresses",
        ],
        best_outerwear=[
            "Long coats", "Duster cardigans", "Oversized blazers",
            "Trench coats",
        ],
        patterns_and_prints=[
            "Bold, large-scale prints", "Horizontal stripes",
            "Color blocking", "All-over patterns",
        ],
        fabrics=[
            "Any fabric works", "Can carry heavier materials well",
            "Layered textures",
        ],
        avoid=[
            "Nothing is truly off-limits",
            "Very short hemlines if seeking proportion",
        ],
        tips=[
            "You can pull off oversized and voluminous pieces beautifully.",
            "Maxi and midi lengths are made for you.",
            "Bold prints and wide silhouettes look proportional on a tall frame.",
            "Embrace your height; it is a fashion asset.",
        ],
    ),
    BodyType.PLUS_SIZE: BodyTypeGuidelines(
        description="Fuller figure; focus on fit and flattering lines.",
        goal="Celebrate curves with well-fitted clothing that offers comfort and style.",
        best_tops=[
            "Wrap tops", "V-necks", "Empire waist tops",
            "Structured blouses", "Well-fitted knits",
        ],
        best_bottoms=[
            "High-waisted trousers", "Bootcut jeans", "A-line skirts",
            "Straight-leg pants with stretch", "Midi skirts",
        ],
        best_dresses=[
            "Wrap dresses", "A-line dresses", "Fit-and-flare",
            "Empire waist dresses", "Draped jersey dresses",
        ],
        best_outerwear=[
            "Tailored blazers", "Long cardigans", "Trench coats with a belt",
            "Single-breasted coats",
        ],
        patterns_and_prints=[
            "Vertical patterns", "Medium-scale prints",
            "Solid, rich colors", "Strategic color blocking",
        ],
        fabrics=[
            "Structured jersey", "Ponte", "Tailored wovens",
            "Medium-weight fabrics with drape",
            "Avoid very thin or very stiff fabrics",
        ],
        avoid=[
            "Ill-fitting clothes (too tight or too loose)",
            "Very thin, clingy fabrics without structure",
            "Oversized shapeless pieces",
            "Tiny, busy prints that create visual noise",
        ],
        tips=[
            "Fit is everything; tailoring transforms an outfit.",
            "Define the waist for an elegant silhouette.",
            "Rich, saturated colors look stunning.",
            "Invest in quality undergarments for a smooth foundation.",
        ],
    ),
}


class BodyTypeAnalyzer:
    """Analyze body types and provide tailored fashion recommendations.

    Uses evidence-based fashion styling principles to suggest flattering
    garment types, silhouettes, and styling strategies for each body type.
    """

    def __init__(self) -> None:
        self._guidelines = BODY_TYPE_GUIDELINES

    def get_guidelines(self, body_type: BodyType) -> BodyTypeGuidelines:
        """Return the full styling guidelines for a body type."""
        return self._guidelines[body_type]

    def recommend_categories(
        self, body_type: BodyType, category: GarmentCategory
    ) -> list[str]:
        """Get specific recommendations for a garment category and body type."""
        g = self._guidelines[body_type]
        mapping: dict[GarmentCategory, list[str]] = {
            GarmentCategory.TOP: g.best_tops,
            GarmentCategory.BOTTOM: g.best_bottoms,
            GarmentCategory.DRESS: g.best_dresses,
            GarmentCategory.OUTERWEAR: g.best_outerwear,
        }
        return mapping.get(category, [])

    def get_tips(self, body_type: BodyType) -> list[str]:
        """Return styling tips for a body type."""
        return self._guidelines[body_type].tips

    def get_avoid_list(self, body_type: BodyType) -> list[str]:
        """Return the list of things to avoid for a body type."""
        return self._guidelines[body_type].avoid

    def score_garment_fit(self, body_type: BodyType, garment_description: str) -> tuple[float, str]:
        """Score how well a garment description matches the body type guidelines.

        Returns (score 0-10, explanation).
        Uses simple keyword matching against recommended and avoid lists.
        """
        g = self._guidelines[body_type]
        desc_lower = garment_description.lower()

        # Check against avoid list
        for avoid_item in g.avoid:
            if any(word in desc_lower for word in avoid_item.lower().split() if len(word) > 3):
                return 3.0, f"Consider alternatives: {avoid_item}"

        # Check against recommended lists
        all_recs = g.best_tops + g.best_bottoms + g.best_dresses + g.best_outerwear
        for rec in all_recs:
            if any(word in desc_lower for word in rec.lower().split() if len(word) > 3):
                return 9.0, f"Great match for {body_type.value}: {rec}"

        return 6.0, "Neutral choice; check the detailed guidelines for optimal options."

    def summarize(self, body_type: BodyType) -> str:
        """Return a concise text summary of guidelines for a body type."""
        g = self._guidelines[body_type]
        lines = [
            f"Body Type: {body_type.value.replace('_', ' ').title()}",
            f"Description: {g.description}",
            f"Goal: {g.goal}",
            "",
            "Best Tops: " + ", ".join(g.best_tops),
            "Best Bottoms: " + ", ".join(g.best_bottoms),
            "Best Dresses: " + ", ".join(g.best_dresses),
            "Best Outerwear: " + ", ".join(g.best_outerwear),
            "",
            "Tips:",
        ]
        for tip in g.tips:
            lines.append(f"  - {tip}")
        lines.append("")
        lines.append("Avoid:")
        for item in g.avoid:
            lines.append(f"  - {item}")
        return "\n".join(lines)
