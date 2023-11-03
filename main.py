# main.py
import os
import subprocess

# Step 1: Data Preprocessing
print("Step 1: Data Preprocessing")
subprocess.run(["python", "preprocess.py"])

# Step 2: Model Training
print("Step 2: Model Training")
subprocess.run(["onmt_preprocess", "-train_src", "data/preprocessed_urhobo.txt", "-train_tgt", "data/preprocessed_english.txt", "-valid_src", "data/preprocessed_urhobo.txt", "-valid_tgt", "data/preprocessed_english.txt", "-save_data", "data/demo", "-overwrite"])
subprocess.run(["onmt_train", "-data", "data/demo", "-save_model", "model/demo-model", "-gpu_ranks", "0", "-world_size", "1"])

# Step 3: Running the API
print("Step 3: Running the API")
subprocess.Popen(["python", "api/app.py"])
