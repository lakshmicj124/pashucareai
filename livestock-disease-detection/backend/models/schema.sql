CREATE DATABASE cow_disease_db;

\c cow_disease_db;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user', -- 'user' or 'admin'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS diseases (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    animal_type VARCHAR(50) NOT NULL, -- 'cow', 'goat', 'sheep'
    description TEXT,
    treatment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS detection_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    image_url VARCHAR(255),
    detected_disease VARCHAR(255),
    confidence_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
