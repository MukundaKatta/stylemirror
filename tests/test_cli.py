"""Tests for the CLI interface."""

import pytest
from click.testing import CliRunner

from stylemirror.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


class TestCLI:
    def test_help(self, runner):
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "STYLEMIRROR" in result.output

    def test_version(self, runner):
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.output

    def test_profile_command(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, [
                "profile",
                "--body-type", "hourglass",
                "--style", "classic",
                "--colors", "navy,white",
            ])
            assert result.exit_code == 0
            assert "Profile saved" in result.output

    def test_wardrobe_add(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, [
                "wardrobe", "add",
                "--name", "Blue Shirt",
                "--category", "top",
                "--color", "blue",
                "--formality", "casual",
            ])
            assert result.exit_code == 0
            assert "Added" in result.output

    def test_wardrobe_list_empty(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, ["wardrobe", "list"])
            assert result.exit_code == 0

    def test_wardrobe_add_and_list(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            runner.invoke(cli, [
                "wardrobe", "add",
                "--name", "Red Dress",
                "--category", "dress",
                "--color", "red",
                "--formality", "semi_formal",
            ])
            result = runner.invoke(cli, ["wardrobe", "list"])
            assert result.exit_code == 0
            assert "Red Dress" in result.output

    def test_wardrobe_remove(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            runner.invoke(cli, [
                "wardrobe", "add",
                "--name", "Test Item",
                "--category", "top",
                "--color", "white",
            ])
            result = runner.invoke(cli, ["wardrobe", "remove", "Test Item"])
            assert result.exit_code == 0
            assert "Removed" in result.output

    def test_colors_harmony(self, runner):
        result = runner.invoke(cli, ["colors", "--color", "navy"])
        assert result.exit_code == 0
        assert "Navy" in result.output

    def test_colors_palette(self, runner):
        result = runner.invoke(cli, ["colors", "--palette", "navy,white,burgundy"])
        assert result.exit_code == 0

    def test_colors_season(self, runner):
        result = runner.invoke(cli, ["colors", "--season", "autumn"])
        assert result.exit_code == 0

    def test_colors_no_args(self, runner):
        result = runner.invoke(cli, ["colors"])
        assert result.exit_code == 0
        assert "Provide" in result.output

    def test_body_type_info(self, runner):
        result = runner.invoke(cli, ["body-type", "hourglass"])
        assert result.exit_code == 0
        assert "Hourglass" in result.output

    def test_style_guide(self, runner):
        result = runner.invoke(cli, ["style-guide", "minimalist"])
        assert result.exit_code == 0
        assert "Minimalist" in result.output

    def test_trends(self, runner):
        result = runner.invoke(cli, ["trends", "--season", "winter"])
        assert result.exit_code == 0
        assert "Winter" in result.output

    def test_occasion_info(self, runner):
        result = runner.invoke(cli, ["occasion", "wedding_guest"])
        assert result.exit_code == 0

    def test_recommend_empty_wardrobe(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, ["recommend"])
            assert result.exit_code == 0
            assert "empty" in result.output.lower()

    def test_report(self, runner, tmp_path):
        with runner.isolated_filesystem(temp_dir=tmp_path):
            result = runner.invoke(cli, ["report", "--season", "summer"])
            assert result.exit_code == 0
            assert "STYLEMIRROR" in result.output
