-- Create a table to store user information
CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY, -- A unique identifier for each user
username VARCHAR(100) NOT NULL, -- User's name (required)
password_hash VARCHAR(255) NOT NULL, -- Password stored as a hash for security
email VARCHAR(100) UNIQUE NOT NULL, -- User's email address, must be unique
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Create a table to store blog posts
CREATE TABLE blogs (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL, -- Title of the blog post
content TEXT NOT NULL, -- Main content of the blog
author_id INT, -- ID of the user who wrote the blog
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (author_id) REFERENCES users(id) -- Link the author to a user
);

-- Create a table for e-commerce products
CREATE TABLE products (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL, -- Product name
description TEXT, -- Description of the product
price DECIMAL(10, 2) NOT NULL, -- Product price, e.g., 19.99
stock INT DEFAULT 0, -- Stock quantity of the product
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store customer orders
CREATE TABLE orders (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT, -- ID of the user placing the order
product_id INT, -- ID of the product being purchased
quantity INT DEFAULT 1, -- Number of units ordered
total_price DECIMAL(10, 2) NOT NULL, -- Total price of the order
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(id), -- Link to the user who placed the order
FOREIGN KEY (product_id) REFERENCES products(id) -- Link to the product ordered
);

-- Create a table for comments on blog posts
CREATE TABLE comments (
id INT AUTO_INCREMENT PRIMARY KEY,
blog_id INT, -- ID of the blog post being commented on
user_id INT, -- ID of the user who made the comment
content TEXT NOT NULL, -- Content of the comment
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (blog_id) REFERENCES blogs(id), -- Link to the blog post
FOREIGN KEY (user_id) REFERENCES users(id) -- Link to the user who commented
);
