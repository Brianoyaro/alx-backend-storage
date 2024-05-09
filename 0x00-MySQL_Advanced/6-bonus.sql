DELIMITER **
CREATE PROCEDURE addBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
	DECLARE p_id INT;
	SELECT id INTO p_id FROM projects WHERE name = project_name;
	IF p_id = NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SELECT id INTO p_id FROM projects WHERE name = project_name;
	ENDIF;
	INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, p_id, score);
END**
DELIMITER ;
