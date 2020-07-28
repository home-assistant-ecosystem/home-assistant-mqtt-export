"""
MQTT publisher for all Home Assistant states.

Copyright (c) 2016-2020 Fabian Affolter <fabian@affolter-engineering.ch>
Licensed under MIT

For questions and issues please use https://community.home-assistant.io

To use this component you will need to add something like the
following to your configuration.yaml file.

mqtt_export:
  publish_topic: "home/states"
"""
import json

import homeassistant.loader as loader
from homeassistant.components import mqtt #Updated 7/28/2020 - DB
from homeassistant.const import STATE_UNKNOWN, EVENT_STATE_CHANGED
from homeassistant.helpers.json import JSONEncoder # Updated 7/28/2020 DB

DOMAIN = "mqtt_export"
DEPENDENCIES = ["mqtt"]

DEFAULT_TOPIC = "home-assistant/states"
PAYLOAD = None


def setup(hass, config):
    """Set up the MQTT export component."""
    #mqtt = loader.get_component("mqtt") # Commented Out as per module import above 7/28/2020 DB
    pub_topic = config[DOMAIN].get("publish_topic", DEFAULT_TOPIC)

    global PAYLOAD
    PAYLOAD = dict(states=None, details=None)

    # Add the configuration
    PAYLOAD["details"] = hass.config.as_dict()

    def mqtt_event_listener(event):
        """Listen for new messages on the bus and send data to MQTT."""
        state = event.data.get("new_state")
        if state is None or state.state in (STATE_UNKNOWN, ""):
            return None

        PAYLOAD["states"] = hass.states.all()

        payload = json.dumps(PAYLOAD, cls=JSONEncoder)
        mqtt.publish(hass, pub_topic, payload)

    hass.bus.listen(EVENT_STATE_CHANGED, mqtt_event_listener)

    return True

