import requests
import argparse


def main(text_path):
    with open(text_path, 'r') as file:
        contents = file.read()

        response = requests.post(
            "https://piratexx-ai-content-detector.hf.space/run/predict",
              json = {"data": [contents] }).json()
        
        data = response["data"]
        fake_probability = data[0][0]['Fake']
        print(f"{fake_probability:.6f}")
        
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='execute program with text file path')
    parser.add_argument('text_path', type=str, help='<text_path>')
    args = parser.parse_args()

    text_path = args.text_path
    print(f"Argument: {text_path}")
    main(text_path)

