#!/bin/bash

CODICE_HOME=https://github.com/codice/
OPENDX_HOME=https://github.com/OpenDX/
BRADH_HOME=https://github.com/bradh/

# DDF_COMPONENTS=(ddf-support ddf-parent ddf-platform ddf-admin  ddf-security ddf-catalog ddf-content ddf-spatial ddf-solr ddf-stomp ddf-ui ddf)
DDF_COMPONENTS=(ddf-support ddf-parent ddf-platform ddf-admin  ddf-security ddf-catalog ddf-content ddf-spatial ddf-solr ddf-ui ddf)
# OPENDX_COMPONENTS=(nitf-input-transformer ais-parser ais-input-transformer xmpp-input-transformer)
OPENDX_COMPONENTS=(nitf-input-transformer xmpp-input-transformer)
BRADH_COMPONENTS=(imaging-nitf ddf-nitfinputtransformer ddf-jpeginputransformer)

export MAVEN_OPTS='-Xmx1024M -XX:MaxPermSize=512M'

# Exit if anything breaks
set -e

function cloneCodiceComponentIfNeeded {
  GITHUB_PATH=$CODICE_HOME$1
  echo $GITHUB_PATH
  # if we don't already have repo checked out, clone it
  if [[ ! -d $1 ]]; then
    git clone $GITHUB_PATH
  fi
}

function cloneOpenDXComponentIfNeeded {
  GITHUB_PATH=$OPENDX_HOME$1
  echo $GITHUB_PATH
  # if we don't already have repo checked out, clone it
  if [[ ! -d $1 ]]; then
    git clone $GITHUB_PATH
  fi
}

function cloneBradhComponentIfNeeded {
  GITHUB_PATH=$BRADH_HOME$1
  echo $GITHUB_PATH
  # if we don't already have repo checked out, clone it
  if [[ ! -d $1 ]]; then
    git clone $GITHUB_PATH
  fi
}

# change into the working directory, update, build and move back to this directory
function buildUsingMaven {
  cd $1
  git reset --hard
  git pull
  mvn clean install -DskipTests=true
  mvn sonar:sonar
  cd ..
}

for DDF_COMPONENT in ${DDF_COMPONENTS[*]}
do
  cloneCodiceComponentIfNeeded $DDF_COMPONENT
  buildUsingMaven $DDF_COMPONENT
done

for OPENDX_COMPONENT in ${OPENDX_COMPONENTS[*]}
do
  cloneOpenDXComponentIfNeeded $OPENDX_COMPONENT
  buildUsingMaven $OPENDX_COMPONENT
done

for BRADH_COMPONENT in ${BRADH_COMPONENTS[*]}
do
  cloneBradhComponentIfNeeded $BRADH_COMPONENT
  buildUsingMaven $BRADH_COMPONENT
done


