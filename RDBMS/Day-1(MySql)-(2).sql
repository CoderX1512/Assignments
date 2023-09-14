CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT,
    mfgDate DATE,
    expDate DATE,
    brand VARCHAR(50)
);

INSERT INTO product(product_name, price, mfgDate, expDate, brand)
VALUES ('A', 1000, '2000-01-02', '2001-02-03', 'Dell');

INSERT INTO product(product_name, price, mfgDate, expDate, brand)
VALUES ('B', 2000, '2000-02-03', '2001-03-04', 'HP');

INSERT INTO product(product_name, price, mfgDate, expDate, brand)
VALUES ('C', 3000, '2000-03-04', '2001-04-05', 'Sony');

INSERT INTO product(product_name, price, mfgDate, expDate, brand)
VALUES ('D', 4000, '2000-04-05', '2001-05-06', 'ASUS');

INSERT INTO product(product_name, price, mfgDate, expDate, brand)
VALUES ('E', 5000, '2000-05-06', '2001-06-07', 'Intel');

SELECT * FROM product;

UPDATE product
SET brand = 'Apple'
WHERE id = 5;

DELETE FROM product
WHERE id = 3;
