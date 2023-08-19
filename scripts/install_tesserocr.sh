#!/bin/bash

# Installing prerequisites
apt update && \
    apt install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    pkg-config
