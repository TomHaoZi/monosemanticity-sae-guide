# 概念与符号

本页用于配合 [18 页幻灯片](slides.md) 和 [逐页讲稿](speaker-notes.md) 阅读。公式统一采用列向量约定；原论文中的部分公式使用行向量，两者需通过转置对应。

## 先分清分析对象

- **Token**：模型词表中的文本片段。一个可见字符可能由多个 token 表示，一个 token 也可能包含多个字符。
- **MLP 激活**：前馈网络经过 ReLU 后的中间向量。本研究分析的激活为 $a\in\mathbb{R}^{512}$。
- **神经元**：该激活向量的一个原始坐标。第 $j$ 个坐标轴记为 $e_j\in\mathbb{R}^{512}$，只有第 $j$ 项为 1；它不是额外训练的矩阵。
- **特征**：SAE 学到的一个解码方向及其在不同文本位置的激活模式。语义名称来自事后解释，特征编号本身没有语义。
- **单义性 / 多义性**：一个单元的激活能否由相对一致的属性解释。它是解释一致程度的描述，不能直接等同于模型是否有用。

## SAE 怎样分解激活

稀疏自编码器（Sparse Autoencoder，SAE）尝试用少量非零特征系数重构原始激活：

$$
f=\operatorname{ReLU}\bigl(W_{\mathrm{enc}}(a-b_d)+b_e\bigr),
\qquad
\hat a=b_d+Df.
$$

重点字典 A/1 中，各对象的形状是：

- $a,\hat a,b_d\in\mathbb{R}^{512}$：原激活、重构激活和解码偏置。
- $f,b_e\in\mathbb{R}^{4096}$：稀疏码和编码偏置。
- $W_{\mathrm{enc}}\in\mathbb{R}^{4096\times512}$：编码矩阵。
- $D\in\mathbb{R}^{512\times4096}$：解码矩阵。

**编码器的一行是检测方向，解码器的一列是写入方向。** 两者不要求相同。

第 $i$ 个特征的强度为非负标量 $f_i(a)$，随 token 和上下文改变；解码方向为 $d_i=D_{:,i}\in\mathbb{R}^{512}$，训练后固定。它在重构中的贡献是 $f_i(a)d_i$。

- **点火**：$f_i(a)>0$。强度不是经过校准的语义概率。
- **稀疏码**：多数元素为零的特征强度向量 $f$。
- **字典学习**：从数据学习一组重构方向及其系数。
- **过完备**：方向数超过原空间维度，例如 4,096 个方向对应 512 维激活空间。
- **叠加（superposition）**：模型用共享维度、非正交方向表示多于坐标数的特征。
- **L0**：向量中非零项的数量。图中的平均 L0 是每个 token 的平均非零特征数，不是字典总大小。

`A/1/3450` 应读作“基础语言模型 A / SAE 字典训练运行 1 / 特征 3450”。A/1 是一套完整字典，不是模型中的第 1 层。

## 代理与语义检验

**计算代理**是研究者写出的程序，用于估计文本是否符合目标语境。用 $z$ 表示字符串、$H$ 表示目标生成假设，代理分数可写为：

$$
s_H(z)=\log\frac{P(z\mid H)}{P(z)}.
$$

字符集合类可用理想生成器，例如 DNA 对 A/T/C/G 各赋概率 $1/4$；文字系统类结合 Unicode 区块和贝叶斯估计；不完整字节片段通过语料中的真实出现位置估计。它们都包含近似，也可能出错。

- **特异性**：特征点火时，目标语境通常是否存在。
- **敏感性**：目标语境存在时，特征通常是否响应。
- **Pearson 相关**：比较两个数值变量的线性关联程度；它不自动等于准确率、召回率或语义纯度。
- **Spearman 相关**：比较两个变量的排序是否一致；论文用它评价文字解释预测新激活的能力。

## Logit 与输出效应

**Logit** 是 softmax 前的词表分数。若 $z\in\mathbb{R}^{V}$，则：

$$
P(u)=\frac{\exp z_u}{\sum_v\exp z_v},
\qquad z_u-z_v=\log\frac{P(u)}{P(v)}.
$$

给全部 logits 加同一个常数不会改变概率，因此论文将固定方向的词表权重减去中位数。正负零点不能脱离这一约定解释。

本模型中，$W_{\mathrm{out}}\in\mathbb{R}^{128\times512}$ 把 MLP 激活写回残差流，$W_U\in\mathbb{R}^{V\times128}$ 把残差状态映射到词表。考虑 LayerNorm 的线性近似后，特征与神经元的效应表分别为：

$$
w_i\approx W_U L\pi W_{\mathrm{out}}d_i,
\qquad
w_j^{\mathrm{neuron}}\approx W_U L\pi W_{\mathrm{out}}e_j.
$$

其中 $\pi\in\mathbb{R}^{128\times128}$ 执行去均值，$L\in\mathbb{R}^{128\times128}$ 是近似缩放矩阵。两种分析单位都能计算效应表。真实 LayerNorm 的缩放依赖当前残差状态，所以此式不是任意文本上的精确概率变化。

## 干预与全局评估

- **消融**：在原始激活上减去特征贡献，$a'=a-f_i(a)d_i$，然后继续模型计算。该操作保留其余成分与 SAE 的重构残差。
- **钉住采样**：设定目标强度 $m$，使用 $a'=a+[m-f_i(a)]d_i$ 并继续生成。论文个案把 $m$ 设为最大观测激活值。
- **Rubric**：人工评分的分项规则。论文的条件计分使满分为 14，不是把各项上限无条件相加所得的 15。
- **权重打乱对照**：打乱已训练模型各矩阵内部的权重条目，保留每个矩阵的数值分布、破坏其组织结构。
- **单 token 特征**：论文的操作性定义是，最高激活档的 20 个样例中，最大激活位置始终为同一个 token。
- **特征分裂**：扩大字典后，原来较宽泛的反应由多个更具体的特征共同描述。
- **FSA 式结构**：特征影响生成的 token，后者在随后位置触发自身或其他特征，形成类似有限状态自动机的转移。它不表示同一层 SAE 特征之间存在直接连接。
- **死单元重采样**：重置长期不激活的 SAE 单元。本文在 25k、50k、75k、100k 四个检查点，检查此前 12.5k 步未激活者。

## 损失恢复

令 $L_{\mathrm{orig}}$ 为原模型损失，$L_{\mathrm{zero}}$ 为 MLP 激活清零后的损失，$L_{\mathrm{SAE}}$ 为用 $\hat a$ 替换 $a$ 后的损失。恢复比例定义为：

$$
R=\frac{L_{\mathrm{zero}}-L_{\mathrm{SAE}}}
{L_{\mathrm{zero}}-L_{\mathrm{orig}}}.
$$

它衡量相对清零基线恢复了多少该层的损失改善，不衡量已经解释了多少模型行为。

定义与公式来源：[模型分解](https://transformer-circuits.pub/2023/monosemantic-features/index.html#problem-setup-decomposition)、[SAE 设置](https://transformer-circuits.pub/2023/monosemantic-features/index.html#setup-autoencoder)、[代理方法](https://transformer-circuits.pub/2023/monosemantic-features/index.html#appendix-proxies)、[下游效应](https://transformer-circuits.pub/2023/monosemantic-features/index.html#feature-arabic-effect)。

继续阅读：[实验读图与数字口径](experiment-notes.md) · [原文与引用](references.md)
