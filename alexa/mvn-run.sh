#!/usr/bin/env bash
#
# 

shout() { echo "$0: $*" >&2; }
barf() { shout "$*"; exit 100; }
safe() { "$@" || barf "cannot $*"; }

APPDIR="alexa-avs-sample-app/samples/javaclient"

safe cd $APPDIR
safe mvn exec:exec
