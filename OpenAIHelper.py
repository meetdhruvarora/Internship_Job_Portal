import requests
import base64
import time
def call_openai_api(prompt, image_path=None):
    headers = {
        "Content-Type": "application/json",
        "api-key": "83f4484027a74428ac5153a70db2143c",
    }

    # Base payload with prompt
    payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 100
    }

    # Add image to payload if provided
    if image_path is not None:
        try:
            encoded_image = base64.b64encode(open(image_path, 'rb').read()).decode('ascii')
            payload['messages'][0]['content'].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            })
        except Exception as e:
            print(f"Error reading or encoding the image: {e}")
            return

    endpoint = "https://mechaknights-ai-res.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

    for _ in range(3):  # Retry mechanism
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to make the request. Error: {e}")
            time.sleep(10)  # Wait for 10 seconds before retrying

    raise SystemExit("Failed to make the request after 3 attempts.")

# Call the APIs
