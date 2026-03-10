# 分子生物学 Benchmarks

## 1. 蛋白质结构预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **CASP14** | 2020 | 3D结构预测（自由建模） | ~100 targets/届 | GDT_TS, TM-score, lDDT-Cα | AlphaFold2: GDT_TS **92.4**，sum-z-score 244 | [PMC9299164](https://pmc.ncbi.nlm.nih.gov/articles/PMC9299164/) |
| **CASP15** | 2022 | 单链+复合体结构预测 | 100+ targets | GDT_TS, DockQ | AF2变体仍主导；ESMFold（纯PLM）竞争力不足 | [PMC10792517](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792517/) |
| **CAMEO** | 持续 | 自动连续评测（每周新结构） | ~200 targets/周 | lDDT, QS-score | AF2变体长期领先 | [cameo3d.org](https://www.cameo3d.org/) |

**空白**：蛋白质复合体预测（>2条链）、本征无序区域、共折叠蛋白动态构象。

---

## 2. 蛋白质功能与适应性预测

> ⚠️ 注：蛋白质fitness类benchmark性能以**跨assay中位数Spearman ρ**衡量，不同蛋白家族间差异很大，不存在单一SOTA数字。下表列出目前最佳已知分数。

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA（最佳已知分数） | 参考 |
|-----------|------|------|------|------|---------------------|------|
| **ProteinGym** | 2023 (NeurIPS) | 蛋白质适应性预测（零样本+监督） | 2.7M missense变体 × 217 DMS实验；~300K indels × 74实验；2,525临床蛋白 | 中位数 Spearman ρ | 零样本：Tranception L **0.46**；ESM-1v 0.44；EVE 0.44；监督微调：~0.57 | [proteingym.org](https://proteingym.org/benchmarks) |
| **FLIP** | 2021 | 蛋白质适应性/性质预测（标准化切分） | AAV/GFP/GB1/热稳定性等多个实验 | 每任务 Spearman ρ | GB1 low-vs-high split: ESM2微调 **~0.75**；AAV: ~0.85（任务差异大） | [GitHub FLIP](https://github.com/J-SNACKKB/FLIP) |
| **PEER** | 2022 | 多任务蛋白质理解（功能/结构/互作/定位） | 15个数据集×5类 | AUC, Spearman ρ | ESM2/ProtTrans微调；各子任务平均 AUC **~0.85** | [arXiv 2206.02096](https://arxiv.org/abs/2206.02096) |
| **ProteinGLUE** | 2022 | 自监督蛋白建模，7个下游任务 | 多任务 | 各任务独立指标 | ESM-1b 在7个任务中5个最优；二级结构 Q3 **~84%** | [Sci. Reports 2022](https://www.nature.com/articles/s41598-022-19608-4) |
| **FLIP2** | 2026 | 蛋白质fitness landscape基准（扩展版） | 比FLIP更多蛋白+更多样选择压力 | 中位数 Spearman ρ | 竞赛进行中，暂无公开SOTA | [bioRxiv 2026.02.23](https://www.biorxiv.org/content/10.64898/2026.02.23.707496v1) |
| **CAFA6** | 2026 | 蛋白质GO功能注释预测（竞赛） | 上百万未注释蛋白序列；时间切片后续注释为金标准 | F-max, S_min | Kaggle竞赛进行中，暂无公开SOTA | [Kaggle CAFA6](https://www.kaggle.com/competitions/cafa-6-protein-function-prediction) |
| **1.4M结构基准集** | 2025 | 结构质量/泛化性评估（大规模统计） | 140万经质量检查的蛋白结构 | 结构质量评分 | 为AF2/3等提供长期可更新的统计严格测试集（非竞赛型，无排行榜） | [Briefings Bioinformatics 2025](https://academic.oup.com/bib/article/26/2/bbaf104/8069415) |

**空白**：多蛋白体系功能、酶催化机制定量预测、蛋白-配体结合自由能。

---

## 3. 蛋白质-蛋白质互作（PPI）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **PRING** | 2024–2025 | 图级别PPI，多物种，无泄露切分 | 21,484蛋白，186,818互作对 | AUROC, F1 | 图模型 | [arXiv 2507.05101](https://arxiv.org/html/2507.05101v1) |
| **SHS27k / SHS148k** | 2019–2021 | 二分类PPI | 27K / 148K对（来自STRING） | AUROC, accuracy | KSGPPI: **88.96%** accuracy, MCC 0.781 | [PMC8746451](https://pmc.ncbi.nlm.nih.gov/articles/PMC8746451/) |
| **Human PPI社区评测** | 2023 | 26种方法横向比较，4物种，6个蛋白质组 | 多物种 | 多指标 | 随机切分数据泄露是主要陷阱 | [Nat. Commun. 2023](https://www.nature.com/articles/s41467-023-37079-7) |

**空白**：界面残基预测精度、弱互作（Kd > μM级别）、条件依赖性PPI（磷酸化依赖等）。

---

## 4. 蛋白质语言模型（PLM）序列理解

| Benchmark | 年份 | 任务 | 模型 | 指标 | 关键发现 | 参考 |
|-----------|------|------|------|------|---------|------|
| **多任务PLM评测** | 2024 | 二级结构/无序/定位/稳定性/溶解度/表位 | ESM2, ProtT5, Ankh, ProstT5, xTrimoPGLM, SaProt | AUC, Spearman ρ | 微调几乎在所有任务上必要；ESM2/Ankh持续领先 | [Nat. Commun. 2024](https://www.nature.com/articles/s41467-024-51844-2) |
| **DARKIN** | 2024 | 零样本黑暗激酶-磷酸化位点分类 | 多PLM零样本 | AUC | 新兴零样本PLM能力测试 | [OpenReview](https://openreview.net/forum?id=a4x5tbYRYV) |

**当前水平小结**：PLM在结构和功能预测上成熟，但零样本迁移能力仍有差距；多任务统一评测体系缺失。
