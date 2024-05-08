-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
RETURNS INT DETERMINISTIC
BEGIN
	UPDATE corrections SET score = (SELECT (score * (SELECT weight FROM projects WHERE projects.id = corrections.projects_id))) WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) WHERE users.id = user_id;
END//
DELIMITER ;
