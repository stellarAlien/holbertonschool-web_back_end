-- create funciton that  divides (and returns) the first by the second number
-- or returns 0 if the second number is equal to 0.
DELIMITER $$
create FUNCTION SafeDiv(a INT, b INT)
    returns FLOAT DETERMINISTIC
    BEGIN
      IF (b = 0) Then
        Return(0);
      Else
        Return(a/b);
     END IF;
     END; $$
