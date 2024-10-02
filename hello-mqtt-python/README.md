# hello-mqtt python

This is a simple example of using the MQTT protocol with the Python programming language.

It uses the [Eclipse Paho MQTT Python client library](https://github.com/eclipse/paho.mqtt.python) to interact with the MQTT broker.

The scripts are implemented as a cli using the [Click](https://click.palletsprojects.com/en/8.0.x/) library.

## Pre-requisites

You need to have [rye](https://rye.astral.sh/) installed. If you don't have it, you can install it with the following command:

```bash
% curl -sSf https://rye.astral.sh/get | bash
```

## Running the server

See the [hello-mqtt-mqtt5](../hello-mqtt-mqtt5/README.md) example for instructions on how to run the MQTT broker.

## Running the cli

```bash
% rye sync # to install the dependencies
% rye run hello-mqtt-python --help
```

### Running the subscriber

In a terminal, run the following command to subscribe to the `hello/world` topic:

```bash
% rye run hello-mqtt-python subscribe -t "hello/world"
```

To stop the subscriber, press `Ctrl+C`.

### Running the publisher

In a different terminal, run the following command to publish a message to the `hello/world` topic:

```bash
% rye run hello-mqtt-python publish -t "hello/world" -m "Hello world"
```
