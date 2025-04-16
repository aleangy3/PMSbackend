import json
import random
import time

import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Starts the Dummy MWbot for handling parking spot dispatches"

    BOT_ID = 1
    MQTT_BROKER = "localhost"
    MQTT_PORT = 1883

    def handle(self, *args, **kwargs):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.MQTT_BROKER, self.MQTT_PORT, 60)
        self.client.loop_forever()  # Keeps running and listening for messages

    def on_connect(self, client, userdata, flags, rc):
        print(f"Dummy MWbot connected to MQTT Broker (rc={rc})")
        client.subscribe(f"mwbot/dispatch/{self.BOT_ID}")

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        spot_id = payload.get("spotID")
        action = payload.get("action")

        if action == "dispatch":
            print(f"MWbot received dispatch command for Spot {spot_id}")
            self.simulate_charging_process(spot_id)  # Now calling correctly

    def simulate_charging_process(self, spot_id):
        statuses = ["moving", "charging", "completed"]
        for status in statuses:
            time.sleep(random.randint(2, 5))  # Simulate movement and charging process
            message = json.dumps(
                {"botID": self.BOT_ID, "status": status, "spotID": spot_id}
            )
            self.client.publish(f"mwbot/status/{self.BOT_ID}", message)
            print(f"MWbot updated status: {status}")
