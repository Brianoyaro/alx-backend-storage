-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
--	UPDATE users SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) FROM corrections JOIN projects ON corrections.project_id = projects.id WHERE corrections.projects_id = projects.id) JOIN corrections ON users.id = corrections.user_id WHERE corrections.user_id = users.id;
CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users));
END //
DELIMITER ;
