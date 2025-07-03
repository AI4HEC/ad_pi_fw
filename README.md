# ad_pi_fw
Speaker array driver, Rapsberry-pi firmware

## Firmware Overview: `ad_pi_fw` - Audio Processing & Speaker Array Driver

This is a **Raspberry Pi firmware for a speaker array driver** that implements audio signal processing, amplitude modulation, and HiFi DAC output capabilities. The system is designed to process audio files and transmit them through a high-quality digital-to-analog converter.

### 🎯 **Core Purpose**
The firmware creates a sophisticated audio processing pipeline that:
- Loads and processes audio files (WAV/MP3)
- Applies amplitude modulation at ultrasonic frequencies
- Outputs the processed signal through a HiFi DAC for speaker array control

### 🏗️ **System Architecture**

#### **Configuration (config.yaml)**
- **Audio Settings**: 192 kHz sample rate, 16-bit depth
- **Modulation**: 40 kHz carrier frequency with 0.9 modulation index
- **DAC Interface**: SPI-based (Bus 0, Device 0), 16-bit resolution, 3.3V reference

#### **Core Modules**

1. **`AudioProcessor`** (audio_processor.py)
   - Loads WAV and MP3 audio files
   - Converts to mono (monotone)
   - Normalizes audio data to [-1, 1] range
   - Applies pre-emphasis filtering (α=0.97)
   - Performs oversampling to target frequency (192 kHz)
   - Saves processed audio files

2. **`AmModulator`** (am_modulator.py)
   - Implements amplitude modulation (AM)
   - Uses 40 kHz carrier frequency (ultrasonic)
   - Multiplies audio signal with carrier wave
   - Configurable carrier frequency and modulation parameters

3. **`DacInterface`** (dac_interface.py)
   - Interfaces with DAC hardware via device file (`/dev/dac`)
   - Outputs processed audio data as raw bytes
   - Configurable sample rate support

4. **`ConfigManager`** (config.py)
   - YAML-based configuration management
   - Runtime configuration updates
   - Settings persistence

### 🔄 **Signal Processing Pipeline**

```
Audio File (WAV/MP3) 
    ↓
Audio Processing (normalize, mono, pre-emphasis)
    ↓
Oversampling to 192 kHz
    ↓
Amplitude Modulation (40 kHz carrier)
    ↓
DAC Output via SPI
    ↓
Speaker Array
```

### 🎛️ **Key Features**

- **High-Quality Audio**: 192 kHz sampling, 16-bit resolution
- **Ultrasonic Modulation**: 40 kHz carrier for specialized applications
- **Multi-Format Support**: WAV and MP3 input files
- **SPI DAC Interface**: Direct hardware control
- **Configurable Parameters**: YAML-based settings management
- **Signal Processing**: Pre-emphasis, normalization, oversampling

### 🧪 **Testing Infrastructure**
The firmware includes comprehensive tests for:
- `test_am_modulator.py` - AM modulation functionality
- `test_audio_processor.py` - Audio processing pipeline
- `test_dac_interface.py` - DAC hardware interface

### 💡 **Technical Applications**

This firmware appears designed for specialized audio applications such as:
- **Directional Audio Systems** (using ultrasonic carriers)
- **Audio Beamforming** with speaker arrays
- **Parametric Speakers** (ultrasonic demodulation)
- **High-fidelity audio research** and prototyping

The 40 kHz carrier frequency suggests this might be implementing **parametric audio** or **directional audio** technology, where ultrasonic frequencies are used to create focused audio beams that demodulate in air to produce audible sound.

### 📦 **Dependencies**
- `PyYAML` - Configuration management
- `numpy` - Numerical processing
- `scipy` - Signal processing
- `pydub` - Audio file handling

The firmware is well-structured with clear separation of concerns, comprehensive error handling, and a modular design that allows for easy extension and testing.