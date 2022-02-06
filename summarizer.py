from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, modeling_outputs
import torch


class generate_summary:
  def __init__(self, original_text, max_sum_len, min_sum_len, model_name):
    self.original_text = original_text
    self.max_len = max_sum_len
    self.min_len = min_sum_len
    self.model_name = model_name
  
  def load_model(self):
    try:
      self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, local_files_only=True)
      self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name, local_files_only=True)
    except:
      self.tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-6-6")
      self.model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-6-6")

  def tokenize_input(self):
    self.encoded_input = self.tokenizer(self.original_text, truncation=True, return_tensors='pt')

  def predict(self):
    self.outputs = self.model.generate(self.encoded_input["input_ids"], max_length=self.max_len, min_length=self.min_len, length_penalty=2.0, num_beams=4, early_stopping=True)

  def decode_output(self):
    self.decoded_outputs = self.tokenizer.decode(self.outputs[0])[8:-4]

  def summarize(self):
    self.load_model()
    self.tokenize_input()
    self.predict()
    self.decode_output()
    return self.decoded_outputs
    
