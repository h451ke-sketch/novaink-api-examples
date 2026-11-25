import os
import time
import requests

API_KEY = os.environ["NOVAINK_API_KEY"]
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

task = requests.post(
    "https://novaink.ai/v1/videos",
    headers=HEADERS,
    json={
        "model": "veo3.1-fast",  # Or: doubao-seedance-2.5, viduq3-pro, kling-v2-master
        "prompt": "Cinematic drone glide over neon cyber-noir Tokyo street at twilight, 4K",
        "seconds": "5",
    },
    timeout=60,
).json()

task_id = task["id"]
print("Queued task:", task_id)

while True:
    res = requests.get(f"https://novaink.ai/v1/videos/{task_id}", headers=HEADERS, timeout=30).json()
    status = res.get("status")
    print("Status:", status)
    if status in ("completed", "succeeded"):
        print("Video URL:", res.get("url") or res.get("video_url"))
        break
    if status in ("failed", "error"):
        raise RuntimeError(f"Task failed (auto-refunded): {res}")
    time.sleep(8)
