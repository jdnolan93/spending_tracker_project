DROP TABLE IF EXISTS purchases;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS places;

CREATE TABLE places(
    id SERIAL PRIMARY KEY,
    place_name VARCHAR(255)
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY, 
    tag_name VARCHAR(255),
);

CREATE TABLE purchases(
    id SERIAL PRIMARY KEY,
    price FLOAT,
    place_id INT REFERENCES places(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);
