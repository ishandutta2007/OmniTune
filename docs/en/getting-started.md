# Getting Started

OmniTune is a unified, high-performance training and fine-tuning platform for 100+ large language models (LLMs) and multimodal vision-language models (VLMs).

## Supported Training Methods

| Method | Full-Parameter | Freeze Tuning | LoRA | QLoRA |
| :--- | :---: | :---: | :---: | :---: |
| **Supervised Fine-Tuning (SFT)** | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| **Direct Preference Optimization (DPO)** | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| **Reward Modeling (RM)** | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| **PPO / ORPO / KTO** | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Installation

```bash
git clone https://github.com/omnitune/omnitune.git
cd omnitune
pip install -e ".[torch,metrics]"
```

### Optional Dependencies
- **FlashAttention-2**: `pip install flash-attn --no-build-isolation`
- **DeepSpeed**: `pip install deepspeed`
- **vLLM Engine**: `pip install vllm`

## Quickstart

### 1. Zero-Code Web UI (OmniTune-Board)
Launch the interactive web interface:
```bash
omnitune webui
```
Open [http://localhost:7860](http://localhost:7860) in your browser.

### 2. Command-Line Training (CLI)
Fine-tune models using concise CLI commands or YAML configurations:
```bash
omnitune train examples/train_lora/llama3_lora_sft.yaml
```

### 3. Interactive Inference
Test your fine-tuned model via terminal chat:
```bash
omnitune chat --model_name_or_path saves/llama3-8b/lora/sft --adapter_name_or_path saves/llama3-8b/lora/sft
```
