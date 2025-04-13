SELECT
  CENTROID_ID AS cluster,
  confort,
  SUM(prix_travel) AS chiffre_affaire_total
FROM
  ML.PREDICT(
    MODEL projetkefta.mosefdata.kmeansmodele_projet,
    (
      SELECT
        CAST(SPLIT(locationClient, ',')[OFFSET(0)] AS FLOAT64) AS lon,
        CAST(SPLIT(locationClient, ',')[OFFSET(1)] AS FLOAT64) AS lat,
        confort,
        prix_travel
      FROM
        projetkefta.mosefdata.external_table
      WHERE
        locationClient IS NOT NULL
        AND SAFE_CAST(SPLIT(locationClient, ',')[OFFSET(0)] AS FLOAT64) IS NOT NULL
        AND SAFE_CAST(SPLIT(locationClient, ',')[OFFSET(1)] AS FLOAT64) IS NOT NULL
    )
  )
GROUP BY
  cluster, confort
ORDER BY
  cluster, confort;