-- mail trigger
CREATE TRIGGER mailvalid
AFTER ALTER ON email
FOR EACH ROW
UPDATE users
SET valid_email = 0
WHERE email = NEW.email;
