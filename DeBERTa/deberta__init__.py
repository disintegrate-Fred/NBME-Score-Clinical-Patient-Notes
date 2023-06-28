from typing import TYPE_CHECKING
from ...file_utils import _LazyModule, is_tf_available, is_tokenizers_available, is_torch_available

_import_structure = {
    "configuration_deberta_v2": ["DEBERTA_V2_PRETRAINED_CONFIG_ARCHIVE_MAP", "DebertaV2Config"],
    "tokenization_deberta_v2": ["DebertaV2Tokenizer"],
}

if is_tokenizers_available():
    _import_structure["tokenization_deberta_v2_fast"] = ["DebertaV2TokenizerFast"]

if is_tf_available():
    _import_structure["modeling_tf_deberta_v2"] = [
        "TF_DEBERTA_V2_PRETRAINED_MODEL_ARCHIVE_LIST",
        "TFDebertaV2ForMaskedLM",
        "TFDebertaV2ForQuestionAnswering",
        "TFDebertaV2ForSequenceClassification",
        "TFDebertaV2ForTokenClassification",
        "TFDebertaV2Model",
        "TFDebertaV2PreTrainedModel",
    ]

if is_torch_available():
    _import_structure["modeling_deberta_v2"] = [
        "DEBERTA_V2_PRETRAINED_MODEL_ARCHIVE_LIST",
        "DebertaV2ForMaskedLM",
        "DebertaV2ForQuestionAnswering",
        "DebertaV2ForSequenceClassification",
        "DebertaV2ForTokenClassification",
        "DebertaV2Model",
        "DebertaV2PreTrainedModel",
    ]


if TYPE_CHECKING:
    from .configuration_deberta_v2 import DEBERTA_V2_PRETRAINED_CONFIG_ARCHIVE_MAP, DebertaV2Config
    from .tokenization_deberta_v2 import DebertaV2Tokenizer

    if is_tokenizers_available():
        from .tokenization_deberta_v2_fast import DebertaV2TokenizerFast

    if is_tf_available():
        from .modeling_tf_deberta_v2 import (
            TF_DEBERTA_V2_PRETRAINED_MODEL_ARCHIVE_LIST,
            TFDebertaV2ForMaskedLM,
            TFDebertaV2ForQuestionAnswering,
            TFDebertaV2ForSequenceClassification,
            TFDebertaV2ForTokenClassification,
            TFDebertaV2Model,
            TFDebertaV2PreTrainedModel,
        )

    if is_torch_available():
        from .modeling_deberta_v2 import (
            DEBERTA_V2_PRETRAINED_MODEL_ARCHIVE_LIST,
            DebertaV2ForMaskedLM,
            DebertaV2ForQuestionAnswering,
            DebertaV2ForSequenceClassification,
            DebertaV2ForTokenClassification,
            DebertaV2Model,
            DebertaV2PreTrainedModel,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
