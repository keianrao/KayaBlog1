
CREATE
TABLE Blogposts
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(256) NOT NULL,
    tags VARCHAR(128)[],
    author VARCHAR(256) REFERENCES Authors(username),
    submissionDate TIMESTAMP NOT NULL,
    contents TEXT NOT NULL
);

CREATE
TABLE Authors
(
    username VARCHAR(256) PRIMARY KEY,
    password VARCHAR(256) NOT NULL
);
