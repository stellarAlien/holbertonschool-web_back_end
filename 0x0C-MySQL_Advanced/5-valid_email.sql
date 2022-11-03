-- trigger for validating email  on update
DELIMITER $$
CREATE TRIGGER `verify_email`
before update
ON holberton.users FOR EACH Row
BEGIN
    IF NOT(OLD.email like NEW.email) THEN
        SET NEW.valid_email = 0;
    END IF; 
END; $$