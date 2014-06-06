# -*- mode: shell-script -*-
#
# Made by Nabuco (http://www.nomadblue.com/).
# This script destroys and re-creates the postgresql project database
# with a new backup generated and downloaded from Heroku project app.
#
# WARNING: You need to be collaborator of the Heroku app. Also please
# note that this script downloads a backup file which is not removed
# afterwards, so be careful not to commit it into your repo by mistake.

purge=false
newpgbackup=false
while getopts "pb" opt; do
    case $opt in
        p)
            purge=true
            ;;
        b)
            newpgbackup=true
            ;;
    esac
done

shift $(( ${OPTIND} - 1 ))
if [ $# -ne 2 ]; then
    echo "Usage: $0 [-pb] <database-name> <heroku-app-name>"
    echo
    echo "Options:"
    echo "      -p      Runs a custom command to set all image fields to None"
    echo "      -b      Generate a new heroku pgbackup and download it"
    exit 2
fi

# Check that db exists
echo Checking psql database $1...
psql $1 -c '\q'
status=$?
if test $status -ne 0
then
    exit 2
fi

# Check that heroku app exists
heroku config -a $2
status=$?
if test $status -ne 0
then
    exit 2
fi

if $newpgbackup ; then
    echo Generating new pgbackup on $2...
    heroku pgbackups:capture --expire -a $2
    echo Downloading pgbackup...
    curl -o latest.pgdump `heroku pgbackups:url -a $2`
fi

echo Dropping db $1...
dropdb $1
echo Creating db $1...
createdb $1
echo Restoring pgbackup...
pg_restore --verbose --clean --no-acl --no-owner -h localhost -d $1 latest.pgdump

if $purge ; then
    echo Purging images...
    python manage.py purge_images
fi

echo Finished!
