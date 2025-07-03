#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: oversample.py
Author: Thimira Hirushan
Date: 2025-07-03
Description: This module oversamples audio data by a given factor using interpolation.
Version: 1.0
"""

import numpy as np
import scipy.signal
import soundfile as sf
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(script_dir, 'file_example_WAV_5MG.wav')  # Default input file path
output_file = os.path.join(script_dir, 'file_example_WAV_5MG_5x.wav')  # Default output file path
upsample_factor = 5 # Default upsample factor for oversampling

def load_audio_data(file_path):
    """
    Load audio data from a file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        tuple: (audio_data, sample_rate) where audio_data is a numpy array and sample_rate is an integer.
    """
    audio_data, sample_rate = sf.read(file_path)
    return audio_data, sample_rate

def oversample_audio(audio_data, upsample_factor):
    """
    Oversample audio data by a given factor using interpolation.

    Args:
        audio_data (numpy.ndarray): Input audio data.
        upsample_factor (int): Factor by which to oversample the audio data.

    Returns:
        numpy.ndarray: Oversampled audio data.
    """
    # Use scipy's resample_poly for efficient upsampling
    oversampled_data = scipy.signal.resample_poly(audio_data, upsample_factor, 1)
    return oversampled_data

def save_audio_data(file_path, audio_data, sample_rate):
    """
    Save audio data to a file.

    Args:
        file_path (str): Path to save the audio file.
        audio_data (numpy.ndarray): Audio data to save.
        sample_rate (int): Sample rate of the audio data.
    """
    sf.write(file_path, audio_data, sample_rate)

def main(input_file=input_file, output_file=output_file, upsample_factor=upsample_factor):
    """
    Main function to load, oversample, and save audio data.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the oversampled audio file.
        upsample_factor (int): Factor by which to oversample the audio data.
    """
    audio_data, sample_rate = load_audio_data(input_file)
    oversampled_data = oversample_audio(audio_data, upsample_factor)
    save_audio_data(output_file, oversampled_data, sample_rate * upsample_factor)

if __name__ == "__main__":
    """
    # This script oversamples an audio file by a specified factor and saves the result.
    # It uses scipy's resample_poly for efficient upsampling and soundfile for audio file handling.
    # The main function orchestrates loading, processing, and saving the audio data.
    # The script prints out details about the original and oversampled audio files.
    """

    main(input_file, output_file, upsample_factor)
    print(f"Oversampled audio saved to {output_file} with upsample factor {upsample_factor}.")
    print(f"Original sample rate: {sf.info(input_file).samplerate}, New sample rate: {sf.info(output_file).samplerate}")
    print(f"Original duration: {sf.info(input_file).duration} seconds, New duration: {sf.info(output_file).duration} seconds")
    print(f"Original number of samples: {sf.info(input_file).frames}, New number of samples: {sf.info(output_file).frames}")
        