"""Style profile definitions and guidance.

Defines the key characteristics, wardrobe essentials, and styling rules
for each personal style archetype.
"""

from stylemirror.models import StyleType


# Detailed style profile definitions with real fashion guidance.
STYLE_PROFILES: dict[StyleType, dict] = {
    StyleType.MINIMALIST: {
        "motto": "Less is more.",
        "description": (
            "A minimalist wardrobe focuses on clean lines, neutral colors, "
            "quality over quantity, and timeless pieces that mix and match "
            "effortlessly. Every item earns its place."
        ),
        "key_colors": ["black", "white", "gray", "navy", "beige", "camel"],
        "signature_pieces": [
            "Tailored white shirt",
            "Black slim trousers",
            "Cashmere crewneck sweater",
            "Structured leather bag",
            "White leather sneakers",
            "Wool overcoat in camel or black",
        ],
        "fabrics": ["Cotton", "Wool", "Cashmere", "Silk", "Leather", "Linen"],
        "patterns": ["Solid colors", "Subtle textures", "Tonal variations"],
        "accessories": [
            "Simple watch",
            "Delicate gold or silver jewelry",
            "Structured leather belt",
        ],
        "rules": [
            "Stick to a neutral palette with one accent at most.",
            "Invest in quality basics that last years.",
            "Every piece should work with at least three others.",
            "Avoid logos, bold prints, and trendy pieces.",
            "Perfect fit is non-negotiable.",
        ],
    },
    StyleType.CLASSIC: {
        "motto": "Timeless elegance never goes out of style.",
        "description": (
            "Classic style is rooted in traditional, enduring fashion. "
            "Think Audrey Hepburn, Grace Kelly, or a well-dressed diplomat. "
            "Structured, polished, and always appropriate."
        ),
        "key_colors": ["navy", "white", "cream", "burgundy", "gray", "camel", "forest green"],
        "signature_pieces": [
            "Navy blazer",
            "Trench coat",
            "Breton striped shirt",
            "Tailored trousers",
            "Pearl or diamond stud earrings",
            "Leather loafers or ballet flats",
            "Little black dress",
        ],
        "fabrics": ["Wool", "Cotton", "Tweed", "Silk", "Fine leather"],
        "patterns": ["Stripes", "Houndstooth", "Plaid", "Polka dots (small)"],
        "accessories": [
            "Silk scarf",
            "Leather handbag",
            "Pearl necklace",
            "Classic watch",
            "Leather belt",
        ],
        "rules": [
            "Invest in quality tailoring.",
            "Stick to heritage patterns and traditional silhouettes.",
            "Accessories should be elegant and understated.",
            "When in doubt, dress up rather than down.",
            "A navy blazer is your most versatile piece.",
        ],
    },
    StyleType.BOHEMIAN: {
        "motto": "Free-spirited and artistically expressive.",
        "description": (
            "Bohemian style draws from artistic, hippie, and global influences. "
            "It celebrates individuality with flowing fabrics, layered jewelry, "
            "and an eclectic mix of textures and patterns."
        ),
        "key_colors": ["rust", "terracotta", "olive", "mustard", "cream", "turquoise", "burgundy"],
        "signature_pieces": [
            "Flowing maxi dress",
            "Embroidered blouse",
            "Fringe suede jacket",
            "Wide-brim hat",
            "Layered necklaces",
            "Ankle boots",
            "Woven or macrame bag",
        ],
        "fabrics": ["Cotton", "Linen", "Suede", "Crochet", "Chiffon", "Denim"],
        "patterns": ["Paisley", "Tie-dye", "Floral", "Ethnic prints", "Ikat"],
        "accessories": [
            "Layered bracelets and rings",
            "Long pendant necklaces",
            "Woven belts",
            "Headbands and scarves",
            "Fringe bags",
        ],
        "rules": [
            "Mix patterns and textures fearlessly, but keep a common color thread.",
            "Layer is a verb; use it liberally.",
            "Vintage and handmade pieces add authenticity.",
            "Comfort and movement are essential.",
            "More is more with accessories, but balance with simple garments.",
        ],
    },
    StyleType.STREETWEAR: {
        "motto": "Culture meets fashion; the street is the runway.",
        "description": (
            "Streetwear blends casual, athletic, and urban influences with "
            "a focus on comfort, self-expression, and cultural relevance. "
            "Sneakers are sacred, and the right graphic tee is art."
        ),
        "key_colors": ["black", "white", "gray", "olive", "earth tones", "bold accents"],
        "signature_pieces": [
            "Oversized graphic tee or hoodie",
            "Cargo pants or joggers",
            "Premium sneakers",
            "Bomber jacket",
            "Baseball cap or beanie",
            "Crossbody bag",
        ],
        "fabrics": ["Cotton jersey", "Nylon", "Denim", "Fleece", "Technical fabrics"],
        "patterns": ["Graphics", "Logos", "Camo", "Color blocking", "Abstract prints"],
        "accessories": [
            "Statement sneakers",
            "Chain necklaces",
            "Bucket hats",
            "Tech-inspired watches",
            "Crossbody or belt bags",
        ],
        "rules": [
            "Sneakers are the foundation; invest accordingly.",
            "Oversized silhouettes are intentional, not sloppy.",
            "Mix high-end with everyday brands for authenticity.",
            "Stay current with drops, collabs, and cultural moments.",
            "Confidence is the ultimate accessory.",
        ],
    },
    StyleType.PREPPY: {
        "motto": "Polished, put-together, and ivy-league inspired.",
        "description": (
            "Preppy style is rooted in American East Coast collegiate traditions. "
            "It is clean, colorful, and structured, with an emphasis on layering, "
            "patterns, and a polished appearance."
        ),
        "key_colors": ["navy", "white", "pink", "kelly green", "red", "khaki", "light blue"],
        "signature_pieces": [
            "Oxford button-down shirt",
            "V-neck cable-knit sweater",
            "Chinos or khaki pants",
            "Polo shirt",
            "Boat shoes or penny loafers",
            "Blazer with brass buttons",
            "Ribbon belt",
        ],
        "fabrics": ["Cotton Oxford", "Cable knit", "Seersucker", "Madras", "Twill", "Pique"],
        "patterns": ["Stripes", "Plaid", "Gingham", "Argyle", "Madras", "Cable knit"],
        "accessories": [
            "Ribbon or woven belt",
            "Pearl jewelry",
            "Headband",
            "Tortoiseshell sunglasses",
            "Canvas tote",
        ],
        "rules": [
            "Layer with purpose: collared shirt under sweater under blazer.",
            "Color is encouraged; pastels and brights are welcome.",
            "Patterns can be mixed if they share a color.",
            "Fit should be neat and trim, never sloppy.",
            "Grooming and neatness are part of the style.",
        ],
    },
    StyleType.ROMANTIC: {
        "motto": "Soft, feminine, and dreamily elegant.",
        "description": (
            "Romantic style embraces femininity with soft fabrics, floral prints, "
            "lace details, and flowing silhouettes. It is the style of garden "
            "parties and candlelit dinners."
        ),
        "key_colors": ["blush", "lavender", "rose", "cream", "soft blue", "mauve", "champagne"],
        "signature_pieces": [
            "Lace blouse",
            "Flowy midi skirt",
            "Wrap dress",
            "Silk camisole",
            "Cashmere cardigan",
            "Delicate heels",
        ],
        "fabrics": ["Lace", "Silk", "Chiffon", "Satin", "Cashmere", "Tulle"],
        "patterns": ["Florals", "Lace", "Delicate prints", "Watercolor patterns"],
        "accessories": [
            "Delicate layered necklaces",
            "Pearl earrings",
            "Floral hair accessories",
            "Dainty rings",
            "Small structured bag",
        ],
        "rules": [
            "Soft fabrics that drape and flow are essential.",
            "Florals are always in season for romantic style.",
            "Keep accessories delicate and feminine.",
            "Embrace gentle colors and avoid harsh contrasts.",
            "A wrap dress is the ultimate romantic wardrobe staple.",
        ],
    },
    StyleType.EDGY: {
        "motto": "Break the rules with intention.",
        "description": (
            "Edgy style pushes boundaries with dark palettes, leather, hardware, "
            "and unexpected combinations. It is confident, urban, and unapologetically bold."
        ),
        "key_colors": ["black", "charcoal", "burgundy", "dark red", "silver", "deep purple"],
        "signature_pieces": [
            "Leather moto jacket",
            "Black skinny jeans or leather pants",
            "Combat or Chelsea boots",
            "Band or graphic tee",
            "Studded belt",
            "Dark denim jacket",
        ],
        "fabrics": ["Leather", "Denim", "Metal hardware", "Mesh", "Distressed fabrics"],
        "patterns": ["Solid darks", "Animal print (subtle)", "Studs", "Distressed textures"],
        "accessories": [
            "Silver or gunmetal jewelry",
            "Chunky rings",
            "Studded belts",
            "Aviator sunglasses",
            "Structured black bag",
        ],
        "rules": [
            "Black is a color, a mood, and a lifestyle.",
            "One statement piece per outfit; let it command attention.",
            "Mix textures: leather with knit, metal with silk.",
            "Fit can be either sharp and slim or dramatically oversized.",
            "Attitude is half the outfit.",
        ],
    },
    StyleType.ATHLEISURE: {
        "motto": "Performance meets style; gym to street.",
        "description": (
            "Athleisure blurs the line between workout wear and everyday fashion. "
            "Technical fabrics, sleek silhouettes, and sporty details create a "
            "look that is active, modern, and effortlessly cool."
        ),
        "key_colors": ["black", "gray", "white", "navy", "neon accents", "olive"],
        "signature_pieces": [
            "High-quality leggings or joggers",
            "Performance sneakers",
            "Fitted zip-up jacket",
            "Matching set (top + bottom)",
            "Sports bra as a layering piece",
            "Sleek backpack",
        ],
        "fabrics": ["Nylon", "Spandex", "Performance knit", "Scuba", "Mesh"],
        "patterns": ["Color blocking", "Subtle logos", "Tonal patterns", "Mesh panels"],
        "accessories": [
            "Smart watch or fitness tracker",
            "Premium sneakers",
            "Sleek sunglasses",
            "Minimalist crossbody",
            "Baseball cap",
        ],
        "rules": [
            "Fit is paramount; too loose looks sloppy, too tight looks like gym-only.",
            "Invest in one premium sneaker that works for everything.",
            "Matching sets are the easiest path to looking put-together.",
            "Layer a structured jacket to dress up athletic basics.",
            "Quality fabrics elevate athleisure from lazy to intentional.",
        ],
    },
}


