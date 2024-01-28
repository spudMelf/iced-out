import joblib
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import argparse

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

def extract_audio_features(mp3):
    y, sr = librosa.load(mp3, sr=None)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rms = librosa.feature.rms(y=y)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfccs_avg = []
    for mfc in mfccs:
        mfccs_avg.append(np.mean(mfc))
    
    features = {
        'chroma_stft': np.mean(chroma_stft),
        'rms': np.mean(rms),
        'spectral_centroid': np.mean(spectral_centroid),
        'spectral_bandwidth': np.mean(spectral_bandwidth),
        'rolloff': np.mean(rolloff),
        'zero_crossing_rate':np.mean(zero_crossing_rate),
        'mfccs': mfccs_avg
    }
    return features

def main(audio_clip):

    model = joblib.load('models/audio_deepfake_model.joblib')
    features = extract_audio_features(audio_clip)

    arr= []
    arr.append(features['chroma_stft'])
    arr.append(features['rms'])
    arr.append(features['spectral_centroid'])
    arr.append(features['spectral_bandwidth'])
    arr.append(features['rolloff'])
    arr.append(features['zero_crossing_rate'])
    
    for m in features['mfccs']:
        arr.append(m)
    arr_reshaped = np.array(arr).reshape(1, 26)

    #print(arr_reshaped)
    df = pd.DataFrame(arr_reshaped)
    prediction = model.predict(df)
    
    # with open('output.txt', 'w') as file:
    #     file.write(str(prediction))
    
    result = 0 if prediction[0] == 1 else 1
    print(result)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='execute program with audio file path')
    parser.add_argument('audio_path', type=str, help='<audio_path>')
    args = parser.parse_args()

    audio_path = args.audio_path
    # print(f"Argument: {audio_path}")
    main(audio_path)

    


