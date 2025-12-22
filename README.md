# 📘 LLM Fine-tuning Impact Analysis on LLM Behavior

This project demonstrates an **interactive analysis system** to compare the behavior of a **base language model** and a **fine-tuned language model**, based on concepts from **HW8: Fine-tuning Leads to Forgetting**.  
The system is implemented using **Streamlit** and follows the **CRISP-DM methodology**.

🔗 **Live Demo (Streamlit Cloud):**  
👉 [Run the App Here](https://aiothw4taica-aigc-application-edfolp2vlbsvownf5vi5bk.streamlit.app)
---

## 🔍 Project Overview

- **Goal**  
  Analyze how fine-tuning changes the behavior of large language models (LLMs), including instruction-following, reasoning style, and output structure.

- **Approach**  
  Build an interactive demo that allows users to input prompts and compare outputs from:
  - a base LLM
  - a fine-tuned LLM (behavior simulated based on HW8 concepts)

- **Key Concept**  
  *Catastrophic Forgetting* — fine-tuning on a specific task may improve performance on that task while degrading other capabilities.


---

# 🧭 CRISP-DM Steps

## 1️⃣ Business Understanding

The objective of this project is to **understand and visualize the impact of fine-tuning on LLM behavior**.  
Instead of focusing only on accuracy, this project emphasizes **behavioral changes**, such as:

- Instruction-following tendency  
- Step-by-step reasoning bias  
- Reduced diversity in open-ended responses  

This aligns with the course topic *“Fine-tuning Leads to Forgetting”*.

---

## 2️⃣ Data Understanding

- No external dataset is required.
- Input data consists of **user-provided prompts**, including:
  - General knowledge questions
  - Instruction-following prompts
  - Reasoning-oriented prompts
  - Open-ended creative prompts

The generated outputs are treated as qualitative data for comparison.

---

## 3️⃣ Data Preparation

- Prompts are taken directly from user input.
- To simulate fine-tuning behavior:
  - The original prompt is **augmented with a step-by-step instruction**
  - This reflects the bias introduced by fine-tuning on structured tasks (as discussed in HW8)

Example:

---

## 4️⃣ Modeling

- **Model type**: Transformer-based language model
- **Implementation**: HuggingFace `transformers` pipeline
- **Model used for demo stability**:
  - `distilgpt2` (lightweight and CPU-friendly)

Two models are instantiated:
- **Base model**: receives the original prompt
- **Fine-tuned model**: receives the modified (instruction-biased) prompt

> For demonstration stability, a lightweight model is used.  
> The fine-tuning concept and behavioral interpretation follow HW8.

---

## 5️⃣ Evaluation

The evaluation is **qualitative and behavior-oriented**, focusing on:

- Output length
- Structural organization
- Instruction adherence
- Reasoning style

Example comparison:

| Aspect | Base Model | Fine-tuned Model |
|---|---|---|
| Instruction following | Moderate | Strong |
| Step-by-step reasoning | Rare | Frequent |
| Creativity | Higher | Lower |
| Output structure | Loose | Structured |

These observations are consistent with the catastrophic forgetting phenomenon discussed in HW8.

---

## 6️⃣ Deployment

The system is deployed as an **interactive Streamlit web application**, allowing real-time testing and visualization.

### Features
- Custom prompt input
- Side-by-side output comparison
- Simple quantitative metrics (word count)
- Stable execution on CPU environments

---

# 🚀 How to Run the Project

## 1️⃣ Environment Setup

Python **3.10** is recommended (Conda environment suggested).

```bash
conda activate pycaret_env
