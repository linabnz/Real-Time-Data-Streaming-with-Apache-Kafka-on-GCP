CREATE OR REPLACE EXTERNAL TABLE  projetkefta.mosefdata.external_table
OPTIONS (
  format = 'NEWLINE_DELIMITED_JSON',
  uris = ['gs://kefta_bucket/keftafolder/*.json']
); 

select *   from  projetkefta.mosefdata.external_table