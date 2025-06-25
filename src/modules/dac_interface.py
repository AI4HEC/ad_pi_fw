#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: dac_interface.py
Author: Thimira Hirushan
Date: 2025-06-13
Description: This module provides a DacInterface class for interfacing with a Digital-to-Analog Converter (DAC) to output audio signals.
Version: 1.0
"""

import sounddevice as sd
import numpy as np

class DacInterface:
    """
    A class to interface with a Digital-to-Analog Converter (DAC) for audio output.

    Attributes:
        sample_rate (int): Sample rate for audio output in Hz.
        device (str or int): ALSA device name or index.
    """

    def __init__(self, sample_rate=44100, device=None):
        """
        Initialize the DacInterface with the specified sample rate and device.

        Args:
            sample_rate (int): Sample rate for audio output in Hz.
            device (str or int): ALSA device name or index.
        """
        self.sample_rate = sample_rate
        self.device = device  # ALSA device name or index

    def output_audio(self, audio_data):
        """
        Output audio data to the DAC.

        Args:
            audio_data (numpy.ndarray): Audio data to be sent to the DAC (float32, -1.0 to 1.0).
        """
        sd.play(audio_data, samplerate=self.sample_rate, device=self.device)
        sd.wait()

