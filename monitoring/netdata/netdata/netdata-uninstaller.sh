#!/usr/bin/env bash

# this script will uninstall netdata

if [ "$1" != "--force" ]
    then
    echo >&2 "This script will REMOVE netdata from your system."
    echo >&2 "Run it again with --force to do it."
    exit 1
fi

source installer/functions.sh || exit 1

echo >&2 "Stopping a possibly running netdata..."
for p in $(pidof netdata); do run kill $p; done
sleep 2

if [ ! -z "" -a -d "" ]
    then
    # installation prefix was given

    portable_deletedir_recursively_interactively ""

else
    # installation prefix was NOT given

    if [ -f "/usr/sbin/netdata" ]
        then
        echo "Deleting /usr/sbin/netdata ..."
        run rm -i "/usr/sbin/netdata"
    fi

    portable_deletedir_recursively_interactively "/etc/netdata"
    portable_deletedir_recursively_interactively "/usr/share/netdata"
    portable_deletedir_recursively_interactively "/usr/libexec/netdata"
    portable_deletedir_recursively_interactively "/var/lib/netdata"
    portable_deletedir_recursively_interactively "/var/cache/netdata"
    portable_deletedir_recursively_interactively "/var/log/netdata"
fi

if [ -f /etc/logrotate.d/netdata ]
    then
    echo "Deleting /etc/logrotate.d/netdata ..."
    run rm -i /etc/logrotate.d/netdata
fi

if [ -f /etc/systemd/system/netdata.service ]
    then
    echo "Deleting /etc/systemd/system/netdata.service ..."
    run rm -i /etc/systemd/system/netdata.service
fi

if [ -f /lib/systemd/system/netdata.service ]
    then
    echo "Deleting /lib/systemd/system/netdata.service ..."
    run rm -i /lib/systemd/system/netdata.service
fi

if [ -f /etc/init.d/netdata ]
    then
    echo "Deleting /etc/init.d/netdata ..."
    run rm -i /etc/init.d/netdata
fi

if [ -f /etc/periodic/daily/netdata-updater ]
    then
    echo "Deleting /etc/periodic/daily/netdata-updater ..."
    run rm -i /etc/periodic/daily/netdata-updater
fi

if [ -f /etc/cron.daily/netdata-updater ]
    then
    echo "Deleting /etc/cron.daily/netdata-updater ..."
    run rm -i /etc/cron.daily/netdata-updater
fi

portable_check_user_exists netdata
if [ $? -eq 0 ]
    then
    echo
    echo "You may also want to remove the user netdata"
    echo "by running:"
    echo "   userdel netdata"
fi

portable_check_group_exists netdata > /dev/null
if [ $? -eq 0 ]
    then
    echo
    echo "You may also want to remove the group netdata"
    echo "by running:"
    echo "   groupdel netdata"
fi

for g in  adm nobody
do
    portable_check_group_exists $g > /dev/null
    if [ $? -eq 0 ]
        then
        echo
        echo "You may also want to remove the netdata user from the $g group"
        echo "by running:"
        echo "   gpasswd -d netdata $g"
    fi
done

