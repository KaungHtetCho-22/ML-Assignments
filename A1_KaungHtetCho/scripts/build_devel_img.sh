#!/bin/env bash

docker build \
	--build-arg="USERNAME=`(whoami)`" \
	--build-arg="USER_UID=`(id -u)`" \
	--build-arg="USER_GID=`(id -g)`" \
	-t a1_assignment:devel \
	--target devel \
	-f A1_KaungHtetCho/docker/Dockerfile \
    A1_KaungHtetCho
