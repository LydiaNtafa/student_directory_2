from lib.database_connection import DatabaseConnection
from lib.cohorts_repository import CohortsRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/students_directory_2.sql")

# Retrieve all artists
cohorts_repository = CohortsRepository(connection)
print(cohorts_repository.find_cohort_with_students(1))
