import click
from click import ClickException
import paho.mqtt.client as paho


@click.command()
@click.option(
    "--broker",
    "-b",
    required=False,
    help="MQTT broker to connect to",
    default="localhost",
)
@click.option("--topic", "-t", required=True, help="MQTT topic to publish to")
@click.option("--message", "-m", required=True, help="Message to publish")
def publish(broker, topic, message):
    """Publish a message to an MQTT broker"""
    client = paho.Client()

    try:
        client.connect(broker, 1883, 60)
    except ConnectionRefusedError as e:
        raise ClickException(f"Failed to connect to broker: {e}")

    client.publish(topic, message)
    client.disconnect()
    print(f'Publishing message "{message}" to topic "{topic}"')
