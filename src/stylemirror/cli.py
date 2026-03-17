"""CLI interface for STYLEMIRROR using Click and Rich."""

import json
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel

from stylemirror.models import (
    BodyType,
    Formality,
    Garment,
    GarmentCategory,
    OccasionType,
    Season,
    StyleProfile,
    StyleType,
    Weather,
)
from stylemirror.fashion.occasions import OccasionDresscode
from stylemirror.fashion.styles import StyleProfileGuide
from stylemirror.fashion.trends import TrendTracker
from stylemirror.report import StyleReporter
from stylemirror.stylist.body_type import BodyTypeAnalyzer
from stylemirror.stylist.color_theory import ColorHarmonyEngine
from stylemirror.stylist.recommender import OutfitRecommender
from stylemirror.stylist.wardrobe import WardrobeManager

console = Console()
PROFILE_PATH = Path("stylemirror_profile.json")
WARDROBE_PATH = Path("wardrobe.json")


def _load_wardrobe() -> WardrobeManager:
    wm = WardrobeManager(storage_path=WARDROBE_PATH)
    wm.load()
    return wm


def _load_profile() -> StyleProfile | None:
    if PROFILE_PATH.exists():
        data = json.loads(PROFILE_PATH.read_text())
        return StyleProfile.model_validate(data)
    return None


def _save_profile(profile: StyleProfile) -> None:
    PROFILE_PATH.write_text(json.dumps(profile.model_dump(mode="json"), indent=2))


@click.group()
@click.version_option(version="0.1.0", prog_name="stylemirror")
def cli() -> None:
    """STYLEMIRROR - AI Personal Stylist.

    Get outfit recommendations based on occasion, weather, body type,
    and color theory.
    """


# ------------------------------------------------------------------
# Profile commands
# ------------------------------------------------------------------


@cli.command()
@click.option(
    "--body-type",
    type=click.Choice([bt.value for bt in BodyType], case_sensitive=False),
    required=True,
    help="Your body type.",
)
@click.option(
    "--style",
    type=click.Choice([s.value for s in StyleType], case_sensitive=False),
    default="classic",
    help="Your preferred style.",
)
@click.option("--colors", default="", help="Comma-separated preferred colors.")
@click.option("--avoid-colors", default="", help="Comma-separated colors to avoid.")
def profile(body_type: str, style: str, colors: str, avoid_colors: str) -> None:
    """Set up or update your style profile."""
    preferred = [c.strip() for c in colors.split(",") if c.strip()]
    avoided = [c.strip() for c in avoid_colors.split(",") if c.strip()]

    p = StyleProfile(
        body_type=BodyType(body_type),
        preferred_style=StyleType(style),
        preferred_colors=preferred,
        avoided_colors=avoided,
    )
    _save_profile(p)
    console.print(f"[green]Profile saved![/green]")
    console.print(f"  Body Type: {p.body_type.value}")
    console.print(f"  Style: {p.preferred_style.value}")
    if preferred:
        console.print(f"  Preferred Colors: {', '.join(preferred)}")


# ------------------------------------------------------------------
# Wardrobe commands
# ------------------------------------------------------------------


@cli.group()
def wardrobe() -> None:
    """Manage your wardrobe."""


@wardrobe.command("add")
@click.option("--name", required=True, help="Name of the garment.")
@click.option(
    "--category",
    type=click.Choice([c.value for c in GarmentCategory], case_sensitive=False),
    required=True,
    help="Garment category.",
)
@click.option("--color", required=True, help="Primary color.")
@click.option("--secondary-color", default=None, help="Secondary color.")
@click.option(
    "--formality",
    type=click.Choice([f.value for f in Formality], case_sensitive=False),
    default="casual",
    help="Formality level.",
)
@click.option("--material", default=None, help="Material/fabric.")
@click.option("--brand", default=None, help="Brand name.")
@click.option("--tags", default="", help="Comma-separated tags.")
@click.option("--favorite", is_flag=True, help="Mark as favorite.")
def wardrobe_add(
    name: str,
    category: str,
    color: str,
    secondary_color: str | None,
    formality: str,
    material: str | None,
    brand: str | None,
    tags: str,
    favorite: bool,
) -> None:
    """Add a garment to your wardrobe."""
    wm = _load_wardrobe()
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    garment = Garment(
        name=name,
        category=GarmentCategory(category),
        color=color,
        secondary_color=secondary_color,
        formality=Formality(formality),
        material=material,
        brand=brand,
        tags=tag_list,
        favorite=favorite,
    )
    wm.add_garment(garment)
    wm.save()
    console.print(f"[green]Added '{name}' to your wardrobe.[/green]")


@wardrobe.command("remove")
@click.argument("name")
def wardrobe_remove(name: str) -> None:
    """Remove a garment by name."""
    wm = _load_wardrobe()
    if wm.remove_garment(name):
        wm.save()
        console.print(f"[green]Removed '{name}' from your wardrobe.[/green]")
    else:
        console.print(f"[red]Garment '{name}' not found.[/red]")


