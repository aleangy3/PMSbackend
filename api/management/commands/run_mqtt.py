import json

import paho.mqtt.client as mqtt
from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import ChargingRequest, ParkingSpot


class Command(BaseCommand):
    help = "Start MQTT client to listen for MWBot status updates"

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            self.stdout.write(self.style.SUCCESS(f"Connected to MQTT Broker (rc={rc})"))
            client.subscribe("mwbot/status/#")

        def on_message(client, userdata, msg):
            payload = json.loads(msg.payload.decode())
            bot_id = payload.get("botID")
            status = payload.get("status")
            spot_id = payload.get("spotID")

            try:
                charging_request = ChargingRequest.objects.filter(
                    bot_id=bot_id, spot_id=spot_id
                ).first()
                charging_request.status = status
                charging_request.save()
                if status == "completed":
                    parking_spot = ParkingSpot.objects.get(id=spot_id)
                    parking_spot.is_occupied = False
                    parking_spot.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Spot {spot_id} is now free for use."
                        )
                    )
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated Charging Request {charging_request.id} → Status: {status}"
                    )
                )
            except ChargingRequest.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(
                        f"No Charging Request found for MWbot ID {bot_id}"
                    )
                )

        mqtt_client = mqtt.Client()
        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = on_message
        mqtt_client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)
        mqtt_client.loop_forever()
