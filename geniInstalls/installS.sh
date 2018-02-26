#!/bin/sh

# Usual directory for downloading software in ProtoGENI hosts is `/local`
cd /local

##### Check if file is there #####
if [ ! -f "./installed.txt" ]
then
       #### Create the file ####
        sudo touch "./installed.txt"

       #### Run  one-time commands ####
       
       #Install necessary packages
        sudo apt update & EPID=$!
        wait $EPID
        sudo apt -y install git-core unzip cmake libpcap-dev libxerces-c2-dev libpcre3-dev flex bison g++ autoconf libtool pkg-config libboost-dev libboost1.40-all-dev gawk & EPID=$!
        wait $EPID

       # Install custom software
       	sudo mkdir chatServer & EPID=$!
	wait $EPID
       	sudo sudo wget http://mountrouidoux.people.cofc.edu/CyberPaths/chat/chats2.py chatServer/ & EPID=$!
       	wait $EPID
       	
       
       ## Reboot the OS to run a latest kernel without IPv6.
       sudo reboot
fi
