CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_not_so_secret VARCHAR(100) NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE assistants (
    assistant_id SERIAL PRIMARY KEY,
    assistant_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE threads (
    thread_id SERIAL PRIMARY KEY,
    thread_name VARCHAR(100),
    user_id INT NOT NULL,
    assistant_id INT NOT NULL,
    created_at DATE NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id),
    CONSTRAINT fk_assistant
        FOREIGN KEY (assistant_id)
        REFERENCES assistants(assistant_id)
);
