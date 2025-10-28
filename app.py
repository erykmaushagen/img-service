
from main import app

from flask import Flask, jsonify, send_file
from models import Basis
import json
import io
import base64



@app.route("/api/<uuid:image_id>/raw", methods=['GET'])
def get_raw_image(image_id):
    images = Basis.query.get(image_id)
    if not images:
        return {"error": "Image not found"}, 404
    
    # Base64 dekodieren und als Bild senden
    image_data = base64.b64decode(images.image)
    image_extension = images.image_name.split('.')[-1].lower()
    
    return send_file(
        io.BytesIO(image_data),
        mimetype=f'image/{image_extension}',
        as_attachment=False
    )

@app.route("/api/test_route")
def test_route(): 
    all_data = Basis.query.all()
    print(all_data)
    print("test ist abgeschlossen")
    return "all Daten angezeigt"
