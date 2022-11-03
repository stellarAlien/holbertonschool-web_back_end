--  creates a view need_meeting that lists all students that have a score under
-- 80 (strict) and no last_meeting or more than 1 month.
CREATE view need_meeting AS
select name FROM students
WHERE score < 80 AND (last_meeting is NULL or last_meeting < ADDDATE(CURDATE(), interval -1 month));