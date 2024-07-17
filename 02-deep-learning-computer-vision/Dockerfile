# Use a base image that supports CUDA and cuDNN
FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Install Jupyter and fast.ai
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir nbdev \
    && pip3 install --no-cache-dir gradio \
    && pip3 install --no-cache-dir jupyter \
    && pip3 install --no-cache-dir fastai \
    && pip3 install --no-cache-dir timm

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
