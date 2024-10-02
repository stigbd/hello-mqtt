# hello-mqtt-mqtt5

This is a simple example of using the MQTT protocol with the MQTT 5.0 version.

## Running the server

The server will pick up the configuration from the `config/mosquitto.conf` file. It is set up with unauthenticated access.

To start the server and inspect the logs, run the following commands:

```bash
% docker compose up -d
% docker compose logs -f
```

To stop the server, run the following command from a different terminal:

```bash
% docker compose down
```

References:
<https://mosquitto.org/documentation/authentication-methods/>
 <https://github.com/sukesh-ak/setup-mosquitto-with-docker>
