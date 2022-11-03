-- computes and store the average score for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE procedure ComputeAverageScoreForUser(IN user_id INT)
BEGIN
UPDATE users SET average_score = (SELECT AVG(score) 
FROM corrections Where user_id = corrections.user_id) Where id = user_id;
END; $$