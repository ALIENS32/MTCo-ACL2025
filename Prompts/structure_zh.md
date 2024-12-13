我们计划评估大型语言模型在多轮对话中遵循指令的能力。为此，我们设计了三种复杂场景，并希望通过建立多轮对话结构模板来指导创建评估数据集。这将有助于测试模型是否能够根据用户的提示正确地进行对话延续、澄清、回忆、扩展以及总结。

以下是用Python代码表示的人与大模型之间的多轮对话结构。每个`Node`类的实例代表一轮对话，包括一个提问和一段来自大模型的回答。节点名中的数字（如`k1`）表示该轮对话在整个对话序列中的位置。

两轮对话之间存在两种关系类型：
- **跟进（follow-up）**：用户基于上一轮对话中大模型的回答提出新的问题或评论。这种关系通过实线边表示。
- **澄清（refinement）**：用户修改或澄清之前的提示，可能是因为需要更正信息或表达得更清楚。这种关系通过虚线边表示。

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_follow_up(self, target):
        # 添加跟进关系，使用实线表示
        edge = Edge(self, target, 'solid')
        self.edges.append(edge)

    def add_refinement(self, target):
        # 添加澄清关系，使用虚线表示
        edge = Edge(self, target, 'dashed')
        self.edges.append(edge)

# 示例：跟进关系
node_k0 = Node('k0')  # 初始对话
node_k1 = Node('k1')  # 第一轮对话
node_k0.add_follow_up(node_k1)  # k0 -> k1 跟进

# 示例：澄清关系
node_k2 = Node('k2')  # 第二轮对话
node_k1.add_refinement(node_k2)  # k1 -> k2 澄清
```

除了上述的基本结构外，还有以下几种对话模式：

- **回忆（recollection）**：用户基于较早的一轮对话重新开始讨论。例如，用户可能会回到最初的对话点并提出新的问题。结构示例如下：

```python
# 示例：回忆关系
node_kn = Node('kn')  # 基于早期对话的新对话
node_k0.add_follow_up(node_kn)  # k0 -> kn 回忆
```

- **扩展（expansion）**：用户在了解了一个话题后，会在后续对话中探讨该话题的不同方面。结构示例如下：

```python
# 示例：扩展关系
node_k3 = Node('k3')  # 探讨新子话题
node_k2 = Node('k2')  # 探讨新子话题
node_k0.add_follow_up(node_k2)  # k0 -> k2 扩展
node_k0.add_follow_up(node_k3)  # k0 -> k3 扩展
```

- **总结（summary）**：用户要求大模型根据之前多轮对话的内容做出总结。结构示例如下：

```python
# 示例：总结关系
node_summary = Node('summary')  # 总结节点
node_k0.add_follow_up(node_summary)  # k0 -> summary
node_k1.add_follow_up(node_summary)  # k1 -> summary
node_k2.add_follow_up(node_summary)  # k2 -> summary
```

