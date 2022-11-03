-- create a trigger that decreases quantity of item
DELIMITER $$
DROP TRIGGER IF EXISTS sell_trigger;
CREATE TRIGGER  sell_trigger
AFTER INSERT
ON holberton.orders
FOR EACH Row
BEGIN
    update items set quantity = quantity - NEW.number Where items.name = NEW.item_name;
END; $$ 