class StyleProfileGuide:
    """Guidance engine for personal style archetypes.

    Provides detailed information about each style type including
    signature pieces, color palettes, fabric preferences, and styling rules.
    """

    def __init__(self) -> None:
        self._profiles = STYLE_PROFILES

    def get_profile(self, style: StyleType) -> dict:
        """Return the full profile for a style type."""
        return self._profiles[style]

    def get_motto(self, style: StyleType) -> str:
        """Return the style motto."""
        return self._profiles[style]["motto"]

    def get_signature_pieces(self, style: StyleType) -> list[str]:
        """Return the signature wardrobe pieces for a style."""
        return self._profiles[style]["signature_pieces"]

    def get_key_colors(self, style: StyleType) -> list[str]:
        """Return the key color palette for a style."""
        return self._profiles[style]["key_colors"]

    def get_rules(self, style: StyleType) -> list[str]:
        """Return the styling rules for a style."""
        return self._profiles[style]["rules"]

    def get_fabrics(self, style: StyleType) -> list[str]:
        """Return preferred fabrics for a style."""
        return self._profiles[style]["fabrics"]

    def list_styles(self) -> list[StyleType]:
        """Return all available style types."""
        return list(self._profiles.keys())

    def summarize(self, style: StyleType) -> str:
        """Return a formatted text summary of a style profile."""
        p = self._profiles[style]
        lines = [
            f"Style: {style.value.replace('_', ' ').title()}",
            f'Motto: "{p["motto"]}"',
            f"Description: {p['description']}",
            "",
            f"Key Colors: {', '.join(p['key_colors'])}",
            "",
            "Signature Pieces:",
        ]
        for piece in p["signature_pieces"]:
            lines.append(f"  - {piece}")
        lines.append("")
        lines.append("Style Rules:")
        for rule in p["rules"]:
            lines.append(f"  - {rule}")
        return "\n".join(lines)
