#!/bin/env bash

docker build \
	-t A1_assignment:prod \
	--target prod \
	-f docker/Dockerfile .
