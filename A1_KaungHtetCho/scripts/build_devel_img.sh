#!/bin/env bash

docker build \
	--build-arg="USERNAME=`(whoami)`" \
	--build-arg="USER_UID=`(id -u)`" \
	--build-arg="USER_GID=`(id -g)`" \
	-t A1_assignment:devel \
	--target devel \
	-f docker/Dockerfile .
