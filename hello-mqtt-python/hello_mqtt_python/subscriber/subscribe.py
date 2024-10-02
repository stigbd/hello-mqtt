import click
from click import ClickException
import paho.mqtt.client as paho


def on_message(client, userdata, message):
    print(f'Received message "{message.payload.decode()}" on topic "{message.topic}"')


@click.command()
@click.option(
    "--broker",
    "-b",
    required=False,
    help="MQTT broker to connect to",
    default="localhost",
)
@click.option("--topic", "-t", required=True, help="MQTT topic to subscribe to")
def subscribe(broker, topic):
    """Subscribe to an MQTT topic"""
    client = paho.Client()
    client.on_message = on_message

    try:
        client.connect(broker, 1883, 60)
    except ConnectionRefusedError as e:
        raise ClickException(f"Failed to connect to broker: {e}")

    client.subscribe(topic)
    print(f'Subscribing to topic "{topic}"')

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        print("\nDisconnected from broker")
