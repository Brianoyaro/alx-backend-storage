-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;
	SELECT COUNT(*) FROM users INTO n;
	SET i=1;
	WHILE i<=n DO
		CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE id = i));
		-- INSERT INTO table_B(ID, VAL) SELECT (ID, VAL) FROM table_A LIMIT i,1;
		SET i = i + 1;
	END WHILE;
END //
DELIMITER ;
