#!/bin/bash

# Script to run the calculator with Docker
# This script handles X11 forwarding for GUI support

echo "בונה את תמונת הדוקר..."
docker build -t hebrew-calculator .

echo "מפעיל את המחשבון בדוקר..."

# For Linux systems with X11
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Allow X11 forwarding
    xhost +local:docker
    
    docker run -it --rm \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
        --name hebrew-calculator \
        hebrew-calculator
        
    # Restore X11 security
    xhost -local:docker

# For macOS with XQuartz
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "עבור macOS, וודא ש-XQuartz מותקן ופועל"
    echo "הפעל: brew install --cask xquartz"
    
    # Get IP address
    IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
    
    docker run -it --rm \
        -e DISPLAY=$IP:0 \
        --name hebrew-calculator \
        hebrew-calculator

# For Windows with WSL2
else
    echo "עבור Windows, השתמש ב-WSL2 עם X11 server כמו VcXsrv"
    
    docker run -it --rm \
        -e DISPLAY=host.docker.internal:0 \
        --name hebrew-calculator \
        hebrew-calculator
fi

echo "המחשבון הופעל!"
