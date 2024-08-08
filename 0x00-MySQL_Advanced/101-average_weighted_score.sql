-- bonus procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    UPDATE users
    SET average_score = (SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight))
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id
    );
END $$
DELIMITER ;
