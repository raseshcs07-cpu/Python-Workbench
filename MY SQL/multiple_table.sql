-- joining three tables, ""joining ""

-- CREATE DATABASE
-- CREATE DATABASE magazine_db;

-- SELECT DATABASE
-- USE magazine_db;

-- TABLE 1: CUSTOMERS
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    address VARCHAR(200)
);

INSERT INTO customers VALUES
(1, 'John Smith', '123 Main Street'),
(2, 'Jane Doe', '456 Park Avenue'),
(3, 'Joe Schmo', '798 Broadway'),
(4, 'Alice Brown', '12 Lake Road'),
(5, 'Robert Wilson', '89 Hill Street');


-- TABLE 2: SUBSCRIPTIONS
CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY,
    description VARCHAR(100),
    price_per_month INT,
    subscription_length INT
);

INSERT INTO subscriptions VALUES
(1, 'Politics Magazine', 5, 12),
(2, 'Fashion Magazine', 10, 6),
(3, 'Sports Magazine', 7, 3),
(4, 'Technology Magazine', 15, 12),
(5, 'Science Magazine', 12, 6);


-- TABLE 3: ORDERS
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    subscription_id INT,
    purchase_date DATE,

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY (subscription_id)
    REFERENCES subscriptions(subscription_id)
);

INSERT INTO orders VALUES
(1, 2, 3, '2017-01-01'),
(2, 2, 2, '2017-01-01'),
(3, 3, 1, '2017-01-01'),
(4, 4, 5, '2017-02-15'),
(5, 5, 4, '2017-03-20');


-- DISPLAY ALL TABLES
SELECT * FROM customers;
SELECT * FROM subscriptions;
SELECT * FROM orders;




-- Q1: Customer name and order ID
SELECT customers.customer_name, orders.order_id
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;


-- Q2: Order ID and magazine description
SELECT orders.order_id, subscriptions.description
FROM orders
JOIN subscriptions
ON orders.subscription_id = subscriptions.subscription_id;


-- Q3: Customer name and magazine description
SELECT customers.customer_name, subscriptions.description
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN subscriptions
ON orders.subscription_id = subscriptions.subscription_id;


SELECT * 
FROM orders
JOIN customers
 ON orders.customer_id = customers.customer_id;
-- The second line specifies the first table that we want to look in, orders
-- The third line uses JOIN to say that we want to combine information from orders with customers.
-- The fourth line tells us how to combine the two tables. We want to match orders table’s customer_id column with customers table’s customer_id column.


SELECT * 
FROM orders
JOIN subscriptions
 ON orders.subscription_id = subscriptions.subscription_id;
 WHERE subscriptions.description = 'Fashion Magazine';


SELECT COUNT(*)
FROM orders;

SELECT COUNT(*)
FROM subscriptions;

-- SELECT COUNT(*)
-- FROM newspaper
-- JOIN online
-- 	ON newspaper.subscriber_id = online.subscriber_id;

-- SELECT *
-- FROM table1
-- LEFT JOIN table2
--   ON table1.c2 = table2.c2;

-- Suppose we want to know how many users subscribe to the print newspaper, but not to the online.
SELECT *
FROM newspaper
LEFT JOIN online
  ON newspaper.subscriber_id = online.subscriber_id;

-- This will select rows where there was no corresponding row from the online table.
SELECT *
FROM newspaper
LEFT JOIN online
  ON newspaper.subscriber_id = online.subscriber_id;
  WHERE online.subscriber_id IS NULL


-- order_id for orders
-- subscription_id for subscriptions
-- customer_id for customers
-- these are primary key

-- Primary keys have a few requirements:
-- None of the values can be NULL.
-- Each value must be unique (i.e., you can’t have two customers with the same customer_id in the customers table).
-- A table can not have more than one primary key column.

-- When the primary key for one table appears in a different table, it is called a 
-- foreign key
-- Preview: Docs Loading link description.

-- So customer_id is a primary key when it appears in customers, but a foreign key when it appears in orders.

SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id



-- Cross Join
-- 4 customers × 3 subscription types = 12 customer-subscription combinations

SELECT customers.customer_name, 
  subscriptions.description 
FROM customers 
CROSS JOIN subscriptions; 

SELECT customers.customer_name, 
  subscriptions.description,
  subscriptions.price_per_month 
FROM customers 
CROSS JOIN subscriptions
WHERE subscriptions.price_per_month < 15; 

SELECT subscriptions.description,
  COUNT(*) AS possible_customers
FROM customers
CROSS JOIN subscriptions
WHERE subscriptions.price_per_month < 15
GROUP BY subscriptions.description;


SELECT *
FROM newspaper
UNION
SELECT *
FROM online;


WITH checkpoint_one_query AS (
    SELECT
        customer_id,
        COUNT(subscription_id) AS subscriptions
    FROM orders
    GROUP BY customer_id
)

SELECT
    customers.customer_name,
    checkpoint_one_query.subscriptions
FROM customers
JOIN checkpoint_one_query
    ON customers.customer_id = checkpoint_one_query.customer_id;
