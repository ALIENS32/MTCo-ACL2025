import json

# 读取原始JSON文件
input_file_path = 'Datasets\WildChat\wild_filtered_data.json'
output_file_path = r'Datasets\WildChat\wild_filtered_user_data.json'

# 读取并解析JSON数据
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化一个空列表用于存储过滤后的对话
filtered_data = []

# 遍历外层列表中的每个内部列表（即每次对话）
for conversation in data:
    # 过滤每个内部列表，只保留role为'user'的条目
    filtered_conversation = [item for item in conversation if isinstance(item, dict) and item.get('role') == 'user']
    
    # 如果过滤后有内容，则添加到总的过滤数据中
    if filtered_conversation:
        filtered_data.append(filtered_conversation)

# 将过滤后的数据写入新的JSON文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)

print(f"Filtered data has been saved to {output_file_path}")