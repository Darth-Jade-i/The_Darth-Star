# XERVER - SQL Sub-Directory

## Overview
The `sql` sub-directory contains essential files for managing and setting up the MySQL database used in the project. This database, named **the_darth_star**, is the backbone for storing user data, blog posts, e-commerce products, and related information. Below is a detailed breakdown of the files in this directory and their purpose.

## Files

### 1. `darth_star_db.sh`
This is a simple Bash script that provides an easy way to access the **the_darth_star** database directly. When executed, it prompts for the MySQL password and then connects the user to the MySQL instance as the user `knight`. 

#### Components:
- **MySQL connection command**: Uses the `mysql` command-line tool to connect to the MySQL server using the specified username and database.

#### Usage:
To run this script, execute the following command:
```bash
./darth_star_db.sh
```
You will be prompted for the MySQL password associated with the `knight` user, and then you’ll be logged into the database.

### 2. `setup.sql`
This SQL file contains the necessary SQL commands to create and set up all the tables required for the project. It defines tables to manage user accounts, blog posts, e-commerce products, and customer orders, along with establishing relationships between them using foreign keys.

#### Key Components:
- **Users table**: Stores user credentials and information like username, password (hashed), and email address. Each user gets a unique ID.
- **Blogs table**: Stores blog posts, linking each post to a user (author) via the foreign key `author_id`.
- **Categories table**: Used to categorize products with fields like name and description.
- **Products table**: Contains information on products, including name, description, price, stock, and creation time.
- **Orders table**: Stores customer orders, linking them to both users and products. It also tracks the order status (e.g., pending, completed).
- **Comments table**: Allows users to comment on blog posts, linking comments to both blogs and users.
- **Articles table**: Contains articles with fields like title, content, author, and timestamps for when the article was created and last updated.

#### Usage:
To set up the database schema, this SQL file needs to be executed on the MySQL server. This can be done manually through the MySQL CLI or automatically using the `setup_db.sh` script.

### 3. `setup_db.sh`
This Bash script automates the process of setting up the database by executing the `setup.sql` file. It prompts for the MySQL password and runs the SQL commands from the `setup.sql` file to create the necessary tables and relationships in the database.

#### Components:
- **MySQL command**: The script uses the MySQL command-line tool to execute the SQL file and create tables.
- **Error handling**: The script checks the exit status of the MySQL command and reports whether the database setup was successful or if it failed.

#### Dependencies:
- **MySQL Server**: Make sure that MySQL is installed and running on your system. You can install MySQL using the following command:
```bash
sudo apt-get install mysql-server
```
- **MySQL Client**: The script uses the `mysql` command-line tool, which is part of the MySQL client package. If it’s not installed, use the following command to install it:
```bash
sudo apt-get install mysql-client
```

#### Usage:
To set up the database, run the script by executing the following command:
```bash
./setup_db.sh
```
You will be prompted for the MySQL password, and the script will automatically create the required tables.

### Running the Scripts
1. Ensure MySQL is installed and running on your system.
2. Navigate to the `sql` sub-directory.
3. To manually access the database, use the `darth_star_db.sh` script:
```bash
./darth_star_db.sh
```
4. To automatically set up the database schema, run the `setup_db.sh` script:
```bash
./setup_db.sh
```

Once the tables are set up, you can start inserting and managing data within **the_darth_star** database to support the blog, e-commerce, and user-related functionalities of the project.