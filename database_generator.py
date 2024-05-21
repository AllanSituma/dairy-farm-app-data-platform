from pymongo import MongoClient
from faker import Faker
import mysql.connector
from datetime import datetime, timedelta
import random

fake = Faker()

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['farmer_app_db']
mongo_farmers_collection = mongo_db['farmers']
mongo_user_activity_collection = mongo_client['user_activity_db']['user_activity']

# MySQL connection
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="web_app_db"
)
mysql_cursor = mysql_connection.cursor()


def generate_farmer_data(num_records):
    farmer_data = []
    for farmer_id in range(1, num_records + 1):
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address()
        farmer_data.append((farmer_id, username, password, email, phone, address))
    return farmer_data


def generate_animal_records_data(num_records):
    animal_data = []
    for farmer_id in range(1, num_records + 1):
        for _ in range(random.randint(1, 5)):  # Generate random number of animals per farmer
            species = fake.random_element(elements=("Cow", "Sheep", "Goat", "Pig"))
            breed = fake.random_element(elements=("Angus", "Holstein", "Duroc", "Suffolk"))
            birthdate = fake.date_between(start_date='-5y', end_date='today')
            sex = fake.random_element(elements=("Male", "Female"))
            animal_data.append((farmer_id, species, breed, birthdate, sex))
    return animal_data


def generate_activity_tracking_data(num_records):
    activity_data = []
    for farmer_id in range(1, num_records + 1):
        for _ in range(random.randint(1, 10)):  # Generate random number of activities per farmer
            animal_id = random.randint(1, 500)  # Assuming 500 animals per farmer
            activity_type = fake.random_element(elements=("Vaccination", "Insemination", "Visit", "Purchase"))
            activity_date = fake.date_time_between(start_date='-1y', end_date='today')
            description = fake.sentence(nb_words=6, variable_nb_words=True)
            activity_data.append((farmer_id, animal_id, activity_type, activity_date, description))
    return activity_data


def generate_admins_data(num_records):
    admin_data = []
    for admin_id in range(1, num_records + 1):
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        # Add other admin details as needed
        admin_data.append((admin_id, username, password, email))
    return admin_data


def generate_purchase_orders_data(num_records):
    purchase_data = []
    for farmer_id in range(1, num_records + 1):
        for _ in range(random.randint(1, 5)):  # Generate random number of orders per farmer
            order_date = fake.date_time_this_year()
            status = fake.random_element(elements=("pending", "fulfilled", "cancelled"))
            # Add other order details as needed
            purchase_data.append((farmer_id, order_date, status))
    return purchase_data


def generate_messages_data(num_records):
    messages_data = []
    for _ in range(num_records * 2):  # Generate messages for both farmers and admins
        sender_id = random.randint(1, num_records)
        recipient_id = random.randint(1, num_records)
        message = fake.text(max_nb_chars=200)
        timestamp = fake.date_time_this_year()
        messages_data.append((sender_id, recipient_id, message, timestamp))
    return messages_data


def generate_visits_data(num_records):
    visits_data = []
    for farmer_id in range(1, num_records + 1):
        for _ in range(random.randint(1, 5)):  # Generate random number of visits per farmer
            visit_date = fake.date_time_this_year()
            purpose = fake.sentence(nb_words=3, variable_nb_words=True)
            duration = random.randint(10, 120)  # minutes
            visits_data.append((farmer_id, visit_date, purpose, duration))
    return visits_data


def insert_farmer_data(data):
    mongo_farmers_collection.insert_many(data)
    print("Farmer data inserted into MongoDB.")


def insert_animal_records_data(data):
    for record in data:
        farmer_id, species, breed, birthdate, sex = record
        # Example MongoDB query to insert data into the Animal Records collection
        mongo_db.animal_records.insert_one({
            'farmer_id': farmer_id,
            'species': species,
            'breed': breed,
            'birthdate': birthdate,
            'sex': sex
        })
    print("Animal records data inserted into MongoDB.")


def insert_activity_tracking_data(data):
    for record in data:
        farmer_id, animal_id, activity_type, activity_date, description = record
        # Example MySQL query to insert data into the Activity Tracking table
        sql = "INSERT INTO activity_tracking (farmer_id, animal_id, activity_type, activity_date, description) VALUES " \
              "(%s,%s,%s,%s)"
        mysql_cursor.execute(sql, (farmer_id, animal_id, activity_type, activity_date, description))
    mysql_connection.commit()
    print("Activity tracking data inserted into MySQL.")


def insert_admins_data(data):
    for record in data:
        admin_id, username, password, email = record
        # Example MySQL query to insert data into the Admins table
        sql = "INSERT INTO admins (admin_id, username, password, email) VALUES (%s, %s, %s, %s)"
        mysql_cursor.execute(sql, (admin_id, username, password, email))
    mysql_connection.commit()
    print("Admins data inserted into MySQL.")


def insert_purchase_orders_data(data):
    for record in data:
        farmer_id, order_date, status = record
        # Example MySQL query to insert data into the Purchase Orders table
        sql = "INSERT INTO purchase_orders (farmer_id, order_date, status) VALUES (%s, %s, %s)"
        mysql_cursor.execute(sql, (farmer_id, order_date, status))
    mysql_connection.commit()
    print("Purchase orders data inserted into MySQL.")


def insert_messages_data(data):
    for record in data:
        sender_id, recipient_id, message, timestamp = record
        # Example MySQL query to insert data into the Messages table
        sql = "INSERT INTO messages (sender_id, recipient_id, message, timestamp) VALUES (%s, %s, %s, %s)"
        mysql_cursor.execute(sql, (sender_id, recipient_id, message, timestamp))
    mysql_connection.commit()
    print("Messages data inserted into MySQL.")


def insert_visits_data(data):
    for record in data:
        farmer_id, visit_date, purpose, duration = record
        # Example MySQL query to insert data into the Visits table
        sql = "INSERT INTO visits (farmer_id, visit_date, purpose, duration) VALUES (%s, %s, %s, %s)"
        mysql_cursor.execute(sql, (farmer_id, visit_date, purpose, duration))
    mysql_connection.commit()
    print("Visits data inserted into MySQL.")


if __name__ == "__main__":
    num_farmers = 100  # Number of farmers
    # Generate farmer app data and insert into MongoDB
    farmer_data = generate_farmer_data(num_farmers)
    insert_farmer_data(farmer_data)
    print("Farmer app data inserted into MongoDB.")

    # Generate animal records data and insert into MongoDB
    animal_data = generate_animal_records_data(num_farmers)
    insert_animal_records_data(animal_data)
    print("Animal records data inserted into MongoDB.")

    # Generate activity tracking data and insert into MySQL
    activity_data = generate_activity_tracking_data(num_farmers)
    insert_activity_tracking_data(activity_data)
    print("Activity tracking data inserted into MySQL.")

    # Generate admins data and insert into MySQL
    admins_data = generate_admins_data(10)  # Adjust number of admins as needed
    insert_admins_data(admins_data)

    # Generate purchase orders data and insert into MySQL
    purchase_orders_data = generate_purchase_orders_data(num_farmers)
    insert_purchase_orders_data(purchase_orders_data)

    # Generate messages data and insert into MySQL
    messages_data = generate_messages_data(num_farmers)
    insert_messages_data(messages_data)

    # Generate visits data and insert into MySQL
    visits_data = generate_visits_data(num_farmers)
    insert_visits_data(visits_data)
