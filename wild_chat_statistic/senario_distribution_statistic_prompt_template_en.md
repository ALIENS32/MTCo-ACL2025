## Background Knowledge
**Classification of Multi-Turn Dialogue Scenarios Based on User's Purpose**

1. **Purposeless Dialogue**
    - Definition: The user has no clear goal in the conversation, and topics can change at any time. The user switches topics multiple times within the same multi-turn dialogue.
    - Structure: The entire dialogue can be divided into multiple segments, each with its own independent topic, with topics being mutually independent. Each segment involves different topics, tasks, and sub-dialogue structures, and the overall structure can be described as a forest, consisting of multiple dialogue trees.
    - Practical Scenario: Suitable for casual social interactions or entertainment, where the content is typically informal.
    - Example: The user starts talking with the AI about the news of the day, then suddenly shifts to discussing their favorite music genre, followed by a mention of a book they recently read, and finally talks about their holiday plans.
2. **Clear Purpose Dialogue**
    - Definition: The user has a clear overall goal in the multi-turn dialogue, which can be broken down into several ordered sub-tasks. The user completes these sub-tasks one by one during the conversation to eventually achieve the overall goal.
    - Structure: The entire dialogue can be seen as a tree, with a path from the root node (the first round of dialogue) to a specific leaf node (the node that achieves the user's overall goal) being the required path. The nodes along this path represent dialogues where the user completes each sub-task, while other nodes in the tree can be seen as attempts to reach the required nodes. In these dialogues, the user does not complete the sub-task but keeps trying until they eventually complete the sub-task, returning to the required path.
    - Practical Scenario: Suitable for scenarios that require efficiently completing specific tasks, such as writing reports, solving problems, or making plans.
    - Example: The user requests help writing a work report, first inquiring about the structure of the report, then gradually completing the content of each section, and finally integrating them into the final version.
3. **Unclear Purpose Dialogue**
    - Definition: The user starts with a vague initial purpose and is unclear about what the final satisfying result should be. There are multiple possible answers that could satisfy the user, and they explore different options and possibilities throughout the conversation, ultimately selecting one that meets their satisfaction.
    - Structure: Represented as a tree, but without a required path.
    - Practical Scenario: Suitable for scenarios where the user is unsure how to begin or needs to explore multiple possibilities, such as career planning, travel arrangements, or personal development. This type of dialogue usually involves the user asking the model for advice or guidance on what to do.
    - Example: The user asks how to choose a suitable travel destination. Initially, they just want to relax but are unsure whether to go to the beach or the mountains. In the end, they select the most suitable place from multiple options.
4. **Hybrid Purpose Dialogue**
    - Definition: The user may start with a vague purpose, which gradually becomes clearer as the conversation progresses. Alternatively, the user may begin with a clear goal but shift toward broader exploration. The overall logic of the conversation remains coherent, and the user does not completely deviate from their original intent.
    - Structure: Represented as a tree, combining the structures of both Clear Purpose and Unclear Purpose dialogues.
    - Practical Scenario: Suitable for complex or dynamic scenarios, such as learning new skills, health management, or personal growth, where the user's needs may evolve as the conversation progresses.
    - Example: The user begins by asking how to improve fitness results and sets a goal for their ideal body shape. As the conversation progresses, they become interested in aspects such as diet and sleep, eventually forming a more comprehensive health plan.

## Output Format
```json
{
    "senario":
    {
        "name":"<str: Classification Scenario Name>",
        "probability": {
            "Purposeless Dialogue": "<int: Classification Probability Value>",
            "Clear Purpose Dialogue": "<int: Classification Probability Value>",
            "Unclear Purpose": "<int: Classification Probability Value>",
            "Hybrid Purpose": "<int: Classification Probability Value>"
        },
        "rationale": "<str: Rationale for classifying the current dialogue into this scenario>"
    }
}
```

## Your Task
Classify the given dialogue data into one of the four scenarios above.
While classifying, please carefully follow the definitions of the four scenarios above for the given dialogue data.
When outputting:
- Output in JSON format, only the JSON code, no additional content!
- Ensure the sum of all classification probabilities equals 1.
- In the "rationale" section, explain in detail the rationale for the classification, citing specific dialogue content, and also explain why it does not belong to the other categories.

Dialogue to classify:
{specific_dialogue}