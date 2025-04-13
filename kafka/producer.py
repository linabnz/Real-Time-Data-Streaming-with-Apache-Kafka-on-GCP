# -*- coding: utf-8 -*-

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer
message = {
   "data":[
      {
         "confort":"standard",
         "prix_base_per_km":2,
         "properties-client":{
            "logitude":6.3522,
            "latitude":23.8566,
            "nomclient":"Sharon",
            "telephoneClient":"060786575"
         },
         "properties-driver":{
            "logitude":4.7038,
            "latitude":24.4168,
            "nomDriver":"Gaetan",
            "telephoneDriver":"0760786575"
         }
      }
   ]
}


# Envoi du message au topic 'test'
producer.send('kefta', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer (avec noms et zones géographiques très éloignées)
message = {
   "data": [
      {
         "confort": "low",
         "prix_base_per_km": 2,
         "properties-client": {
            "logitude": -74.0060,    # New York, USA
            "latitude": 40.7128,
            "nomclient": "Alicia",
            "telephoneClient": "0611223344"
         },
         "properties-driver": {
            "logitude": 151.2093,    # Sydney, Australie
            "latitude": -33.8688,
            "nomDriver": "Takeshi",
            "telephoneDriver": "0799887766"
         }
      }
   ]
}

# Envoi du message au topic 'kefta'
producer.send('kefta', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer
message = {
   "data": [
      {
         "confort": "standard",
         "prix_base_per_km": 2,
         "properties-client": {
            "logitude": 31.2357,     # Le Caire, Égypte
            "latitude": 30.0444,
            "nomclient": "Fatima",
            "telephoneClient": "0622334455"
         },
         "properties-driver": {
            "logitude": -122.4194,   # San Francisco, USA
            "latitude": 37.7749,
            "nomDriver": "Carlos",
            "telephoneDriver": "0788991122"
         }
      }
   ]
}

# Envoi du message au topic 'kefta'
producer.send('kefta', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer
message = {
   "data": [
      {
         "confort": "low",
         "prix_base_per_km": 2,
         "properties-client": {
            "logitude": -58.3816,     # Buenos Aires, Argentine
            "latitude": -34.6037,
            "nomclient": "Lucia",
            "telephoneClient": "0633445566"
         },
         "properties-driver": {
            "logitude": 139.6917,     # Tokyo, Japon
            "latitude": 35.6895,
            "nomDriver": "Hiroshi",
            "telephoneDriver": "0777888999"
         }
      }
   ]
}

# Envoi du message au topic 'kefta'
producer.send('kefta', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

from kafka import KafkaProducer
import json
import random

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Liste de zones géographiques simulées (latitude, longitude)
geo_zones = [
    (48.8566, 2.3522), (40.7128, -74.0060), (35.6895, 139.6917),
    (-33.8688, 151.2093), (55.7558, 37.6173), (19.0760, 72.8777),
    (-23.5505, -46.6333), (34.0522, -118.2437), (51.5074, -0.1278),
    (1.3521, 103.8198), (41.9028, 12.4964), (52.5200, 13.4050),
    (31.2304, 121.4737), (37.7749, -122.4194), (39.9042, 116.4074),
    (6.5244, 3.3792), (13.7563, 100.5018), (50.8503, 4.3517),
    (45.4654, 9.1859), (25.276987, 55.296249), (43.6532, -79.3832),
    (-34.6037, -58.3816), (59.3293, 18.0686), (35.6762, 139.6503),
    (60.1695, 24.9354), (21.0285, 105.8542), (12.9716, 77.5946),
    (38.9072, -77.0369), (30.0444, 31.2357), (33.5731, -7.5898),
    (-1.2921, 36.8219), (37.9838, 23.7275)
]


# Générer et envoyer 50 messages
for i in range(50):
    lat_client, lon_client = random.choice(geo_zones)
    lat_driver, lon_driver = random.choice(geo_zones)

    message = {
        "data": [
            {
                "confort": random.choice(['standard', 'high', 'low']),
                "prix_base_per_km": 2,
                "properties-client": {
                    "logitude": round(lon_client, 4),
                    "latitude": round(lat_client, 4),
                    "nomclient": f"Client{i}",
                    "telephoneClient": f"06000000{i}"
                },
                "properties-driver": {
                    "logitude": round(lon_driver, 4),
                    "latitude": round(lat_driver, 4),
                    "nomDriver": f"Driver{i}",
                    "telephoneDriver": f"07000000{i}"
                }
            }
        ]
    }

    # Envoi du message au topic 'kefta'
    producer.send('kefta', value=message)

# Attente de la livraison de tous les messages
producer.flush()
print("Messages envoyés avec succès.")

pip install Faker

import json
import random
from faker import Faker
from kafka import KafkaProducer
import time

faker = Faker()

producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

confort_options = ['standard', 'high', 'low']

for _ in range(20):
    message = {
        "data": [
            {
                "confort": random.choice(confort_options),
                "prix_base_per_km": round(random.uniform(1.0, 3.5), 2),
                "properties-client": {
                    "logitude": round(random.uniform(-180.0, 180.0), 4),
                    "latitude": round(random.uniform(-90.0, 90.0), 4),
                    "nomclient": faker.first_name(),
                    "telephoneClient": "060786575"
                },
                "properties-driver": {
                    "logitude": round(random.uniform(-180.0, 180.0), 4),
                    "latitude": round(random.uniform(-90.0, 90.0), 4),
                    "nomDriver": faker.first_name(),
                    "telephoneDriver": "0760786575"
                }
            }
        ]
    }


    producer.send('kefta', value=message)
    print(f"Message envoyé : {message}")
    time.sleep(0.5)

producer.flush()

print("20 messages envoyés avec succès.")

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "Benze",
    group_id="group",
    bootstrap_servers="kfakasda.eastus.cloudapp.azure.com:9092",
    session_timeout_ms=60000
)

for msg in consumer:
    print(msg)

import requests
from datetime import datetime

# création du Document JSON à indexer
document_to_index = {
  "data": [
    {
      "confort": "standard",
      "prix_base_per_km": 2,
      "properties-client": {
        "longitude": 2.3522,
        "latitude": 48.8566,
        "nomClient": "FALL",
        "telephoneClient": "060786575"
      },
      "properties-driver": {
        "longitude": 3.7038,
        "latitude": 40.4168,
        "nomDriver": "DIOP",
        "telephoneDriver": "070786575"
      }
    }
  ]
}

# Nom de l'index
index_name = "kefta"

# URL Elasticsearch avec authentification basique
url = "http://hostname:9200/" + index_name + "/_doc"
url = "http://clustersdaelatsic.eastus.cloudapp.azure.com:9200/" + index_name + "/_doc"

# Headers JSON
headers = {'Content-Type': 'application/json'}

# Authentification Elasticsearch (elastic / changeme)
auth = ('elastic', 'changeme')

# Indexation du document
response = requests.post(url, json=document_to_index, headers=headers, auth=auth)
response.raise_for_status()

# Affichage du statut de la requête et de la réponse
print("Statut de la requête:", response.status_code)
print("Réponse de Elasticsearch:",response.text)

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='broker:https://127.0.0.1:8443/nifi/',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer
message = {"location":"14.76, -14.76",
 "typeProduit":"coca",
 "price":100
}

# Envoi du message au topic 'test'
producer.send('sorb', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers="kfakasda.eastus.cloudapp.azure.com:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Message JSON à envoyer
message = {"location":"14.76, -14.76","typeProduit":"coca","price":100}

# Envoi du message au topic 'test'
producer.send("kb9", value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")

from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Message JSON à envoyer
message = {"location":"14.76, -14.76","typeProduit":"coca","price":100}


# Envoi du message au topic 'test'
producer.send('kb9', value=message)

# Attente de la livraison de tous les messages
producer.flush()

print("Message envoyé avec succès.")