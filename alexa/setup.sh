#!/usr/bin/env bash
#
# Sets up Amazon Alexa Sample App

shout() { echo "$0: $*" >&2; }
barf() { shout "$*"; exit 100; }
safe() { "$@" || barf "cannot $*"; }

APPDIR="alexa-avs-sample-app"

# Clone the repo
safe git clone https://github.com/alexa/alexa-avs-sample-app
safe cd $APPDIR

echo -n "Enter your ProductID: "
read productid

echo -n "Enter your ClientID: "
read clientid

echo -n "Enter your ClientSecret: "
read clientsecret

# Editing automated_install.sh
# ProductId
safe sed -i '8s/.*/ProductID='"$productid"'/' automated_install.sh
# ClientID
safe sed -i '11s/.*/ClientID='"$clientid"'/' automated_install.sh
# Clientsecret
safe sed -i '14s/.*/ClientSecret='"$clientsecret"'/' automated_install.sh

. automated_install.sh

cd $APPDIR/samples/companionService && npm install
cd $APPDIR/samples/javaclient && mvn -X install

echo "Done!"
