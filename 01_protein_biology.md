# 分子生物学 Benchmarks

## 1. 蛋白质结构预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **CASP14** | 2020 | 3D结构预测（自由建模） | ~100 targets/届 | GDT_TS, TM-score, lDDT-Cα | AlphaFold2: GDT_TS **92.4**，sum-z-score 244 | [PMC9299164](https://pmc.ncbi.nlm.nih.gov/articles/PMC9299164/) |
| **CASP15** | 2022 | 单链+复合体结构预测 | 100+ targets | GDT_TS, DockQ | 单链：AF2变体 TM-score **~0.92**；复合体：AF-Multimer DockQ ~0.60 | [PMC10792517](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792517/) |
| **CAMEO** | 持续 | 自动连续评测（每周新结构） | ~200 targets/周 | lDDT, QS-score | AF2-based方法平均 lDDT **>0.85**；长期占据排行榜前列 | [cameo3d.org](https://www.cameo3d.org/) |
| **1.4M结构基准集** | 2025 | 结构质量/泛化性评估（大规模统计） | 140万经质量检查的蛋白结构 | 结构质量评分 | 非竞赛型工具集，无排行榜；为AF2/3等提供长期可更新测试集 | [Briefings Bioinformatics 2025](https://academic.oup.com/bib/article/26/2/bbaf104/8069415) |

**任务类型**：生成类（条件生成）— 以氨基酸序列为条件，输出每个残基的三维原子坐标。

```python
# 输入：氨基酸单字母序列
input_sequence = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSR..."  # 长度 N

# 输出：每个 Cα 残基的三维坐标 + 模型置信度（pLDDT）
output = {
    "residue_coords": [          # shape (N, 3)，单位 Å
        {"res_id": 1, "aa": "M", "x": 10.23, "y": -4.51, "z":  7.88, "pLDDT": 91.2},
        {"res_id": 2, "aa": "K", "x": 11.84, "y": -3.12, "z":  8.43, "pLDDT": 89.7},
        # ... 共 N 条
    ],
    "global_pLDDT": 87.3,   # >70 通常可信；>90 高可信
    # 与金标准结构比对（评测阶段）
    "TM_score": 0.924,      # ∈ [0,1]，>0.5 视为同折叠
    "lDDT_Ca":  0.881,      # 局部距离差异检验，越高越好
    "GDT_TS":   92.4,       # CASP 主指标（0–100）
}
```

**空白**：蛋白质复合体预测（>2条链）、本征无序区域、共折叠蛋白动态构象。

---

## 2. 蛋白质功能预测

> ⚠️ 注：蛋白质fitness类benchmark性能以**跨assay中位数Spearman ρ**衡量，不同蛋白家族间差异很大，不存在单一SOTA数字。下表列出目前最佳已知分数。

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA（最佳已知分数） | 参考 |
|-----------|------|------|------|------|---------------------|------|
| **ProteinGym** | 2023 (NeurIPS) | 蛋白质适应性预测（零样本+监督） | 2.7M missense变体 × 217 DMS实验；~300K indels × 74实验；2,525临床蛋白 | 中位数 Spearman ρ | 零样本：Tranception L **0.46**；ESM-1v 0.44；监督微调：~0.57 | [proteingym.org](https://proteingym.org/benchmarks) |
| **FLIP** | 2021 | 蛋白质适应性/性质预测（标准化切分） | AAV/GFP/GB1/热稳定性等多个实验 | 每任务 Spearman ρ | GB1 low-vs-high: ESM2微调 **~0.75**；AAV: ~0.85（任务差异大） | [GitHub FLIP](https://github.com/J-SNACKKB/FLIP) |
| **PEER** | 2022 | 多任务蛋白质理解（功能/结构/互作/定位） | 15个数据集×5类 | AUC, Spearman ρ | ESM2/ProtTrans微调；各子任务平均 AUC **~0.85** | [arXiv 2206.02096](https://arxiv.org/abs/2206.02096) |
| **ProteinGLUE** | 2022 | 自监督蛋白建模，7个下游任务 | 多任务 | 各任务独立指标 | ESM-1b 在7任务中5个最优；二级结构 Q3 **~84%** | [Sci. Reports 2022](https://www.nature.com/articles/s41598-022-19608-4) |
| **FLIP2** | 2026 | 蛋白质fitness landscape基准（扩展版） | 比FLIP更多蛋白+更多样选择压力 | 中位数 Spearman ρ | 竞赛进行中，暂无公开SOTA | [bioRxiv 2026.02.23](https://www.biorxiv.org/content/10.64898/2026.02.23.707496v1) |
| **CAFA6** | 2026 | 蛋白质GO功能注释预测（竞赛） | 上百万未注释蛋白序列；时间切片后续注释为金标准 | F-max, S_min | Kaggle竞赛进行中，暂无公开SOTA | [Kaggle CAFA6](https://www.kaggle.com/competitions/cafa-6-protein-function-prediction) |

**任务类型**：① 回归类（突变→适应性分数，ProteinGym / FLIP）；② 多标签分类（序列→GO功能注释，CAFA）。

```python
# ── 子任务① 回归：突变适应性预测（ProteinGym / FLIP）──────────────────────
# 输入：野生型序列 + 突变列表
input_wt  = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNG..."   # 野生型氨基酸序列
input_mut = [{"pos": 39, "wt": "G", "mut": "A"},      # G39A
             {"pos": 59, "wt": "K", "mut": "R"}]      # K59R

# 输出：相对适应性得分（连续值）
output_fitness = {
    "mutant":        "G39A:K59R",
    "delta_fitness": -0.34,   # 负值 = 有害突变（相对野生型）
    # 评测：跨 assay 中位数 Spearman ρ（ProteinGym 主指标）
    "spearman_rho":   0.46,   # SOTA（Tranception L，零样本）
}

# ── 子任务② 多标签分类：GO 功能注释（CAFA6）─────────────────────────────
# 输入：未知功能的蛋白质序列
input_sequence = "MKTIIALSYIFCLVFA..."

# 输出：预测的 GO term 及置信度
output_go = {
    "predictions": [
        {"GO": "GO:0003677", "name": "DNA binding",             "prob": 0.91},
        {"GO": "GO:0006351", "name": "transcription by RNA Pol","prob": 0.87},
        {"GO": "GO:0005634", "name": "nucleus (localization)",  "prob": 0.83},
    ],
    # 评测：在最优阈值下的 F-max（precision-recall 曲线）
    "F_max": 0.54,
}
```

**空白**：多蛋白体系功能、酶催化机制定量预测、蛋白-配体结合自由能。

---

## 3. 蛋白质-蛋白质互作（PPI）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **PRING** | 2024–2025 | 图级别PPI，多物种，无泄露切分 | 21,484蛋白，186,818互作对 | AUROC, F1 | 最优图模型 AUROC **~0.85**；严格切分下明显低于随机切分结果 | [arXiv 2507.05101](https://arxiv.org/html/2507.05101v1) |
| **SHS27k / SHS148k** | 2019–2021 | 二分类PPI | 27K / 148K对（来自STRING） | AUROC, accuracy | KSGPPI: Accuracy **88.96%**, MCC 0.781 | [PMC8746451](https://pmc.ncbi.nlm.nih.gov/articles/PMC8746451/) |
| **Human PPI社区评测** | 2023 | 26种方法横向比较，4物种，6个蛋白质组 | 多物种 | AUROC, AUPRC | 随机切分虚高：AUROC ~0.92；严格物种切分降至 **~0.72**；数据泄露是主要陷阱 | [Nat. Commun. 2023](https://www.nature.com/articles/s41467-023-37079-7) |

**任务类型**：二分类（蛋白质对 → 是否存在相互作用）。

```python
# 输入：两条蛋白质序列（或 UniProt ID）
input_pair = {
    "protein_A": "MSSVSFDGLVEGASTTQRFLKKNLQAGF...",   # 序列 / P12345
    "protein_B": "MGPNPTAAFLCTGQTADLSITFDIKDGA...",   # 序列 / Q67890
}

# 输出：互作概率 + 二值标签
output = {
    "interacts":  True,   # 二分类标签（阈值通常 0.5）
    "confidence": 0.87,   # 模型输出概率
    # 评测指标
    "AUROC":  0.85,       # 严格物种切分（PRING）
    # ⚠️ 随机切分下同一模型 AUROC 可虚高至 ~0.92，严格切分降至 ~0.72
}
```

**空白**：界面残基预测精度、弱互作（Kd > μM级别）、条件依赖性PPI（磷酸化依赖等）。

---

## 4. [蛋白质语言模型（PLM）序列理解](notes/plm_sequence_understanding.md)

| Benchmark | 年份 | 任务 | 模型 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **多任务PLM评测** | 2024 | 二级结构/无序/定位/稳定性/溶解度/表位 | ESM2, ProtT5, Ankh, ProstT5, xTrimoPGLM, SaProt | AUC, Spearman ρ | ESM2-3B: 定位 AUC **~0.90**，稳定性 Spearman **~0.67**；微调在所有任务必要 | [Nat. Commun. 2024](https://www.nature.com/articles/s41467-024-51844-2) |
| **DARKIN** | 2024 | 零样本黑暗激酶-磷酸化位点分类 | 多PLM零样本 | AUC | 最优PLM零样本 AUC **~0.75**；监督微调可达 ~0.88 | [OpenReview](https://openreview.net/forum?id=a4x5tbYRYV) |

**任务类型**：多任务混合 — PLM 提取序列嵌入后，接不同下游头，涵盖每残基分类、全序列分类、全序列回归。

```python
# 输入：氨基酸序列
input_sequence = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQ..."  # 长度 L

# PLM 编码（以 ESM2-3B 为例）
plm_embedding = esm2_3b.encode(input_sequence)  # shape: (L, 2560)

# 输出（多个下游任务并行预测）
output = {
    # 每残基多分类：二级结构（Q3）
    "secondary_structure": ["H","H","E","E","C","C","H", ...],
    # H = α-helix，E = β-strand，C = coil；共 L 个标签
    "ss_Q3_accuracy": 0.84,

    # 每残基二分类：本征无序（IDP）
    "disorder": [0, 0, 1, 1, 1, 0, ...],   # 1 = 无序区域
    "disorder_AUC": 0.82,

    # 全序列多分类：亚细胞定位（10类）
    "localization": "nucleus",
    "localization_AUC": 0.90,

    # 全序列回归：热稳定性 Tm（°C）
    "Tm_predicted": 62.4,
    "stability_spearman_rho": 0.67,

    # 每残基二分类：激酶磷酸化位点（DARKIN）
    "phospho_sites": [0, 0, 0, 1, 0, ...],
    "phospho_AUC_zeroshot": 0.75,   # 零样本；监督微调可达 ~0.88
}
```

**当前水平小结**：PLM在结构和功能预测上成熟，但零样本迁移能力仍有差距；多任务统一评测体系缺失。
