第一轮对话：
## 背景信息
### 五种基本对话结构
我们设计的对话结构中包含五种基本结构：follow-up、refinement、recollection、expansion、summary，希望基于这五种基本结构描述复杂场景下的对话结构

### 使用代码描述对话结构
我们使用下列python代码描述上述五种基本对话结构

每个`Node`类的实例代表一轮对话，包括一个提问和一段来自大模型的回答。节点名中的数字（如`k1`实例代表第一轮对话）表示该轮对话在整个对话序列中的位置。

**注意**：两轮对话之间**只存在两种关系类型**
- **跟进（follow-up）**：用户基于上一轮对话中大模型的回答提出新的问题或评论。这种关系通过实线边表示。
- **澄清（refinement）**：用户修改或澄清之前的提示，可能是因为需要更正信息或表达得更清楚。这种关系通过虚线边表示。


```python
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_follow_up(self, target): # slef和target之间存在follow-up关系
        pass

    def add_refinement(self, target): # slef和target之间存在refinement关系
        pass

# 示例：跟进关系
node_k0 = Node('k0')  # 初始对话
node_k1 = Node('k1')  # 第一轮对话
node_k0.add_follow_up(node_k1)  # k0 -> k1 跟进

# 示例：澄清关系
node_k2 = Node('k2')  # 第二轮对话
node_k1.add_refinement(node_k2)  # k1 -> k2 澄清
```

除了上述的基本结构外，还有以下几种对话模式：

- **回忆（recollection）**：用户基于较早的一轮对话重新开始讨论。例如，用户可能会回到最初的对话点并提出新的问题。结构示例如下：**一个节点指向多轮以后的节点**
```python
# 示例：回忆关系
node_kn = Node('kn')  # 基于早期对话的新对话
node_k0.add_follow_up(node_kn)  # k0 -> kn 回忆
```

- **扩展（expansion）**：用户在了解了一个话题后，会在后续对话中探讨该话题的不同方面。结构示例如下：**一个节点指向多个节点**
```python
# 示例：扩展关系
node_k3 = Node('k3')  # 探讨新子话题
node_k2 = Node('k2')  # 探讨新子话题
node_k0.add_follow_up(node_k2)  # k0 -> k2 扩展
node_k0.add_follow_up(node_k3)  # k0 -> k3 扩展
```

- **总结（summary）**：用户要求大模型根据之前多轮对话的内容做出总结。结构示例如下：**多个节点指向一个节点**
```python
# 示例：总结关系
node_summary = Node('summary')  # 总结节点
node_k0.add_follow_up(node_summary)  # k0 -> summary
node_k1.add_follow_up(node_summary)  # k1 -> summary
node_k2.add_follow_up(node_summary)  # k2 -> summary
```

**假设：所有多轮对话的结构都是由以上五种基本结构组合形成的**

### 多轮对话的三种复杂场景

- 无目的（no-purpose）：在同一多轮对话中，用户不局限于同一主题的内容，可能会在对话中多次切换主题（每个主题有不同的话题和任务以及子对话结构），在这种场景中，多轮对话实际上是由多个属于同一个主题的对话组合而成的
- 自顶向下（up-down）：用户对如何完成任务有明确的规划，在多轮对话中分别完成子任务；或者在前几轮对话中根据回答得到清晰的规划，然后在多轮对话中分别完成子任务
- 自底向上（bottom-up）：包含两种子场景
    - 整体定义：用户在初始阶段给出的提示词并不完善，在与模型的多轮对话中通过模型的反馈不断通过增加或者删除限制来调整提示词，最终使大模型生成令用户满意的结果
    - 子场景（ambiguous pupose）：用户虽然想完成一个复杂任务，但由于对目标不够明确，或者对实现路径不够清晰，需要通过试探和迭代来逐步明确方向
    - 子场景（prompt trial）：用户有明确清晰的目标，但因不清楚怎样的提示能让大模型合理回复，因而需要试错，不断修改提示词直到得到满意的回答

**请你深入理解以上三种场景的区别以便在任务中能做出准确的判断**

后续对话

## 你的任务
我们需要你分析我在接下来对话中给定的多轮对话数据属于上述四种场景（no-purpose、up-down、bottom-up|ambiguous pupose、bottom-up|prompt trial)中的哪一种

### 输出格式
按照下面的格式输出，{}内的内容由你来写，其他内容不变：
#### 结论
{场景名}
#### 置信度
- no-purpose：{数值}
- up-down：{数值}
- bottom-up|ambiguous pupose：{数值}
- bottom-up|prompt trial：{数值}
#### 判断依据
{你给出的判断依据}

给定的多轮对话数据（只包含用户提示）：{多轮对话中用户的提示部分}

