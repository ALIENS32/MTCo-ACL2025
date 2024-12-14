### Background Information
We need to construct an evaluation dataset to assess the large model's ability to follow instructions in multi-turn dialogues. Below, we require you to build multi-turn dialogue data for a bottom-up scenario, which is defined and described as follows:
- **Definition**: The user's initial prompt is not fully developed. Through multiple rounds of dialogue with the model, the user continuously adjusts the prompt by adding or removing constraints based on the model's feedback, ultimately leading the large model to generate results that satisfy the user.
- **Description**: Although the user intends to complete a complex task, they may lack clarity on the objective or the path to achieve it, requiring exploration and iteration to gradually clarify the direction.

The instruction-following data also includes two dimensions of requirements:
- **Task**: Each round of dialogue data should belong to a specific task type, categorized into: Writing (creative, practical, professional), Reasoning (logical, mathematical, coding), Q&A (common knowledge, comprehension).
- **Constraints**: A single prompt contains multiple constraints, and the large model's response is evaluated on whether each constraint is met, assessing the model's ability to follow instructions. Constraint types include: Lexical constraints (keyword inclusion, word search), Structural constraints (length, template, special language format), Semantic constraints (language style, topic, sentiment, creativity), Holistic constraints (target language, provision of evidence, consistency, helpfulness).

### Your Task
Design multi-turn dialogue data and the corresponding structural description that fit the bottom-up scenario. Provide only the prompts for each round of dialogue without the responses. Ensure that the dialogue data are complex and challenging, reflecting this in the structure, such as having more than six turns and incorporating various basic structures mentioned earlier, like recollection, where a later turn connects back to one from several turns ago. Define the task and the number and types of constraints for each round, ensuring they are complex and challenging. The first user prompt for the multi-turn dialogue you construct is: {__sampled from other datasets__}

The output should contain three parts: multi-turn dialogue data, a code description of the dialogue structure, and an explanation of which basic structures are included. Follow the specified format strictly as outlined below!

### Format
The prompt data for multi-turn dialogues must be output in the following JSON format:
```json
[
    {
        "conv":[
            {
                "turn_id": "<int: turn number>",
                "task_types": "<str: task type>",
                "instruction": "<str: user's prompt>",
                "constraint_dimensions": [
                    "<str: constraint type 1>",
                    "<str: constraint type 2>"
                ],
                "relation": "<str: relationship with the previous turn, such as follow-up>"
            },
            {
                // Additional turns would be listed here in the same format
            }
        ]
    }
]
```

Use code to describe the structure of the multi-turn dialogue data you design, using the method provided in the earlier conversation. Note! Only follow-up and refinement relationships between dialogues in the structure are allowed; do not add any other types of relationships!!!

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_follow_up(self, target): # There is a follow-up relationship between self and target
        pass

    def add_refinement(self, target): # There is a refinement relationship between self and target
        pass
```

Finally, provide an explanation of which basic structures are included.
