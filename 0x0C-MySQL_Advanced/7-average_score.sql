-- computes and store the average score for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
UPDATE users SET average_score = (SELECT user_id, project_id, AVG(score) 
FROM holberton.corrections
Where user_id = corrections.user_id)
where id = user_id;
END; $$