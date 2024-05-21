# Dairy Farmer App Data Platform

The Dairy Farmer App Data Platform is an end-to-end solution for dairy farm management, leveraging modern data engineering and analytics tools. It includes scripts for generating sample data, orchestrating the ETL process, and visualizing the data for analysis and reporting. The platform utilizes Docker for containerization, allowing easy deployment and scaling. Data generation and ETL processes are orchestrated using Docker Compose, while database management is handled by MySQL and MongoDB. Data visualization and analysis are facilitated by Metabase. The ETL process includes data modeling using dbt (data build tool) to transform and organize data in a structured manner.

## Features

- Generates mock data for dairy farmers, farm activities, inventory, and user activity
- Orchestrates the ETL process to extract data from multiple sources, transform it, and load it into a data warehouse
- Provides visualization and analysis capabilities for dairy farm data using Metabase

## Directory Structure

```
dairy-farmerapp-data-platform/
├── data_generator/
│   ├── generate_mysql_data.py
│   ├── generate_mongo_data.py
│   ├── generate_user_activity_data.py
├── etl_pipeline/
│   ├── scripts/
│   │   ├── extract_transform_load.py
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── staging_mysql/
│   │   │   │   ├── stg_farmers.sql
│   │   │   │   ├── stg_animal_records.sql
│   │   │   │   ├── stg_activity_tracking.sql
│   │   │   │   ├── stg_inventory.sql
│   │   │   ├── staging_mongo/
│   │   │   │   ├── stg_user_activity.sql
│   ├── dbt_project.yml
├── docker-scripts/
│   ├── Docker_dbt
│   ├── Docker_database_generator
├── docker-compose.yml
├── README.md
```

## Setup Instructions

1. **Clone the Repository**: `git clone https://github.com/your-username/dairy-farmerapp-data-platform.git`
2. **Run Docker Compose**: `docker-compose up`
3. **Access Generated Data**: Mock data will be generated and stored in the respective databases (MySQL and MongoDB).
4. **Run ETL Pipeline**:
   - Once the containers are up and running, execute the ETL script `extract_transform_load.py` to orchestrate the ETL process.
5. **Connecting to Metabase**:
   - Open a web browser and go to `http://localhost:3000` to access Metabase.
   - Follow the on-screen instructions to set up Metabase and connect it to the data warehouse where your data is stored.
   - Use the provided connection details to connect Metabase to the data warehouse and start visualizing your data.

## Usage

- `generate_mysql_data.py`: Generates mock data for dairy farmers, farm activities, and inventory and inserts them into a MySQL database.
- `generate_mongo_data.py`: Generates mock data for user activity and inserts them into a MongoDB database.
- `generate_user_activity_data.py`: Simulates user activity data similar to Google Analytics and inserts them into a MongoDB database.
- `extract_transform_load.py`: Orchestrates the ETL process by extracting data from sources, transforming it, and loading it into a data warehouse.

## Contributing

Contributions to the Dairy Farmer App Data Platform project are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
