##  Apache NiFi Flow – Description du Pipeline de Kefta Group

Ce flow NiFi traite les données provenant de Kafka et les redirige vers deux destinations :
-  Elasticsearch (pour la visualisation en temps réel)
-  Google Cloud Storage (GCS) au format Parquet, pour analyse dans BigQuery

---

###  Étapes du flow

1. ### `ConsumeKafka_2_6`
   - **Source** : Consomme des messages JSON depuis un topic Kafka
   - **Sortie** : Envoie les messages vers le `TravelProcessor`

2. ### `TravelProcessor` (Processor personnalisé)
   - **But** : Calcul de la distance, enrichissement des données
   - **Sortie `SUCCESS`** : Données enrichies envoyées vers `JoltTransformJSON`
   - **Sortie `FAILURE`** : Gestion des erreurs (debug ou log)

3. ### `JoltTransformJSON`
   - **But** : Transformation du JSON selon une spécification JOLT (changement de format/structure)
   - **Sortie `SUCCESS`** : Envoi vers `MergeRecord`

4. ### `MergeRecord`
   - **But** : Regroupe les fichiers par lot de X records (ex : 10 000) pour écrire en batch
   - **Sortie `MERGED`** : Passe à l’étape suivante `UpdateAttribute`

5. ### `UpdateAttribute`
   - **But** : Renomme dynamiquement les fichiers avec un timestamp pour GCS (ex: `${now():format("yyyy-MM-dd'T'HH:mm:ss'Z'", "GMT")}.parquet`)
   - **Sortie `SUCCESS`** : Vers `PutGCSObject`

6. ### `PutGCSObject`
   - **But** : Envoie les fichiers `.parquet` dans un bucket Google Cloud Storage (GCS)
   - **Sortie `FAILURE`** : Peut être utilisée pour alerter ou journaliser

---

###  Branche parallèle vers Elasticsearch

Depuis `JoltTransformJSON` :

- Les données sont aussi envoyées vers `PutElasticsearchHttp`
  - **But** : Indexer les données dans Elasticsearch
  - **Utilisé par Kibana** pour créer des dashboards en temps réel
  - **Sortie `failure, retry`** : Gestion des erreurs avec politique de retry

---

###  Résumé

| Source     | Traitement principal         | Destinations finales            |
|------------|------------------------------|----------------------------------|
| Kafka      | Calcul, transformation, merge| Elasticsearch & Google Cloud Storage |

---

Ce flow permet un **traitement temps réel** avec **visualisation** (Kibana) et **stockage analytique** (BigQuery via GCS).
