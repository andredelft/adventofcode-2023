import click
from datetime import datetime
from aocd import get_data, submit as aocd_submit
from pathlib import Path
import yaml
import importlib
from templates import TEMPLATE, TEST_TEMPLATE
from typing import Literal

Part = Literal["a", "b"]

TODAY = datetime.now().day

ENTRYPOINTS_FILENAME = "entrypoints.yaml"
with open(ENTRYPOINTS_FILENAME) as f:
    ENTRYPOINTS = yaml.safe_load(f) or {}


def update_entrypoints():
    with open(ENTRYPOINTS_FILENAME, "w") as f:
        yaml.safe_dump(ENTRYPOINTS, f)


def get_day_path(day: int):
    return Path(f"day_{day:02d}")


def get_module_name(day: int) -> str:
    module_name = ENTRYPOINTS.get(day)

    if not module_name:
        click.BadParameter(f"Day {day} is not initialized yet")

    return module_name


def get_solution(part: Part, day: int, input_string: str):
    module_name = get_module_name(day)

    m = importlib.import_module(f"{get_day_path(day)}.{module_name}")
    solve = getattr(m, f"solve_{part}")
    return solve(input_string)


def test_solution(part: Part, day: int):
    module_name = get_module_name(day)

    m = importlib.import_module(f"{get_day_path(day)}.test_{module_name}")
    test = getattr(m, f"test_{part}")

    try:
        test()
    except AssertionError:
        click.echo("Test failed (refer to PyTest for details)")
    else:
        click.echo("Test succeeded!")


arg_module_name = click.argument("module_name")
arg_part = click.argument("part", type=click.Choice(["a", "b"]))
arg_day = click.argument("day", default=TODAY, type=int)


@click.command()
@arg_module_name
@arg_day
def prepare(module_name: str, day: int):
    """Prepare a new AoC puzzle.

    Args:
        module_name (str): Provide a catchy module name that reflects todays puzzle!
        day (int): The day number of the puzzle (defaults to today).
    """
    day_path = get_day_path(day)
    day_path.mkdir(exist_ok=True)

    with open(day_path / "input.txt", "w") as f:
        f.write(get_data(day=day))

    with open(day_path / f"{module_name}.py", "w") as f:
        f.write(TEMPLATE)

    with open(day_path / f"test_{module_name}.py", "w") as f:
        f.write(TEST_TEMPLATE.format(module_name=module_name, day_path=day_path))

    ENTRYPOINTS[day] = module_name
    update_entrypoints()


@click.command()
@arg_part
@arg_day
def test(part: Part, day: int):
    """Test a given puzzle."""

    test_solution(part, day)


@click.command()
@arg_part
@arg_day
def solve(part: Part, day: int):
    """Get the solution of a given puzzle."""

    with open(get_day_path(day) / "input.txt") as f:
        click.echo(get_solution(part, day, f.read()))


@click.command()
@arg_part
@arg_day
def submit(part: Part, day: int):
    """Submit the solution of a given puzzle."""

    with open(get_day_path(day) / "input.txt") as f:
        solution = get_solution(part, day, f.read())

        if solution == None:
            click.echo("Nothing to submit")
            return

        aocd_submit(solution, part=part, day=day)
