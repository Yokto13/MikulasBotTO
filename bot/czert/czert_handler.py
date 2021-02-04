import os
from transformers import AutoConfig, BertTokenizerFast, TFAutoModelForSequenceClassification
from typing import List, Optional

CZERT_MODEL_PATH = "czert_model/CZERT-B-sts-CNA"

class CzertHandler:
    """Class handling communication with the model"""
    def __init__(self):
        self.config = AutoConfig.from_pretrained(CZERT_MODEL_PATH, num_labels=1)
        self.tokenizer = BertTokenizerFast(os.path.join(CZERT_MODEL_PATH, "vocab.txt"), strip_accents=False,
                                           do_lower_case=False)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(CZERT_MODEL_PATH, config=self.config)

    def get_closest_question(self, options: List[str], sentence: str, threshold: float = -10.0) -> Optional[str]:
        """
        Returns a string from [options] such that it is closest to the given one according to czert.
        
        If none of the strings is closer that the given threshold, returns None.
        If the threshold is not provided, such a situation cannot occur.
        """
        best_match = None
        best_value = threshold
        for option in options:
            inp = self.tokenizer(option, sentence, return_tensors="tf")
            out = self.model(inp)
            value = out[0].numpy()
            if value > best_value:
                best_value = value
                best_match = option
        return best_match

