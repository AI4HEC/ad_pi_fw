#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: audio_processor.py
Author: Thimira Hirushan
Date: 2025-06-12
Description: A module for processing audio files, including loading, pre-emphasizing,
             oversampling, and saving audio files. Supports both WAV and MP3 formats.
"""

import numpy as np
from scipy.io import wavfile
import pydub

class AudioProcessor:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        
    def load_audio(self, file_path):
        """Load audio file and convert to mono"""
        if file_path.endswith('.mp3'):
            audio = pydub.AudioSegment.from_mp3(file_path)
            samples = np.array(audio.get_array_of_samples())
            if audio.channels > 1:
                samples = samples[::audio.channels]  # convert to mono
        elif file_path.endswith('.wav'):
            rate, samples = wavfile.read(file_path)
            if len(samples.shape) > 1:
                samples = samples[:, 0]  # take left channel
            if rate != self.sample_rate:
                # Simple resampling (for better quality consider libsamplerate)
                ratio = self.sample_rate / rate
                samples = np.interp(
                    np.arange(0, len(samples), ratio),
                    np.arange(0, len(samples)),
                    samples
                )
        else:
            raise ValueError("Unsupported file format")
            
        # Normalize to [-1, 1]
        samples = samples / np.max(np.abs(samples))
        return samples
    
    def pre_emphasize(self, samples, alpha=0.97):
        """Apply pre-emphasis to enhance high frequencies"""
        emphasized = np.zeros_like(samples)
        emphasized[0] = samples[0]
        for i in range(1, len(samples)):
            emphasized[i] = samples[i] - alpha * samples[i-1]
        return emphasized
    
    def oversample(self, samples, output_frequency):
        """Oversample audio to a higher frequency"""
        if output_frequency <= self.sample_rate:
            raise ValueError("Output frequency must be greater than sample rate")
        
        ratio = output_frequency / self.sample_rate
        oversampled = np.interp(
            np.arange(0, len(samples), ratio),
            np.arange(0, len(samples)),
            samples
        )
        return oversampled
    
    def save_audio(self, samples, file_path):
        """Save audio samples to a file"""
        samples = (samples * 32767).astype(np.int16)
        if file_path.endswith('.wav'):
            wavfile.write(file_path, self.sample_rate, samples)
        elif file_path.endswith('.mp3'):
            audio_segment = pydub.AudioSegment(
                samples.tobytes(), 
                frame_rate=self.sample_rate, 
                sample_width=2, 
                channels=1
            )
            audio_segment.export(file_path, format='mp3')
        else:
            raise ValueError("Unsupported file format for saving")