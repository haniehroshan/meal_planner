CREATE DATABASE planner;

CREATE TABLE planner.user_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    family VARCHAR(20),
    mobile VARCHAR(13) UNIQUE,
    password VARCHAR(20)
);

CREATE TABLE planner.patient_visit_table(
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES user_table(id),
    weight FLOAT,
    height FLOAT,
    age INT,
    gender VARCHAR(6),
    date DATE
);