# Network Security

Jupyter Notebooks for learning network security, network utility tools and scapy library - a powerful interactive packet manipulation program for Python.

Some of the contents are based on:

1. [SEED Labs](https://seedsecuritylabs.org/)
2. Scapy: [https://github.com/secdev/scapy/](https://github.com/secdev/scapy/)

## Requirements

- x86/64 Machine preferably Mac (Intel)/Linux
- Docker
- Docker Compose

## Run Jupyter Notebook in Docker Container

```bash
cd <cloned_repo>
docker compose build
docker compose up -d
docker ps
docker exec -it seedubuntu bash
jupyter server list
```

- Open browser and go to: [http://127.0.0.1:8888/](http://127.0.0.1:8888/)
- Copy and paste authentication token
- Open course/notebooks/00-TableOfContents.ipynb chapter and access all the notebooks
