USE the_darth_star; -- Database to use

-- Create a table to store user information
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY, -- A unique identifier for each user
username VARCHAR(100) NOT NULL, -- User's name (required)
password_hash VARCHAR(255) NOT NULL, -- Password stored as a hash for security
email VARCHAR(100) UNIQUE NOT NULL, -- User's email address, must be unique
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Create a table to store blog posts
CREATE TABLE IF NOT EXISTS blogs (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL, -- Title of the blog post
content TEXT NOT NULL, -- Main content of the blog
author_id INT, -- ID of the user who wrote the blog
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (author_id) REFERENCES users(id) -- Link the author to a user
);

-- Create a table that stores product categories
CREATE TABLE IF NOT EXISTS categories (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, -- Category type
    description TEXT -- Short description of cartegory
);

-- Create a table for e-commerce products
CREATE TABLE IF NOT EXISTS products (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL, -- Product name
description TEXT, -- Description of the product
price DECIMAL(10, 2) NOT NULL, -- Product price, e.g., 19.99
stock INT DEFAULT 0, -- Stock quantity of the product
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store customer orders
CREATE TABLE IF NOT EXISTS orders (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
product_id INT,
quantity INT DEFAULT 1,
total_price DECIMAL(10, 2) NOT NULL,
status VARCHAR(50) DEFAULT 'pending', -- New status column
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create a table for comments on blog posts
CREATE TABLE IF NOT EXISTS comments (
id INT AUTO_INCREMENT PRIMARY KEY,
blog_id INT, -- ID of the blog post being commented on
user_id INT, -- ID of the user who made the comment
content TEXT NOT NULL, -- Content of the comment
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (blog_id) REFERENCES blogs(id), -- Link to the blog post
FOREIGN KEY (user_id) REFERENCES users(id) -- Link to the user who commented
);

-- Create a table for e-commerce products
CREATE TABLE IF NOT EXISTS products (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL, -- Product name
description TEXT, -- Description of the product
price DECIMAL(10, 2) NOT NULL, -- Product price, e.g., 19.99
stock INT DEFAULT 0, -- Stock quantity of the product
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS articles (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL, -- tITLE OF ARTICLE
content TEXT NOT NULL,
author VARCHAR(100) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
