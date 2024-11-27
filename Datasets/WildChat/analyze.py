# 设置环境变量
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# # 代码下载
# from huggingface_hub import snapshot_download
# # 使用cache_dir参数，将模型/数据集保存到指定“本地路径”
# snapshot_download(repo_id="allenai/WildChat-1M", repo_type="dataset")

from collections import Counter
from datasets import load_dataset
# 加载数据集
ds = load_dataset("allenai/WildChat-1M")

# region 统计turn字段值出现的次数，以便确定轮数
account_factor=0.98
# 获取训练集
train_dataset = ds['train']
# 过滤掉 turn 为 1 的部分
filtered_turns = [turn for turn in train_dataset['turn'] if turn > 1]
# 统计 turn 字段的值
turn_counts = Counter(filtered_turns)
# 按照次数降序排序
sorted_turn_counts = sorted(turn_counts.items(), key=lambda item: item[1], reverse=True)
# 计算总数量
total_count = sum(turn_counts.values())
# 计算80%的总数量
target_count = account_factor * total_count
# 累加 turn 的次数，直到达到或超过80%的总数量
cumulative_count = 0
covered_turns = []
for turn, count in sorted_turn_counts:
    cumulative_count += count
    covered_turns.append((turn, count))
    if cumulative_count >= target_count:
        break
# 打印结果
print(f"Total number of records: {total_count}")
print(f"80% of total records: {target_count}")
print(f"Number of unique turns covering 80%: {len(covered_turns)}")
print("Covered turns and their counts:")
for turn, count in covered_turns:
    print(f"{turn}: {count}")
# endregion
