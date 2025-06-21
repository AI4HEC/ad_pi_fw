#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: dac_interface.py
Author: Thimira Hirushan
Date: 2025-06-13
Description: This module provides a DacInterface class for interfacing with a Digital-to-Analog Converter (DAC) to output audio signals.
Version: 1.0
"""

class DacInterface:
    """
    A class to interface with a Digital-to-Analog Converter (DAC) for audio output.

    Attributes:
        dac_device (str): The device file path for the DAC.
        sample_rate (int): Sample rate for audio output in Hz.
    """

    def __init__(self, dac_device='/dev/dac', sample_rate=44100):
        """
        Initialize the DacInterface with the specified DAC device and sample rate.

        Args:
            dac_device (str): Path to the DAC device file.
            sample_rate (int): Sample rate for audio output in Hz.
        """
        self.dac_device = dac_device
        self.sample_rate = sample_rate

    def output_audio(self, audio_data):
        """
        Output audio data to the DAC.

        Args:
            audio_data (bytes): Audio data to be sent to the DAC.
        """
        with open(self.dac_device, 'wb') as dac:
            dac.write(audio_data)
