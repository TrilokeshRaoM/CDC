This repo has information on how to setup MSSQL, Zookeeper, Kafka, Kafka Connect, Kafka UI, and Debezium in the Docker environment to test CDC on MSSQL via. Kafka.

# Instructions

## Docker
- Navigate to the folder of the docker-compose.yml file location and run "docker-compose up -d"
- Open Docker desktop and check if all the containers are running

### SQL Server
- Download Azure Data Studio
- Connect to the server based on the Config information you provided
![SettingupSQLServer](images/AzureDSExampleSetup.png)
- Create a new DB and Table to check CDC.
- Enable CDC for that table
- Check if the CDC job is running on SQL Server Agent, by right clicking on the connection > Manage > SQL Agent
- Make some inserts into the table and check if it appears on the CDC table.
- You can check for the name of the CDC table if not defined by: SELECT * FROM sys.tables; Please note the schema for the table will be cdc.<table name>

### Kafka connect
- Please follow the instructions on this page - https://debezium.io/documentation/reference/1.9/connectors/sqlserver.html#sqlserver-deploying-a-connector
- Get into the Kafka Connect docker container and check in /kafka/connect if the needed plug-in is present. If not please download from the above link and place it in Kafka Connect (Make sure you check the documentation for the correct version of the Docker image used).
- Now configure the connector by using CURL or REST request: https://debezium.io/documentation/reference/1.9/connectors/sqlserver.html#sqlserver-example-configuration
Example: curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{
  "name": "mysql-cdc-test-connector-1",
  "config": {
    "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
    "database.hostname": "mssql",
    "database.port": "1433",
    "database.user": "sa",
    "database.password": "My#mssqlpassw0rd",
    "database.dbname": "cdc_test",
    "database.server.name": "my_cdc_test",
    "database.history.kafka.bootstrap.servers": "kafka:9092",
    "database.history.kafka.topic": "schema-changes.cdc_test",
    "database.encrypt":"false"
  }
}'
- Restart the connector using the help of this: https://kafka.apache.org/documentation/#connect_rest
POST: http://localhost:8083/connectors/mysql-cdc-test-connector-1/restart?includeTasks=true
- Check connections
GET: http://localhost:8083/connectors
- Please check the logs of Kafka Connect to see if the CDC information is coming into the topic
- You can also use the Kafka UI at location localhost:8080 to check the details.

- Check tasks status for a connection
GET: http://localhost:8083/connectors/mysql-cdc-test-connector-1/tasks/0/status
- Delete a connection
DELETE: http://localhost:8083/connectors/mysql-cdc-test-connector-1


