import numpy as np
import scipy as scipy

from soundpredictor import yamnet_predictor, class_names
from config.constants import FS


def ensure_sample_rate(original_sample_rate, waveform,
                       desired_sample_rate=FS):
    """Resample waveform if required."""
    if original_sample_rate != desired_sample_rate:
        desired_length = int(round(float(len(waveform)) /
                                   original_sample_rate * desired_sample_rate))
        waveform = scipy.signal.resample(waveform, desired_length)
    return desired_sample_rate, waveform


def get_top_audio_scores(fs, audio, top_n = 10):
    fs, audio = ensure_sample_rate(fs, audio)

    scores, embeddings, spectrogram = yamnet_predictor(audio)
    scores = scores.numpy()
    mean_scores = np.mean(scores, axis=0)
    top_class_indices = np.argsort(mean_scores)[::-1][:top_n]
    yticks = range(0, top_n, 1)
    top_n_results = [(top_class_indices[x], class_names[top_class_indices[x]], mean_scores[top_class_indices[x]]) for x in yticks]
    return top_n_results, scores