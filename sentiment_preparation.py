import transformers
import torch.utils.data as data
from tqdm import tqdm
import torch

def prepare_pipeline(model_name="finiteautomata/bertweet-base-sentiment-analysis",
                     device=1):
    # Load the sentiment analysis pipeline
    device = torch.device(f"cuda:{device}" if torch.cuda.is_available() else "cpu")
    model = transformers.pipeline('sentiment-analysis', model=model_name, device=device)
    return model


class DatasetReddit(data.Dataset):
    def __init__(self, text_list):
        self.text_list = text_list

    def __getitem__(self, item):
        return self.text_list[item]

    def __len__(self):
        return len(self.text_list)
    
      
def get_sentiment_batch(text_list: list):
    model = prepare_pipeline()
    model: transformers.pipelines.Pipeline
    # sentiment_list = model(text_list, truncation="only_first", batch_size=100)
    # use tqdm to show the progress bar
    sentiment_list = []
    for sentiment_output in tqdm(
            model(DatasetReddit(text_list), truncation="only_first", batch_size=100
                  ), total=len(text_list)):
        sentiment_list.append(sentiment_output)

    sentiment = []
    for item in sentiment_list:
        if item['label'] == 'POS':
            sentiment.append(1)
        elif item['label'] == 'NEG':
            sentiment.append(-1)
        else:
            sentiment.append(0)
    return sentiment