from PIL import Image
import hashlib
import io

#Load image
with open("path", "rb") as f: #Retrieve path from HTTP POST upload
    upload = io.BytesIO(f.read())
img = Image.open("upload")

#Convert image to bytes
buffer = io.BytesIO()
img.save(buffer, format="PNG")
img = buffer.getvalue()

#Hash image bytes
data = b"Test"
img_hash = hashlib.sha256(img).hexdigest()
print(f"SHA256 hash: {img_hash}")