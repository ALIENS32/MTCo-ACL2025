import json
# 设置环境变量
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# # 代码下载
# from huggingface_hub import snapshot_download
# # 使用cache_dir参数，将模型/数据集保存到指定“本地路径”
# snapshot_download(repo_id="allenai/WildChat-1M", repo_type="dataset")
# 加载数据集
from datasets import load_dataset
ds = load_dataset("allenai/WildChat-1M")
train_dataset = ds['train']
filtered_data = [[{"content": item["content"], "role": item["role"]}
                 for item in item['conversation']] for item in train_dataset if item['turn']>1]

with open("wild_filtered_data.json", "a", encoding="utf-8") as f:
    # f.write(",")
    # f.write("\n")  # 先写入一个换行符
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)
