"""CLI module for the hello-mqtt-python package."""

import click

from .mouse_events_publisher import publish_mouse_events
from .publisher import publish
from .subscriber import subscribe


@click.group()
@click.version_option()
def cli() -> None:
    """A simple MQTT publisher/subscriber CLI."""  # noqa: D401


cli.add_command(publish)
cli.add_command(subscribe)
cli.add_command(publish_mouse_events)
