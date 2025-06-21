#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: config.py
Author: Thimira Hirushan
Date: 2025-06-12
Description: This module provides functions to load and save configuration settings from a YAML file.
Version: 1.0
"""

import os
import yaml

class ConfigManager:
    """
    A class to manage configuration settings stored in a YAML file.

    Attributes:
        config_file (str): Path to the YAML configuration file.
        config (dict): Dictionary holding the configuration data.

    Methods:
        save(): Save the current configuration to the YAML file.
        update(new_settings): Update the configuration with new settings and save.
        get(key, default=None): Retrieve a value for a given key.
        set(key, value): Set a value for a given key and save.
        delete(key): Delete a key from the configuration and save.
        keys(): Return a list of all configuration keys.
        clear(): Clear all configuration settings and save.
        exists(): Check if the configuration file exists.
    """

    def __init__(self, config_file='config.yaml'):
        """
        Initialize the ConfigManager.

        Args:
            config_file (str): Path to the YAML configuration file.
        """
        self.config_file = config_file
        self.config = self._load()

    def _load(self):
        """
        Load the configuration from the YAML file.

        Returns:
            dict: The loaded configuration, or an empty dict if the file does not exist.
        """
        if not os.path.exists(self.config_file):
            return {}
        with open(self.config_file, 'r') as file:
            config = yaml.safe_load(file)
            return config if config else {}

    def save(self):
        """
        Save the current configuration to the YAML file.
        """
        with open(self.config_file, 'w') as file:
            yaml.safe_dump(self.config, file, default_flow_style=False)

    def update(self, new_settings):
        """
        Update the configuration with new settings and save.

        Args:
            new_settings (dict): Dictionary of settings to update.
        """
        self.config.update(new_settings)
        self.save()

    def get(self, key, default=None):
        """
        Retrieve a value for a given key.

        Args:
            key (str): The configuration key.
            default: The default value if the key is not found.

        Returns:
            The value for the key, or default if not found.
        """
        return self.config.get(key, default)

    def set(self, key, value):
        """
        Set a value for a given key and save.

        Args:
            key (str): The configuration key.
            value: The value to set.
        """
        self.config[key] = value
        self.save()

    def delete(self, key):
        """
        Delete a key from the configuration and save.

        Args:
            key (str): The configuration key to delete.
        """
        if key in self.config:
            del self.config[key]
            self.save()

    def keys(self):
        """
        Return a list of all configuration keys.

        Returns:
            list: List of configuration keys.
        """
        return list(self.config.keys())

    def clear(self):
        """
        Clear all configuration settings and save.
        """
        self.config = {}
        self.save()

    def exists(self):
        """
        Check if the configuration file exists.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(self.config_file)



