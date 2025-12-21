#!/bin/bash
-- Comment to start



# Check if a database name was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <database_name>"
  exit 1
fi

DB_NAME=$1

# Execute the command
mysql -u your_username -p -e "SHOW TABLES;" "$DB_NAME"
