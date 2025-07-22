import pandas as pd
import os

input_path = os.path.join("/data","Medicaldataset.csv")
output_path = os.path.join("/data", "CleanedMedicaldata.csv")

def extract_data(path):
    data = pd.read_csv(path)
    return data

def transform_data(data):
    data_clean = data.dropna()
    data_clean.columns = [col.strip().lower().replace("", "_") for col in data_clean.columns]
    print("Data Transform complete")
    return data_clean

def load__data(data, output_path):
    data.to_csv(output_path, index=False)
    print("Data Loading Complete")
    
def run_pipeline():
    data_raw = extract_data(input_path)
    data_clean = transform_data(data_raw)
    load_data (data_clean, output_path)
    print("Data pipeline completed succefully")
    
if __name__ == "__main__":
    run_pipeline()