import hashlib
import os
import psycopg2

# Retrieve database details from the environment variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_HHAE")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)
cur = conn.cursor()

# Load image
with open("Blank diagram.png", "rb") as f: # Retrieve path from HTTP POST upload
    img_bytes = f.read()

# Hash image bytes
img_hash = hashlib.sha256(img_bytes).hexdigest()
print(f"SHA256 hash: {img_hash}")

# Store hash in database
cur.execute(
    "INSERT INTO images (sha256) VALUES (%s)",
    (img_hash,)
)
conn.commit()

# Closing database connection
cur.close()
conn.close()