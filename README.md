1. Obtain self-signed certificates:
openssl req -x509 -newkey rsa:4096 -keyout certificates/key.pem -out certificates/cert.pem -days 365 -nodes
2. Start server on localhost:
python main.py
3. Paste in browser to test:
https://127.0.0.1:5000