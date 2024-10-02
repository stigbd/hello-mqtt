import click

from .publisher import publish
from .subscriber import subscribe


@click.group()
@click.version_option()
def cli():
    """A simple MQTT publisher/subscriber CLI"""
    pass


cli.add_command(publish)
cli.add_command(subscribe)
