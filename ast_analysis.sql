DROP DATABASE astmine;
CREATE SCHEMA astmine;
USE astmine;

FLUSH privileges;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';

USE astmine;

CREATE TABLE `output` (
  `l1` VARCHAR(255) DEFAULT NULL,
  `l2` VARCHAR(255) DEFAULT NULL,
  `l3` VARCHAR(255) DEFAULT NULL,
  `fullpath` VARCHAR(255) DEFAULT NULL,
  `filename` VARCHAR(255) DEFAULT NULL, 
  `functype` VARCHAR(255) DEFAULT NULL,
  `funcname` VARCHAR(255) DEFAULT NULL,
  `linenumber` VARCHAR(255) DEFAULT NULL
);
-- ["SET "+part1[i]+" = (@var"+str(i+1)+" = \'Y\');\n" for i in range(len(part1))]
SET GLOBAL local_infile = 'ON';

LOAD data local INFILE 'C:/Users/18604/Desktop/research/ast_analysis/ast_analysis_data.csv' INTO TABLE output 
  FIELDS TERMINATED BY ', ' ENCLOSED BY '\"'
  LINES TERMINATED BY '\n' (l1,l2,l3,fullpath,filename,functype,funcname,linenumber);

SHOW WARNINGS;
SELECT * FROM output;
