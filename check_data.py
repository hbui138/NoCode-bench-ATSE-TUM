# check_data.py
from datasets import load_dataset

print("Dang tai dataset NoCode-bench Verified...")
# Tải dataset theo hướng dẫn trong README
dataset = load_dataset('NoCode-bench/NoCode-bench_Verified', split='test')

print(f"Tai thanh cong! Tong so instance: {len(dataset)}")

# In thử 1 bài toán để xem cấu trúc
sample = dataset[0]
print("\n--- Vi du Instance ID: ", sample['instance_id'])
print("--- Input cho Model (Problem Statement):")
print(sample['problem_statement'][:500] + "...") # In 500 ký tự đầu