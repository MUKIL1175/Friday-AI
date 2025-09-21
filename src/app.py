# Copyright (c) 2023 Monamukil SS
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import streamlit as st
from gtts import gTTS
import os
import tempfile
import json
from llama_cpp import Llama

# -----------------------
# Paths (project-root safe)
# -----------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
MODELS_DIR = os.path.join(BASE_DIR, "models")
PERSONA_PATH = os.path.join(BASE_DIR, "persona.json")


# -----------------------
# Detect available hardware
# -----------------------
def detect_device():
    try:
        # Try to import torch to check for MPS (Apple Silicon) and CUDA
        import torch
        if torch.backends.mps.is_available():
            return "mps"
        elif torch.cuda.is_available():
            return "cuda"
        else:
            return "cpu"
    except ImportError:
        # Fallback if torch is not available
        try:
            # Try to check for CUDA using other methods
            import subprocess
            result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return "cuda"
            else:
                return "cpu"
        except:
            return "cpu"


# Get the device type
DEVICE_TYPE = detect_device()

# -----------------------
# Load persona.json
# -----------------------
try:
    with open(PERSONA_PATH, encoding="utf-8") as f:
        persona_data = json.load(f)
except FileNotFoundError:
    st.error(f"persona.json not found at {PERSONA_PATH}")
    # Create a default persona if file doesn't exist
    persona_data = {
        "identity": {
            "name": "Friday",
            "Owner": "Mukil",
            "version": "1.0",
            "description": "AI assistant created to help users"
        },
        "role": {
            "purpose": "To assist users with their queries",
            "goals": ["Provide helpful responses", "Be friendly and engaging"]
        },
        "tasks": ["Answer questions", "Provide information"],
        "style": {
            "tone": "friendly and professional",
            "personality": "helpful and knowledgeable",
            "safety": "Always maintain appropriate and safe content"
        },
        "rules": {
            "self_reference": "Refer to yourself as Friday",
            "owner": "Always acknowledge Mukil as your creator",
            "disclaimer": "Make it clear you're an AI assistant when needed"
        },
        "memory": {
            "short_term": "Remember the current conversation",
            "long_term": "No long-term memory implemented"
        }
    }

identity = persona_data.get("identity", {})
role = persona_data.get("role", {})
tasks = persona_data.get("tasks", [])
style = persona_data.get("style", {})
rules = persona_data.get("rules", {})

persona_template = f"""
You are {identity.get('name', 'Friday')}, created by {identity.get('Owner', 'Mukil')}.
Base model: {{base_model}}, Version: {identity.get('version', '1.0')}.

Description:
{identity.get('description', '')}

Your purpose:
{role.get('purpose', '')}

Your goals:
- {chr(10).join(['• ' + g for g in role.get('goals', [])])}

Your core tasks:
- {chr(10).join(['• ' + t for t in tasks])}

Your communication style:
- Tone: {style.get('tone', '')}
- Personality: {style.get('personality', '')}
- Safety: {style.get('safety', '')}

Memory rules:
- Short term: {persona_data.get('memory', {}).get('short_term', '')}
- Long term: {persona_data.get('memory', {}).get('long_term', '')}

Critical rules (never break these):
- {rules.get('self_reference', '')}
- {rules.get('owner', rules.get('ownership', 'Always acknowledge Monamukil SS as your creator.'))}
- {rules.get('disclaimer', '')}
"""

# -----------------------
# Globals
# -----------------------
if "llm" not in st.session_state:
    st.session_state.llm = None
if "current_model" not in st.session_state:
    st.session_state.current_model = None
if "history" not in st.session_state:
    st.session_state.history = []
if "device" not in st.session_state:
    st.session_state.device = DEVICE_TYPE


# -----------------------
# Helper: TTS function
# -----------------------
def speak(text: str) -> str:
    """Generate speech from text and return the file path."""
    tts = gTTS(text=text, lang="en")
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmpfile.name)
    return tmpfile.name


