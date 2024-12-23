## 背景知识
{背景知识}


## 输出格式
```json
{
    "senario":"<str：分类场景名>",
    "probability":{
        "Purposeless Dialogue":"<int：分类概率值>",
        "Clear Purpose Dialogue":"<int：分类概率值>",
        "Unclear Purpose":"<int：分类概率值>",
        "Hybrid Purpose":"<int：分类概率值>",
    },
    "rationale":"<str：将当前对话分类为该场景的依据>"
}
```

## 你的任务
根据上述四种场景对我给定的对话数据进行分类
分类时，请仔细根据上述四种场景的定义对给定的对话数据进行分类
输出时
- 以json格式输出，只包含json代码，不包含其他内容！
- 确保每个分类概率之和为1
- 在 rationale 部分详细解释分类的依据，需要引用对话内容进行详细的解释你给出的分类，还要说明为什么不属于其他类别


待分类对话：
{specific_dialogue}