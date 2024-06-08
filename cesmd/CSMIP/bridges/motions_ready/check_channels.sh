#!/usr/bin/bash

for i in CE?????
    do echo $i
        for event in $i/*.zip
            do zipgrep Location $event
        done \
    | grep -i v2 | sed  's/\(.*\) *Location: *\(.*\)/\1 \2/g' | python check_channels.py; done