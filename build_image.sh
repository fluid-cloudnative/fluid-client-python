#!/bin/sh
VERSION=v1.0.0
GIT_SHA=$(git rev-parse --short HEAD || echo "HEAD")
GIT_VERSION=${VERSION}-${GIT_SHA}
IMAGE_REPO=fluidcloudnative
IMAGE_NAME=${IMAGE_REPO}/fluid-client-python

echo "Building image: ${IMAGE_NAME}:${GIT_VERSION}"
docker build --no-cache . -f docker/Dockerfile.fluidclientpython -t ${IMAGE_NAME}:${GIT_VERSION}

while getopts "p" opt
do
    case $opt in
        p)
            echo "Pushing image: ${IMAGE_NAME}:${GIT_VERSION}"
            docker push ${IMAGE_NAME}:${GIT_VERSION}
            ;;
        ?)
            echo "Usage: build_image.sh [OPTION]"
            echo "  -p Push the built image"
            exit 1
            ;;
    esac
done