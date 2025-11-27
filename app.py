import os
from flask import Flask, render_template
import torch
import numpy as np
import io
import os
from timm import create_model
from PIL import Image
from torch.nn.functional import softmax
from torchvision import transforms
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # Required for cross-origin requests from the front-end


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "PLACEHOLDER_API_KEY_NEEDS_TO_BE_REPLACED")

app = Flask(__name__)
CORS(app) # Enable CORS for the front-end

@app.route('/waytoschool')
def waytoschool():
    """Renders the main quiz page."""
    return render_template('waytoschool.html', api_key=GEMINI_API_KEY)

@app.route('/walkfree')
def walkfree():
    """Renders the pavement annotation page."""
    return render_template('walkfree.html', api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    """Renders the main project index page."""
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
