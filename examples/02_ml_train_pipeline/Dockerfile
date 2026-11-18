FROM pytorch/pytorch:1.12.0-cuda11.3-cudnn8-runtime

RUN useradd --create-home --uid 1000 fluid

COPY ./main.py /workspace/main.py

# With --save-model, --save-model-path (default /data/ckpt) must be writable by UID 1000.
USER 1000

ENTRYPOINT ["python", "/workspace/main.py"]
