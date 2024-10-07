"""Publish a message to an MQTT broker."""

import click
import paho.mqtt.client as paho
from click import ClickException


@click.command()
@click.option(
    "--broker",
    "-b",
    required=False,
    help="MQTT broker to connect to",
    default="localhost",
    show_default=True,
)
@click.option("--topic", "-t", required=True, help="MQTT topic to publish to")
@click.option("--message", "-m", required=True, help="Message to publish")
def publish(broker: str, topic: str, message: str) -> None:
    """Publish a message to an MQTT broker."""
    client = paho.Client()

    try:
        client.connect(broker, 1883, 60)
    except ConnectionRefusedError as e:
        msg = f"Failed to connect to broker: {e}"
        raise ClickException(msg) from e

    client.publish(topic, message)
    client.disconnect()
    click.echo(f'Publishing message "{message}" to topic "{topic}"')
