CREATE DATABASE IF NOT EXISTS food_truck_DB;

-- DROP TABLE IF EXISTS food;
CREATE TABLE IF NOT EXISTS food (
    id serial Primary key,
    name varchar(50) NOT NULL,
    image_url text,
    price_in_cents integer NOT NULL,
    description text
);

CREATE TABLE IF NOT EXISTS form(
    id serial Primary key,
    name varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    phone varchar(50),
    message text NOT NULL
)