@wardrobe.command("list")
@click.option(
    "--category",
    type=click.Choice([c.value for c in GarmentCategory], case_sensitive=False),
    default=None,
    help="Filter by category.",
)
@click.option("--color", default=None, help="Filter by color.")
def wardrobe_list(category: str | None, color: str | None) -> None:
    """List wardrobe items."""
    wm = _load_wardrobe()
    reporter = StyleReporter(console)

    if category:
        garments = wm.by_category(GarmentCategory(category))
        # Temporarily replace for display
        filtered_wm = WardrobeManager()
        for g in garments:
            filtered_wm.add_garment(g)
        reporter.display_wardrobe(filtered_wm)
    elif color:
        garments = wm.by_color(color)
        filtered_wm = WardrobeManager()
        for g in garments:
            filtered_wm.add_garment(g)
        reporter.display_wardrobe(filtered_wm)
    else:
        reporter.display_wardrobe(wm)


# ------------------------------------------------------------------
# Recommend command
# ------------------------------------------------------------------


@cli.command()
@click.option(
    "--occasion",
    type=click.Choice([o.value for o in OccasionType], case_sensitive=False),
    default="casual_everyday",
    help="Occasion for the outfit.",
)
@click.option(
    "--weather",
    type=click.Choice([w.value for w in Weather], case_sensitive=False),
    default="mild",
    help="Current weather.",
)
@click.option(
    "--season",
    type=click.Choice([s.value for s in Season], case_sensitive=False),
    default=None,
    help="Current season.",
)
@click.option("--color", default=None, help="Preferred base color.")
@click.option("--max-results", default=5, type=int, help="Max outfits to show.")
def recommend(
    occasion: str, weather: str, season: str | None, color: str | None, max_results: int
) -> None:
    """Get outfit recommendations from your wardrobe."""
    wm = _load_wardrobe()
    sp = _load_profile()

    if wm.count() == 0:
        console.print(
            "[yellow]Your wardrobe is empty. Add items with "
            "'stylemirror wardrobe add' first.[/yellow]"
        )
        return

    recommender = OutfitRecommender(wm, style_profile=sp)
    outfits = recommender.recommend(
        occasion=occasion,
        weather=weather,
        season=season,
        color_preference=color,
        max_results=max_results,
    )

    reporter = StyleReporter(console)
    reporter.display_outfits(outfits)


# ------------------------------------------------------------------
# Color commands
# ------------------------------------------------------------------


@cli.command()
@click.option("--color", default=None, help="Find harmonies for a color.")
@click.option("--palette", default=None, help="Comma-separated colors to evaluate.")
@click.option(
    "--season",
    type=click.Choice([s.value for s in Season], case_sensitive=False),
    default=None,
    help="Show seasonal color recommendations.",
)
def colors(color: str | None, palette: str | None, season: str | None) -> None:
    """Analyze colors and find harmonious combinations."""
    reporter = StyleReporter(console)
    engine = ColorHarmonyEngine()

    if color:
        reporter.display_color_harmonies(color)

    if palette:
        color_list = [c.strip() for c in palette.split(",") if c.strip()]
        reporter.display_color_evaluation(color_list)

    if season:
        seasonal = engine.seasonal_recommendations(Season(season))
        console.print(f"\n[bold]Recommended colors for {season.title()}:[/bold]")
        console.print(f"  {', '.join(c.title() for c in seasonal)}")

    if not color and not palette and not season:
        console.print("[yellow]Provide --color, --palette, or --season.[/yellow]")


# ------------------------------------------------------------------
# Info commands
# ------------------------------------------------------------------


@cli.command("body-type")
@click.argument(
    "body_type",
    type=click.Choice([bt.value for bt in BodyType], case_sensitive=False),
)
def body_type_info(body_type: str) -> None:
    """View dressing guidelines for a body type."""
    analyzer = BodyTypeAnalyzer()
    summary = analyzer.summarize(BodyType(body_type))
    console.print(Panel(summary, title=f"Body Type: {body_type.replace('_', ' ').title()}", border_style="green"))


@cli.command("style-guide")
@click.argument(
    "style",
    type=click.Choice([s.value for s in StyleType], case_sensitive=False),
)
def style_guide(style: str) -> None:
    """View detailed guide for a style archetype."""
    guide = StyleProfileGuide()
    summary = guide.summarize(StyleType(style))
    console.print(Panel(summary, title=f"Style: {style.replace('_', ' ').title()}", border_style="magenta"))


@cli.command()
@click.option(
    "--season",
    type=click.Choice([s.value for s in Season], case_sensitive=False),
    default="spring",
    help="Season for trends.",
)
def trends(season: str) -> None:
    """View current fashion trends for a season."""
    tracker = TrendTracker()
    summary = tracker.summarize_season(Season(season))
    console.print(summary)


@cli.command("occasion")
@click.argument(
    "occasion",
    type=click.Choice([o.value for o in OccasionType], case_sensitive=False),
)
def occasion_info(occasion: str) -> None:
    """View dress code guide for an occasion."""
    guide = OccasionDresscode()
    summary = guide.summarize(OccasionType(occasion))
    console.print(Panel(summary, title="Dress Code Guide", border_style="blue"))


# ------------------------------------------------------------------
# Report command
# ------------------------------------------------------------------


@cli.command()
@click.option(
    "--season",
    type=click.Choice([s.value for s in Season], case_sensitive=False),
    default="spring",
    help="Season for the report.",
)
def report(season: str) -> None:
    """Generate a comprehensive style report."""
    wm = _load_wardrobe()
    sp = _load_profile()
    reporter = StyleReporter(console)
    reporter.full_report(wm, profile=sp, season=Season(season))


if __name__ == "__main__":
    cli()
