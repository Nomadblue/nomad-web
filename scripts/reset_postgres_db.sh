# -*- mode: shell-script -*-
#
# Made by Nabuco (http://www.nomadblue.com/).
# This script destroys and re-creates the postgresql project database.
# It applies all south migrations and, finally, creates a superuser.
#
# WARNING: you must have your project virtualenv activated and you must
# execute this script from the same path as the sqlite and manage.py files:
# ./scripts/reset_postgres_db.sh

if [ $# -ne 1 ]; then
    echo "Usage: $0 <database-name>"
    echo
    exit 2
fi

echo Dropping db $1...
dropdb $1
echo Creating db $1...
createdb $1

python manage.py syncdb --noinput
python manage.py migrate --all
python manage.py createsuperuser --traceback
