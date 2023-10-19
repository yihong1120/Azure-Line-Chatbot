#!/bin/bash

# Build the Docker image for the application
echo "Building the Docker image for the application..."
docker build -t azure-line-chatbot .

# Initialise Docker Swarm if it isn't already initialised
echo "Initialising Docker Swarm..."
docker swarm init

# Create a Docker secret from the Azure App Configuration connection string
echo "Creating Docker secret from the Azure App Configuration connection string..."
docker secret create azure_app_config azure_app_config.txt

# Use docker-compose to bring up the services defined in docker-compose.yml
echo "Starting services using docker-compose..."
docker-compose up -d

echo "Services started successfully!"
