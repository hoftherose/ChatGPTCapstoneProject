CREATE TABLE assistants (
    id SERIAL PRIMARY KEY,
    assistant_id VARCHAR(100) NOT NULL,
    assistant_name VARCHAR(100) NOT NULL,
    thread_id VARCHAR(100) NOT NULL,
    file_path VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    thread_id VARCHAR(100) NOT NULL,
    question VARCHAR(240) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
