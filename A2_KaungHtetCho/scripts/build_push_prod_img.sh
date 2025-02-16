#!/bin/bash

Define Docker Hub Username & Image Name
DOCKER_HUB_USER="koala007"
IMAGE_NAME="a2_assignment"
TAG="prod"

# docker login -u $DOCKER_HUB_USER

echo "Building Production Docker Image..."
docker build --no-cache -t $DOCKER_HUB_USER/$IMAGE_NAME:$TAG --target prod -f A2_KaungHtetCho/docker/Dockerfile .

echo "Pushing to Docker Hub..."
docker push $DOCKER_HUB_USER/$IMAGE_NAME:$TAG

echo "Done!"
