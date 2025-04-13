CREATE OR REPLACE MODEL projetkefta.mosefdata.kmeansmodele_projet
OPTIONS (MODEL_TYPE='KMEANS', NUM_CLUSTERS=8) AS
SELECT lon, lat 
FROM projetkefta.mosefdata.kefta2_table;

SELECT * FROM ML.PREDICT(MODEL projetkefta.mosefdata.kmeansmodele_projet,(SELECT  * FROM  projetkefta.mosefdata.kefta2_table))