# Friday - Offline AI Assistant for MacBook Air(M-Series)

![Friday AI Assistant](https://img.shields.io/badge/Platform-macOS-blue) ![Friday AI Assistant](https://img.shields.io/badge/Model-GGUF-green) ![Friday AI Assistant](https://img.shields.io/badge/Privacy-Offline-purple)

Friday is a privacy-focused, offline AI assistant specifically optimized for MacBook Air with Apple Silicon (M1/M2 chips). It runs completely offline without requiring internet connectivity, ensuring your conversations remain private and secure.

## ✨ Features

- **Complete Privacy**: All processing happens locally on your device
- **Apple Silicon Optimized**: Leverages MPS (Metal Performance Shaders) for optimal performance on MacBook Air
- **Text-to-Speech**: Built-in speech synthesis for vocal responses
- **Multiple Model Support**: Compatible with various GGUF format LLMs
- **Custom Persona**: Configurable AI personality through JSON
- **Fast Inference**: Optimized for Apple's Neural Engine

## 🚀 Getting Started

### Prerequisites

- macOS 12.0 or later
- MacBook Air with Apple Silicon (M1/M2)
- Python 3.9 or later

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MUKIL1175/Friday-AI.git
cd Friday-AI
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add your GGUF model files to the `models/` directory

5. Configure your AI persona in `persona.json` (optional)

### Running the Application

```bash
streamlit run src/app.py
```

## 🎯 Performance Optimization

Friday is specifically optimized for MacBook Air with:

- **MPS Acceleration**: Uses Apple's Metal Performance Shaders for GPU acceleration
- **Memory Efficiency**: Optimized context windows for limited RAM
- **Energy Efficient**: Designed to minimize battery consumption
- **Thermal Management**: Runs cool even during extended sessions

## 📁 Project Structure

```
Friday/
├── .venv/                 # Virtual environment
├── llama.cpp              # Clone the llama.cpp(if required)
├── src/
│   ├── models/           # GGUF model files (add your own)
│   ├── app.py            # Main application
│   └── persona.json      # AI personality configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Configuration

### Model Support

Friday supports any model in GGUF format. Recommended models for MacBook Air:

- **phi-3-mini-4k-instruct.Q4_K_M.gguf** (Lightweight & fast)
- **llama-2-7b-chat.Q4_K_M.gguf** (Balanced performance)
- **mistral-7b-instruct-v0.2.Q4_K_M.gguf** (High quality)

### Persona Customization

Edit `src/persona.json` to customize your AI assistant's personality:

```json
{
  "identity": {
    "name": "Friday",
    "Owner": "Mukil",
    "version": "1.0",
    "description": "Friendly companion"
  },
  "role": {
    "purpose": "Assistant's purpose",
    "goals": ["Goal 1", "Goal 2"]
  }
}
```

## 🏎️ Performance Tips

1. **Use Quantized Models**: Q4_K_M models provide the best balance of quality and performance
2. **Limit Context**: Keep context window reasonable (512-1024 tokens) for better performance
3. **Close Other Apps**: Free up RAM and GPU resources for optimal performance
4. **Keep macOS Updated**: Ensure you have the latest Metal and MPS optimizations
5. **For Nvidia**: Required CUDA Toolkit 12, driver up to date and required 6GB of VRAM 
## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/MUKIL1175/Friday-AI/issues) page
2. Create a new issue with detailed information about your problem

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Developer

**Mukil**  
*AI Engineer & macOS Developer*

- 🔗 LinkedIn: [Monamukil SS](https://www.linkedin.com/in/mukil1175/)
-  🔗 GitHub: [@Monamukil SS](https://github.com/MUKIL1175)
-  🔗 Instagram: [@Friday](https://www.instagram.com/monamukil/)
## 🙏 Acknowledgments

- Thanks to the [llama.cpp](https://github.com/ggerganov/llama.cpp) team for making efficient inference possible
- Apple for MPS framework enabling GPU acceleration on Apple Silicon
- The open-source community for various GGUF model quantizations

---

**⭐ If you find this project useful, please give it a star on GitHub!**

---

*Friday - Your private AI companion for MacBook Air* 