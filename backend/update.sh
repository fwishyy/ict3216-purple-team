#!/bin/bash

# This script is used to update the backend of the project.

# Bring down the api-gateway
docker compose -f docker-compose.yml down "api-gateway"

# Pull the latest changes from the repository
docker compose pull
docker compose -f docker-compose.yml up --build "api-gateway" -d
