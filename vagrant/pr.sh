# #!/usr/bin/env bash
#prerequesitos
sudo add-apt-repository ppa:openjdk-r/ppa -y
sudo apt update
sudo apt-get install -y openjdk-11-jre-headless

# Install CrateDB
#Codigo obtenido en

# Download the CrateDB GPG key
wget https://cdn.crate.io/downloads/deb/DEB-GPG-KEY-crate
# Add the key to Apt
sudo apt-key add DEB-GPG-KEY-crate

# Add CrateDB repositories to Apt
# `lsb_release -cs` returns the codename of your OS

sudo add-apt-repository "deb https://cdn.crate.io/downloads/deb/stable/ $(lsb_release -cs) main"

sudo apt-get update
sudo apt-get -y install crate


# Start "crate" Service.
sudo sysctl -w vm.max_map_count=262144
sudo service crate stop
sudo service crate restart


sudo apt-get update
sudo apt-get -y install python3-dev
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
pip3 install crate

cd app
python3 clientapp.py

sed -i 's/#network.host: _site_/network.host: _site_/g' /etc/crate/crate.yml
sed -i 's/auth.host_based.enabled: true/#auth.host_based.enabled: true/g' /etc/crate/crate.yml


sudo service crate stop
sudo service crate restart