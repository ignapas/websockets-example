# websockets-example

## Server
Server is an aiohttp server using python-socketio library to enable WebSockets communication with a frontend.
To run the server, simply run:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Client
Client is a Vuejs single page application using the Element library
To compile the client and made it available to the server, run:
```
cd client
npm run build
```
