### 背景信息
我们需要构建用于评估大模型在多轮对话中指令遵循的评估数据集
下面我们需要你来构建自底向上情景的多轮对话数据，该场景的定义与描述如下：
- **定义**：用户在初始阶段给出的提示词并不完善，在与模型的多轮对话中通过模型的反馈不断通过增加或者删除限制来调整提示词，最终使大模型生成令用户满意的结果
- **描述**：用户虽然想完成一个复杂任务，但由于对目标不够明确，或者对实现路径不够清晰，需要通过试探和迭代来逐步明确方向

在指令遵循数据中还包含两个维度的要求：
- **任务**：每轮对话数据应该属于一种任务，任务有以下种类：写作（创意性、实用性、专业性）、推理（逻辑、数理、代码）、问答（常识、理解）
- **限制**：一条提示中包含多个限制，根据大模型的回答对每个限制是否满足考察大模型的指令遵循能力，限制类型包括：限制包括词法限制（包含关键词、词查找）、结构限制（长度、模板、特殊语言格式）、语义限制（语言风格、主题、情感、创造性）、整体限制（目标语言、是否提供依据、一致性、帮助性）

### 任务
请你设计以符合自底向上场景的多轮对话数据和对应的结构描述，只需要给出每轮对话的提示词即可，无需给出回答
每轮对话的任务和限制类型与数量由你自定，但是需要比较复杂并具有挑战性
输出包含两部分，多轮对话数据和结构，输出格式如下一段所述

### 格式
多轮对话中的提示数据需要按照如下格式输出：
```
[
    {
        "conv":[
            {
                "turn_id":"<int:轮次编号>",
                "task_types": "<str:任务类型>",
                "instruction":"<str:用户给出的提示词>",
                "constraint_dimensions":[
                    "<str:限制类型1>",
                    "<str:限制类型2>"
                ],
                "relation":"<str:与上一轮对话的关系，如follow-up>",
                ]
            },
            {

            }
        ]
    }
]
```
请你使用代码描述你设计的多轮对话数据的结构，代码类似于先前对话中给你的示例：
```
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_follow_up(self, target):
        # Add a follow-up relationship, represented by a solid line
        edge = Edge(self, target, 'solid')
        self.edges.append(edge)

    def add_refinement(self, target):
        # Add a refinement relationship, represented by a dashed line
        edge = Edge(self, target, 'dashed')
        self.edges.append(edge)
```