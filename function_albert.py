import os
import torch

from transformers import AlbertTokenizer, AlbertForSequenceClassification
import nltk

from config import rsc_dir, model_dir

class albert_predictor():
    def __init__(self, cpu=False):
        if cpu:
            self.device = torch.device("cpu")
        else:
            self.device = torch.device("cuda")

        self.MODEL_NUM = 5
        nltk.download('punkt')
        self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
        self.model_list = []
        for i in range(self.MODEL_NUM):
            model = AlbertForSequenceClassification.from_pretrained('albert-base-v2',num_labels=1)
            model.load_state_dict(torch.load(os.path.join(model_dir, f'deal_tracker_albert_crop_{i}.pt')))
            model.to(self.device)
            model.eval()
            self.model_list.append(model.eval())

    def predict(self,input_txt):
        processed_txt = '[SEP]'.join(nltk.tokenize.sent_tokenize(input_txt.replace('\n',' ')))
        encoded_list = [self.tokenizer.encode(processed_txt[:100000], add_special_tokens=True, truncation = True, max_length=500)]
        padded_list =  [e + [0] * (512-len(e)) for e in encoded_list]
        sample = torch.tensor(padded_list)
        sample = sample.to(self.device)

        output_list = []
        for i in range(self.MODEL_NUM):
            outputs = self.model_list[i](sample)
            logits = outputs
            output_list.append(logits[0].item())

        return sum(output_list)/len(output_list)

if __name__ == "__main__":
    predictor = albert_predictor(cpu = False)
    print(predictor.predict("SDP"))
