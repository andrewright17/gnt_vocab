import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

DATA_PATH = os.environ.get("DATA_PATH")

data = pd.read_csv(f'{DATA_PATH}/lemma_95.tsv', sep = "\t")

print(data.head())
