
#!/bin/bash

mkdir -p ~/.config/systemd/user/

sed -e "s!__PWD__!$(pwd)!" chromesearchfix.service.template > ~/.config/systemd/user/chromesearchfix.service

for c in enable start status; do
    systemctl --user ${c} chromesearchfix.service
done
