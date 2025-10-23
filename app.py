
from main import app

from models import Basis
import json

@app.route("/api/<int:image_id>", methods=['GET'])
def get_image(image_id):
    image = Basis.query.get(image_id)
    if not image:
        return {"error": "Image not found"}, 404

    # Bilddaten kodieren (angenommen image.image_data ist BYTEA)
    encoded_image = base64.b64encode(image.image_data).decode("utf-8")

    return jsonify({"id": image.id, "image_base64": encoded_image})

def portable_format(image) -> json: 
    # erstelle ein format, sodass der browser das bild anzeigen kann, nachdem er es erhalten hat