
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
