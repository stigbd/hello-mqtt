"""Publish mouse events to an MQTT broker."""

import click
import paho.mqtt.client as paho
from click import ClickException
from pynput import mouse


@click.command
@click.option(
    "--broker",
    "-b",
    required=False,
    help="MQTT broker to connect to",
    default="localhost",
    show_default=True,
)
@click.option(
    "--topic",
    "-t",
    required=False,
    help="MQTT topic to publish to",
    default="mouse/events",
    show_default=True,
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose mode",
)
def publish_mouse_events(topic: str, broker: str, verbose: bool) -> None:  # noqa: FBT001
    """Publish mouse events to an MQTT broker."""
    client = paho.Client()

    try:
        client.connect(broker, 1883, 60)
    except ConnectionRefusedError as e:
        msg = f"Failed to connect to broker: {e}"
        raise ClickException(msg) from e

    # Montior mouse events
    mouse_events = MouseEvents(client)
    mouse_events.topic = topic
    mouse_events.verbose = verbose

    # Collect events until released
    with mouse.Listener(
        on_move=mouse_events.on_move, on_click=mouse_events.on_click, on_scroll=mouse_events.on_scroll
    ) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass
        finally:
            click.echo("\nStopped listening to mouse events")
            listener.stop()
            client.disconnect()


class MouseEvents:
    """Mouse events publisher."""

    topic: str = "mouse/events"
    client: paho.Client
    verbose: bool = False

    def __init__(self, client: paho.Client) -> None:
        """Initialize the MouseEvents class."""
        self.client = client

    def on_move(self, x: int, y: int) -> None:
        """Handle mouse move events."""
        click.echo(f"Mouse moved to ({x}, {y})") if self.verbose else None
        _topic = self.topic + "/moved-to"
        self.client.publish(_topic, f"Mouse moved to ({x}, {y})")

    def on_scroll(self, x: int, y: int, dx: int, dy: int) -> None:
        """Handle mouse scroll events."""
        click.echo(f"Mouse scrolled at ({x}, {y})({dx}, {dy})") if self.verbose else None
        _topic = self.topic + "/scrolled"
        self.client.publish(_topic, f"Mouse scrolled at ({x}, {y})({dx}, {dy})")

    def on_click(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:  # noqa: FBT001
        """Handle mouse click events."""
        action = "Pressed" if pressed else "Released"
        _topic = self.topic + "/clicked"
        click.echo(f"{action} at ({x}, {y}) with {button}") if self.verbose else None
        self.client.publish(_topic, f"{action} at ({x}, {y}) with {button}")
