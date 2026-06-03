CREATE TABLE videogames (
    id SERIAL PRIMARY KEY,
    game TEXT,
    price NUMERIC,
    sales NUMERIC,
    platform TEXT,
    cost_to_make NUMERIC
);



INSERT INTO videogames (game, price, sales, platform, cost_to_make) VALUES
('Mario',     50, 2.0, 'Switch', 10),
('Zelda',     60, 1.5, 'Switch', 12),
('Halo',      55, 1.8, 'Xbox',   15),
('FIFA',      40, 3.0, 'PS5',     8),
('Crash Bandicoot', 30, 4.5, 'PC',      5);


SELECT * FROM videogames;
INSERT INTO videogames (game, price, sales, platform, cost_to_make) VALUES
('God of War',        70, 2.2, 'PS5',    20),
('Call of Duty',     75, 3.8, 'PS5',    25),
('Elden Ring',       65, 2.6, 'PC',     18),
('Fortnite',          0, 5.5, 'PC',     12),
('Cyberpunk 2077',   60, 1.9, 'PC',     22),
('Animal Crossing',  55, 2.8, 'Switch', 14);

SELECT 
    game,
    price,
    sales,
    price * sales AS revenue
FROM videogames;
SELECT COUNT(*), MAX(id) FROM videogames;
SELECT
    current_database(),
    current_user,
    inet_server_addr(),
    inet_server_port();




-- DROP TABLE videogames;

 
