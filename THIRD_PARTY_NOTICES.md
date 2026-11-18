# 第三方材料与来源

本仓库的原创中文讲解、文档组织、原生示意图、检查脚本与配置采用 [MIT 许可](LICENSE)。这项许可不覆盖原论文中的图表、原文截图及其在 PPT 和幻灯片预览中的嵌入部分。

## 原论文

Trenton Bricken et al. **Towards Monosemanticity: Decomposing Language Models With Dictionary Learning**. Anthropic, Transformer Circuits Thread, 2023-10-04.

- [论文原文](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
- [官方特征浏览器](https://transformer-circuits.pub/2023/monosemantic-features/vis/index.html)
- 本仓库是独立的中文教学整理，不是 Anthropic 官方仓库。

论文原图的著作权及其他权利仍属于原权利人。本仓库未为这些第三方图像授予额外许可；进一步使用时应保留来源并核对原始材料的适用条款。

## 原图清单

以下文件从论文网页所含图像提取，或在不改变数据的前提下裁切，用于紧邻的教学解读。各文件的主题与原文定位如下。

- `assets/paper/arabic-activation.png`：[Arabic Script · Activations](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-activations)。
- `assets/paper/arabic-logit.png`、`arabic-intervention.png`、`arabic-pinning.png`：[Arabic Script · Effect](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-effect)。
- `assets/paper/arabic-neuron.png`：[Arabic Script · Not a Neuron](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-neuron)。
- `assets/paper/arabic-universality.png`：[Arabic Script · Universality](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-universality)。
- `assets/paper/manual-evaluation.png`：[Manual Interpretability](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-manual)。
- `assets/paper/auto-activation.png`：[Automated Interpretability · Activations](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-auto-acts)。
- `assets/paper/auto-logit.png`：[Automated Interpretability · Logits](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-interp-auto-logits)。
- `assets/paper/randomized-token-split.png`：[Randomized Model Analysis](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-automated-randomized)，从原图裁出单 token 与非单 token 双面板。
- `assets/paper/sparsity-reconstruction.png`：[How Much of the Model Have We Explained?](https://transformer-circuits.pub/2023/monosemantic-features/index.html#global-analysis-how-much)，展示稀疏程度与重构表现的关系。

`reports/sae-experiments.pptx` 及 `assets/slides/` 的第 6–8、10–15 页含上述第三方图像或相应局部。第 6 页的直方图使用原图局部，已在页内注明。其余中文说明、版式和逻辑示意为本仓库整理内容。

## 引用与页码

文档中的打印页码沿用初始汇报附件的定位方式。仓库没有附带固定版本的论文打印 PDF，因此网页章节链接是核验依据。不同浏览器或打印设置可能产生不同页码。
