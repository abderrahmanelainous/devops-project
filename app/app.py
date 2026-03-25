from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "DevOps Project API",
        "status": "running",
        "version": "3.0.0",
        "author": "Abderrahman Elainous",
        "description": "Infrastructure DevOps — Master DSBD & IA"
    })

@app.route('/healthOK')
def health():
    return jsonify({
        "status": "healthy-",
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": socket.gethostname()
    })

@app.route('/info')
def info():
    return jsonify({
        "app": "flask-devops-api",
        "environment": os.getenv("APP_ENV", "production"),
        "pod_name": os.getenv("POD_NAME", "unknown"),
        "node_name": os.getenv("NODE_NAME", "unknown")
    })

@app.route('/status')
def status():
    return jsonify({
        "cluster": "K3s on AWS EC2",
        "nodes": 2,
        "replicas": 2,
        "pipeline": "GitHub Actions",
        "registry": "Docker Hub",
        "deployed_at": datetime.utcnow().isoformat(),
        "message": "Deployed automatically via CI/CD pipeline"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
