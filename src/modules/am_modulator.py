#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: am_modulator.py
Author: Thimira Hirushan
Date: 2025-06-13
Description: This module implements an AmModulator class for amplitude modulation of audio signals.
Version: 1.0
"""

import numpy as np

class AmModulator:
    """
    A class to perform amplitude modulation on audio signals.

    Attributes:
        carrier_freq (float): Frequency of the carrier wave in Hz.
        modulating_signal (np.ndarray): The modulating signal to be used for modulation.
        sample_rate (int): Sample rate of the audio signal in Hz.
    """

    def __init__(self, carrier_freq, modulating_signal, sample_rate):
        """
        Initialize the AmModulator with carrier frequency, modulating signal, and sample rate.

        Args:
            carrier_freq (float): Frequency of the carrier wave in Hz.
            modulating_signal (np.ndarray): The modulating signal to be used for modulation.
            sample_rate (int): Sample rate of the audio signal in Hz.
        """
        self.carrier_freq = carrier_freq
        self.modulating_signal = modulating_signal
        self.sample_rate = sample_rate

    def modulate(self):
        """
        Perform amplitude modulation on the modulating signal using the carrier frequency.

        Returns:
            np.ndarray: The modulated audio signal.
        """
        t = np.arange(len(self.modulating_signal)) / self.sample_rate
        carrier_wave = np.cos(2 * np.pi * self.carrier_freq * t)
        return self.modulating_signal * carrier_wave
    
    def set_carrier_freq(self, carrier_freq):
        """
        Set a new carrier frequency for modulation.
        Args:
            carrier_freq (float): New frequency of the carrier wave in Hz.
        """
        self.carrier_freq = carrier_freq
    
    def set_modulating_signal(self, modulating_signal):
        """
        Set a new modulating signal for modulation.
        Args:
            modulating_signal (np.ndarray): New modulating signal to be used for modulation.
        """
        self.modulating_signal = modulating_signal

    def set_sample_rate(self, sample_rate):
        """
        Set a new sample rate for the audio signal.
        Args:
            sample_rate (int): New sample rate of the audio signal in Hz.
        """
        self.sample_rate = sample_rate

    def get_modulated_signal(self):
        """
        Get the current modulated signal.
        Returns:
            np.ndarray: The current modulated audio signal.
        """
        return self.modulate()


