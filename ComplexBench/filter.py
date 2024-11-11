import json

# 加载 JSON 文件
with open("ComplexBench/raw.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 只保留 instruction 字段
filtered_data = [{"instruction": item["instruction"]} for item in data]

# 将结果写入新的 JSON 文件
with open("ComplexBench/filtered_data_instructions.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)
