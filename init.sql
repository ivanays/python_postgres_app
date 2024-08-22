CREATE TABLE test_table (
    name VARCHAR(10) NULL,
    surname VARCHAR(100) NULL,
    city VARCHAR(100) NULL,
    age INTEGER NULL
);

ALTER TABLE test_table
ADD CONSTRAINT name_check
CHECK ( LENGTH(TRIM(name)) >= 4);

ALTER TABLE test_table
ADD CONSTRAINT name1_check
CHECK ( LENGTH(TRIM(name)) < 10);

ALTER TABLE test_table
ADD CONSTRAINT age_check
CHECK (age > 0);

ALTER TABLE test_table
ADD CONSTRAINT age1_check
CHECK (age < 150);

INSERT INTO test_table (name,surname,city,age) VALUES
('Boris','Ivanovich','Moscow',45),
('Polina','Alekseevna','Tver',22),
('Nikol','Igorevna','Moscow',56),
('Elisabet','Pavlovna','Tver',98),
('Boris','Semenich','Tver',37),
('Robert','Vladimirovich','Tver',45),
('Timofey','Ivanovich','Moscow',12),
('Polina','Pavlovna','Vladimir',65),
('Robert','Semenich','Vladimir',76),
('Elisabet','Igorevna','Tula',16),
('Boris','Vladimirovich','Tula',26),
('Nikol','Vladimirovna','Tula',74),
('Polina','Alekseevna','Tula',89),
('Robert','Ivanovich','Moscow',101),
('Elisabet','Igorevna','Vladimir',35),
('Boris','Vladimirovich','Tula',18),
('Nikol','Pavlovna','Vladimir',77),
('Polina','Igorevna','Moscow',90),
('Elisabet','Alekseevna','Moscow',31),
('Boris','Yuryevich','Vladimir',25);
