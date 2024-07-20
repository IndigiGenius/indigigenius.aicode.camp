# About

This unit was created to leverage the fast.ai library to support learners in creating a computer vision model in a short amount of time. Many of the lessons are based on the Fast.AI Practical Deep Learning for Coders curriculum, so please visit [https://course.fast.ai/](https://course.fast.ai/) to learn more.

# Setup:

## 1. Build docker image
```
docker build -t jupyter/deep_learning .
```

## 2. Run your image (this run command is intended for forked repos)
```

docker run --gpus all --memory=12g --cpus=0.75 --shm-size=12g -it -p 8888:8888 -v ${pwd}\data:/workspace/data/ -v ${pwd}\models:/workspace/models/ -v ${pwd}\notebooks:/workspace/notebooks/ jupyter/deep_learning

```

*Note*: this assumes a windows file system, for **nix *flip the slash from '\data' to '/data' in the -v parameter*

## 3. Monitor your GPU usage in the terminal (use a separate terminal than where you started the container)
```
nvidia-smi
```