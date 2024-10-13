# این دستورات داخل Workbench اجرا شده اند
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
    weight FLOAT,
    height FLOAT,
    age INT,
    gender VARCHAR(6),
    date DATETIME,
    FOREIGN KEY (patient_id) REFERENCES user_table(id)
);
# food_composition_tbl is CSV format and imported into MySql workbench
# جدول food_composition_tbl با فرمت CSV بوده و به ورک بنچ ایمپورت شده

CREATE TABLE planner.meal_plan_tbl(
    patient_id INT,
    date DATETIME,
    plan_info VARCHAR(100),
    calorie_needed DECIMAL(10, 2),
    carbohydrate_percentage DECIMAL(5, 2),
    protein_percentage DECIMAL(5, 2),
    fat_percentage DECIMAL(5, 2),
    carbohydrate_needed DECIMAL(10, 2),
    protein_needed DECIMAL(10, 2),
    fat_needed DECIMAL(10, 2),
    meal VARCHAR(255),
    foods VARCHAR(1100),
    FOREIGN KEY (patient_id) REFERENCES user_table(id)
);
ALTER TABLE planner.meal_plan_tbl ADD id int primary key auto_increment;
ALTER TABLE planner.meal_plan_tbl RENAME COLUMN id TO plan_id;

