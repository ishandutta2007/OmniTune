# Copyright 2025 the LlamaFactory team.
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

import pytest

from llamafactory.eval.template import get_eval_template


@pytest.mark.runs_on(["cpu", "mps"])
def test_eval_template_en():
    support_set = [
        {
            "question": "Fewshot question",
            "A": "Fewshot1",
            "B": "Fewshot2",
            "C": "Fewshot3",
            "D": "Fewshot4",
            "answer": "B",
        }
    ]
    example = {
        "question": "Target question",
        "A": "Target1",
        "B": "Target2",
        "C": "Target3",
        "D": "Target4",
        "answer": "C",
    }
    template = get_eval_template(name="en")
    messages = template.format_example(example, support_set=support_set, subject_name="SubName")
    assert messages == [
        {
            "role": "user",
            "content": (
                "The following are multiple choice questions (with answers) about SubName.\n\n"
                "Fewshot question\nA. Fewshot1\nB. Fewshot2\nC. Fewshot3\nD. Fewshot4\nAnswer:"
            ),
        },
        {"role": "assistant", "content": "B"},
        {
            "role": "user",
            "content": "Target question\nA. Target1\nB. Target2\nC. Target3\nD. Target4\nAnswer:",
        },
        {"role": "assistant", "content": "C"},
    ]


@pytest.mark.runs_on(["cpu", "mps"])
def test_eval_template_zh():
    support_set = [
        {
            "question": "Sample question",
            "A": "Sample answer 1",
            "B": "Sample answer 2",
            "C": "Sample answer 3",
            "D": "Sample answer 4",
            "answer": "B",
        }
    ]
    example = {
        "question": "Target question",
        "A": "Target answer 1",
        "B": "Target answer 2",
        "C": "Target answer 3",
        "D": "Target answer 4",
        "answer": "C",
    }
    template = get_eval_template(name="zh")
    messages = template.format_example(example, support_set=support_set, subject_name="Subject")
    assert messages == [
        {
            "role": "user",
            "content": (
                "The following are multiple choice questions (with answers) about Subject.\n\n"
                "Sample question\nA. Sample answer 1\nB. Sample answer 2\nC. Sample answer 3\nD. Sample answer 4\nAnswer: "
            ),
        },
        {"role": "assistant", "content": "B"},
        {
            "role": "user",
            "content": "Target question\nA. Target answer 1\nB. Target answer 2\nC. Target answer 3\nD. Target answer 4\nAnswer: ",
        },
        {"role": "assistant", "content": "C"},
    ]
