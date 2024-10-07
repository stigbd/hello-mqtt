"""Subscribe to an MQTT topic."""

from typing import Any

import click
import paho.mqtt.client as paho
from click import ClickException


def on_message(client: paho.Client, userdata: Any, message: paho.MQTTMessage) -> None:  # noqa: ARG001
    """Handle incoming messages."""
    click.echo(f'Received message "{message.payload.decode()}" on topic "{message.topic}"')


@click.command()
@click.option(
    "--broker",
    "-b",
    required=False,
    help="MQTT broker to connect to",
    default="localhost",
    show_default=True,
)
@click.option("--topic", "-t", required=True, help="MQTT topic to subscribe to")
def subscribe(broker: str, topic: str) -> None:
    """Subscribe to an MQTT topic."""
    client = paho.Client()
    client.on_message = on_message

    try:
        client.connect(broker, 1883, 60)
    except ConnectionRefusedError as e:
        msg = f"Failed to connect to broker: {e}"
        raise ClickException(msg) from e

    client.subscribe(topic)
    click.echo(f'Subscribing to topic "{topic}"')

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        click.echo("\nDisconnected from broker")
