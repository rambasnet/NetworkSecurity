# Run The Flask Web App on a Linux VM

## Install Flask

```bash
sudo apt update
pip3 install Flask
sudo apt install python3-flask
```

## Run the Flask App on a Different Host and Port

- by default, Flask runs on `localhost` and port `5000`

```bash
flask run --host=<ip> --port=<port>
```

## Open the App in Browser

- http://<ip>:<port>
- http://localhost:5000
