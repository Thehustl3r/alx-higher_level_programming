-- sql command
-- sql cmd that show the description of the table
# Get the information schema table for tables
tables=`SHOW TABLES`

# Loop through the tables and get the CREATE TABLE statement for each table
for table in $tables; do
  create_table_statement=`SHOW CREATE TABLE $table`
  echo "Table: $table"
  echo "Create Table: $create_table_statement"
done
