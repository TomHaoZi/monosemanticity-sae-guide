# 原文、引用与定位

本仓库是中文论文阅读与学术汇报资料，整理人及汇报人为陈俊伟。仓库中的实验数字来自原论文，未在本仓库重新训练语言模型、SAE 或重新计算实验结果。

## 主要文献

Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., et al. (2023). **Towards Monosemanticity: Decomposing Language Models With Dictionary Learning**. *Transformer Circuits Thread*. Anthropic. Published October 4, 2023.

- [论文原文](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
- [官方字典运行与特征浏览入口](https://transformer-circuits.pub/2023/monosemantic-features/vis/index.html)

引用原研究时，应引用这篇论文；引用本仓库的中文讲解时，可另注明仓库与整理人。不要将本仓库称为论文作者发布的实现或 Anthropic 官方中文版本。

## 对应章节

### 模型与方法

- [激活的特征分解](https://transformer-circuits.pub/2023/monosemantic-features/index.html#problem-setup-decomposition)
- [基础 Transformer 设置](https://transformer-circuits.pub/2023/monosemantic-features/index.html#setup-transformer)
- [SAE 设置](https://transformer-circuits.pub/2023/monosemantic-features/index.html#setup-autoencoder)
- [字典与特征编号](https://transformer-circuits.pub/2023/monosemantic-features/index.html#setup-notation)
- [计算代理](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-proxies)
- [SAE 训练数据](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-autoencoder-dataset)
- [死单元重采样](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-autoencoder-resampling)

### 个案证据

- [个案研究总览及选择范围](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-analysis)
- [阿拉伯文字：激活分布](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-activations)
- [阿拉伯文字：敏感性](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-sensitivity)
- [阿拉伯文字：输出效应与干预](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-effect)
- [阿拉伯文字：与神经元的比较](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-neuron)
- [阿拉伯文字：跨模型匹配](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-universality)
- [DNA 个案](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-dna)
- [base64 个案](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-base64)
- [希伯来文字个案](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-hebrew)
- [特征消融方法](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-feature-ablations)

### 全局评估与系统性现象

- [人工评估](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-manual)
- [人工评分 Rubric](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-rubric)
- [自动激活解释](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-auto-acts)
- [自动 logit 解释](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-auto-logits)
- [自动解释抽样与评分](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-automated-setup)
- [重要性评分的稀疏性局限](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-automated-importance-scoring)
- [权重打乱模型与单 token 分组](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-automated-randomized)
- [损失恢复的含义与限制](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-how-much)
- [特征分裂](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-feature-splitting)
- [跨模型普遍性](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-universality)
- [有限状态自动机式结构](https://transformer-circuits.pub/2023/monosemantic-features/index.html#phenomenology-fsa)
- [稀疏性与重构表现](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-hyperparameters)

## 页码与图片的使用方式

讲稿和 PPT 中的 p.19、p.22、p.23 等“打印定位”沿用制作要求附件，没有把网页重新分页后当作同一份 PDF。浏览器、纸张、字体和缩放设置都可能改变打印页码。因此，核验时优先使用以上网页章节锚点与原图，而不是仅按页码寻找。

`assets/paper/` 中的图片来自论文原图，部分为保留相关面板的裁剪；`assets/slides/` 是中文汇报的逐页预览。两类图片用途不同，中文预览不应当作原论文实验图引用。图像权利与本仓库许可边界见 [第三方素材说明](../THIRD_PARTY_NOTICES.md)。

原文有一处需保留的统计差异：自动 logit 测试正文图将特征中位数标为 0.73，附录文字则写 0.74。主讲采用两处一致的均值 0.74，并在 [实验笔记](experiment-notes.md#8-自动-logit-解释均值中位数与两个-50) 中分别说明来源。

## 阅读入口

- [图文首页](../README.md)
- [逐页幻灯片](slides.md)
- [逐页演讲稿与详细解析](speaker-notes.md)
- [概念与符号](concepts.md)
- [实验读图与数字口径](experiment-notes.md)
