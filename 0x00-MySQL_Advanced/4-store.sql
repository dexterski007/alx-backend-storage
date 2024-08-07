-- store of storage
CREATE TRIGGER sales
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
