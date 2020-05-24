-- Use My SQL Work bench 
-- create db catalog
-- run this script 


CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sku` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `desc` text DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  `in_stock` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

INSERT INTO `catalog`.`product`
(`id`,`sku`,`name`,`title`,`desc`,`price`,`date_created`,`date_updated`,`in_stock`)
VALUES (
'3', NULL, 'slim-fit-suit-in-checked-stretch-fabric', 'Slim-fit suit in checked stretch fabric', 'A two-piece suit by BOSS Menswear, crafted in mid-weight fabric with a generous dose of virgin wool and a hint of stretch for an unrestricted feel. Featuring a checkered pattern, this distinctive suit comprises slim-cut pants and a single-breasted jacket with softly constructed shoulders and lined sleeves. A defined fit throughout makes this a contemporary choice for professional dressing.', '537.00', NULL, NULL, 1
);

INSERT INTO `catalog`.`product`
(`id`,`sku`,`name`,`title`,`desc`,`price`,`date_created`,`date_updated`,`in_stock`)
VALUES (
'4', NULL, 'micro-patterned-slim-fit-suit-in-stretch-virgin-wool', 'Micro-patterned slim-fit suit in stretch virgin wool', 'An advanced two-piece suit by BOSS Menswear, designed as part of the BOSS Travel Line with special details to allow for travel in style and comfort. Comprising flat-fronted pants and a jacket with notch lapels, this sharp ensemble features a micro pattern created in virgin wool blended with stretch for freedom of movement. A partial lining allows for easy layering while ensuring optimum breathability.', '895.00', NULL, NULL, 0
);

CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customerNumber` int(11) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `contactLastName` varchar(50) NOT NULL,
  `contactFirstName` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `addressLine1` varchar(50) NOT NULL,
  `addressLine2` varchar(50) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) DEFAULT NULL,
  `postalCode` varchar(15) DEFAULT NULL,
  `country` varchar(50) NOT NULL,
  `salesRepEmployeeNumber` int(11) DEFAULT NULL,
  `creditLimit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;


INSERT INTO `catalog`.`customer`
VALUES
(1,114,'Australian Collectors, Co.','Ferguson','Peter','03 9520 4555','636 St Kilda Road','Level 3','Melbourne','Victoria','3004','Australia',1611,'117300.00')

-- default user 

CREATE USER 'catalog'@'localhost';
GRANT SELECT, INSERT, DELETE ON catalog.* TO 'catalog'@'localhost';
