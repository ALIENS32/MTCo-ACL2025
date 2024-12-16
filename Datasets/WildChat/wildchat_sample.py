'''
从wildchat中采样数据用于分析数据分布
'''

import json
import random
from datasets import load_dataset
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置环境变量
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 加载数据集
ds = load_dataset("allenai/WildChat-1M")
train_dataset = ds['train']

# 定义过滤条件和所需样本数量
required_sample_count = 1000
filtered_data = []
sample_count = 0

# 定义一个函数来检查单个样本是否符合条件
def is_eligible(item):
    return item['turn'] > 3 and item['turn'] <10 and item['language'] == 'English'

# 定义一个函数来处理单个样本
def process_item(item):
    if is_eligible(item):
        conversation = [{"content": message["content"], "role": message["role"]} for message in item['conversation']]
        return conversation
    return None

# 使用多线程处理数据
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = []

    # 迭代数据集，提交任务给线程池
    for item in train_dataset:
        futures.append(executor.submit(process_item, item))
        
        # 检查是否已经找到了足够的样本
        if sample_count >= required_sample_count:
            break

        # 每提交一定数量的任务后，检查已完成的任务
        if len(futures) >= 100:  # 可以根据需要调整这个数字
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    filtered_data.append(result)
                    sample_count += 1
                    
                    # 如果已经找到了足够的样本，停止处理
                    if sample_count >= required_sample_count:
                        break
            
            # 清空已完成的任务
            futures = []

    # 处理剩余的任务
    for future in as_completed(futures):
        result = future.result()
        if result is not None:
            filtered_data.append(result)
            sample_count += 1

# 将过滤后的数据写入JSON文件
with open("Datasets\WildChat\wild_filtered_data.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print(f"Finished processing. Total {sample_count} samples have been saved to wild_filtered_data.json.")