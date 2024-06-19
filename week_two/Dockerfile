# Use a base image that supports Ubuntu 22.04
FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# Install necessary system packages and add deadsnakes PPA for Python versions
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.9 \
    python3.9-distutils \
    python3-pip \
    git \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Ensure python3 points to the installed Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Upgrade pip
RUN python3.9 -m pip install --no-cache-dir --upgrade pip

# Install Jupyter
RUN python3.9 -m pip install --no-cache-dir jupyter

# Install Jupyter Notebook Extensions
# RUN python3.9 -m pip install --no-cache-dir jupyter_contrib_nbextensions

# Install fastai
RUN python3.9 -m pip install --no-cache-dir fastai

# Expose Jupyter notebook port
EXPOSE 8888

# Set the working directory in the container
WORKDIR /workspace

# Create a directory for persisting data
ADD notebooks /workspace/notebooks/.
ADD data /workspace/data/.
ADD images /workspace/images/.
ADD models /workspace/models/.

# Start Jupyter notebook when the container starts
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/workspace"]
