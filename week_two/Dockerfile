FROM nvcr.io/nvidia/pytorch:22.04-py3

RUN pip install onnxruntime-gpu
RUN conda install h5py

ADD notebooks /workspace/notebooks/.
ADD data /workspace/data/.
ADD models /workspace/models/.

RUN echo "c.NotebookApp.custom_display_url = 'http://localhost:8888'" >> /root/.jupyter/jupyter_notebook_config.py

CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
