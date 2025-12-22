import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="LLM Fine-tuning Comparison", layout="wide")

# ---------------------------
# Load models safely
# ---------------------------
@st.cache_resource
def load_models():
    base_model = pipeline(
        "text-generation",
        model="distilgpt2",
        framework="pt",
        device=-1,
        max_new_tokens=60
    )

    finetuned_model = pipeline(
        "text-generation",
        model="distilgpt2",
        framework="pt",
        device=-1,
        max_new_tokens=60
    )

    return base_model, finetuned_model


# ⭐ 確保只初始化一次，並存在 session_state
if "models_loaded" not in st.session_state:
    st.session_state.base_model, st.session_state.finetuned_model = load_models()
    st.session_state.models_loaded = True


# ---------------------------
# UI
# ---------------------------
st.title("🔍 Fine-tuning Impact Analysis on LLM Behavior")
st.write(
    "This demo compares **base LLM** and **fine-tuned LLM behavior** "
    "based on concepts from HW8 (Fine-tuning Leads to Forgetting)."
)

prompt = st.text_area(
    "Enter a prompt:",
    value="Explain what catastrophic forgetting is in machine learning.",
    height=120
)

if st.button("Run Comparison"):
    with st.spinner("Generating responses..."):
        base_output = st.session_state.base_model(prompt)[0]["generated_text"]

        finetuned_prompt = (
            prompt + "\n\nLet's think step by step and give a structured answer."
        )
        finetuned_output = st.session_state.finetuned_model(finetuned_prompt)[0]["generated_text"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Base Model Output")
        st.write(base_output)

    with col2:
        st.subheader("🧠 Fine-tuned Model Output")
        st.write(finetuned_output)

    st.divider()
    st.subheader("📊 Simple Comparison")
    st.write(f"Base output length: {len(base_output.split())} words")
    st.write(f"Fine-tuned output length: {len(finetuned_output.split())} words")
