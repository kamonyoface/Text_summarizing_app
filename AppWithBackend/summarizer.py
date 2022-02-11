from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class sum_model:
    def __init__(self, path=None, name=None):
        self.path = path
        self.name = name

    def initialize_model(self):
        if self.path != None:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.path, local_files_only=True)
            self.tokenizer = AutoTokenizer.from_pretrained(self.path, local_files_only=True)
        else:
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.name)
        print('Summarizing model loaded')
    
    def tokenize_input(self, original_text):
        self.original_text = original_text
        self.encoded_input = self.tokenizer(original_text, truncation=True, return_tensors='pt')

    def predict(self, max_len=200, min_len=100):
        ###
        max_len = int(0.20*len(self.original_text.split(" ")))
        min_len = int(0.15*(len(self.original_text.split(" "))))
        if max_len > 1024:
            max_len = 1024
            min_len = 200
        else:
            pass
        ###
        self.outputs = self.model.generate(self.encoded_input["input_ids"], max_length=max_len, min_length=min_len, length_penalty=2.0, num_beams=4, early_stopping=True)

    def decode_output(self):
        self.decoded_outputs = self.tokenizer.decode(self.outputs[0])[7:-4]

    def summarize(self, original_text):
        self.tokenize_input(original_text)
        self.predict()
        self.decode_output()
        return self.decoded_outputs


    