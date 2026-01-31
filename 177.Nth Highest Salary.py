CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT
AS
BEGIN
    DECLARE @result INT;

    -- Guard against invalid N
    IF @N <= 0
        RETURN NULL;

    -- Use ROW_NUMBER to rank distinct salaries
    SELECT @result = Salary
    FROM (
        SELECT Salary,
               ROW_NUMBER() OVER (ORDER BY Salary DESC) AS rn
        FROM (SELECT DISTINCT Salary FROM Employee) AS e
    ) AS ranked
    WHERE rn = @N;

    RETURN @result;
END;
