-- safediv function
DELIMITER $$
CREATE FUNCTION SafeDiv(IN a INT, IN b INT)
RETURNS FLOAT
BEGIN
    RETURN IF(b = 0, 0, a / b);
END $$
DELIMITER ;
