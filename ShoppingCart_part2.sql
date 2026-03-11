CREATE DATABASE grocery_store;

USE grocery_store;

CREATE TABLE items (
    id INT PRIMARY KEY,
    itemname VARCHAR(50),
    costperitem FLOAT,
    quantity INT
);

INSERT INTO items VALUES
(1,'Biscuits',12.50,10),
(2,'Cereals',10,15),
(3,'Chicken',15,50),
(4,'Coffee',5.50,18),
(5,'Milk',3.50,20);


CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    address VARCHAR(200),
    distance INT,
    total_amount FLOAT
);



