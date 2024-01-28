import requests
import argparse

def main(text_path):
    with open(text_path, 'r') as file:
        file_contents = file.read()

        message = file_contents

        API_URL = "https://api-inference.huggingface.co/models/dima806/phishing-email-detection"
        headers = {"Authorization": f"Bearer {'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'}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": message,
        })

        phishing_chance = output[0][1]['score']
        print(f"{phishing_chance:.6f}")

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='execute program with text file path')
    parser.add_argument('text_path', type=str, help='<text_path>')
    args = parser.parse_args()

    text_path = args.text_path
    print(f"Argument: {text_path}")
    main(text_path)
