# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Code style (auto-fix)
make style

# Code quality check (no modifications)
make quality

# Run all tests
make test

# Run a single test file
WANDB_DISABLED=true pytest -vv --import-mode=importlib tests/path/to/test_file.py

# Run tests matching a pattern
WANDB_DISABLED=true pytest -vv --import-mode=importlib tests/ -k "test_name"

# License header check
make license

# Build package
make build
```

The project uses `uv` as the preferred package manager. Commands automatically use `uv run` / `uvx` if `uv` is available.

## Architecture

OmniTune has two parallel architectures controlled by the `USE_V1` environment variable:

- **v0 (default):** `api, webui > chat, eval, train > data, model > hparams > extras`
- **v1 (experimental, `USE_V1=1`):** `trainers > core > accelerator, plugins, config > utils`

Most active development happens in v0. The v1 architecture lives in `src/omnitune/v1/`.

### Entry Points

CLI entry points are `omnitune` / `ot` / `omnitune-cli` (backward-compat `llamafactory-cli` / `lmf`) → `src/omnitune/cli.py:main()`, which dispatches to `launcher.py` based on `USE_V1`.

Available subcommands: `train`, `chat`, `api`, `export`, `webchat`, `webui`, `env`, `version`, `help`.

### Training Flow (v0)

```
run_exp() [tuner.py]
  → read_args() → parse YAML/JSON config
  → get_train_args() → produces typed argument dataclasses
  → routes to: run_sft / run_dpo / run_ppo / run_rm / run_pt / run_kto
  → optional: export_model()
```

Training is invoked with a YAML config: `omnitune train examples/train_lora/llama3_lora_sft.yaml`

### Configuration System

All training parameters are YAML/JSON config files. Argument parsing in `src/omnitune/hparams/parser.py` produces four typed dataclasses:
- `ModelArguments` — model/tokenizer selection, quantization
- `DataArguments` — datasets, templates, preprocessing
- `FinetuningArguments` — LoRA rank/target, training method (sft/dpo/ppo/rm/pt/kto)
- `TrainingArguments` — extends HuggingFace's `TrainingArguments`

### Key Modules

| Module | Purpose |
|--------|---------|
| `src/omnitune/model/loader.py` | Loads model + tokenizer; applies quantization, LoRA, patches |
| `src/omnitune/model/patcher.py` | Model-specific compatibility patches |
| `src/omnitune/data/template.py` | Prompt templates; `TEMPLATES` dict maps model family → format |
| `src/omnitune/data/mm_plugin.py` | Multi-modal (image/video/audio) data handling |
| `src/omnitune/data/processor/` | Per-stage data processors (supervised, pairwise, pretrain, etc.) |
| `src/omnitune/train/sft/` | SFT trainer; other stages follow same structure |
| `src/omnitune/chat/` | Inference engines: `hf_engine`, `vllm_engine`, `sglang_engine`, `kt_engine` |
| `src/omnitune/extras/constants.py` | Enums and constants used across the project |

### Adding Support for a New Model

1. Add a prompt template to `src/omnitune/data/template.py` in the `TEMPLATES` dict
2. Add any necessary model patches in `src/omnitune/model/patcher.py`
3. Add multi-modal support in `src/omnitune/data/mm_plugin.py` if needed

### Distributed Training

Multi-GPU automatically uses `torchrun`. Additional backends:
- **Ray:** Optional Ray cluster support
- **HyperParallel FSDP2:** `src/omnitune/train/hyper_parallel/`
- **Megatron-core:** `src/omnitune/train/mca/`

### Testing

- `tests/` — v0 tests; `tests_v1/` — v1 tests
- Most training tests require GPU hardware
- pytest markers: `@pytest.mark.slow`, `@pytest.mark.runs_on(['cuda'])`
- Always set `WANDB_DISABLED=true` when running tests

### Code Style

- Ruff for linting and formatting (line length 119, Google-style docstrings)
- Python 3.11+ syntax
- Double quotes for strings
- All new files must include Apache 2.0 license header (checked by `make license`)
