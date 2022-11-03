-- procedure that adds bonis for student
DELIMITER $$
CREATE procedure AddBonus(IN user_id INT, IN project_name varchar(25), IN score FLOAT)
BEGIN
    IF EXISTS (SELECT * FROM projects
                WHERE name LIKE project_name LIMIT 1)
    THEN
        SET @project_id = 
        (SELECT id from holberton.projects 
                WHERE projects.name = project_name);
    ELSE
        INSERT into projects(name) values(project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections values(user_id, @project_id, score);
END; $$ 