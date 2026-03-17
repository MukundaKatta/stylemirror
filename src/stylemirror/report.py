"""Style report generation using Rich for beautiful terminal output."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from stylemirror.models import (
    BodyType,
    ColorHarmonyType,
    Outfit,
    Season,
    StyleProfile as StyleProfileModel,
    StyleType,
)
from stylemirror.fashion.styles import StyleProfileGuide
from stylemirror.fashion.trends import TrendTracker
from stylemirror.stylist.body_type import BodyTypeAnalyzer
from stylemirror.stylist.color_theory import ColorHarmonyEngine
from stylemirror.stylist.wardrobe import WardrobeManager


class StyleReporter:
    """Generate comprehensive style reports with Rich formatting."""

    def __init__(self, console: Console | None = None) -> None:
        self.console = console or Console()
        self.color_engine = ColorHarmonyEngine()
        self.body_analyzer = BodyTypeAnalyzer()
        self.style_guide = StyleProfileGuide()
        self.trend_tracker = TrendTracker()

    # ------------------------------------------------------------------
    # Outfit display
    # ------------------------------------------------------------------

    def display_outfit(self, outfit: Outfit) -> None:
        """Display a single outfit recommendation."""
        score_color = "green" if outfit.score >= 7 else "yellow" if outfit.score >= 5 else "red"
        title = f"[bold]{outfit.name}[/bold]  [{score_color}]{outfit.score}/10[/{score_color}]"

        table = Table(show_header=True, header_style="bold cyan", box=None)
        table.add_column("Item", style="white")
        table.add_column("Category", style="dim")
        table.add_column("Color", style="bold")
        table.add_column("Formality", style="dim")

        for g in outfit.garments:
            table.add_row(g.name, g.category.value, g.color, g.formality.value)

        content_parts = [table]

        panel = Panel(
            table,
            title=title,
            subtitle=f"{outfit.occasion.value} | {outfit.season.value}",
            border_style="blue",
        )
        self.console.print(panel)

        if outfit.notes:
            for note in outfit.notes:
                if note:
                    self.console.print(f"  [dim italic]> {note}[/dim italic]")
            self.console.print()

    def display_outfits(self, outfits: list[Outfit]) -> None:
        """Display multiple outfit recommendations."""
        if not outfits:
            self.console.print("[yellow]No outfit recommendations found.[/yellow]")
            return

        self.console.print(
            Panel(
                f"[bold]Found {len(outfits)} outfit suggestion(s)[/bold]",
                style="green",
            )
        )
        for outfit in outfits:
            self.display_outfit(outfit)

    # ------------------------------------------------------------------
    # Wardrobe report
    # ------------------------------------------------------------------

    def display_wardrobe(self, wardrobe: WardrobeManager) -> None:
        """Display the full wardrobe inventory."""
        garments = wardrobe.get_all()
        if not garments:
            self.console.print("[yellow]Your wardrobe is empty. Add some items![/yellow]")
            return

        table = Table(
            title="Your Wardrobe",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("#", style="dim", width=4)
        table.add_column("Name", style="bold")
        table.add_column("Category")
        table.add_column("Color", style="bold")
        table.add_column("Formality")
        table.add_column("Fav", width=3)

        for i, g in enumerate(garments, 1):
            fav = "[red]<3[/red]" if g.favorite else ""
            table.add_row(
                str(i), g.name, g.category.value, g.color, g.formality.value, fav
            )

        self.console.print(table)
        self.console.print()

        # Distribution summaries
        color_dist = wardrobe.color_distribution()
        if color_dist:
            color_table = Table(title="Color Distribution", box=None)
            color_table.add_column("Color", style="bold")
            color_table.add_column("Count", justify="right")
            for color, count in color_dist.items():
                bar = "[green]" + "|" * count + "[/green]"
                color_table.add_row(color, f"{count} {bar}")
            self.console.print(color_table)
            self.console.print()

        # Wardrobe gaps
        gaps = wardrobe.wardrobe_gaps()
        if gaps:
            self.console.print("[bold yellow]Wardrobe Gaps:[/bold yellow]")
            for gap in gaps:
                self.console.print(f"  [yellow]- {gap}[/yellow]")
            self.console.print()

    # ------------------------------------------------------------------
    # Color harmony report
    # ------------------------------------------------------------------

    def display_color_harmonies(self, color: str) -> None:
        """Display all color harmonies for a given color."""
        harmonies = self.color_engine.find_harmonies(color)

        self.console.print(
            Panel(
                f"[bold]Color Harmonies for [cyan]{color.title()}[/cyan][/bold]",
                style="cyan",
            )
        )

        for harmony_type, colors in harmonies.items():
            color_text = ", ".join(c.title() for c in colors[:6])
            if len(colors) > 6:
                color_text += f" (+{len(colors) - 6} more)"
            self.console.print(
                f"  [bold]{harmony_type.value.replace('_', ' ').title()}:[/bold] {color_text}"
            )
        self.console.print()

    def display_color_evaluation(self, colors: list[str]) -> None:
        """Evaluate and display a color combination."""
        score, harmony, explanation = self.color_engine.evaluate_combination(colors)
        score_color = "green" if score >= 7 else "yellow" if score >= 5 else "red"

        color_str = " + ".join(c.title() for c in colors)
        self.console.print(
            Panel(
                f"[bold]{color_str}[/bold]\n\n"
                f"Score: [{score_color}]{score}/10[/{score_color}]\n"
                f"Harmony: {harmony.value if harmony else 'None detected'}\n\n"
                f"[italic]{explanation}[/italic]",
                title="Color Evaluation",
                border_style="cyan",
            )
        )

    # ------------------------------------------------------------------
    # Full style report
    # ------------------------------------------------------------------

    def full_report(
        self,
        wardrobe: WardrobeManager,
        profile: StyleProfileModel | None = None,
        season: Season = Season.SPRING,
    ) -> None:
        """Generate a comprehensive style report."""
        self.console.print()
        self.console.print(
            Panel(
                "[bold white]STYLEMIRROR[/bold white]\n[dim]AI Personal Stylist Report[/dim]",
                style="bold blue",
                expand=False,
            )
        )
        self.console.print()

        # Profile summary
        if profile:
            self.console.print("[bold underline]Your Style Profile[/bold underline]")
            self.console.print(f"  Body Type: {profile.body_type.value.replace('_', ' ').title()}")
            self.console.print(f"  Style: {profile.preferred_style.value.replace('_', ' ').title()}")
            if profile.preferred_colors:
                self.console.print(f"  Preferred Colors: {', '.join(profile.preferred_colors)}")
            self.console.print()

            # Body type tips
            tips = self.body_analyzer.get_tips(profile.body_type)
            self.console.print("[bold]Body Type Tips:[/bold]")
            for tip in tips:
                self.console.print(f"  [green]- {tip}[/green]")
            self.console.print()

            # Style guide
            style_summary = self.style_guide.get_motto(profile.preferred_style)
            self.console.print(f'[bold]Style Motto:[/bold] [italic]"{style_summary}"[/italic]')
            rules = self.style_guide.get_rules(profile.preferred_style)
            self.console.print("[bold]Style Rules:[/bold]")
            for rule in rules:
                self.console.print(f"  - {rule}")
            self.console.print()

        # Wardrobe overview
        self.console.print("[bold underline]Wardrobe Overview[/bold underline]")
        self.display_wardrobe(wardrobe)

        # Seasonal trends
        self.console.print(f"[bold underline]Trends for {season.value.title()}[/bold underline]")
        trends = self.trend_tracker.get_trends(season)
        for trend in trends:
            self.console.print(f"  [bold]{trend['name']}[/bold]: {trend['description']}")
            self.console.print(f"    [dim]How to wear: {trend['how_to_wear']}[/dim]")
        self.console.print()

        # Seasonal colors
        self.console.print(f"[bold underline]Recommended Colors for {season.value.title()}[/bold underline]")
        seasonal_colors = self.color_engine.seasonal_recommendations(season)
        self.console.print(f"  {', '.join(c.title() for c in seasonal_colors)}")
        self.console.print()

        self.console.print("[dim]Report generated by STYLEMIRROR[/dim]")
