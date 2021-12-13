DROP TABLE IF EXISTS purchases;
DROP TABLE IF EXISTS places;

CREATE TABLE places(
    id SERIAL PRIMARY KEY,
    place_name VARCHAR(255)
)

CREATE TABLE purchases(
    id SERIAL PRIMARY KEY
    item_name VARCHAR(255),
    price FLOAT(2),
    place_id INT REFERENCES places(id)
)
