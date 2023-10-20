#! /bin/bash

if [ -z "$1" ]
then
      echo "Usage: generate_proto.sh <HUBBLE_VERSION>"
      exit 1
else
	HUBBLE_VER=$1
fi

SRC_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"/src/farcaster
source ./BUILD

if [ "$BUILD" ]; then
	BUILD="-${BUILD}"
fi

rm -f $SRC_DIR/fcproto/*
rm -f $SRC_DIR/schemas/*

curl -s -L "https://github.com/farcasterxyz/hub-monorepo/archive/refs/tags/@farcaster/hubble@"${HUBBLE_VER}".tar.gz" \
	| tar -zxvf - -C $SRC_DIR --strip-components 2 hub-monorepo--farcaster-hubble-${HUBBLE_VER}/protobufs/schemas/

if [ $? -ne 0 ]; then
	echo "Failed to download schemas."
	exit 1
fi

python3 -m grpc_tools.protoc \
    -I$SRC_DIR/schemas \
    --python_out=$SRC_DIR/fcproto --pyi_out=$SRC_DIR/fcproto --grpc_python_out=$SRC_DIR/fcproto \
    $SRC_DIR/schemas/*.proto

# A nasty hack :-( Inspired by https://github.com/grpc/grpc/issues/29459#issue-1210216486
sed -I "" -e 's/^import /from \. import /g' $SRC_DIR/fcproto/*.py $SRC_DIR/fcproto/*.pyi
# And it gets nastier:
sed -I "" -e 's/^from . import grpc/import grpc/g' $SRC_DIR/fcproto/*.py $SRC_DIR/fcproto/*.pyi

if [ $? -ne 0 ]; then
	echo "Failed to generate protobuf python files.."
	exit 1
fi

# Automatic versioning needs https://github.com/farcasterxyz/hub-monorepo/issues/1518
# to be resolved first. For now, I'll do versioning manually.
#
# sed '/^version=".*"$/d' ${SRC_DIR}/__about__.py > ${SRC_DIR}/__about__.py.1
# echo version=\"${HUBBLE_VER}${BUILD}\" >> ${SRC_DIR}/__about__.py.1
# mv -f ${SRC_DIR}/__about__.py.1 ${SRC_DIR}/__about__.py

echo
echo "Protobuf schemas parsed."
# echo "Version file updated to $(hatch version)"