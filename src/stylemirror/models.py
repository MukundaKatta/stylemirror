"""Pydantic models for STYLEMIRROR."""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GarmentCategory(str, Enum):
    """Categories of clothing items."""

    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    OUTERWEAR = "outerwear"
    FOOTWEAR = "footwear"
    ACCESSORY = "accessory"
    ACTIVEWEAR = "activewear"
    SWIMWEAR = "swimwear"
    UNDERWEAR = "underwear"


class Formality(str, Enum):
    """Formality levels for garments and occasions."""

    VERY_CASUAL = "very_casual"
    CASUAL = "casual"
    SMART_CASUAL = "smart_casual"
    BUSINESS_CASUAL = "business_casual"
    BUSINESS_FORMAL = "business_formal"
    SEMI_FORMAL = "semi_formal"
    FORMAL = "formal"
    BLACK_TIE = "black_tie"
    WHITE_TIE = "white_tie"


class Season(str, Enum):
    """Seasons affecting fashion choices."""

    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"


class Weather(str, Enum):
    """Weather conditions influencing outfit choices."""

    HOT = "hot"
    WARM = "warm"
    MILD = "mild"
    COOL = "cool"
    COLD = "cold"
    RAINY = "rainy"
    SNOWY = "snowy"


class BodyType(str, Enum):
    """Body type classifications for styling guidance."""

    HOURGLASS = "hourglass"
    PEAR = "pear"
    APPLE = "apple"
    RECTANGLE = "rectangle"
    INVERTED_TRIANGLE = "inverted_triangle"
    ATHLETIC = "athletic"
    PETITE = "petite"
    TALL = "tall"
    PLUS_SIZE = "plus_size"


class StyleType(str, Enum):
    """Personal style archetypes."""

    MINIMALIST = "minimalist"
    CLASSIC = "classic"
    BOHEMIAN = "bohemian"
    STREETWEAR = "streetwear"
    PREPPY = "preppy"
    ROMANTIC = "romantic"
    EDGY = "edgy"
    ATHLEISURE = "athleisure"


class OccasionType(str, Enum):
    """Types of occasions requiring specific dress codes."""

    CASUAL_EVERYDAY = "casual_everyday"
    CASUAL_WEEKEND = "casual_weekend"
    BUSINESS_CASUAL = "business_casual"
    BUSINESS_FORMAL = "business_formal"
    DATE_NIGHT = "date_night"
    COCKTAIL_PARTY = "cocktail_party"
    FORMAL_GALA = "formal_gala"
    WEDDING_GUEST = "wedding_guest"
    JOB_INTERVIEW = "job_interview"
    OUTDOOR_EVENT = "outdoor_event"
    BEACH = "beach"
    WORKOUT = "workout"
    BRUNCH = "brunch"


class ColorHarmonyType(str, Enum):
    """Types of color harmonies from color theory."""

    COMPLEMENTARY = "complementary"
    ANALOGOUS = "analogous"
    TRIADIC = "triadic"
    SPLIT_COMPLEMENTARY = "split_complementary"
    MONOCHROMATIC = "monochromatic"
    NEUTRAL = "neutral"


class Garment(BaseModel):
    """A single clothing item in the wardrobe."""

    name: str = Field(..., description="Name of the garment")
    category: GarmentCategory = Field(..., description="Category of the garment")
    color: str = Field(..., description="Primary color of the garment")
    secondary_color: Optional[str] = Field(None, description="Secondary/accent color")
    formality: Formality = Field(
        Formality.CASUAL, description="Formality level of the garment"
    )
    seasons: list[Season] = Field(
        default_factory=lambda: list(Season),
        description="Seasons this garment is suitable for",
    )
    material: Optional[str] = Field(None, description="Fabric or material")
    brand: Optional[str] = Field(None, description="Brand name")
    tags: list[str] = Field(default_factory=list, description="Custom tags")
    favorite: bool = Field(False, description="Whether this is a favorite item")


class Outfit(BaseModel):
    """A curated combination of garments forming a complete outfit."""

    name: str = Field(..., description="Name or description of the outfit")
    garments: list[Garment] = Field(..., description="List of garments in the outfit")
    occasion: OccasionType = Field(..., description="Occasion this outfit suits")
    formality: Formality = Field(..., description="Overall formality level")
    season: Season = Field(..., description="Best season for this outfit")
    color_harmony: Optional[ColorHarmonyType] = Field(
        None, description="Color harmony type achieved"
    )
    score: float = Field(
        0.0, ge=0.0, le=10.0, description="Style score out of 10"
    )
    notes: list[str] = Field(
        default_factory=list, description="Styling tips and notes"
    )


class ColorPalette(BaseModel):
    """A coordinated set of colors for outfit building."""

    name: str = Field(..., description="Palette name")
    primary: str = Field(..., description="Primary/dominant color")
    secondary: str = Field(..., description="Secondary color")
    accent: Optional[str] = Field(None, description="Accent color")
    neutral: Optional[str] = Field(None, description="Neutral base color")
    harmony_type: ColorHarmonyType = Field(
        ..., description="Type of color harmony used"
    )
    season_affinity: list[Season] = Field(
        default_factory=list, description="Seasons this palette works best for"
    )


class StyleProfile(BaseModel):
    """A user's personal style profile."""

    body_type: BodyType = Field(..., description="Body type classification")
    preferred_style: StyleType = Field(
        StyleType.CLASSIC, description="Preferred style archetype"
    )
    preferred_colors: list[str] = Field(
        default_factory=list, description="Preferred colors"
    )
    avoided_colors: list[str] = Field(
        default_factory=list, description="Colors to avoid"
    )
    preferred_formality: Formality = Field(
        Formality.SMART_CASUAL, description="Default formality preference"
    )
    budget_conscious: bool = Field(
        False, description="Whether to prioritize budget-friendly options"
    )
    sustainability_focus: bool = Field(
        False, description="Whether to prioritize sustainable fashion"
    )
