DDF_VERSION=2.3.1-SNAPSHOT

INSTALL_DIR=install

rm -rf $INSTALL_DIR
mkdir $INSTALL_DIR
cd $INSTALL_DIR
unzip ../ddf/distribution/ddf/target/ddf-$DDF_VERSION.zip
cd ddf-$DDF_VERSION

expect ../../ddfStartup.expect
