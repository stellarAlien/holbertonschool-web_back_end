-- computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE w_avg_score FLOAT;
    SET w_avg_score = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users 
                        JOIN corrections  ON users.id=corrections.user_id 
                        JOIN projects  ON corrections.project_id=projects.id 
                        WHERE users.id=user_id);
    UPDATE users SET average_score = w_avg_score WHERE id=user_id;
END; $$
