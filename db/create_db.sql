CREATE TABLE category
(
	name varchar(50),
	category_id serial PRIMARY KEY
);


CREATE TABLE product
(
	product_id serial PRIMARY KEY,
	name varchar(50),
	description text,
	weight numeric,
	category_id integer REFERENCES category (category_id),
	price numeric,
	image_path text,
	product_size numeric
);

CREATE TABLE client
(
	client_id serial PRIMARY KEY,
	address text,
	phone varchar(50),
	name varchar(50),
	mail varchar(50)
);

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	client_id integer REFERENCES client (client_id),
	date_order date,
	address text,
	quantity_price numeric
);

CREATE TABLE order_details
(
	order_id integer REFERENCES orders (order_id),
	product_id integer REFERENCES product (product_id)
);


INSERT INTO category (name) VALUES
('rolly'),
('pizza'),
('deserty'),
('sushi-sety'),
('zakuski');









