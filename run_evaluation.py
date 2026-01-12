# to run this file -:
#  python<version> run_evaluation.py
# eg: python3 run_evaluation.py

from dataset_loader import load_scam_dataset
from evaluation import evaluate_predictions

# DATASET_PATH='/home/elsner/Documents/ScamGuard/dataset.csv'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")

# <IMPORTANT> CHANGE THIS TO YOUR dataset.csv PATH

def run():
    dataset = load_scam_dataset(DATASET_PATH)

    print('Running Offline classification - only evaluation...\n')

    #Baseline : use dataset labels as predictions

    predictions=[
      {"classification":row["label"]}
      for row in dataset
    ]

    report = evaluate_predictions(dataset, predictions)

    print('======OFFLINE CLASSIFICATION EVALUATION REPORT=====')
    for key, value in report.items(): 
      print(f'{key}:{value}')


if __name__=="__main__":
    run()
