home-assistant-mqtt-export
==========================

Custom MQTT export component for Home Assistant. 


Setup
-----
Put the file ``mqtt_export.py`` file in the folder ``custom_components`` of
your local Home Assistant configuration folder ``.homeassistant``.

Your ``configuration.yaml`` file needs an entry for the component including
the publishing topic (``publish_topic``).

.. code:: yaml

    mqtt_export:
      publish_topic: "home/states"

Sample output
-------------
The component is dumping a lot of information in one MQTT message. 

.. code:: json

    {
       "details":{
          "latitude":46.9432,
          "temperature_unit":"\u00b0C",
          "version":"0.17.0.dev0",
          "location_name":"Test room",
          "time_zone":"Europe/Zurich",
          "longitude":7.6034,
          "components":[
             "recorder",
             "http",
             [...]
             "automation"
          ]
       },
       "states":[
          {
             "attributes":{
                "friendly_name":"Bathroom window",
                "sensor_class":"connectivity"
             },
             "last_updated":"14:10:57 06-04-2016",
             "state":"off",
             "entity_id":"binary_sensor.bathroom_window",
             "last_changed":"14:10:57 06-04-2016"
          },
          {
             "attributes":{
                "next_setting":"18:06:45 06-04-2016",
                "next_rising":"04:56:02 07-04-2016",
                "friendly_name":"Sun",
                "elevation":37.39
             },
             "last_updated":"14:11:30 06-04-2016",
             "state":"above_horizon",
             "entity_id":"sun.sun",
             "last_changed":"14:11:09 06-04-2016"
          },
          [...]
       ]
    }

License
-------
``home-assistant-mqtt-export`` is licensed under MIT, for more details check LICENSE.
