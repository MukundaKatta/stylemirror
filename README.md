# STYLEMIRROR - AI Personal Stylist

An intelligent personal styling assistant that recommends outfits based on occasion, weather, body type, and color preferences using real fashion guidelines and color theory.

## Features

- **Outfit Recommendations**: Smart suggestions based on occasion, weather, body type, and color preferences
- **Wardrobe Management**: Track your owned clothes with categories and colors
- **Color Theory Engine**: Complementary, analogous, and triadic color matching
- **Body Type Analysis**: Dressing guidelines tailored to your body shape
- **Trend Tracking**: Seasonal fashion trend awareness
- **Occasion Dresscodes**: Appropriate styling for casual, business, formal, wedding, and more
- **Style Profiles**: Support for minimalist, classic, bohemian, streetwear, and preppy styles

## Installation

```bash
pip install -e .
```

## Usage

### CLI

```bash
# Set up your style profile
stylemirror profile --body-type hourglass --style classic --colors "navy,white,beige"

# Add items to your wardrobe
stylemirror wardrobe add --name "Navy Blazer" --category outerwear --color navy --formality smart_casual

# Get outfit recommendations
stylemirror recommend --occasion business_casual --weather warm --season summer

# Analyze color harmony
stylemirror colors --palette "navy,white,burgundy"

# View your wardrobe
stylemirror wardrobe list

# Generate a style report
stylemirror report
```

### Python API

```python
from stylemirror.models import Garment, StyleProfile, GarmentCategory, Formality
from stylemirror.stylist.recommender import OutfitRecommender
from stylemirror.stylist.wardrobe import WardrobeManager
from stylemirror.stylist.color_theory import ColorHarmonyEngine

# Create a wardrobe manager and add clothes
wardrobe = WardrobeManager()
wardrobe.add_garment(Garment(
    name="Navy Blazer",
    category=GarmentCategory.OUTERWEAR,
    color="navy",
    formality=Formality.SMART_CASUAL,
))

# Get outfit recommendations
recommender = OutfitRecommender(wardrobe)
outfits = recommender.recommend(occasion="business_casual", weather="warm")

# Analyze color harmony
engine = ColorHarmonyEngine()
harmonies = engine.find_harmonies("navy")
```

## Dependencies

- Python 3.10+
- pydantic
- click
- rich

## License

MIT
