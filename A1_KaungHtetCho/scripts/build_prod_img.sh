#!/bin/env bash

docker build \
	-t a1_assignment:prod \
	--target prod \
	-f docker/Dockerfile .
