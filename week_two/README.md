# Setup:

## 1. Go to week_two folder

Create a folder called "data"

## 2. Add your data

Load your the training data into the *data* folder. This data will show up in Jupyter

## 3. Build docker image
```
docker build . -t jupyter/week_two
```

## 4. Run your image
```
docker run --gpus all --memory=12g --cpus=0.75 --shm-size=12g -it -v ${pwd}\data:/workspace/data/ -v ${pwd}\models:/workspace/models/ -p 8888:8888 jupyter/week_two
```

*Note*: this assumes a windows file system, for **nix *flip the slash from '\data' to '/data' in the -v parameter*
