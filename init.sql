CREATE TABLE assistants (
    assistant_id SERIAL PRIMARY KEY,
    assistant_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    created_at DATE NOT NULL
);
