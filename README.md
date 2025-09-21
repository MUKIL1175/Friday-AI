
# Friday - Offline AI Assistant for MacBook Air (M-Series)

[](https://img.shields.io/badge/Platform-macOS-blue) ![Friday AI Assistant](https://img.shields.io/badge/Model-GGUF-green) ![Friday AI Assistant](https://img.shields.io/badge/Privacy-Offline-purple) ![Friday AI Assistant](https://img.shields.io/badge/Python-3.9%2B-yellow) ![Friday AI Assistant](https://img.shields.io/badge/UI-Streamlit-red)

Friday is a privacy-focused, offline AI assistant specifically optimized for MacBook Air with Apple Silicon (M1/M2/M3 chips). It runs completely offline without requiring internet connectivity, ensuring your conversations remain private and secure.

## Features

- **Complete Privacy**: All processing happens locally on your device - no data leaves your computer
- **Apple Silicon Optimized**: Leverages MPS (Metal Performance Shaders) for optimal performance on MacBook Air
- **Text-to-Speech**: Built-in speech synthesis for vocal responses using gTTS
- **Multiple Model Support**: Compatible with various GGUF format LLMs
- **Custom Persona**: Configurable AI personality through JSON configuration
- **Fast Inference**: Optimized for Apple's Neural Engine and Metal API
- **Energy Efficient**: Designed to minimize battery consumption on MacBook Air
- **Conversation Memory**: Maintains context within sessions
- **Clean UI**: Streamlit-based intuitive interface
## Getting Started
### Prerequisites

- macOS 12.0 or later (Ventura or newer recommended)
- MacBook Air with Apple Silicon (M1/M2/M3)
- Python 3.9 or later
- Xcode Command Line Tools

1.**Installation**:
```bash
Clone the repository:

git clone https://github.com/MUKIL1175/Friday-AI.git
cd Friday-AI
```

2. **Set up virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up llama.cpp (optional but recommended for best performance)**:
```bash
# Clone llama.cpp
git clone https://github.com/ggerganov/llama.cpp.git

# Build with MPS support
cd llama.cpp
LLAMA_METAL=1 make -j
cd ../python
pip install -e .
cd ..
```

5. **Add your GGUF model files** to the `src/models/` directory

6. **Configure your AI persona** in `src/persona.json` (optional)

### Running the Application

```bash
streamlit run src/app.py
```

The application will open in your default browser at `http://localhost:8501`

##  Performance Optimization

Friday is specifically optimized for MacBook Air with:

- **MPS Acceleration**: Uses Apple's Metal Performance Shaders for GPU acceleration
- **Memory Efficiency**: Optimized context windows for limited RAM (8GB/16GB configurations)
- **Energy Efficient**: Designed to minimize battery consumption during use
- **Thermal Management**: Runs cool even during extended sessions
- **Adaptive Loading**: Automatically detects and uses available hardware (MPS → CUDA → CPU)

### Hardware Requirements

| Component | Minimum        | Recommended |
|-----------|----------------|-------------|
| RAM | 8GB            | 16GB+ |
| Storage | 4GB free space | 10GB+ for multiple models |
| macOS | 12.0+          | 13.0+ |
| Model Size | 7B 4-bit       | 7B-13B 4-bit |

## Project Structure

```
Friday-AI/
├── .venv/                 # Virtual environment
├── llama.cpp/             # Local llama.cpp installation (optional)
├── src/
│   ├── models/            # GGUF model files (add your own)
│   ├── app.py             # Main application
│   └── persona.json       # AI personality configuration
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License
└── README.md             # This file
```

## Configuration

### Model Support

Friday supports any model in GGUF format. Recommended models for MacBook Air:

| Model | Size | Quality | Speed | RAM Usage |
|-------|------|---------|-------|-----------|
| **Phi-3-mini** | 3.8B (Q4) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ~3GB |
| **Llama-2-7B** | 7B (Q4) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ~5GB |
| **Mistral-7B** | 7B (Q4) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ~5GB |
| **Gemma-2B** | 2B (Q4) | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ~2GB |

### Persona Customization

Edit `src/persona.json` to customize your AI assistant's personality:

```json
{
  "identity": {
    "name": "Friday",
    "Owner": "Mukil",
    "version": "1.0",
    "description": "Your helpful AI assistant"
  },
  "role": {
    "purpose": "To assist users with tasks and information",
    "goals": ["Provide accurate information", "Be helpful and friendly"]
  },
  "tasks": ["Answer questions", "Provide explanations", "Assist with tasks"],
  "style": {
    "tone": "friendly and professional",
    "personality": "helpful and knowledgeable",
    "safety": "Always maintain appropriate content"
  }
}
```

## Performance Tips

1. **Use Quantized Models**: Q4_K_M models provide the best balance of quality and performance
2. **Limit Context**: Keep context window reasonable (512-1024 tokens) for better performance
3. **Close Memory-Intensive Apps**: Free up RAM and GPU resources for optimal performance
4. **Keep macOS Updated**: Ensure you have the latest Metal and MPS optimizations
5. **Use Low Power Mode**: For extended battery life during casual use
6. **Monitor Temperature**: Ensure proper ventilation for sustained performance

### For NVIDIA GPU Users:
- Required CUDA Toolkit 12+
- Latest NVIDIA drivers
- Minimum 6GB of VRAM recommended
- Set `n_gpu_layers` to 20+ in app.py for better GPU utilization

##  Troubleshooting

### Common Issues:

1. **"Model not loading"**:
   - Ensure GGUF model files are in the `src/models/` directory
   - Check that the model is compatible with your hardware

2. **"MPS not available"**:
   - Update to latest macOS version
   - Ensure you're on Apple Silicon hardware

3. **"Audio not working"**:
   - Check browser permissions for audio playback
   - Ensure system volume is not muted

4. **"Performance is slow"**:
   - Try a smaller model (3B-7B instead of 13B+)
   - Reduce context length in the code

## Contributing

We welcome contributions! Please feel free to:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/MUKIL1175/Friday-AI/issues) page
2. Search existing issues for solutions
3. Create a new issue with detailed information about your problem
4. Include your macOS version, hardware details, and error messages

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Developer

**Monamukil**

- 🔗 LinkedIn: [Monamukil SS](https://www.linkedin.com/in/mukil1175/)
- 🔗 GitHub: [@MUKIL1175](https://github.com/MUKIL1175)
- 🔗 Instagram: [@monamukil](https://www.instagram.com/monamukil/)

## Acknowledgments

- Thanks to the [llama.cpp](https://github.com/ggerganov/llama.cpp) team for making efficient inference possible
- Apple for MPS framework enabling GPU acceleration on Apple Silicon
- The open-source community for various GGUF model quantizations
- Streamlit team for the excellent web framework
- Google for gTTS text-to-speech functionality

**⭐ If you find this project useful, please give it a star on GitHub!**

---

*Friday - Your private AI companion for MacBook Air* 

> "Privacy isn't an option, it's a requirement. Friday keeps your conversations where they belong - on your device."
