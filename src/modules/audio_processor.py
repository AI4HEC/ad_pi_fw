#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: audio_processor.py
Author: Thimira Hirushan
Date: 2025-06-12
Description: A module for processing audio files, including loading, pre-emphasizing,
             oversampling, and saving audio files. Supports both WAV and MP3 formats.
"""

import os
import numpy as np
from scipy.io import wavfile
import pydub

class AudioProcessor:
    def __init__(self, file_path):
        """
        Initialize the AudioProcessor.
        """
        self.file_path = file_path
        self.sample_rate = None
        self.audio_data = None
        self.file_format = None
    
    def load_audio(self, file_path):
        """
        Load an audio file and store its sample rate and data.

        Args:
            file_path (str): Path to the audio file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file {file_path} does not exist.")

        self.file_path = file_path
        if file_path.lower().endswith('.wav'):
            self.sample_rate, self.audio_data = wavfile.read(file_path)
            self.file_format = 'wav'
        elif file_path.lower().endswith('.mp3'):
            audio = pydub.AudioSegment.from_mp3(file_path)
            self.sample_rate = audio.frame_rate
            self.audio_data = np.array(audio.get_array_of_samples())
            self.file_format = 'mp3'
        else:
            raise ValueError("Unsupported audio format. Only WAV and MP3 are supported.")

    def monotone(self):
        """
        Convert the audio data to a monotone signal (single channel).
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please load an audio file first.")
        if self.audio_data.ndim == 0:
            raise ValueError("Audio data is not valid. Ensure the audio file is loaded correctly.")
        if self.audio_data.ndim > 1:
            self.audio_data = np.mean(self.audio_data, axis=1)
        self.audio_data = self.audio_data.astype(np.float32)
        if self.audio_data.ndim == 1:
            self.audio_data = self.audio_data.reshape(-1, 1)
        else:
            raise ValueError("Audio data is not in a valid format for monotone conversion.")

    def normalize_data(self):
        """
        Normalize the audio data to the range [-1, 1].
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please load an audio file first.")
        max_val = np.max(np.abs(self.audio_data))
        if max_val == 0:
            raise ValueError("Audio data cannot be normalized because it contains only zeros.")
        self.audio_data = self.audio_data / max_val
        self.audio_data = self.audio_data.astype(np.float32)
        if self.audio_data.ndim == 1:
            self.audio_data = self.audio_data.reshape(-1, 1)
        else:
            raise ValueError("Audio data is not in a valid format for normalization.")

    def pre_emphasize(self, alpha=0.97):
        """
        Apply pre-emphasis to the audio data.

        Args:
            alpha (float): Pre-emphasis coefficient, typically between 0.95 and 0.99.
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please load an audio file first.")
        if self.audio_data.ndim != 1:
            raise ValueError("Pre-emphasis can only be applied to mono audio data.")
        self.audio_data = np.append(self.audio_data[0], self.audio_data[1:] - alpha * self.audio_data[:-1])
        self.audio_data = self.audio_data.astype(np.float32)
        if self.audio_data.ndim == 1:
            self.audio_data = self.audio_data.reshape(-1, 1)
        else:
            raise ValueError("Audio data is not in a valid format for pre-emphasis.")

    def oversample(self, output_frequency):
        """
        Oversample the audio data to a specified output frequency.

        Args:
            output_frequency (int): Desired output frequency in Hz.
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please load an audio file first.")
        if self.sample_rate is None:
            raise ValueError("Sample rate is not set. Please load an audio file first.")
        
        factor = output_frequency / self.sample_rate
        if factor < 1:
            raise ValueError("Output frequency must be greater than the original sample rate.")
        
        num_samples = int(len(self.audio_data) * factor)
        oversampled_data = np.interp(np.linspace(0, len(self.audio_data), num_samples), 
                                      np.arange(len(self.audio_data)), 
                                      self.audio_data[:, 0])
        self.audio_data = oversampled_data.reshape(-1, 1)
        self.sample_rate = output_frequency

    def save_audio(self, output_path):
        """
        Save the processed audio data to a file.

        Args:
            output_path (str): Path to save the processed audio file.
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please load an audio file first.")
        
        if output_path.lower().endswith('.wav'):
            wavfile.write(output_path, self.sample_rate, self.audio_data.astype(np.int16))
        elif output_path.lower().endswith('.mp3'):
            audio_segment = pydub.AudioSegment(
                self.audio_data.tobytes(),
                frame_rate=self.sample_rate,
                sample_width=self.audio_data.dtype.itemsize,
                channels=1
            )
            audio_segment.export(output_path, format='mp3')
        else:
            raise ValueError("Unsupported output format. Only WAV and MP3 are supported.")
#         """