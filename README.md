# 项目整体结构
按照阶段组织，顺序为：数据分布统计、复杂样例构建、大规模数据构建、评估
每一部分包含各自的数据和提示

# 数据分布统计
- wildchat_sample.py：从wildchat数据集中采样1000个样本用作数据分析
- senario_distribution_statistic.py：调用大模型分析这1000个样本所属的场景类型
- task_distribution_statistic.py：调用大模型分析这1000个样本所属的任务类型