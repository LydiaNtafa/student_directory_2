DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  cohort_name text,
  starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('June 23', '2023-05-30');
INSERT INTO cohorts (cohort_name, starting_date) VALUES ('July 23', '2023-07-30');

INSERT INTO students (student_name, cohort_id) VALUES ('Lydia Ntafa', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Ethan Clawson', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Future me', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Future you', 2);
INSERT INTO students (student_name, cohort_id) VALUES ('Someone Else', 2);