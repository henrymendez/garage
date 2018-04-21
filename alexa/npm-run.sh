#!/usr/bin/env bash
#
# 

shout() { echo "$0: $*" >&2; }
barf() { shout "$*"; exit 100; }
safe() { "$@" || barf "cannot $*"; }

APPDIR="alexa-avs-sample-app/samples/companionService"

safe cd $APPDIR
safe npm start
