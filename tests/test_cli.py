from click.testing import CliRunner

from pirebok import cli


def test_cli():
    payload = "SELECT 42 /*forty-two*/"

    runner = CliRunner()
    result = runner.invoke(cli.main, ["-f", "RandomGenericFuzzer", "-p", payload])
    assert result.output != payload


def test_cli_with_guided_options():
    payload = "SELECT 42 /*forty-two*/"

    runner = CliRunner()
    result = runner.invoke(
        cli.main,
        ["-f", "RandomGenericFuzzer", "-p", payload, "--max-rounds", "50", "--round-size", "10", "--timeout", "5"],
    )
    assert result.exit_code == 0
