--init.sql
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO myuser;
CREATE TABLE zone (
    id SERIAL NOT NULL,
     name VARCHAR(256),
    timezone VARCHAR(20),
    PRIMARY KEY (id),
);
INSERT INTO zone (name, timezone) VALUES ('London', 'Europe/London');
INSERT INTO zone (name, timezone) VALUES ('Moscow', 'Europe/Moscow');
INSERT INTO zone (name, timezone) VALUES ('New York', 'America/New_York');
INSERT INTO zone (name, timezone) VALUES ('Sydney', 'Australia/Sydney');