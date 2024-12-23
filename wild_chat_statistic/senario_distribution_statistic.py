'''
统计四种场景的分布
'''
from openai import OpenAI
import json

key = 'your key'
sampled_data_path = 'wild_chat_statistic\wild_sampled_data.json'
prompt_path = "wild_chat_statistic\senario_distribution_statistic_prompt_template_en.md"

client = OpenAI(
    base_url="https://api2.aigcbest.top/v1",
    api_key=key
)

# 获得提示模板
with open(prompt_path, 'r', encoding='utf-8') as file:
    prompt_template = file.read()

# 遍历json数据
with open(sampled_data_path, 'r', encoding='utf-8') as file:
    sampled_data = json.load(file)

classify_result_list=[]
for idx in range(0,len(sampled_data)):
    prompt = prompt_template.replace(
        'specific_dialogue', str(sampled_data[idx]['conversation']))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    senario_json=response.choices[0].message.content
    print(senario_json)
    senario_dict = json.loads(senario_json[7:-3])#去掉前面的```JSON和结尾的```
    classify_result={
         "index":idx+1,
         "senario":senario_dict['senario']
    }
    classify_result_list.append(classify_result)
    break

output_file_path='wild_chat_statistic\wild_senarion_classify_result.json'
with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(classify_result_list, f, ensure_ascii=False, indent=2)

# ChatCompletion(id='chatcmpl-AhZcjBya7xKZWJGib01xmuLxlvoBt', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='```json\n{\n    "senario": "Clear Purpose Dialogue",\n    "probability": {\n        "Purposeless Dialogue": 0,\n        "Clear Purpose Dialogue": 1,\n        "Unclear Purpose": 0,\n        "Hybrid Purpose": 0\n    },\n    "rationale": "The dialogue demonstrates a clear purpose as the user is systematically inquiring about various aspects of Hurricane Florence and hurricanes in general. The user\'s questions follow a logical sequence aimed at gathering comprehensive information about Hurricane Florence\'s characteristics, behavior, and impact. The user begins with questions about how Hurricane Florence lost its strength, explores its size, pressure, stalling behavior, and concludes by asking about the basic characteristics of hurricanes. This structured approach indicates that the user has a clear overall goal to understand the hurricane in detail, making this a \'Clear Purpose Dialogue\'. The dialogue does not exhibit frequent topic shifts or exploration of multiple possibilities without a fixed path, which rules out it being classified as \'Purposeless Dialogue\', \'Unclear Purpose\', or \'Hybrid Purpose\'."\n}\n```',
#                refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1734948405, model='gpt-4o-2024-08-06', object='chat.completion', service_tier=None, system_fingerprint='fp_d28bcae782', usage=CompletionUsage(completion_tokens=217, prompt_tokens=2081, total_tokens=2298, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))


