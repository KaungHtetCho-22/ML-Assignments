#!/bin/env bash

docker build \
    -t a1_assignment:prod \
    --target prod \
    -f A1_KaungHtetCho/docker/Dockerfile \
    A1_KaungHtetCho
