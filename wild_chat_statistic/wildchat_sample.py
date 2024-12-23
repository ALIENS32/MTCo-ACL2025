import json
import os
import random
from datasets import load_dataset

# Set environment variables
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# Define output file paths
filt_output_file_path = "wild_chat_statistic/wild_filtered_data.json"
sampled_output_file_path = "wild_chat_statistic/wild_sampled_data.json"


def filt_and_save(filt_output_file_path):
    """
    Filters the WildChat-1M dataset for conversations that are in English, have between 3 and 8 turns,
    and contain a 'conversation' field. It then saves these filtered conversations to a JSON file.

    Parameters:
        filt_output_file_path (str): The path where the filtered data will be saved.
    
    Returns:
        None
    """
    # Load the dataset
    ds = load_dataset("allenai/WildChat-1M")
    train_dataset = ds['train']
    # Initialize counters and list for storing conversations
    total_eligible_samples = 0
    conversations_list = []
    dialogue_index = 0  # To keep track of the index of each conversation

    # Iterate over the dataset and process each sample
    for idx, item in enumerate(train_dataset):
        if (item['language'] == 'English' and 3 < item['turn'] < 8 and 'conversation' in item):
            dialogue_index += 1  # Increment index for each qualifying conversation
            # Build a dictionary containing the index and messages
            conversation = {
                "index": dialogue_index,
                "conversation": [{"content": message["content"], "role": message["role"]} for message in item['conversation']]
            }
            conversations_list.append(conversation)
            total_eligible_samples += 1

        # Print progress information every 1000 samples processed
        if (idx + 1) % 1000 == 0:
            print(f"Processed {idx + 1} samples. Total eligible samples: {total_eligible_samples}")

    # Write all conversations as a JSON array to the file
    with open(filt_output_file_path, "w", encoding="utf-8") as f:
        # Use ensure_ascii=False to support non-ASCII characters, like Chinese
        # indent=2 makes the JSON format more readable (optional)
        json.dump(conversations_list, f, ensure_ascii=False, indent=2)

    print(f"Finished processing all data. Total {total_eligible_samples} eligible samples have been saved to {filt_output_file_path}.")


def sample_and_save(input_file_path, output_file_path, sample_size=1000):
    """
    Randomly samples a specified number of entries from a given JSON file and saves them to a new JSON file.

    Parameters:
        input_file_path (str): Path to the input JSON file.
        output_file_path (str): Path to the output JSON file.
        sample_size (int): Number of samples to draw, default is 1000.
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON data.
        ValueError: If there are not enough samples or the JSON file format is incorrect.
    """
    # Load the JSON file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Randomly sample a specified number of unique entries
    sampled_data = random.sample(data, sample_size)

    # Re-index the 'index' field
    for i, item in enumerate(sampled_data, start=1):
        item['index'] = i

    # Write the sampled conversations as a JSON array to the file
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(sampled_data, f, ensure_ascii=False, indent=2)

    print(f"Sampled {sample_size} entries and saved to {output_file_path}.")


# Call the interface functions to perform sampling and saving
if __name__ == "__main__":
    filt_and_save(filt_output_file_path)
    sample_and_save(filt_output_file_path, sampled_output_file_path, sample_size=1000)