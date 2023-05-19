-- Ceates a database and a table inside it
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`)
    `id`        INT          NOT NULL AUTO_ INCREMENT UNIQUE,
    `state_id`  INT          NOT NULL,
    `name`      VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `htb_0d_usa`.`states`(`id`)
);