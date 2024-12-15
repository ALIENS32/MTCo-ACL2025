## Background Knowledge
Our designed dialogue structure includes five fundamental components: follow-up, refinement, recollection, expansion, and summary. We aim to describe the dialogue structure under complex scenarios based on these five basic structures.

### Using Code to Describe the Dialogue Structure
We use the following Python code to depict the above-mentioned five fundamental dialogue structures.

Each instance of the `Node` class represents one round of dialogue, including a question and a response from the large model. The numbers in the node names (e.g., the instance `k1` represents the first round of dialogue) indicate the position of that dialogue round within the entire dialogue sequence.

**Note**: There are **only two types of relationships** between two rounds of dialogue:
- **Follow-up**: The user asks a new question or makes comments based on the large model's response from the previous round of dialogue. This relationship is represented by a solid line.
- **Refinement**: The user modifies or clarifies a previous prompt, possibly due to the need for correcting information or expressing it more clearly. This relationship is indicated by a dashed line.

**Re-emphasize**, there are only two types of relationships between different rounds of dialogue in a multi-round dialogue structure: follow-up and refinement!

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_follow_up(self, target): # self and target have a follow-up relationship
        pass

    def add_refinement(self, target): # self and target have a refinement relationship
        pass

# Example: Follow-up Relationship
node_k0 = Node('k0')  # Initial dialogue
node_k1 = Node('k1')  # First round of dialogue
node_k0.add_follow_up(node_k1)  # k0 -> k1 follow-up

# Example: Refinement Relationship
node_k2 = Node('k2')  # Second round of dialogue
node_k1.add_refinement(node_k2)  # k1 -> k2 refinement
```

In addition to the aforementioned basic structures, there are also the following dialogue patterns:

- **Recollection**: Users start discussing again based on an earlier round of dialogue. For example, users might return to the initial point of dialogue and ask new questions. The structure is as follows: **a node pointing to a node several rounds later**
```python
# Example: Recollection Relationship
node_kn = Node('kn')  # New dialogue based on early dialogue
node_k0.add_follow_up(node_kn)  # k0 -> kn recollection
```

- **Expansion**: After understanding a topic, users will explore different aspects of that topic in subsequent dialogues. The structure is as follows: **a node pointing to multiple nodes**
```python
# Example: Expansion Relationship
node_k3 = Node('k3')  # Exploring a new sub-topic
node_k2 = Node('k2')  # Exploring a new sub-topic
node_k0.add_follow_up(node_k2)  # k0 -> k2 expansion
node_k0.add_follow_up(node_k3)  # k0 -> k3 expansion
```

- **Summary**: Users request the large model to summarize the content based on the previous rounds of dialogue. The structure is as follows: **multiple nodes pointing to one node**
```python
# Example: Summary Relationship
node_summary = Node('summary')  # Summary node
node_k0.add_follow_up(node_summary)  # k0 -> summary
node_k1.add_follow_up(node_summary)  # k1 -> summary
node_k2.add_follow_up(node_summary)  # k2 -> summary
```


## What You Need to Output
We need you to construct multi-round dialogue data for a up-down scenario, with the definition and description of the scenario as follows:
- **Definition**: The user has a clear plan on how to complete the task and completes the sub-tasks separately in multiple rounds of dialogue; or gets a clear plan based on the answers in the previous rounds of dialogue and then completes the sub-tasks separately in multiple rounds of dialogue

The instruction-following data also contains requirements in two dimensions:
- **Task**: Each round of dialogue data should belong to a type of task, which includes the following categories: writing (creativity, practicality, professionalism), reasoning (logic, mathematics, coding), Q&A (common knowledge, comprehension)
- **Constraints**: A prompt contains multiple constraints, and based on the large model's response, it examines the model's ability to follow instructions according to whether each constraint is met. The constraints include lexical constraints (containing keywords, word search), structural constraints (length, template, special language format), semantic constraints (language style, theme, emotion, creativity), overall constraints (target language, providing justification, consistency, helpfulness). For example, for the prompt "please generate a science fiction story of 500 words", the types of constraints include three: length constraint (500 words), semantic constraint (science fiction), structural constraint (story).

Please design multi-round dialogue data and corresponding structural descriptions that fit the up-down scenario, providing only the prompts for each round of dialogue, without the responses.

The dialogue structure of the multi-round dialogue data you build needs to be challenging:
- **The number of dialogue rounds must be more than 8**
- **The dialogue structure must contain more than three of the previously mentioned basic structures**, which must include follow-up, refinement, recollection, expansion, and summary mentioned in the last round of dialogue, **if you use any of these basic structures, you must fully comply with the definitions of the basic structures!! And accurately describe the structure using code!! If expansion is used, the structure has to be one node pointing to multiple nodes; if summary is used, the structure has to be multiple nodes pointing to one node; if recollection is used, the structure has to be one node pointing to nodes after multiple rounds**

**Pay attention to the accurate use and code description of recollection, expansion, and summary structures!!**

The task and restriction types and quantities for each round of dialogue are determined by you and need to be **complex and challenging**

The first user prompt for the multi-round dialogue you construct is: {__sampled from other datasets__}

**The output contains three parts: multi-round dialogue data, using code to describe the structure of the dialogue, and explaining which basic structures are included, please strictly follow my requirements for output!!**

### Format
The prompt data in the multi-round dialogue should be output in the following format:
**Note that the constraint types included must be strictly based on the prompts you design, do not add constraint types in the constraint_dimensions without basis!**
```json
[
    {
        "conv":[
            {
                "turn_id":"<int: turn number>",
                "task_types": "<str: task type>",
                "instruction":"<str: user's prompt>",
                "constraint_dimensions":[
                    "<str: constraint type 1 and content>",
                    "<str: constraint type 2 and content>"
                ],
                "relation":"<str: relationship with the previous round of dialogue, such as follow-up>",
                ]
            },
            {

            }
        ]
    }
]
```
Please describe the structure of the multi-round dialogue data you design according to the code definition I provided.
**Note! The relationships between dialogues in the structure can only be follow-up and refinement, do not add other relationships!!**

Finally, explain which basic structures are included and how this reflects the up-down dialogue scenario.
**Again, if you are designing a dialogue that contains some sort of basic structure, you need to make the basic structure contained in the dialogue match the description in the code for the background information**