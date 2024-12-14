请你理解以下内容，在后续的对话中，我们会让你根据以下内容使用代码描述对话结构
### 背景
我们计划评估大型语言模型在多轮对话中遵循指令的能力。为此，我们设计了三种复杂场景，并希望通过建立多轮对话结构模板来指导创建评估数据集，我们设计的对话结构中包含五种基本结构：follow-up、refinement、recollection、expansion、summary，希望基于这五种基本结构描述复杂场景下的对话结构

### 使用代码描述对话结构
我们使用下列python代码描述上述五种基本对话结构

每个`Node`类的实例代表一轮对话，包括一个提问和一段来自大模型的回答。节点名中的数字（如`k1`实例代表第一轮对话）表示该轮对话在整个对话序列中的位置。

两轮对话之间只存在两种关系类型：
- **跟进（follow-up）**：用户基于上一轮对话中大模型的回答提出新的问题或评论。这种关系通过实线边表示。
- **澄清（refinement）**：用户修改或澄清之前的提示，可能是因为需要更正信息或表达得更清楚。这种关系通过虚线边表示。

再次强调，在多轮对话结构中不同轮次对话之间只存在两种关系：跟进与澄清！

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

