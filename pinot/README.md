#### Access Docker Container

````

docker exec -it pinot-controller /bin/bash

````

#### Delete Table and Delete Schema

````

curl -X DELETE "http://localhost:9000/tables/stocks?type=realtime" -H "accept: application/json"

curl -X DELETE "http://localhost:9000/schemas/stocks" -H "accept: application/json"

````

#### Build a Schema From JSON Data

````

docker exec -it pinot-controller bin/pinot-admin.sh JsonToPinotSchema \
  -timeColumnName ts \
  -metrics "volume,price"\
  -dimensions "symbol" \
  -pinotSchemaName=stocks \
  -jsonFile=/data/stocks.json \
  -outputDir=/config
  
````

#### Add our schema

````

docker exec -it pinot-controller bin/pinot-admin.sh AddSchema   \
  -schemaFile /config/stocksschema.json \
  -exec
  
````

#### Add Table via local Linux

````
./access.sh

bin/pinot-admin.sh AddTable -tableConfigFile /config/stockstable.json -schemaFile /config/stocksschema.json -exec

````

#### Add Table Via Swagger UI / Curl

````

curl -X POST "http://localhost:9000/tables" -H "accept: application/json" -H "Content-Type: application/json" -d ""

````


#### Fix a segment

````
curl -X POST "{host}/segments/thermal_REALTIME/{segmentName}/reset"

````

#### Defining Pulsar-Pinot Realtime Table

If you use stream.pulsar.consumer.prop.auto.offset.reset=smallest than it goes back earliest which can be a lot of data.

https://docs.pinot.apache.org/basics/data-import/pinot-stream-ingestion/apache-pulsar

This could be millions or billions of records.  

#### References

* https://github.com/tspannhw/FLiP-Pi-DeltaLake-Thermal
* https://github.com/tspannhw/FLiP-Pi-Thermal
* https://github.com/tspannhw/FLiP-Pi-Thermal/blob/main/cloudsensors.md
* https://docs.pinot.apache.org/integrations/superset
* https://dev.startree.ai/docs/pinot/recipes/pulsar
* https://dev.startree.ai/docs/pinot/recipes/infer-schema-json-data
* https://github.com/startreedata/pinot-recipes/blob/main/recipes/json-nested/README.md
* https://dev.startree.ai/docs/pinot/recipes/pulsar
* https://github.com/startreedata/pinot-recipes/tree/main/recipes/pulsar
* https://github.com/apache/pinot/blob/master/pinot-tools/src/main/resources/examples/stream/airlineStats/airlineStats_schema.json
* https://www.markhneedham.com/blog/2021/06/21/pinot-broker-resource-missing/
* https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations
* https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/show/
* https://github.com/tspannhw/FLiP-SQL
* https://github.com/tspannhw/FLiP-Py-Pi-GasThermal
* https://github.com/tspannhw/FLiPS-Xavier-Sensor

![mastodon](https://github.com/tspannhw/pulsar-thermal-pinot/raw/main/images/timmastodon.jpg)
