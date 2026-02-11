import sys
from functools import reduce
from operator import iconcat

import click

from pirebok.banner import banner
from pirebok.fuzzers import Fuzzer, FuzzerBuilder


class BannerCommand(click.Command):
    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        if not ctx.params.get("silent"):
            print(banner(), file=sys.stderr)
        super().format_help(ctx, formatter)


@click.command(cls=BannerCommand, no_args_is_help=True, context_settings={'show_default': True})
@click.option(
    "-f",
    "--fuzzer",
    required=True,
    type=click.Choice(
        map(lambda x: x.__name__, reduce(iconcat, map(lambda x: x.__subclasses__(), Fuzzer.__subclasses__()))),
        case_sensitive=False,
    ),
    help="choose fuzzer",
)
@click.option("-s", "--steps", default=10, help="Number of iteration")
@click.option("-t", "--threshold", default=0.5, help="Threshold for the guided fuzzers")
@click.option("--max-rounds", default=100, help="Maximum mutation rounds for guided fuzzers")
@click.option("--round-size", default=20, help="Mutations per round for guided fuzzers")
@click.option("--timeout", default=0, help="Timeout in seconds, 0=unlimited")
@click.option("-p", "--payload", required=True, help="Payload to fuzz")
@click.option("-q", "--silent", is_flag=True, default=False, help="Suppress banner")
def main(
    fuzzer: str,
    steps: int,
    threshold: float,
    max_rounds: int,
    round_size: int,
    timeout: int,
    payload: str,
    silent: bool,
) -> None:
    if not silent:
        print(banner(), file=sys.stderr)
    fuzzer_builder = FuzzerBuilder()
    fzzer = (
        fuzzer_builder.choice(fuzzer)
        .threshold(threshold)
        .max_rounds(max_rounds)
        .round_size(round_size)
        .timeout(timeout)
        .build()
    )
    print("\n".join(map(repr, set(map(lambda _: fzzer.fuzz(payload), range(steps))))))


if __name__ == "__main__":
    main()  # pragma: no cover
