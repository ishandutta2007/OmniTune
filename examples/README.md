We provide diverse examples about fine-tuning LLMs.

Make sure to execute these commands in the `OmniTune` directory.

## Table of Contents

- [LoRA Fine-Tuning](#lora-fine-tuning)
- [QLoRA Fine-Tuning](#qlora-fine-tuning)
- [Full-Parameter Fine-Tuning](#full-parameter-fine-tuning)
- [Merging LoRA Adapters and Quantization](#merging-lora-adapters-and-quantization)
- [Inferring LoRA Fine-Tuned Models](#inferring-lora-fine-tuned-models)
- [Extras](#extras)

Use `CUDA_VISIBLE_DEVICES` (GPU) or `ASCEND_RT_VISIBLE_DEVICES` (NPU) to choose computing devices.

By default, OmniTune uses all visible computing devices.

Basic usage:

```bash
omnitune train examples/train_lora/qwen3_lora_sft.yaml
```

Advanced usage:

```bash
CUDA_VISIBLE_DEVICES=0,1 omnitune train examples/train_lora/qwen3_lora_sft.yaml \
    learning_rate=1e-5 \
    logging_steps=1
```

```bash
bash examples/train_lora/qwen3_lora_sft.sh
```

## Examples

### LoRA Fine-Tuning

#### (Continuous) Pre-Training

```bash
omnitune train examples/train_lora/qwen3_lora_pretrain.yaml
```

#### Supervised Fine-Tuning

```bash
omnitune train examples/train_lora/qwen3_lora_sft.yaml
```

#### Multimodal Supervised Fine-Tuning

```bash
omnitune train examples/train_lora/qwen3vl_lora_sft.yaml
```

#### DPO/ORPO/SimPO Training

```bash
omnitune train examples/train_lora/qwen3_lora_dpo.yaml
```

#### Multimodal DPO/ORPO/SimPO Training

```bash
omnitune train examples/train_lora/qwen3vl_lora_dpo.yaml
```

#### Reward Modeling

```bash
omnitune train examples/train_lora/qwen3_lora_reward.yaml
```

#### KTO Training

```bash
omnitune train examples/train_lora/qwen3_lora_kto.yaml
```

#### Preprocess Dataset

It is useful for large dataset, use `tokenized_path` in config to load the preprocessed dataset.

```bash
omnitune train examples/train_lora/qwen3_preprocess.yaml
```

#### Supervised Fine-Tuning on Multiple Nodes

```bash
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=0 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 omnitune train examples/train_lora/qwen3_lora_sft.yaml
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=1 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 omnitune train examples/train_lora/qwen3_lora_sft.yaml
```

#### Supervised Fine-Tuning with DeepSpeed ZeRO-3 (Weight Sharding)

```bash
FORCE_TORCHRUN=1 omnitune train examples/train_lora/qwen3_lora_sft_ds3.yaml
```

#### Supervised Fine-Tuning with Ray on 4 GPUs

```bash
USE_RAY=1 omnitune train examples/train_lora/qwen3_lora_sft_ray.yaml
```

### QLoRA Fine-Tuning

#### Supervised Fine-Tuning with 4/8-bit Bitsandbytes/HQQ/EETQ Quantization (Recommended)

```bash
omnitune train examples/train_qlora/qwen3_lora_sft_otfq.yaml
```

#### Supervised Fine-Tuning with 4-bit Bitsandbytes Quantization on Ascend NPU

```bash
omnitune train examples/train_qlora/qwen3_lora_sft_bnb_npu.yaml
```

#### Supervised Fine-Tuning with 4/8-bit GPTQ Quantization

```bash
omnitune train examples/train_qlora/llama3_lora_sft_gptq.yaml
```

#### Supervised Fine-Tuning with 4-bit AWQ Quantization

```bash
omnitune train examples/train_qlora/llama3_lora_sft_awq.yaml
```

#### Supervised Fine-Tuning with 2-bit AQLM Quantization

```bash
omnitune train examples/train_qlora/llama3_lora_sft_aqlm.yaml
```

### Full-Parameter Fine-Tuning

#### Supervised Fine-Tuning on Single Node

```bash
FORCE_TORCHRUN=1 omnitune train examples/train_full/qwen3_full_sft.yaml
```

#### Supervised Fine-Tuning on Multiple Nodes

```bash
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=0 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 omnitune train examples/train_full/qwen3_full_sft.yaml
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=1 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 omnitune train examples/train_full/qwen3_full_sft.yaml
```

### Elastic and Fault-Tolerant Supervised Fine-Tuning on Multiple Nodes

To launch an elastic job with `MAX_RESTARTS` failures retries, run the following on at least `MIN_NNODES` nodes and at most `MAX_NNODES` nodes. `RDZV_ID` should be set as a unique job id (shared by all nodes participating in the job). See also [torchrun](https://docs.pytorch.org/docs/stable/elastic/run.html).

```bash
FORCE_TORCHRUN=1 MIN_NNODES=1 MAX_NNODES=3 MAX_RESTARTS=3 RDZV_ID=omnitune MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 omnitune train examples/train_full/qwen3_full_sft.yaml
```

#### Multimodal Supervised Fine-Tuning

```bash
FORCE_TORCHRUN=1 omnitune train examples/train_full/qwen3vl_full_sft.yaml
```

### Merging LoRA Adapters and Quantization

#### Merge LoRA Adapters

Note: DO NOT use quantized model or `quantization_bit` when merging LoRA adapters.

```bash
omnitune export examples/merge_lora/qwen3_lora_sft.yaml
```

#### Quantizing Model using AutoGPTQ

```bash
omnitune export examples/merge_lora/qwen3_gptq.yaml
```

### Save Ollama modelfile

```bash
omnitune export examples/merge_lora/qwen3_full_sft.yaml
```

### Inferring LoRA Fine-Tuned Models

#### Evaluation using vLLM's Multi-GPU Inference

```
python scripts/vllm_infer.py --model_name_or_path Qwen/Qwen3-4B-Instruct-2507 --template qwen3_nothink --dataset alpaca_en_demo
python scripts/eval_bleu_rouge.py generated_predictions.jsonl
```

#### Use CLI ChatBox

```bash
omnitune chat examples/inference/qwen3_lora_sft.yaml
```

#### Use Web UI ChatBox

```bash
omnitune webchat examples/inference/qwen3_lora_sft.yaml
```

#### Launch OpenAI-style API

```bash
omnitune api examples/inference/qwen3_lora_sft.yaml
```

### Extras

#### Full-Parameter Fine-Tuning using GaLore

```bash
omnitune train examples/extras/galore/llama3_full_sft.yaml
```

#### Full-Parameter Fine-Tuning using APOLLO

```bash
omnitune train examples/extras/apollo/llama3_full_sft.yaml
```

#### Full-Parameter Fine-Tuning using BAdam

```bash
omnitune train examples/extras/badam/llama3_full_sft.yaml
```

#### Full-Parameter Fine-Tuning using Adam-mini

```bash
omnitune train examples/extras/adam_mini/qwen2_full_sft.yaml
```

#### Full-Parameter Fine-Tuning using Muon

```bash
omnitune train examples/extras/muon/qwen2_full_sft.yaml
```

#### LoRA+ Fine-Tuning

```bash
omnitune train examples/extras/loraplus/llama3_lora_sft.yaml
```

#### PiSSA Fine-Tuning

```bash
omnitune train examples/extras/pissa/llama3_lora_sft.yaml
```

#### Mixture-of-Depths Fine-Tuning

```bash
omnitune train examples/extras/mod/llama3_full_sft.yaml
```

#### LLaMA-Pro Fine-Tuning

```bash
bash examples/extras/llama_pro/expand.sh
omnitune train examples/extras/llama_pro/llama3_freeze_sft.yaml
```

#### FSDP+QLoRA Fine-Tuning

```bash
bash examples/extras/fsdp_qlora/train.sh
```

#### OFT Fine-Tuning

```bash
omnitune train examples/extras/oft/llama3_oft_sft.yaml
```

#### QOFT Fine-Tuning

```bash
omnitune train examples/extras/qoft/llama3_oft_sft_bnb_npu.yaml
```
