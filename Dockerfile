FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8

# Grant ROOT access
USER root

# Set working directory
WORKDIR /opt/app

# Copy stable scripts
COPY scripts/install_packages.sh .
COPY scripts/install_tesserocr.sh .

# Install packages and dependencies
RUN bash ./install_packages.sh && rm ./install_packages.sh
RUN bash ./install_tesserocr.sh && rm ./install_tesserocr.sh

# Copy files
COPY scripts/install_dependencies.sh .
COPY requirements.in .

# Install dependencies
RUN bash ./install_dependencies.sh ./requirements.in && \
    rm ./install_dependencies.sh ./requirements.in

# Application
# Set PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/opt/app/"

# Copy modules and app.py
ADD src ./src
COPY app.py .

# Expose port
EXPOSE 7860

# Run APP
CMD ["python", "app.py"]
