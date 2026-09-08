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

LOCALES = {
    "title": {
        "en": {
            "value": "<h1><center>🚀 OmniTune: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs</center></h1>",
        },
        "ru": {
            "value": "<h1><center>OmniTune: Унифицированная эффективная тонкая настройка 100+ LLMs</center></h1>",
        },
        "ko": {
            "value": "<h1><center>OmniTune: 100+ LLMs를 위한 통합 효율적인 튜닝</center></h1>",
        },
        "ja": {
            "value": "<h1><center>OmniTune: 100+ LLMs の統合効率的なチューニング</center></h1>",
        },
    },
    "subtitle": {
        "en": {
            "value": (
                "<h3><center>Visit <a href='https://github.com/hiyouga/OmniTune' target='_blank'>"
                "GitHub Page</a> <a href='https://omnitune.readthedocs.io/en/latest/' target='_blank'>"
                "Documentation</a> <a href='https://blog.omnitune.net/en/' target='_blank'>"
                "Blog</a></center></h3>"
            ),
        },
        "ru": {
            "value": (
                "<h3><center>Посетить <a href='https://github.com/hiyouga/OmniTune' target='_blank'>"
                "страницу GitHub</a> <a href='https://omnitune.readthedocs.io/en/latest/' target='_blank'>"
                "Документацию</a> <a href='https://blog.omnitune.net/en/' target='_blank'>"
                "Блог</a></center></h3>"
            ),
        },
        "ko": {
            "value": (
                "<h3><center><a href='https://github.com/hiyouga/OmniTune' target='_blank'>"
                "GitHub 페이지</a> <a href='https://omnitune.readthedocs.io/en/latest/' target='_blank'>"
                "공식 문서</a> <a href='https://blog.omnitune.net/en/' target='_blank'>"
                "블로그</a>를 방문하세요.</center></h3>"
            ),
        },
        "ja": {
            "value": (
                "<h3><center><a href='https://github.com/hiyouga/OmniTune' target='_blank'>"
                "GitHub ページ</a> <a href='https://omnitune.readthedocs.io/en/latest/' target='_blank'>"
                "ドキュメント</a> <a href='https://blog.omnitune.net/en/' target='_blank'>"
                "ブログ</a>にアクセスする</center></h3>"
            ),
        },
    },
    "lang": {
        "en": {
            "label": "Language",
        },
        "ru": {
            "label": "Язык",
        },
        "ko": {
            "label": "언어",
        },
        "ja": {
            "label": "言語",
        },
    },
    "model_name": {
        "en": {
            "label": "Model name",
            "info": "Input the initial name to search for the model.",
        },
        "ru": {
            "label": "Название модели",
            "info": "Введите начальное имя для поиска модели.",
        },
        "ko": {
            "label": "모델 이름",
            "info": "모델을 검색할 초기 이름을 입력하세요.",
        },
        "ja": {
            "label": "モデル名",
            "info": "モデルを検索するための初期名を入力してください。",
        },
    },
    "model_path": {
        "en": {
            "label": "Model path",
            "info": "Path to pretrained model or model identifier from Hugging Face.",
        },
        "ru": {
            "label": "Путь к модели",
            "info": "Путь к предварительно обученной модели или идентификатор модели от Hugging Face.",
        },
        "ko": {
            "label": "모델 경로",
            "info": "사전 훈련된 모델의 경로 또는 Hugging Face의 모델 식별자.",
        },
        "ja": {
            "label": "モデルパス",
            "info": "事前学習済みモデルへのパス、または Hugging Face のモデル識別子。",
        },
    },
    "hub_name": {
        "en": {
            "label": "Hub name",
            "info": "Choose the model download source.",
        },
        "ru": {
            "label": "Имя хаба",
            "info": "Выберите источник загрузки модели.",
        },
        "ko": {
            "label": "모델 다운로드 소스",
            "info": "모델 다운로드 소스를 선택하세요.",
        },
        "ja": {
            "label": "モデルダウンロードソース",
            "info": "モデルをダウンロードするためのソースを選択してください。",
        },
    },
    "finetuning_type": {
        "en": {
            "label": "Finetuning method",
        },
        "ru": {
            "label": "Метод дообучения",
        },
        "ko": {
            "label": "파인튜닝 방법",
        },
        "ja": {
            "label": "ファインチューニング方法",
        },
    },
    "checkpoint_path": {
        "en": {
            "label": "Checkpoint path",
        },
        "ru": {
            "label": "Путь контрольной точки",
        },
        "ko": {
            "label": "체크포인트 경로",
        },
        "ja": {
            "label": "チェックポイントパス",
        },
    },
    "quantization_bit": {
        "en": {
            "label": "Quantization bit",
            "info": "Enable quantization (QLoRA).",
        },
        "ru": {
            "label": "Уровень квантования",
            "info": "Включить квантование (QLoRA).",
        },
        "ko": {
            "label": "양자화 비트",
            "info": "양자화 활성화 (QLoRA).",
        },
        "ja": {
            "label": "量子化ビット",
            "info": "量子化を有効にする (QLoRA)。",
        },
    },
    "quantization_method": {
        "en": {
            "label": "Quantization method",
            "info": "Quantization algorithm to use.",
        },
        "ru": {
            "label": "Метод квантования",
            "info": "Алгоритм квантования, который следует использовать.",
        },
        "ko": {
            "label": "양자화 방법",
            "info": "사용할 양자화 알고리즘.",
        },
        "ja": {
            "label": "量子化方法",
            "info": "使用する量子化アルゴリズム。",
        },
    },
    "template": {
        "en": {
            "label": "Chat template",
            "info": "The chat template used in constructing prompts.",
        },
        "ru": {
            "label": "Шаблон чата",
            "info": "Шаблон чата используемый для составления подсказок.",
        },
        "ko": {
            "label": "채팅 템플릿",
            "info": "프롬프트 작성에 사용되는 채팅 템플릿.",
        },
        "ja": {
            "label": "チャットテンプレート",
            "info": "プロンプトの構築に使用されるチャットテンプレート。",
        },
    },
    "rope_scaling": {
        "en": {
            "label": "RoPE scaling",
            "info": "RoPE scaling method to use.",
        },
        "ru": {
            "label": "Масштабирование RoPE",
            "info": "Метод масштабирования RoPE для использования.",
        },
        "ja": {
            "label": "RoPE スケーリング",
            "info": "使用する RoPE スケーリング方法。",
        },
    },
    "booster": {
        "en": {
            "label": "Booster",
            "info": "Approach used to boost training speed.",
        },
        "ru": {
            "label": "Ускоритель",
            "info": "Подход, используемый для ускорения обучения.",
        },
        "ja": {
            "label": "ブースター",
            "info": "トレーニング速度を向上させるためのアプローチ。",
        },
    },
    "training_stage": {
        "en": {
            "label": "Stage",
            "info": "The stage to perform in training.",
        },
        "ru": {
            "label": "Этап",
            "info": "Этап выполнения обучения.",
        },
        "ko": {
            "label": "학습 단계",
            "info": "수행할 학습 방법.",
        },
        "ja": {
            "label": "ステージ",
            "info": "トレーニングで実行するステージ。",
        },
    },
    "dataset_dir": {
        "en": {
            "label": "Data dir",
            "info": "Path to the data directory.",
        },
        "ru": {
            "label": "Директория данных",
            "info": "Путь к директории данных.",
        },
        "ko": {
            "label": "데이터 디렉토리",
            "info": "데이터 디렉토리의 경로.",
        },
        "ja": {
            "label": "データディレクトリ",
            "info": "データディレクトリへのパス。",
        },
    },
    "dataset": {
        "en": {
            "label": "Dataset",
        },
        "ru": {
            "label": "Набор данных",
        },
        "ko": {
            "label": "데이터셋",
        },
        "ja": {
            "label": "データセット",
        },
    },
    "data_preview_btn": {
        "en": {
            "value": "Preview dataset",
        },
        "ru": {
            "value": "Просмотреть набор данных",
        },
        "ko": {
            "value": "데이터셋 미리보기",
        },
        "ja": {
            "value": "データセットをプレビュー",
        },
    },
    "preview_count": {
        "en": {
            "label": "Count",
        },
        "ru": {
            "label": "Количество",
        },
        "ko": {
            "label": "개수",
        },
        "ja": {
            "label": "カウント",
        },
    },
    "page_index": {
        "en": {
            "label": "Page",
        },
        "ru": {
            "label": "Страница",
        },
        "ko": {
            "label": "페이지",
        },
        "ja": {
            "label": "ページ",
        },
    },
    "prev_btn": {
        "en": {
            "value": "Prev",
        },
        "ru": {
            "value": "Предыдущая",
        },
        "ko": {
            "value": "이전",
        },
        "ja": {
            "value": "前へ",
        },
    },
    "next_btn": {
        "en": {
            "value": "Next",
        },
        "ru": {
            "value": "Следующая",
        },
        "ko": {
            "value": "다음",
        },
        "ja": {
            "value": "次へ",
        },
    },
    "close_btn": {
        "en": {
            "value": "Close",
        },
        "ru": {
            "value": "Закрыть",
        },
        "ko": {
            "value": "닫기",
        },
        "ja": {
            "value": "閉じる",
        },
    },
    "preview_samples": {
        "en": {
            "label": "Samples",
        },
        "ru": {
            "label": "Примеры",
        },
        "ko": {
            "label": "샘플",
        },
        "ja": {
            "label": "サンプル",
        },
    },
    "learning_rate": {
        "en": {
            "label": "Learning rate",
            "info": "Initial learning rate for AdamW.",
        },
        "ru": {
            "label": "Скорость обучения",
            "info": "Начальная скорость обучения для AdamW.",
        },
        "ko": {
            "label": "학습률",
            "info": "AdamW의 초기 학습률.",
        },
        "ja": {
            "label": "学習率",
            "info": "AdamW の初期学習率。",
        },
    },
    "num_train_epochs": {
        "en": {
            "label": "Epochs",
            "info": "Total number of training epochs to perform.",
        },
        "ru": {
            "label": "Эпохи",
            "info": "Общее количество эпох обучения.",
        },
        "ko": {
            "label": "에포크",
            "info": "수행할 총 학습 에포크 수.",
        },
        "ja": {
            "label": "エポック数",
            "info": "実行するトレーニングの総エポック数。",
        },
    },
    "max_grad_norm": {
        "en": {
            "label": "Maximum gradient norm",
            "info": "Norm for gradient clipping.",
        },
        "ru": {
            "label": "Максимальная норма градиента",
            "info": "Норма для обрезки градиента.",
        },
        "ko": {
            "label": "최대 그레디언트 노름(norm)",
            "info": "그레디언트 클리핑을 위한 노름(norm).",
        },
        "ja": {
            "label": "最大勾配ノルム",
            "info": "勾配クリッピングのためのノルム。",
        },
    },
    "train_seed": {
        "en": {
            "label": "Seed",
            "info": "Random seed for training.",
        },
        "ru": {
            "label": "Seed",
            "info": "Random seed for training.",
        },
        "ko": {
            "label": "Seed",
            "info": "Random seed for training.",
        },
        "ja": {
            "label": "Seed",
            "info": "Random seed for training.",
        },
    },
    "max_samples": {
        "en": {
            "label": "Max samples",
            "info": "Maximum samples per dataset.",
        },
        "ru": {
            "label": "Максимальное количество образцов",
            "info": "Максимальное количество образцов на набор данных.",
        },
        "ko": {
            "label": "최대 샘플 수",
            "info": "데이터셋 당 최대 샘플 수.",
        },
        "ja": {
            "label": "最大サンプル数",
            "info": "データセットごとの最大サンプル数。",
        },
    },
    "compute_type": {
        "en": {
            "label": "Compute type",
            "info": "Whether to use mixed precision training.",
        },
        "ru": {
            "label": "Тип вычислений",
            "info": "Использовать ли обучение смешанной точности.",
        },
        "ko": {
            "label": "연산 유형",
            "info": "혼합 정밀도 훈련을 사용할지 여부.",
        },
        "ja": {
            "label": "計算タイプ",
            "info": "混合精度トレーニングを使用するかどうか。",
        },
    },
    "cutoff_len": {
        "en": {
            "label": "Cutoff length",
            "info": "Max tokens in input sequence.",
        },
        "ru": {
            "label": "Длина обрезки",
            "info": "Максимальное количество токенов во входной последовательности.",
        },
        "ko": {
            "label": "컷오프 길이",
            "info": "입력 시퀀스의 최대 토큰 수.",
        },
        "ja": {
            "label": "カットオフ長",
            "info": "入力シーケンスの最大トークン数。",
        },
    },
    "batch_size": {
        "en": {
            "label": "Batch size",
            "info": "Number of samples processed on each GPU.",
        },
        "ru": {
            "label": "Размер пакета",
            "info": "Количество образцов для обработки на каждом GPU.",
        },
        "ko": {
            "label": "배치 크기",
            "info": "각 GPU에서 처리되는 샘플 수.",
        },
        "ja": {
            "label": "バッチサイズ",
            "info": "各 GPU で処理されるサンプル数。",
        },
    },
    "gradient_accumulation_steps": {
        "en": {
            "label": "Gradient accumulation",
            "info": "Number of steps for gradient accumulation.",
        },
        "ru": {
            "label": "Накопление градиента",
            "info": "Количество шагов накопления градиента.",
        },
        "ko": {
            "label": "그레디언트 누적",
            "info": "그레디언트 누적 단계 수.",
        },
        "ja": {
            "label": "勾配累積",
            "info": "勾配累積のステップ数。",
        },
    },
    "val_size": {
        "en": {
            "label": "Val size",
            "info": "Percentage of validation set from the entire dataset.",
        },
        "ru": {
            "label": "Размер валидации",
            "info": "Пропорция данных в наборе для разработки.",
        },
        "ko": {
            "label": "검증 데이터셋 크기",
            "info": "개발 데이터셋에서 검증 데이터의 비율.",
        },
        "ja": {
            "label": "検証セットサイズ",
            "info": "データセット全体に対する検証セットの割合。",
        },
    },
    "lr_scheduler_type": {
        "en": {
            "label": "LR scheduler",
            "info": "Name of the learning rate scheduler.",
        },
        "ru": {
            "label": "Планировщик скорости обучения",
            "info": "Название планировщика скорости обучения.",
        },
        "ko": {
            "label": "LR 스케줄러",
            "info": "학습률 스케줄러의 이름.",
        },
        "ja": {
            "label": "学習率スケジューラ",
            "info": "学習率スケジューラの名前。",
        },
    },
    "extra_tab": {
        "en": {
            "label": "Extra configurations",
        },
        "ru": {
            "label": "Дополнительные конфигурации",
        },
        "ko": {
            "label": "추가 구성(configuration)",
        },
        "ja": {
            "label": "追加設定",
        },
    },
    "logging_steps": {
        "en": {
            "label": "Logging steps",
            "info": "Number of steps between two logs.",
        },
        "ru": {
            "label": "Шаги логирования",
            "info": "Количество шагов между двумя записями в журнале.",
        },
        "ko": {
            "label": "로깅 스텝",
            "info": "이전 로깅과 다음 로깅 간 스텝 수.",
        },
        "ja": {
            "label": "ロギングステップ",
            "info": "2 つのログ間のステップ数。",
        },
    },
    "save_steps": {
        "en": {
            "label": "Save steps",
            "info": "Number of steps between two checkpoints.",
        },
        "ru": {
            "label": "Шаги сохранения",
            "info": "Количество шагов между двумя контрольными точками.",
        },
        "ko": {
            "label": "저장 스텝",
            "info": "이전 체크포인트와 다음 체크포인트 사이의 스텝 수.",
        },
        "ja": {
            "label": "保存ステップ",
            "info": "2 つのチェックポイント間のステップ数。",
        },
    },
    "warmup_steps": {
        "en": {
            "label": "Warmup steps",
            "info": "Number of steps used for warmup.",
        },
        "ru": {
            "label": "Шаги прогрева",
            "info": "Количество шагов, используемых для прогрева.",
        },
        "ko": {
            "label": "Warmup 스텝",
            "info": "Warmup에 사용되는 스텝 수.",
        },
        "ja": {
            "label": "ウォームアップステップ",
            "info": "ウォームアップに使用されるステップ数。",
        },
    },
    "neftune_alpha": {
        "en": {
            "label": "NEFTune alpha",
            "info": "Magnitude of noise adding to embedding vectors.",
        },
        "ru": {
            "label": "NEFTune alpha",
            "info": "Величина шума, добавляемого к векторам вложений.",
        },
        "ko": {
            "label": "NEFTune 알파",
            "info": "임베딩 벡터에 추가되는 노이즈의 크기.",
        },
        "ja": {
            "label": "NEFTune alpha",
            "info": "埋め込みベクトルに追加されるノイズの大きさ。",
        },
    },
    "extra_args": {
        "en": {
            "label": "Extra arguments",
            "info": "Extra arguments passed to the trainer in JSON format.",
        },
        "ru": {
            "label": "Дополнительные аргументы",
            "info": "Дополнительные аргументы, которые передаются тренеру в формате JSON.",
        },
        "ko": {
            "label": "추가 인수",
            "info": "JSON 형식으로 트레이너에게 전달할 추가 인수입니다.",
        },
        "ja": {
            "label": "追加引数",
            "info": "JSON 形式でトレーナーに渡される追加引数。",
        },
    },
    "packing": {
        "en": {
            "label": "Pack sequences",
            "info": "Pack sequences into samples of fixed length.",
        },
        "ru": {
            "label": "Упаковка последовательностей",
            "info": "Упаковка последовательностей в образцы фиксированной длины.",
        },
        "ko": {
            "label": "시퀀스 패킹",
            "info": "고정된 길이의 샘플로 시퀀스를 패킹합니다.",
        },
        "ja": {
            "label": "シーケンスパッキング",
            "info": "シーケンスを固定長のサンプルにパッキングします。",
        },
    },
    "neat_packing": {
        "en": {
            "label": "Use neat packing",
            "info": "Avoid cross-attention between packed sequences.",
        },
        "ru": {
            "label": "Используйте аккуратную упаковку",
            "info": "избегайте перекрестного внимания между упакованными последовательностями.",
        },
        "ko": {
            "label": "니트 패킹 사용",
            "info": "패킹된 시퀀스 간의 크로스 어텐션을 피합니다.",
        },
        "ja": {
            "label": "無汚染パッキングを使用",
            "info": "パッキング後のシーケンス間のクロスアテンションを避けます。",
        },
    },
    "train_on_prompt": {
        "en": {
            "label": "Train on prompt",
            "info": "Disable the label mask on the prompt (only for SFT).",
        },
        "ru": {
            "label": "Тренировка на подсказке",
            "info": "Отключить маску меток на подсказке (только для SFT).",
        },
        "ko": {
            "label": "프롬프트도 학습",
            "info": "프롬프트에서 라벨 마스킹을 비활성화합니다 (SFT에만 해당).",
        },
        "ja": {
            "label": "プロンプトで学習",
            "info": "プロンプト部分にマスクを追加しない（SFT のみ）。",
        },
    },
    "mask_history": {
        "en": {
            "label": "Mask history",
            "info": "Train on the last turn only (only for SFT).",
        },
        "ru": {
            "label": "История масок",
            "info": "Тренироваться только на последнем шаге (только для SFT).",
        },
        "ko": {
            "label": "히스토리 마스킹",
            "info": "대화 데이터의 마지막 턴만 학습합니다 (SFT에만 해당).",
        },
        "ja": {
            "label": "履歴をマスク",
            "info": "最後のターンのみを学習する（SFT のみ）。",
        },
    },
    "resize_vocab": {
        "en": {
            "label": "Resize token embeddings",
            "info": "Resize the tokenizer vocab and the embedding layers.",
        },
        "ru": {
            "label": "Изменение размера токенных эмбеддингов",
            "info": "Изменить размер словаря токенизатора и слоев эмбеддинга.",
        },
        "ko": {
            "label": "토큰 임베딩의 사이즈 조정",
            "info": "토크나이저 어휘와 임베딩 레이어의 크기를 조정합니다.",
        },
        "ja": {
            "label": "トークン埋め込みのサイズ変更",
            "info": "トークナイザーの語彙と埋め込み層のサイズを変更します。",
        },
    },
    "use_llama_pro": {
        "en": {
            "label": "Enable LLaMA Pro",
            "info": "Make the parameters in the expanded blocks trainable.",
        },
        "ru": {
            "label": "Включить LLaMA Pro",
            "info": "Сделать параметры в расширенных блоках обучаемыми.",
        },
        "ko": {
            "label": "LLaMA Pro 사용",
            "info": "확장된 블록의 매개변수를 학습 가능하게 만듭니다.",
        },
        "ja": {
            "label": "LLaMA Pro を有効化",
            "info": "拡張ブロックのパラメータのみをトレーニングします。",
        },
    },
    "enable_thinking": {
        "en": {
            "label": "Enable thinking",
            "info": "Whether or not to enable thinking mode for reasoning models.",
        },
        "ru": {
            "label": "Включить мысли",
            "info": "Включить режим мысли для моделей решающего характера.",
        },
        "ko": {
            "label": "생각 모드 활성화",
            "info": "추론 모델의 생각 모드를 활성화할지 여부.",
        },
        "ja": {
            "label": "思考モードを有効化",
            "info": "推論モデルの思考モードを有効にするかどうか。",
        },
    },
    "report_to": {
        "en": {
            "label": "Enable external logger",
            "info": "Use TensorBoard or wandb to log experiment.",
        },
        "ru": {
            "label": "Включить внешний регистратор",
            "info": "Использовать TensorBoard или wandb для ведения журнала экспериментов.",
        },
        "ko": {
            "label": "외부 logger 활성화",
            "info": "TensorBoard 또는 wandb를 사용하여 실험을 기록합니다.",
        },
        "ja": {
            "label": "外部ロガーを有効化",
            "info": "TensorBoard または wandb を使用して実験を記録します。",
        },
    },
    "freeze_tab": {
        "en": {
            "label": "Freeze tuning configurations",
        },
        "ru": {
            "label": "конфигурации для настройки заморозки",
        },
        "ko": {
            "label": "Freeze tuning 설정",
        },
        "ja": {
            "label": "フリーズチューニング設定",
        },
    },
    "freeze_trainable_layers": {
        "en": {
            "label": "Trainable layers",
            "info": "Number of the last(+)/first(-) hidden layers to be set as trainable.",
        },
        "ru": {
            "label": "Обучаемые слои",
            "info": "Количество последних (+)/первых (-) скрытых слоев, которые будут установлены как обучаемые.",
        },
        "ko": {
            "label": "학습 가능한 레이어",
            "info": "학습 가능하게 설정할 마지막(+)/처음(-) 히든 레이어의 수.",
        },
        "ja": {
            "label": "学習可能なレイヤー",
            "info": "最後（+）/最初（-）の学習可能な隠れ層の数。",
        },
    },
    "freeze_trainable_modules": {
        "en": {
            "label": "Trainable modules",
            "info": "Name(s) of trainable modules. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Обучаемые модули",
            "info": "Название обучаемых модулей. Используйте запятые для разделения нескольких модулей.",
        },
        "ko": {
            "label": "학습 가능한 모듈",
            "info": "학습 가능한 모듈의 이름. 여러 모듈을 구분하려면 쉼표(,)를 사용하세요.",
        },
        "ja": {
            "label": "学習可能なモジュール",
            "info": "学習可能なモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "freeze_extra_modules": {
        "en": {
            "label": "Extra modules (optional)",
            "info": (
                "Name(s) of modules apart from hidden layers to be set as trainable. "
                "Use commas to separate multiple modules."
            ),
        },
        "ru": {
            "label": "Дополнительные модули (опционально)",
            "info": (
                "Имена модулей, кроме скрытых слоев, которые следует установить в качестве обучаемых. "
                "Используйте запятые для разделения нескольких модулей."
            ),
        },
        "ko": {
            "label": "추가 모듈 (선택 사항)",
            "info": "히든 레이어 외에 학습 가능하게 설정할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
        "ja": {
            "label": "追加モジュール（オプション）",
            "info": "隠れ層以外の学習可能なモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "lora_tab": {
        "en": {
            "label": "LoRA configurations",
        },
        "ru": {
            "label": "Конфигурации LoRA",
        },
        "ko": {
            "label": "LoRA 구성",
        },
        "ja": {
            "label": "LoRA 設定",
        },
    },
    "lora_rank": {
        "en": {
            "label": "LoRA rank",
            "info": "The rank of LoRA matrices.",
        },
        "ru": {
            "label": "Ранг матриц LoRA",
            "info": "Ранг матриц LoRA.",
        },
        "ko": {
            "label": "LoRA 랭크",
            "info": "LoRA 행렬의 랭크.",
        },
        "ja": {
            "label": "LoRA ランク",
            "info": "LoRA 行列のランク。",
        },
    },
    "lora_alpha": {
        "en": {
            "label": "LoRA alpha",
            "info": "Lora scaling coefficient.",
        },
        "ru": {
            "label": "LoRA alpha",
            "info": "Коэффициент масштабирования LoRA.",
        },
        "ko": {
            "label": "LoRA 알파",
            "info": "LoRA 스케일링 계수.",
        },
        "ja": {
            "label": "LoRA alpha",
            "info": "LoRA スケーリング係数。",
        },
    },
    "lora_dropout": {
        "en": {
            "label": "LoRA dropout",
            "info": "Dropout ratio of LoRA weights.",
        },
        "ru": {
            "label": "Вероятность отсева LoRA",
            "info": "Вероятность отсева весов LoRA.",
        },
        "ko": {
            "label": "LoRA 드롭아웃",
            "info": "LoRA 가중치의 드롭아웃 비율.",
        },
        "ja": {
            "label": "LoRA ドロップアウト",
            "info": "LoRA 重みのドロップアウト確率。",
        },
    },
    "loraplus_lr_ratio": {
        "en": {
            "label": "LoRA+ LR ratio",
            "info": "The LR ratio of the B matrices in LoRA.",
        },
        "ru": {
            "label": "LoRA+ LR коэффициент",
            "info": "Коэффициент LR матриц B в LoRA.",
        },
        "ko": {
            "label": "LoRA+ LR 비율",
            "info": "LoRA에서 B 행렬의 LR 비율.",
        },
        "ja": {
            "label": "LoRA+ LR 比率",
            "info": "LoRA+ の B 行列の学習率倍率。",
        },
    },
    "create_new_adapter": {
        "en": {
            "label": "Create new adapter",
            "info": "Create a new adapter with randomly initialized weight upon the existing one.",
        },
        "ru": {
            "label": "Создать новый адаптер",
            "info": "Создать новый адаптер с случайной инициализацией веса на основе существующего.",
        },
        "ko": {
            "label": "새 어댑터 생성",
            "info": "기존 어댑터 위에 무작위로 초기화된 가중치를 가진 새 어댑터를 생성합니다.",
        },
        "ja": {
            "label": "新しいアダプターを作成",
            "info": "既存のアダプター上にランダムに初期化された新しいアダプターを作成します。",
        },
    },
    "use_rslora": {
        "en": {
            "label": "Use rslora",
            "info": "Use the rank stabilization scaling factor for LoRA layer.",
        },
        "ru": {
            "label": "Использовать rslora",
            "info": "Использовать коэффициент масштабирования стабилизации ранга для слоя LoRA.",
        },
        "ko": {
            "label": "rslora 사용",
            "info": "LoRA 레이어에 랭크 안정화 스케일링 계수를 사용합니다.",
        },
        "ja": {
            "label": "rslora を使用",
            "info": "LoRA 層にランク安定化スケーリング方法を使用します。",
        },
    },
    "use_dora": {
        "en": {
            "label": "Use DoRA",
            "info": "Use weight-decomposed LoRA.",
        },
        "ru": {
            "label": "Используйте DoRA",
            "info": "Используйте LoRA с декомпозицией весов.",
        },
        "ko": {
            "label": "DoRA 사용",
            "info": "가중치-분해 LoRA를 사용합니다.",
        },
        "ja": {
            "label": "DoRA を使用",
            "info": "重み分解された LoRA を使用します。",
        },
    },
    "use_pissa": {
        "en": {
            "label": "Use PiSSA",
            "info": "Use PiSSA method.",
        },
        "ru": {
            "label": "используйте PiSSA",
            "info": "Используйте метод PiSSA.",
        },
        "ko": {
            "label": "PiSSA 사용",
            "info": "PiSSA 방법을 사용합니다.",
        },
        "ja": {
            "label": "PiSSA を使用",
            "info": "PiSSA メソッドを使用します。",
        },
    },
    "lora_target": {
        "en": {
            "label": "LoRA modules (optional)",
            "info": "Name(s) of modules to apply LoRA. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Модули LoRA (опционально)",
            "info": "Имена модулей для применения LoRA. Используйте запятые для разделения нескольких модулей.",
        },
        "ko": {
            "label": "LoRA 모듈 (선택 사항)",
            "info": "LoRA를 적용할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
        "ja": {
            "label": "LoRA モジュール（オプション）",
            "info": "LoRA を適用するモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "additional_target": {
        "en": {
            "label": "Additional modules (optional)",
            "info": (
                "Name(s) of modules apart from LoRA layers to be set as trainable. "
                "Use commas to separate multiple modules."
            ),
        },
        "ru": {
            "label": "Дополнительные модули (опционально)",
            "info": (
                "Имена модулей, кроме слоев LoRA, которые следует установить в качестве обучаемых. "
                "Используйте запятые для разделения нескольких модулей."
            ),
        },
        "ko": {
            "label": "추가 모듈 (선택 사항)",
            "info": "LoRA 레이어 외에 학습 가능하게 설정할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
        "ja": {
            "label": "追加モジュール（オプション）",
            "info": "LoRA 層以外の学習可能なモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "rlhf_tab": {
        "en": {
            "label": "RLHF configurations",
        },
        "ru": {
            "label": "Конфигурации RLHF",
        },
        "ko": {
            "label": "RLHF 구성",
        },
        "ja": {
            "label": "RLHF 設定",
        },
    },
    "pref_beta": {
        "en": {
            "label": "Beta value",
            "info": "Value of the beta parameter in the loss.",
        },
        "ru": {
            "label": "Бета значение",
            "info": "Значение параметра бета в функции потерь.",
        },
        "ko": {
            "label": "베타 값",
            "info": "손실 함수에서 베타 매개 변수의 값.",
        },
        "ja": {
            "label": "Beta 値",
            "info": "損失関数における beta ハイパーパラメータの値。",
        },
    },
    "pref_ftx": {
        "en": {
            "label": "Ftx gamma",
            "info": "The weight of SFT loss in the final loss.",
        },
        "ru": {
            "label": "Ftx гамма",
            "info": "Вес потери SFT в итоговой потере.",
        },
        "ko": {
            "label": "Ftx 감마",
            "info": "최종 로스 함수에서 SFT 로스의 가중치.",
        },
        "ja": {
            "label": "Ftx gamma",
            "info": "損失関数における SFT 損失の重み。",
        },
    },
    "pref_loss": {
        "en": {
            "label": "Loss type",
            "info": "The type of the loss function.",
        },
        "ru": {
            "label": "Тип потерь",
            "info": "Тип функции потерь.",
        },
        "ko": {
            "label": "로스 유형",
            "info": "로스 함수의 유형.",
        },
        "ja": {
            "label": "損失タイプ",
            "info": "損失関数のタイプ。",
        },
    },
    "reward_model": {
        "en": {
            "label": "Reward model",
            "info": "Adapter of the reward model in PPO training.",
        },
        "ru": {
            "label": "Модель вознаграждения",
            "info": "Адаптер модели вознаграждения для обучения PPO.",
        },
        "ko": {
            "label": "리워드 모델",
            "info": "PPO 학습에서 사용할 리워드 모델의 어댑터.",
        },
        "ja": {
            "label": "報酬モデル",
            "info": "PPO トレーニングにおける報酬モデルのアダプター。",
        },
    },
    "ppo_score_norm": {
        "en": {
            "label": "Score norm",
            "info": "Normalizing scores in PPO training.",
        },
        "ru": {
            "label": "Норма оценок",
            "info": "Нормализация оценок в тренировке PPO.",
        },
        "ko": {
            "label": "스코어 정규화",
            "info": "PPO 학습에서 스코어를 정규화합니다.",
        },
        "ja": {
            "label": "スコア正規化",
            "info": "PPO トレーニングにおける報酬スコアの正規化。",
        },
    },
    "ppo_whiten_rewards": {
        "en": {
            "label": "Whiten rewards",
            "info": "Whiten the rewards in PPO training.",
        },
        "ru": {
            "label": "Белые вознаграждения",
            "info": "Осветлите вознаграждения в обучении PPO.",
        },
        "ko": {
            "label": "보상 백화",
            "info": "PPO 훈련에서 보상을 백화(Whiten)합니다.",
        },
        "ja": {
            "label": "報酬のホワイトニング",
            "info": "PPO トレーニングにおいて報酬スコアをホワイトニング処理します。",
        },
    },
    "mm_tab": {
        "en": {
            "label": "Multimodal configurations",
        },
        "ru": {
            "label": "Конфигурации мультимедиа",
        },
        "ko": {
            "label": "멀티모달 구성",
        },
        "ja": {
            "label": "多モーダル設定",
        },
    },
    "freeze_vision_tower": {
        "en": {
            "label": "Freeze vision tower",
            "info": "Freeze the vision tower in the model.",
        },
        "ru": {
            "label": "Заморозить башню визиона",
            "info": "Заморозить башню визиона в модели.",
        },
        "ko": {
            "label": "비전 타워 고정",
            "info": "모델의 비전 타워를 고정합니다.",
        },
        "ja": {
            "label": "ビジョンタワーの固定",
            "info": "モデルのビジョンタワーを固定します。",
        },
    },
    "freeze_multi_modal_projector": {
        "en": {
            "label": "Freeze multi-modal projector",
            "info": "Freeze the multi-modal projector in the model.",
        },
        "ru": {
            "label": "Заморозить мультимодальный проектор",
            "info": "Заморозить мультимодальный проектор в модели.",
        },
        "ko": {
            "label": "멀티모달 프로젝터 고정",
            "info": "모델의 멀티모달 프로젝터를 고정합니다.",
        },
        "ja": {
            "label": "多モーダルプロジェクターの固定",
            "info": "モデルの多モーダルプロジェクターを固定します。",
        },
    },
    "freeze_language_model": {
        "en": {
            "label": "Freeze language model",
            "info": "Freeze the language model in the model.",
        },
        "ru": {
            "label": "Заморозить язык модели",
            "info": "Заморозить язык модели в модели.",
        },
        "ko": {
            "label": "언어 모델 고정",
            "info": "모델의 언어 모델을 고정합니다.",
        },
        "ja": {
            "label": "言語モデルの固定",
            "info": "モデルの言語モデルを固定します。",
        },
    },
    "image_max_pixels": {
        "en": {
            "label": "Image max pixels",
            "info": "The maximum number of pixels of image inputs.",
        },
        "ru": {
            "label": "Максимальное количество пикселей изображения",
            "info": "Максимальное количество пикселей изображения.",
        },
        "ko": {
            "label": "이미지 최대 픽셀",
            "info": "이미지 입력의 최대 픽셀 수입니다.",
        },
        "ja": {
            "label": "画像最大ピクセル",
            "info": "画像入力の最大ピクセル数です。",
        },
    },
    "image_min_pixels": {
        "en": {
            "label": "Image min pixels",
            "info": "The minimum number of pixels of image inputs.",
        },
        "ru": {
            "label": "Минимальное количество пикселей изображения",
            "info": "Минимальное количество пикселей изображения.",
        },
        "ko": {
            "label": "이미지 최소 픽셀",
            "info": "이미지 입력의 최소 픽셀 수입니다.",
        },
        "ja": {
            "label": "画像最小ピクセル",
            "info": "画像入力の最小ピクセル数です。",
        },
    },
    "video_max_pixels": {
        "en": {
            "label": "Video max pixels",
            "info": "The maximum number of pixels of video inputs.",
        },
        "ru": {
            "label": "Максимальное количество пикселей видео",
            "info": "Максимальное количество пикселей видео.",
        },
        "ko": {
            "label": "비디오 최대 픽셀",
            "info": "비디오 입력의 최대 픽셀 수입니다.",
        },
        "ja": {
            "label": "ビデオ最大ピクセル",
            "info": "ビデオ入力の最大ピクセル数です。",
        },
    },
    "video_min_pixels": {
        "en": {
            "label": "Video min pixels",
            "info": "The minimum number of pixels of video inputs.",
        },
        "ru": {
            "label": "Минимальное количество пикселей видео",
            "info": "Минимальное количество пикселей видео.",
        },
        "ko": {
            "label": "비디오 최소 픽셀",
            "info": "비디오 입력의 최소 픽셀 수입니다.",
        },
        "ja": {
            "label": "ビデオ最小ピクセル",
            "info": "ビデオ入力の最小ピクセル数です。",
        },
    },
    "galore_tab": {
        "en": {
            "label": "GaLore configurations",
        },
        "ru": {
            "label": "Конфигурации GaLore",
        },
        "ko": {
            "label": "GaLore 구성",
        },
        "ja": {
            "label": "GaLore 設定",
        },
    },
    "use_galore": {
        "en": {
            "label": "Use GaLore",
            "info": "Use [GaLore](https://github.com/jiaweizzhao/GaLore) optimizer.",
        },
        "ru": {
            "label": "Использовать GaLore",
            "info": "Используйте оптимизатор [GaLore](https://github.com/jiaweizzhao/GaLore).",
        },
        "ko": {
            "label": "GaLore 사용",
            "info": "[GaLore](https://github.com/jiaweizzhao/GaLore) 최적화를 사용하세요.",
        },
        "ja": {
            "label": "GaLore を使用",
            "info": "[GaLore](https://github.com/jiaweizzhao/GaLore) オプティマイザーを使用します。",
        },
    },
    "galore_rank": {
        "en": {
            "label": "GaLore rank",
            "info": "The rank of GaLore gradients.",
        },
        "ru": {
            "label": "Ранг GaLore",
            "info": "Ранг градиентов GaLore.",
        },
        "ko": {
            "label": "GaLore 랭크",
            "info": "GaLore 그레디언트의 랭크.",
        },
        "ja": {
            "label": "GaLore ランク",
            "info": "GaLore 勾配のランク。",
        },
    },
    "galore_update_interval": {
        "en": {
            "label": "Update interval",
            "info": "Number of steps to update the GaLore projection.",
        },
        "ru": {
            "label": "Интервал обновления",
            "info": "Количество шагов для обновления проекции GaLore.",
        },
        "ko": {
            "label": "업데이트 간격",
            "info": "GaLore 프로젝션을 업데이트할 간격의 스텝 수.",
        },
        "ja": {
            "label": "更新間隔",
            "info": "隣接する 2 回の投影更新間のステップ数。",
        },
    },
    "galore_scale": {
        "en": {
            "label": "GaLore scale",
            "info": "GaLore scaling coefficient.",
        },
        "ru": {
            "label": "LoRA Alpha",
            "info": "Коэффициент масштабирования GaLore.",
        },
        "ko": {
            "label": "GaLore 스케일",
            "info": "GaLore 스케일링 계수.",
        },
        "ja": {
            "label": "GaLore スケール",
            "info": "GaLore スケーリング係数。",
        },
    },
    "galore_target": {
        "en": {
            "label": "GaLore modules",
            "info": "Name(s) of modules to apply GaLore. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Модули GaLore",
            "info": "Имена модулей для применения GaLore. Используйте запятые для разделения нескольких модулей.",
        },
        "ko": {
            "label": "GaLore 모듈",
            "info": "GaLore를 적용할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
        "ja": {
            "label": "GaLore モジュール",
            "info": "GaLore を適用するモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "apollo_tab": {
        "en": {
            "label": "APOLLO configurations",
        },
        "ru": {
            "label": "Конфигурации APOLLO",
        },
        "ko": {
            "label": "APOLLO 구성",
        },
        "ja": {
            "label": "APOLLO 設定",
        },
    },
    "use_apollo": {
        "en": {
            "label": "Use APOLLO",
            "info": "Use [APOLLO](https://github.com/zhuhanqing/APOLLO) optimizer.",
        },
        "ru": {
            "label": "Использовать APOLLO",
            "info": "Используйте оптимизатор [APOLLO](https://github.com/zhuhanqing/APOLLO).",
        },
        "ko": {
            "label": "APOLLO 사용",
            "info": "[APOLLO](https://github.com/zhuhanqing/APOLLO) 최적화를 사용하세요.",
        },
        "ja": {
            "label": "APOLLO を使用",
            "info": "[APOLLO](https://github.com/zhuhanqing/APOLLO) オプティマイザーを使用します。",
        },
    },
    "apollo_rank": {
        "en": {
            "label": "APOLLO rank",
            "info": "The rank of APOLLO gradients.",
        },
        "ru": {
            "label": "Ранг APOLLO",
            "info": "Ранг градиентов APOLLO.",
        },
        "ko": {
            "label": "APOLLO 랭크",
            "info": "APOLLO 그레디언트의 랭크.",
        },
        "ja": {
            "label": "APOLLO ランク",
            "info": "APOLLO 勾配のランク。",
        },
    },
    "apollo_update_interval": {
        "en": {
            "label": "Update interval",
            "info": "Number of steps to update the APOLLO projection.",
        },
        "ru": {
            "label": "Интервал обновления",
            "info": "Количество шагов для обновления проекции APOLLO.",
        },
        "ko": {
            "label": "업데이트 간격",
            "info": "APOLLO 프로젝션을 업데이트할 간격의 스텝 수.",
        },
        "ja": {
            "label": "更新間隔",
            "info": "隣接する 2 回の投影更新間のステップ数。",
        },
    },
    "apollo_scale": {
        "en": {
            "label": "APOLLO scale",
            "info": "APOLLO scaling coefficient.",
        },
        "ru": {
            "label": "LoRA Alpha",
            "info": "Коэффициент масштабирования APOLLO.",
        },
        "ko": {
            "label": "APOLLO 스케일",
            "info": "APOLLO 스케일링 계수.",
        },
        "ja": {
            "label": "APOLLO スケール",
            "info": "APOLLO スケーリング係数。",
        },
    },
    "apollo_target": {
        "en": {
            "label": "APOLLO modules",
            "info": "Name(s) of modules to apply APOLLO. Use commas to separate multiple modules.",
        },
        "ru": {
            "label": "Модули APOLLO",
            "info": "Имена модулей для применения APOLLO. Используйте запятые для разделения нескольких модулей.",
        },
        "ko": {
            "label": "APOLLO 모듈",
            "info": "APOLLO를 적용할 모듈의 이름. 모듈 간에는 쉼표(,)로 구분하십시오.",
        },
        "ja": {
            "label": "APOLLO モジュール",
            "info": "APOLLO を適用するモジュールの名前。複数のモジュールを区切るにはカンマを使用します。",
        },
    },
    "badam_tab": {
        "en": {
            "label": "BAdam configurations",
        },
        "ru": {
            "label": "Конфигурации BAdam",
        },
        "ko": {
            "label": "BAdam 설정",
        },
        "ja": {
            "label": "BAdam 設定",
        },
    },
    "use_badam": {
        "en": {
            "label": "Use BAdam",
            "info": "Enable the [BAdam](https://github.com/Ledzy/BAdam) optimizer.",
        },
        "ru": {
            "label": "Использовать BAdam",
            "info": "Включите оптимизатор [BAdam](https://github.com/Ledzy/BAdam).",
        },
        "ko": {
            "label": "BAdam 사용",
            "info": "[BAdam](https://github.com/Ledzy/BAdam) 옵티마이저를 사용합니다.",
        },
        "ja": {
            "label": "BAdam を使用",
            "info": "[BAdam](https://github.com/Ledzy/BAdam) オプティマイザーを使用します。",
        },
    },
    "badam_mode": {
        "en": {
            "label": "BAdam mode",
            "info": "Whether to use layer-wise or ratio-wise BAdam optimizer.",
        },
        "ru": {
            "label": "Режим BAdam",
            "info": "Использовать ли оптимизатор BAdam с послоевой или пропорциональной настройкой.",
        },
        "ko": {
            "label": "BAdam 모드",
            "info": "레이어-BAdam 옵티마이저인지 비율-BAdam 옵티마이저인지.",
        },
        "ja": {
            "label": "BAdam モード",
            "info": "layer-wise または ratio-wise BAdam オプティマイザーを使用します。",
        },
    },
    "badam_switch_mode": {
        "en": {
            "label": "Switch mode",
            "info": "The strategy of picking block to update for layer-wise BAdam.",
        },
        "ru": {
            "label": "Режим переключения",
            "info": "Стратегия выбора блока для обновления для послойного BAdam.",
        },
        "ko": {
            "label": "스위치 모드",
            "info": "레이어-BAdam을 위한 블록 선택 전략.",
        },
        "ja": {
            "label": "切り替え戦略",
            "info": "Layer-wise BAdam オプティマイザーのブロック切り替え戦略。",
        },
    },
    "badam_switch_interval": {
        "en": {
            "label": "Switch interval",
            "info": "Number of steps to update the block for layer-wise BAdam.",
        },
        "ru": {
            "label": "Интервал переключения",
            "info": "количество шагов для обновления блока для пошагового BAdam.",
        },
        "ko": {
            "label": "전환 간격",
            "info": "레이어-BAdam을 위한 블록 업데이트 간 스텝 수.",
        },
        "ja": {
            "label": "切り替え頻度",
            "info": "Layer-wise BAdam オプティマイザーのブロック切り替え頻度。",
        },
    },
    "badam_update_ratio": {
        "en": {
            "label": "Update ratio",
            "info": "The ratio of the update for ratio-wise BAdam.",
        },
        "ru": {
            "label": "Коэффициент обновления",
            "info": "Коэффициент обновления для BAdam с учётом соотношений.",
        },
        "ko": {
            "label": "업데이트 비율",
            "info": "비율-BAdam의 업데이트 비율.",
        },
        "ja": {
            "label": "ブロック更新比率",
            "info": "Ratio-wise BAdam オプティマイザーの更新比率。",
        },
    },
    "swanlab_tab": {
        "en": {
            "label": "SwanLab configurations",
        },
        "ru": {
            "label": "Конфигурации SwanLab",
        },
        "ko": {
            "label": "SwanLab 설정",
        },
        "ja": {
            "label": "SwanLab 設定",
        },
    },
    "use_swanlab": {
        "en": {
            "label": "Use SwanLab",
            "info": "Enable [SwanLab](https://swanlab.cn/) for experiment tracking and visualization.",
        },
        "ru": {
            "label": "Использовать SwanLab",
            "info": "Включить [SwanLab](https://swanlab.cn/) для отслеживания и визуализации экспериментов.",
        },
        "ko": {
            "label": "SwanLab 사용",
            "info": "[SwanLab](https://swanlab.cn/) 를 사용하여 실험을 추적하고 시각화합니다.",
        },
        "ja": {
            "label": "SwanLab を使用",
            "info": "[SwanLab](https://swanlab.cn/) を有効にして実験の追跡と可視化を行います。",
        },
    },
    "swanlab_project": {
        "en": {
            "label": "SwanLab project",
        },
        "ru": {
            "label": "SwanLab Проект",
        },
        "ko": {
            "label": "SwanLab 프로젝트",
        },
        "ja": {
            "label": "SwanLab プロジェクト",
        },
    },
    "swanlab_run_name": {
        "en": {
            "label": "SwanLab experiment name (optional)",
        },
        "ru": {
            "label": "SwanLab Имя эксперимента (опционально)",
        },
        "ko": {
            "label": "SwanLab 실험 이름 (선택 사항)",
        },
        "ja": {
            "label": "SwanLab 実験名（オプション）",
        },
    },
    "swanlab_workspace": {
        "en": {
            "label": "SwanLab workspace (optional)",
            "info": "Workspace for SwanLab. Defaults to the personal workspace.",
        },
        "ru": {
            "label": "SwanLab Рабочая область (опционально)",
            "info": "Рабочая область SwanLab, если не заполнено, то по умолчанию в личной рабочей области.",
        },
        "ko": {
            "label": "SwanLab 작업 영역 (선택 사항)",
            "info": "SwanLab 조직의 작업 영역, 비어 있으면 기본적으로 개인 작업 영역에 있습니다.",
        },
        "ja": {
            "label": "SwanLab ワークスペース（オプション）",
            "info": "SwanLab のワークスペース。デフォルトでは個人ワークスペースです。",
        },
    },
    "swanlab_api_key": {
        "en": {
            "label": "SwanLab API key (optional)",
            "info": "API key for SwanLab.",
        },
        "ru": {
            "label": "SwanLab API ключ (опционально)",
            "info": "API ключ для SwanLab.",
        },
        "ko": {
            "label": "SwanLab API 키 (선택 사항)",
            "info": "SwanLab의 API 키.",
        },
        "ja": {
            "label": "SwanLab API キー（オプション）",
            "info": "SwanLab の API キー。",
        },
    },
    "swanlab_mode": {
        "en": {
            "label": "SwanLab mode",
            "info": "Cloud or offline version.",
        },
        "ru": {
            "label": "SwanLab Режим",
            "info": "Версия в облаке или локальная версия.",
        },
        "ko": {
            "label": "SwanLab 모드",
            "info": "클라우드 버전 또는 오프라인 버전.",
        },
        "ja": {
            "label": "SwanLab モード",
            "info": "クラウド版またはオフライン版 SwanLab を使用します。",
        },
    },
    "swanlab_logdir": {
        "en": {
            "label": "SwanLab log directory",
            "info": "The log directory for SwanLab.",
        },
        "ru": {
            "label": "SwanLab 로그 디렉토리",
            "info": "SwanLab의 로그 디렉토리.",
        },
        "ko": {
            "label": "SwanLab 로그 디렉토리",
            "info": "SwanLab의 로그 디렉토리.",
        },
        "ja": {
            "label": "SwanLab ログ ディレクトリ",
            "info": "SwanLab のログ ディレクトリ。",
        },
    },
    "cmd_preview_btn": {
        "en": {
            "value": "Preview command",
        },
        "ru": {
            "value": "Просмотр команды",
        },
        "ko": {
            "value": "명령어 미리보기",
        },
        "ja": {
            "value": "コマンドをプレビュー",
        },
    },
    "arg_save_btn": {
        "en": {
            "value": "Save arguments",
        },
        "ru": {
            "value": "Сохранить аргументы",
        },
        "ko": {
            "value": "Argument 저장",
        },
        "ja": {
            "value": "引数を保存",
        },
    },
    "arg_load_btn": {
        "en": {
            "value": "Load arguments",
        },
        "ru": {
            "value": "Загрузить аргументы",
        },
        "ko": {
            "value": "Argument 불러오기",
        },
        "ja": {
            "value": "引数を読み込む",
        },
    },
    "start_btn": {
        "en": {
            "value": "Start",
        },
        "ru": {
            "value": "Начать",
        },
        "ko": {
            "value": "시작",
        },
        "ja": {
            "value": "開始",
        },
    },
    "stop_btn": {
        "en": {
            "value": "Abort",
        },
        "ru": {
            "value": "Прервать",
        },
        "ko": {
            "value": "중단",
        },
        "ja": {
            "value": "中断",
        },
    },
    "output_dir": {
        "en": {
            "label": "Output dir",
            "info": "Directory for saving results.",
        },
        "ru": {
            "label": "Выходной каталог",
            "info": "Каталог для сохранения результатов.",
        },
        "ko": {
            "label": "출력 디렉토리",
            "info": "결과를 저장할 디렉토리.",
        },
        "ja": {
            "label": "出力ディレクトリ",
            "info": "結果を保存するパス。",
        },
    },
    "config_path": {
        "en": {
            "label": "Config path",
            "info": "Path to config saving arguments.",
        },
        "ru": {
            "label": "Путь к конфигурации",
            "info": "Путь для сохранения аргументов конфигурации.",
        },
        "ko": {
            "label": "설정 경로",
            "info": "Arguments 저장 파일 경로.",
        },
        "ja": {
            "label": "設定パス",
            "info": "トレーニングパラメータを保存する設定ファイルのパス。",
        },
    },
    "device_count": {
        "en": {
            "label": "Device count",
            "info": "Number of devices available.",
        },
        "ru": {
            "label": "Количество устройств",
            "info": "Количество доступных устройств.",
        },
        "ko": {
            "label": "디바이스 수",
            "info": "사용 가능한 디바이스 수.",
        },
        "ja": {
            "label": "デバイス数",
            "info": "現在利用可能な演算デバイス数。",
        },
    },
    "ds_stage": {
        "en": {
            "label": "DeepSpeed stage",
            "info": "DeepSpeed stage for distributed training.",
        },
        "ru": {
            "label": "Этап DeepSpeed",
            "info": "Этап DeepSpeed для распределенного обучения.",
        },
        "ko": {
            "label": "DeepSpeed 단계",
            "info": "분산 학습을 위한 DeepSpeed 단계.",
        },
        "ja": {
            "label": "DeepSpeed stage",
            "info": "マルチ GPU トレーニングの DeepSpeed stage。",
        },
    },
    "ds_offload": {
        "en": {
            "label": "Enable offload",
            "info": "Enable DeepSpeed offload (slow down training).",
        },
        "ru": {
            "label": "Включить выгрузку",
            "info": "включить выгрузку DeepSpeed (замедлит обучение).",
        },
        "ko": {
            "label": "오프로딩 활성화",
            "info": "DeepSpeed 오프로딩 활성화 (훈련 속도 느려짐).",
        },
        "ja": {
            "label": "オフロードを使用",
            "info": "DeepSpeed オフロードを使用します（速度が遅くなります）。",
        },
    },
    "output_box": {
        "en": {
            "value": "Ready.",
        },
        "ru": {
            "value": "Готово.",
        },
        "ko": {
            "value": "준비 완료.",
        },
        "ja": {
            "value": "準備完了。",
        },
    },
    "loss_viewer": {
        "en": {
            "label": "Loss",
        },
        "ru": {
            "label": "Потери",
        },
        "ko": {
            "label": "손실",
        },
        "ja": {
            "label": "損失",
        },
    },
    "predict": {
        "en": {
            "label": "Save predictions",
        },
        "ru": {
            "label": "Сохранить предсказания",
        },
        "ko": {
            "label": "예측 결과 저장",
        },
        "ja": {
            "label": "予測結果を保存",
        },
    },
    "infer_backend": {
        "en": {
            "label": "Inference engine",
        },
        "ru": {
            "label": "Инференс движок",
        },
        "ko": {
            "label": "추론 엔진",
        },
        "ja": {
            "label": "推論エンジン",
        },
    },
    "infer_dtype": {
        "en": {
            "label": "Inference data type",
        },
        "ru": {
            "label": "Тип данных для вывода",
        },
        "ko": {
            "label": "추론 데이터 유형",
        },
        "ja": {
            "label": "推論データタイプ",
        },
    },
    "load_btn": {
        "en": {
            "value": "Load model",
        },
        "ru": {
            "value": "Загрузить модель",
        },
        "ko": {
            "value": "모델 불러오기",
        },
        "ja": {
            "value": "モデルを読み込む",
        },
    },
    "unload_btn": {
        "en": {
            "value": "Unload model",
        },
        "ru": {
            "value": "Выгрузить модель",
        },
        "ko": {
            "value": "모델 언로드",
        },
        "ja": {
            "value": "モデルをアンロード",
        },
    },
    "info_box": {
        "en": {
            "value": "Model unloaded, please load a model first.",
        },
        "ru": {
            "value": "Модель не загружена, загрузите модель сначала.",
        },
        "ko": {
            "value": "모델이 언로드되었습니다. 모델을 먼저 불러오십시오.",
        },
        "ja": {
            "value": "モデルがロードされていません。最初にモデルをロードしてください。",
        },
    },
    "role": {
        "en": {
            "label": "Role",
        },
        "ru": {
            "label": "Роль",
        },
        "ko": {
            "label": "역할",
        },
        "ja": {
            "label": "役割",
        },
    },
    "system": {
        "en": {
            "placeholder": "System prompt (optional)",
        },
        "ru": {
            "placeholder": "Системный запрос (по желанию)",
        },
        "ko": {
            "placeholder": "시스템 프롬프트 (선택 사항)",
        },
        "ja": {
            "placeholder": "システムプロンプト（オプション）",
        },
    },
    "tools": {
        "en": {
            "placeholder": "Tools (optional)",
        },
        "ru": {
            "placeholder": "Инструменты (по желанию)",
        },
        "ko": {
            "placeholder": "툴 (선택 사항)",
        },
        "ja": {
            "placeholder": "ツールリスト（オプション）",
        },
    },
    "image": {
        "en": {
            "label": "Image (optional)",
        },
        "ru": {
            "label": "Изображение (по желанию)",
        },
        "ko": {
            "label": "이미지 (선택 사항)",
        },
        "ja": {
            "label": "画像（オプション）",
        },
    },
    "video": {
        "en": {
            "label": "Video (optional)",
        },
        "ru": {
            "label": "Видео (по желанию)",
        },
        "ko": {
            "label": "비디오 (선택 사항)",
        },
        "ja": {
            "label": "動画（オプション）",
        },
    },
    "query": {
        "en": {
            "placeholder": "Input...",
        },
        "ru": {
            "placeholder": "Ввод...",
        },
        "ko": {
            "placeholder": "입력...",
        },
        "ja": {
            "placeholder": "入力...",
        },
    },
    "submit_btn": {
        "en": {
            "value": "Submit",
        },
        "ru": {
            "value": "Отправить",
        },
        "ko": {
            "value": "제출",
        },
        "ja": {
            "value": "送信",
        },
    },
    "max_length": {
        "en": {
            "label": "Maximum length",
        },
        "ru": {
            "label": "Максимальная длина",
        },
        "ko": {
            "label": "최대 길이",
        },
        "ja": {
            "label": "最大長",
        },
    },
    "max_new_tokens": {
        "en": {
            "label": "Maximum new tokens",
        },
        "ru": {
            "label": "Максимальное количество новых токенов",
        },
        "ko": {
            "label": "응답의 최대 길이",
        },
        "ja": {
            "label": "最大生成長",
        },
    },
    "top_p": {
        "en": {
            "label": "Top-p",
        },
        "ru": {
            "label": "Лучшие-p",
        },
        "ko": {
            "label": "Top-p",
        },
        "ja": {
            "label": "Top-p",
        },
    },
    "temperature": {
        "en": {
            "label": "Temperature",
        },
        "ru": {
            "label": "Температура",
        },
        "ko": {
            "label": "온도",
        },
        "ja": {
            "label": "温度",
        },
    },
    "seed": {
        "en": {
            "label": "Generation seed (-1 for random)",
        },
        "ru": {
            "label": "Generation seed (-1 = random)",
        },
        "ko": {
            "label": "Generation seed (-1 = random)",
        },
        "ja": {
            "label": "Generation seed (-1 = random)",
        },
    },
    "eval_seed": {
        "en": {
            "label": "Seed",
            "info": "Random seed for evaluation and prediction.",
        },
        "ru": {
            "label": "Seed",
            "info": "Random seed for evaluation and prediction.",
        },
        "ko": {
            "label": "Seed",
            "info": "Random seed for evaluation and prediction.",
        },
        "ja": {
            "label": "Seed",
            "info": "Random seed for evaluation and prediction.",
        },
    },
    "skip_special_tokens": {
        "en": {
            "label": "Skip special tokens",
        },
        "ru": {
            "label": "Пропустить специальные токены",
        },
        "ko": {
            "label": "스페셜 토큰을 건너뛰기",
        },
        "ja": {
            "label": "スペシャルトークンをスキップ",
        },
    },
    "escape_html": {
        "en": {
            "label": "Escape HTML tags",
        },
        "ru": {
            "label": "Исключить HTML теги",
        },
        "ko": {
            "label": "HTML 태그 이스케이프",
        },
        "ja": {
            "label": "HTML タグをエスケープ",
        },
    },
    "clear_btn": {
        "en": {
            "value": "Clear history",
        },
        "ru": {
            "value": "Очистить историю",
        },
        "ko": {
            "value": "기록 지우기",
        },
        "ja": {
            "value": "履歴をクリア",
        },
    },
    "export_size": {
        "en": {
            "label": "Max shard size (GB)",
            "info": "The maximum size for a model file.",
        },
        "ru": {
            "label": "Максимальный размер фрагмента (ГБ)",
            "info": "Максимальный размер файла модели.",
        },
        "ko": {
            "label": "최대 샤드 크기 (GB)",
            "info": "모델 파일의 최대 크기.",
        },
        "ja": {
            "label": "最大シャードサイズ（GB）",
            "info": "単一のモデルファイルの最大サイズ。",
        },
    },
    "export_quantization_bit": {
        "en": {
            "label": "Export quantization bit.",
            "info": "Quantizing the exported model.",
        },
        "ru": {
            "label": "Экспорт бита квантования",
            "info": "Квантование экспортируемой модели.",
        },
        "ko": {
            "label": "양자화 비트 내보내기",
            "info": "내보낸 모델의 양자화.",
        },
        "ja": {
            "label": "量子化ビットをエクスポート",
            "info": "エクスポートするモデルを量子化します。",
        },
    },
    "export_quantization_dataset": {
        "en": {
            "label": "Export quantization dataset",
            "info": "The calibration dataset used for quantization.",
        },
        "ru": {
            "label": "Экспорт набора данных для квантования",
            "info": "Набор данных калибровки, используемый для квантования.",
        },
        "ko": {
            "label": "양자화 데이터셋 내보내기",
            "info": "양자화에 사용되는 교정 데이터셋.",
        },
        "ja": {
            "label": "量子化データセットをエクスポート",
            "info": "量子化プロセスで使用されるキャリブレーションデータセット。",
        },
    },
    "export_device": {
        "en": {
            "label": "Export device",
            "info": "Which device should be used to export model.",
        },
        "ru": {
            "label": "Экспорт устройство",
            "info": "Какое устройство следует использовать для экспорта модели.",
        },
        "ko": {
            "label": "내보낼 장치",
            "info": "모델을 내보내는 데 사용할 장치.",
        },
        "ja": {
            "label": "エクスポートデバイス",
            "info": "モデルをエクスポートするために使用するデバイスタイプ。",
        },
    },
    "export_legacy_format": {
        "en": {
            "label": "Export legacy format",
            "info": "Do not use safetensors to save the model.",
        },
        "ru": {
            "label": "Экспорт в устаревший формат",
            "info": "Не использовать safetensors для сохранения модели.",
        },
        "ko": {
            "label": "레거시 형식 내보내기",
            "info": "모델을 저장하는 데 safetensors를 사용하지 않습니다.",
        },
        "ja": {
            "label": "レガシーフォーマットをエクスポート",
            "info": "safetensors フォーマットを使用せずにモデルを保存します。",
        },
    },
    "export_dir": {
        "en": {
            "label": "Export dir",
            "info": "Directory to save exported model.",
        },
        "ru": {
            "label": "Каталог экспорта",
            "info": "Каталог для сохранения экспортированной модели.",
        },
        "ko": {
            "label": "내보내기 디렉토리",
            "info": "내보낸 모델을 저장할 디렉토리.",
        },
        "ja": {
            "label": "エクスポートディレクトリ",
            "info": "エクスポートしたモデルを保存するフォルダのパス。",
        },
    },
    "export_hub_model_id": {
        "en": {
            "label": "HF Hub ID (optional)",
            "info": "Repo ID for uploading model to Hugging Face hub.",
        },
        "ru": {
            "label": "HF Hub ID (опционально)",
            "info": "Идентификатор репозитория для загрузки модели на Hugging Face hub.",
        },
        "ko": {
            "label": "HF 허브 ID (선택 사항)",
            "info": "모델을 Hugging Face 허브에 업로드하기 위한 레포 ID.",
        },
        "ja": {
            "label": "HF Hub ID（オプション）",
            "info": "Hugging Face Hub にモデルをアップロードするためのリポジトリ ID。",
        },
    },
    "export_btn": {
        "en": {
            "value": "Export",
        },
        "ru": {
            "value": "Экспорт",
        },
        "ko": {
            "value": "내보내기",
        },
        "ja": {
            "value": "エクスポート",
        },
    },
    "device_memory": {
        "en": {
            "label": "Device memory",
            "info": "Current memory usage of the device (GB).",
        },
        "ru": {
            "label": "Память устройства",
            "info": "Текущая память на устройстве (GB).",
        },
        "ko": {
            "label": "디바이스 메모리",
            "info": "지금 사용 중인 기기 메모리 (GB).",
        },
        "ja": {
            "label": "デバイスメモリ",
            "info": "現在のデバイスのメモリ（GB）。",
        },
    },
}


ALERTS = {
    "err_conflict": {
        "en": "A process is in running, please abort it first.",
        "ru": "Процесс уже запущен, пожалуйста, сначала прервите его.",
        "ko": "프로세스가 실행 중입니다. 먼저 중단하십시오.",
        "ja": "プロセスが実行中です。最初に中断してください。",
    },
    "err_exists": {
        "en": "You have loaded a model, please unload it first.",
        "ru": "Вы загрузили модель, сначала разгрузите ее.",
        "ko": "모델이 로드되었습니다. 먼저 언로드하십시오.",
        "ja": "モデルがロードされています。最初にアンロードしてください。",
    },
    "err_no_model": {
        "en": "Please select a model.",
        "ru": "Пожалуйста, выберите модель.",
        "ko": "모델을 선택하십시오.",
        "ja": "モデルを選択してください。",
    },
    "err_no_path": {
        "en": "Model not found.",
        "ru": "Модель не найдена.",
        "ko": "모델을 찾을 수 없습니다.",
        "ja": "モデルが見つかりません。",
    },
    "err_no_dataset": {
        "en": "Please choose a dataset.",
        "ru": "Пожалуйста, выберите набор данных.",
        "ko": "데이터 세트를 선택하십시오.",
        "ja": "データセットを選択してください。",
    },
    "err_no_adapter": {
        "en": "Please select an adapter.",
        "ru": "Пожалуйста, выберите адаптер.",
        "ko": "어댑터를 선택하십시오.",
        "ja": "アダプターを選択してください。",
    },
    "err_no_output_dir": {
        "en": "Please provide output dir.",
        "ru": "Пожалуйста, укажите выходную директорию.",
        "ko": "출력 디렉토리를 제공하십시오.",
        "ja": "出力ディレクトリを入力してください。",
    },
    "err_no_reward_model": {
        "en": "Please select a reward model.",
        "ru": "Пожалуйста, выберите модель вознаграждения.",
        "ko": "리워드 모델을 선택하십시오.",
        "ja": "報酬モデルを選択してください。",
    },
    "err_no_export_dir": {
        "en": "Please provide export dir.",
        "ru": "Пожалуйста, укажите каталог для экспорта.",
        "ko": "Export 디렉토리를 제공하십시오.",
        "ja": "エクスポートディレクトリを入力してください。",
    },
    "err_gptq_lora": {
        "en": "Please merge adapters before quantizing the model.",
        "ru": "Пожалуйста, объедините адаптеры перед квантованием модели.",
        "ko": "모델을 양자화하기 전에 어댑터를 병합하십시오.",
        "ja": "モデルを量子化する前にアダプターをマージしてください。",
    },
    "err_failed": {
        "en": "Failed.",
        "ru": "Ошибка.",
        "ko": "실패했습니다.",
        "ja": "失敗しました。",
    },
    "err_demo": {
        "en": "Training is unavailable in demo mode, duplicate the space to a private one first.",
        "ru": "Обучение недоступно в демонстрационном режиме, сначала скопируйте пространство в частное.",
        "ko": "데모 모드에서는 훈련을 사용할 수 없습니다. 먼저 프라이빗 레포지토리로 작업 공간을 복제하십시오.",
        "ja": "デモモードではトレーニングは利用できません。最初にプライベートスペースに複製してください。",
    },
    "err_tool_name": {
        "en": "Tool name not found.",
        "ru": "Имя инструмента не найдено.",
        "ko": "툴 이름을 찾을 수 없습니다.",
        "ja": "ツール名が見つかりません。",
    },
    "err_json_schema": {
        "en": "Invalid JSON schema.",
        "ru": "Неверная схема JSON.",
        "ko": "잘못된 JSON 스키마입니다.",
        "ja": "JSON スキーマが無効です。",
    },
    "err_config_not_found": {
        "en": "Config file is not found.",
        "ru": "Файл конфигурации не найден.",
        "ko": "Config 파일을 찾을 수 없습니다.",
        "ja": "設定ファイルが見つかりません。",
    },
    "warn_no_cuda": {
        "en": "CUDA environment was not detected.",
        "ru": "Среда CUDA не обнаружена.",
        "ko": "CUDA 환경이 감지되지 않았습니다.",
        "ja": "CUDA 環境が検出されませんでした。",
    },
    "warn_output_dir_exists": {
        "en": "Output dir already exists, will resume training from here.",
        "ru": "Выходной каталог уже существует, обучение будет продолжено отсюда.",
        "ko": "출력 디렉토리가 이미 존재합니다. 위 출력 디렉토리에 저장된 학습을 재개합니다.",
        "ja": "出力ディレクトリが既に存在します。このチェックポイントからトレーニングを再開します。",
    },
    "warn_no_instruct": {
        "en": "You are using a non-instruct model, please fine-tune it first.",
        "ru": "Вы используете модель без инструкции, пожалуйста, primeros выполните донастройку этой модели.",
        "ko": "당신은 지시하지 않은 모델을 사용하고 있습니다. 먼저 이를 미세 조정해 주세요.",
        "ja": "インストラクションモデルを使用していません。まずモデルをアダプターに適合させてください。",
    },
    "info_aborting": {
        "en": "Aborted, wait for terminating...",
        "ru": "Прервано, ожидание завершения...",
        "ko": "중단되었습니다. 종료를 기다리십시오...",
        "ja": "トレーニングが中断されました。プロセスの終了を待っています...",
    },
    "info_aborted": {
        "en": "Ready.",
        "ru": "Готово.",
        "ko": "준비되었습니다.",
        "ja": "準備完了。",
    },
    "info_finished": {
        "en": "Finished.",
        "ru": "Завершено.",
        "ko": "완료되었습니다.",
        "ja": "トレーニングが完了しました。",
    },
    "info_config_saved": {
        "en": "Arguments have been saved at: ",
        "ru": "Аргументы были сохранены по адресу: ",
        "ko": "매개변수가 저장되었습니다: ",
        "ja": "トレーニングパラメータが保存されました: ",
    },
    "info_config_loaded": {
        "en": "Arguments have been restored.",
        "ru": "Аргументы были восстановлены.",
        "ko": "매개변수가 복원되었습니다.",
        "ja": "トレーニングパラメータが読み込まれました。",
    },
    "info_loading": {
        "en": "Loading model...",
        "ru": "Загрузка модели...",
        "ko": "모델 로딩 중...",
        "ja": "モデルをロード中...",
    },
    "info_unloading": {
        "en": "Unloading model...",
        "ru": "Выгрузка модели...",
        "ko": "모델 언로딩 중...",
        "ja": "モデルをアンロード中...",
    },
    "info_loaded": {
        "en": "Model loaded, now you can chat with your model!",
        "ru": "Модель загружена, теперь вы можете общаться с вашей моделью!",
        "ko": "모델이 로드되었습니다. 이제 모델과 채팅할 수 있습니다!",
        "ja": "モデルがロードされました。チャットを開始できます！",
    },
    "info_unloaded": {
        "en": "Model unloaded.",
        "ru": "Модель выгружена.",
        "ko": "모델이 언로드되었습니다.",
        "ja": "モデルがアンロードされました。",
    },
    "info_thinking": {
        "en": "🌀 Thinking...",
        "ru": "🌀 Думаю...",
        "ko": "🌀 생각 중...",
        "ja": "🌀 考えています...",
    },
    "info_thought": {
        "en": "✅ Thought",
        "ru": "✅ Думать закончено",
        "ko": "✅ 생각이 완료되었습니다",
        "ja": "✅ 思考完了",
    },
    "info_exporting": {
        "en": "Exporting model...",
        "ru": "Экспорт модели...",
        "ko": "모델 내보내기 중...",
        "ja": "モデルをエクスポート中...",
    },
    "info_exported": {
        "en": "Model exported.",
        "ru": "Модель экспортирована.",
        "ko": "모델이 내보내졌습니다.",
        "ja": "モデルのエクスポートが完了しました。",
    },
    "info_swanlab_link": {
        "en": "### SwanLab Link\n",
        "ru": "### SwanLab ссылка\n",
        "ko": "### SwanLab 링크\n",
        "ja": "### SwanLab リンク\n",
    },
}
