# Copyright 2025 the OmniTune team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""OmniTune v1 Next-Generation Engine.

Architecture:
  trainers > core > accelerator, plugins, config > utils
"""

from .core.base_trainer import BaseTrainer
from .core.data_engine import DataEngine
from .core.model_engine import ModelEngine
from .trainers.dpo_trainer import DPOTrainer, run_dpo
from .trainers.rm_trainer import RMTrainer, run_rm
from .trainers.sft_trainer import SFTTrainer, run_sft


__all__ = [
    "BaseTrainer",
    "DPOTrainer",
    "DataEngine",
    "ModelEngine",
    "RMTrainer",
    "SFTTrainer",
    "run_dpo",
    "run_rm",
    "run_sft",
]
