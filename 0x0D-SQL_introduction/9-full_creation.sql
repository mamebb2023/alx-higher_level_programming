-- Create a full table
CREATE TABLE IF NOT EXISTS `second_table` (
	`id` INT,
	`name` VARCHAR(256),
	`score` INT
);
INSERT INTO `second_table` (id, name) VALUES
	(`John`, 10),
	(`Alex`, 3),
	(`Bob`, 14),
	(`George`, 8);
