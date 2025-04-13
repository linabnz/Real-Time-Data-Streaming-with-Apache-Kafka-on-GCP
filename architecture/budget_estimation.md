##  Estimation des Coûts GCP – Cas Réel (Scénario Uber)

### 1. Hypothèses de volumétrie

| **Paramètre**                 | **Valeur estimée**             |
|------------------------------|--------------------------------|
| Trajets Uber par jour        | 20 millions                    |
| Taille moyenne JSON          | 3 Ko                           |
| Volume quotidien             | 60 Go / jour                   |
| Volume mensuel               | 1.8 To (1800 Go)               |
| Format des données           | Fichiers Parquet (GCS)         |
| Outils d’analyse             | BigQuery SQL + ML              |

---

### 2. Coûts estimés par service

| **Service**          | **Coût estimé**                       |
|----------------------|---------------------------------------|
| GCS (stockage)       | 1800 Go × 0.02 $ = **36.00 $**        |
| BigQuery SQL         | 1.8 To × 5 $ = **9.00 $**             |
| BigQuery ML (KMeans) | 10 Go/mois = **0.00 $**               |

** Total mensuel estimé** : **45.00 $** (≈ 42 €)

---

##  Remarques

-  **Stockage GCS Nearline** possible à **0.01 $/Go**, moins cher que le standard.
-  Si le volume monte à **100 millions de trajets/jour** (≈ 300 Go/jour), les coûts sont multipliés par 5 :
  - GCS : **180.00 $ / mois**
  - BigQuery : **45.00 $ / mois**
  - **Total mensuel** : **225.00 $**

---

##  Références officielles

- [Google Cloud Storage Pricing](https://cloud.google.com/storage/pricing)
- [BigQuery Pricing](https://cloud.google.com/bigquery/pricing)
- [BigQuery ML Pricing](https://cloud.google.com/bigquery-ml/pricing)
- [Uber Ride Volume (Statista)](https://www.statista.com/statistics/833743/us-uber-trips/)
