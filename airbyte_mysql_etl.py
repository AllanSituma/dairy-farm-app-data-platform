from pyairbyte import AirbyteClient
import duckdb

# Define Airbyte client and server URL
airbyte_server_url = "http://localhost:8000"  # Update if your Airbyte server is running on a different URL
airbyte_client = AirbyteClient(airbyte_server_url)

# Define MySQL and DuckDB connection configurations
mysql_config = {
    "host": "mysql-db",
    "port": 3306,
    "username": "user",
    "password": "password",
    "database": "web_app_db"
}

duckdb_config = {
    "file": "/app/duckdb/farmer_data.duckdb"
}

# Create MySQL source
source_definition = airbyte_client.get_source_definitions(name="MySQL")
source = airbyte_client.create_source(
    name="My MySQL Source",
    source_definition_id=source_definition.sourceDefinitionId,
    connection_configuration=mysql_config
)

# Create DuckDB destination
destination_definition = airbyte_client.get_destination_definitions(name="DuckDB")
destination = airbyte_client.create_destination(
    name="My DuckDB Destination",
    destination_definition_id=destination_definition.destinationDefinitionId,
    connection_configuration=duckdb_config
)

# Create connection between source and destination
connection = airbyte_client.create_connection(
    name="My MySQL to DuckDB Connection",
    source_id=source.sourceId,
    destination_id=destination.destinationId,
    sync_mode="full_refresh",
    destination_sync_mode="overwrite",
    schema_name="public",
    stream_name="farmers"
)

# Trigger sync
airbyte_client.trigger_connection_sync(connection.connectionId)