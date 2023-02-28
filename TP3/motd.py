import os
import random
import argparse
from flask import Flask, jsonify

app = Flask(__name__)

# Arguments en ligne de commande
parser = argparse.ArgumentParser()
parser.add_argument('--motd', default='Default MOTD !', help='MOTD')
parser.add_argument('--port', type=int, default=8000, help='Port')

args = parser.parse_args()

motd = args.motd
port = args.port

# Route a appeler pour recuperer le motd au format JSON
@app.route('/motd')
def get_motd():
    return jsonify({'message': motd})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