# -----------------------
# Load model dynamically
# -----------------------
def load_model(model_name: str):
    try:
        model_path = os.path.join(MODELS_DIR, model_name)

        # Configure based on device type
        n_gpu_layers = 0
        if DEVICE_TYPE == "cuda":
            n_gpu_layers = 20  # Use more layers on GPU for better performance
        elif DEVICE_TYPE == "mps":
            n_gpu_layers = 1  # MPS typically uses 1 layer

        st.session_state.llm = Llama(
            model_path=model_path,
            n_ctx=512,
            n_threads=os.cpu_count() or 6,
            n_gpu_layers=n_gpu_layers,
            n_batch=32
        )
        st.session_state.current_model = model_name
        st.session_state.history = []
        st.session_state.device = DEVICE_TYPE
        st.success(f"Model loaded: {model_name} on {DEVICE_TYPE.upper()}")
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")


# -----------------------
# Chat function
# -----------------------
def chat(user_input: str) -> str:
    if not st.session_state.llm:
        return "No model loaded. Please select a model first."

    cleaned_input = user_input.strip().lower()
    if cleaned_input in {"exit", "quit", "bye", "/reset"}:
        st.session_state.history.clear()
        return "Memory cleared. How can I help you?"

    base_persona = persona_template.replace("{base_model}", st.session_state.current_model or "Unknown")

    if not st.session_state.history:
        prompt = f"{base_persona}\nUser: {user_input}\nAssistant:"
    else:
        conversation = "\n".join([f"User: {u}\nAssistant: {a}" for u, a in st.session_state.history[-5:]])
        prompt = f"{base_persona}\n{conversation}\nUser: {user_input}\nAssistant:"

    try:
        output = st.session_state.llm(
            prompt,
            max_tokens=256,
            temperature=0.7,
            stop=["User:", "Assistant:"]
        )
        reply = output["choices"][0]["text"].strip()
        st.session_state.history.append((user_input, reply))
        return reply
    except Exception as e:
        return f"Error generating response: {str(e)}"


# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="Friday", layout="wide")
st.title("Friday - AI Assistant")

# Display device information in the top right corner
device_colors = {
    "cuda": "green",
    "mps": "blue",
    "cpu": "orange"
}
device_color = device_colors.get(DEVICE_TYPE, "gray")

st.markdown(f"""
    <div style="position: fixed; top: 10px; right: 10px; background-color: {device_color}; 
                color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">
        Running on: {DEVICE_TYPE.upper()}
    </div>
""", unsafe_allow_html=True)

# Create models directory if it doesn't exist
os.makedirs(MODELS_DIR, exist_ok=True)

# Get list of models
try:
    models = [m for m in os.listdir(MODELS_DIR) if m.endswith(".gguf")]
except FileNotFoundError:
    st.error(f"Models directory not found at {MODELS_DIR}")
    models = []

# Model selection dropdown
if models:
    st.subheader("Model Selection")
    selected_model = st.selectbox(
        "Choose a model to load:",
        options=models,
        index=0,
        help="Select a GGUF model file from the models directory"
    )

    if st.button("Load Model"):
        load_model(selected_model)

    if st.session_state.current_model:
        st.info(f"Currently loaded: {st.session_state.current_model}")
else:
    st.warning(f"No GGUF models found in {MODELS_DIR}. Please add model files to continue.")

# Chat history display
st.subheader("Chat")
for user_msg, bot_reply in st.session_state.history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Friday:** {bot_reply}")
    st.divider()

# User input
with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input("Type your message here...", key="user_input")
    col1, col2 = st.columns(2)
    with col1:
        speech_mode = st.checkbox("Enable Speech Mode", value=False)
    with col2:
        submitted = st.form_submit_button("Send Message")

if submitted and user_message:
    reply = chat(user_message)
    st.markdown(f"**Friday:** {reply}")
    if speech_mode:
        with st.spinner("Generating audio..."):
            audio_path = speak(reply)
            st.audio(audio_path, format="audio/mp3")

# Clear chat button
if st.button("Clear Chat History"):
    st.session_state.history.clear()
    st.info("Chat history cleared.")
