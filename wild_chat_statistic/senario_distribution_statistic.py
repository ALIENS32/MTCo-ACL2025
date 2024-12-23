"""
Count the distribution of four types of scenarios in the conversation data.
"""

from openai import OpenAI
import json

# Initialize API key and file paths
API_KEY = 'your key'
SAMPLED_DATA_PATH = 'wild_chat_statistic\\wild_sampled_data.json'
PROMPT_TEMPLATE_PATH = "wild_chat_statistic\\senario_distribution_statistic_prompt_template_en.md"

# Create an instance of the OpenAI client with a custom base URL and the API key
client = OpenAI(
    base_url="https://api2.aigcbest.top/v1",  # Custom base URL for the API
    api_key=API_KEY  # The API key for authentication
)

# Load the prompt template from the specified file
with open(PROMPT_TEMPLATE_PATH, 'r', encoding='utf-8') as file:
    prompt_template = file.read()  # Read the prompt template as a string

# Load the sampled conversation data from the JSON file
with open(SAMPLED_DATA_PATH, 'r', encoding='utf-8') as file:
    sampled_data = json.load(file)  # Parse the JSON data into a Python object

# Initialize counters for each scenario type
classify_result_list = []
purposeless_dialogue_num = 0
clear_purpose_dialogue_num = 0
unclear_purpose_dialogue_num = 0
hybrid_purpose_dialogue_num = 0

# Iterate over each conversation in the sampled data
for idx in range(len(sampled_data)):
    # Prepare the prompt by replacing the placeholder with the current conversation
    prompt = prompt_template.replace('specific_dialogue', str(sampled_data[idx]['conversation']))
    
    # Send the prompt to the OpenAI API and get a response
    response = client.chat.completions.create(
        model="gpt-4o",  # Specify the model to use for generating the response
        messages=[
            {"role": "user", "content": prompt},  # The user message contains the prompt
        ]
    )
    
    # Extract the scenario JSON string from the response content
    senario_json = response.choices[0].message.content  # The response content is nested deeply
    senario_dict = json.loads(senario_json[7:-3])  # Remove leading '```JSON' and trailing '```'
    
    # Prepare the classification result for the current conversation
    classify_result = {
        "index": idx + 1,  # Index of the conversation in the dataset
        "senario": senario_dict['senario']  # The classified scenario from the response
    }

    # Count the number of conversations for each scenario type
    if senario_dict['senario']['name'] == "Purposeless Dialogue":
        purposeless_dialogue_num += 1
    elif senario_dict['senario']['name'] == "Clear Purpose Dialogue":
        clear_purpose_dialogue_num += 1
    elif senario_dict['senario']['name'] == "Unclear Purpose":
        unclear_purpose_dialogue_num += 1
    elif senario_dict['senario']['name'] == "Hybrid Purpose":
        hybrid_purpose_dialogue_num += 1

    # Add the classification result to the list
    classify_result_list.append(classify_result)
    
    # For debugging purposes, limit the number of processed items (can be removed for full processing)
    if idx == 2:
        break

# Insert the summary of scenario counts at the beginning of the results list
classify_result_list.insert(0, {
    "Purposeless Dialogue Num": purposeless_dialogue_num,
    "Clear Purpose Dialogue Num": clear_purpose_dialogue_num,
    "Unclear Purpose Num": unclear_purpose_dialogue_num,
    "Hybrid Purpose Num": hybrid_purpose_dialogue_num
})

# Define the path where the output JSON file will be saved
OUTPUT_FILE_PATH = 'wild_chat_statistic\\wild_senarion_classify_result.json'

# Write the classification results to a JSON file
with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(classify_result_list, f, ensure_ascii=False, indent=2)  # Save the results with proper formatting