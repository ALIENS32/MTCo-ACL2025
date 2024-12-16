import os
from collections import Counter
from datasets import load_dataset

# 设置环境变量
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 加载数据集
ds = load_dataset("allenai/WildChat-1M")

# 定义一个函数来计算平均轮数
def calculate_average_turns(covered_turns, total_count):
    # 计算被覆盖的turns的总和
    covered_turn_sum = sum(turn * count for turn, count in covered_turns)
    # 计算平均轮数
    average_turns = covered_turn_sum / total_count
    return average_turns

# region 统计turn字段值出现的次数，以便确定轮数
account_factor = 0.98  # 修改为80%
# 获取训练集
train_dataset = ds['train']
# 过滤掉 turn 为 1 的部分，并统计 turn 字段的值
turn_counts = Counter(turn for turn in train_dataset['turn'] if turn > 1)
# 按照turn升序排序（因为我们要按对话长度来覆盖）
sorted_turn_counts = sorted(turn_counts.items(), key=lambda item: item[0])
# 计算总数量
total_count = sum(turn_counts.values())
# 计算80%的总数量
target_count = account_factor * total_count
# 累加 turn 的次数，直到达到或超过80%的总数量
cumulative_count = 0
covered_turns = []

for turn, count in sorted_turn_counts:
    if cumulative_count < target_count:
        cumulative_count += count
        covered_turns.append((turn, count))
    else:
        break

# 如果累加的数量超过了目标数量，则需要从最后一个加入的turn中减去超出的部分
if cumulative_count > target_count:
    last_turn, last_count = covered_turns[-1]
    excess_count = cumulative_count - target_count
    covered_turns[-1] = (last_turn, last_count - int(excess_count))

# 打印结果
print(f"Total number of records: {total_count}")
print(f"80% of total records: {target_count}")
print(f"Number of unique turns covering 80%: {len(covered_turns)}")
print("Covered turns and their counts:")
for turn, count in covered_turns:
    print(f"{turn}: {count}")

# 计算并打印平均轮数
average_turns = calculate_average_turns(covered_turns, cumulative_count)
print(f"Average number of turns in the top 80% of conversations: {average_turns:.2f}")
# endregion