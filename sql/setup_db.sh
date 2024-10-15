#!/bin/bash

# Script to set up the database using a SQL file
# Define variables
DB_USER="knight"
DB_NAME="the_darth_star"
SQL_FILE="setup.sql"

# Prompt for MySQL password
echo "Enter MySQL password for user $DB_USER:"
read -s DB_PASSWORD

# Run the SQL file to set up tables in the specified database
mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < "$SQL_FILE"

# Check if the operation was successful
if [ $? -eq 0 ]; then
    echo "Database setup completed successfully."
else
    echo "Failed to set up the database."
fi
