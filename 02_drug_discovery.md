# 药物发现 Benchmarks

## 1. ADMET 预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **TDC ADMET Benchmark Group** | 2021–持续 | 22个ADMET任务（吸收/分布/代谢/排泄/毒性），分类+回归 | 每个数据集数千个化合物 | AUROC（分类），MAE/Spearman ρ（回归） | ADMET-AI（Chemprop-RDKit GNN）：22任务平均 AUROC **~0.871**，全面领先 | [tdcommons.ai](https://tdcommons.ai/benchmark/admet_group/overview/) |
| **PharmaBench** | 2024 | 11个关键ADMET性质，比TDC更大更多样 | >22性质，化合物数量实质更大 | AUROC, RMSE | LLM增强的SMILES表示：平均 AUROC **~0.86**；与专用GNN持平 | [Nat. Sci. Data 2024](https://www.nature.com/articles/s41597-024-03793-0) |
| **Tox21 Challenge** | 2014–持续 | 12个毒理学终点 | ~12,000化合物×12实验 | AUROC | Chemprop / GROVER：各终点 AUROC **~0.85–0.88**；2024年建立可复现排行榜 | [arXiv 2511.14744](https://arxiv.org/html/2511.14744v1) |

**任务类型**：多任务分类 + 回归（同一分子同时预测多种 ADMET 属性）。

```python
# 输入：分子 SMILES 字符串
input_smiles = "CC(=O)Oc1ccccc1C(=O)O"   # 阿司匹林

# 输出：多个 ADMET 属性（分类 or 回归，任务类型各异）
output = {
    # 分类：血脑屏障穿透（BBBP）
    "BBB_penetration": True,
    "BBB_prob":        0.73,
    # 分类：hERG 心脏毒性
    "hERG_inhibitor":  False,
    "hERG_prob":       0.12,
    # 回归：水溶性 logS（mol/L，log scale）
    "logS":           -1.94,
    # 回归：Caco-2 渗透率（log cm/s）
    "Caco2_perm":     -4.87,
    # 评测：TDC ADMET 22任务平均 AUROC
    "avg_AUROC_22tasks": 0.871,   # SOTA: ADMET-AI
}
```

**空白**：多目标ADMET联合建模（非独立任务）；稀有毒性（hERG以外）；跨物种代谢差异。

---

## 2. 药物-靶标互作（DTI）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Davis** | 2011 | 结合亲和力Kd，激酶家族 | 442蛋白 × 68配体 | MSE, CI | 注意力DTA：CI **0.893**，MSE 0.229 | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **KIBA** | 2014 | 整合生物活性评分（IC50/Ki/Kd） | 117,657对；2,068药物；229蛋白 | MSE, CI | 最佳DTA模型：CI **~0.901**，MSE ~0.143 | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **BindingDB** | 持续 | 多亲和力类型（Kd/IC50/Ki） | 991K+ IC50对；375K+ Ki对 | AUROC, MSE | FragXsiteDTI / GraphsformerCPI: AUROC **~0.99**（二分类）；亲和力回归 Pearson r ~0.82 | [Briefings Bioinformatics 2025](https://academic.oup.com/bib/article/26/5/bbaf491/8260789) |
| **Structure-based DTI** | 2024 | 3D结构感知DTI，30+模型横评 | Davis/KIBA/BindingDB_Kd | MSE, CI, AUROC | Transformer+GNN混合：CI **~0.91**（Davis）；标准化实验条件下结构信息提升 ~2% | [arXiv 2407.04055](https://arxiv.org/html/2407.04055v1) |

**任务类型**：回归（药物-蛋白质对 → 结合亲和力）/ 二分类（结合/不结合）。

```python
# 输入：药物 SMILES + 靶标蛋白氨基酸序列
input_drug    = "CC1=CC=C(C=C1)NC2=NC=CC(=N2)NC3=CC=CC(=C3)S(=O)(=O)N"   # 达沙替尼类
input_protein = "MRGARGAWDFLCVLLLLLRVQTGSSQPSVSPGEPSPPSIHPGKSDLIVRVGD..."   # BCR-ABL 激酶

# 输出：结合亲和力预测
output = {
    "binding_affinity_pKd": 9.14,   # pKd = -log10(Kd)，值越高亲和力越强
    "binding_label":         True,   # 二分类（阈值 30 nM）
    # 评测（Davis 数据集）
    "CI":  0.893,   # Concordance Index（排序一致性）
    "MSE": 0.229,   # 均方误差（pKd 空间）
}
```

**空白**：共价结合药物、变构位点、选择性预测（vs. 整个激酶组）。

---

## 3. 分子性质预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MoleculeNet** | 2018 | 17+数据集（QM7/9, ESOL, FreeSolv, Lipophilicity, HIV, BACE, BBBP, Tox21, SIDER, ClinTox等） | 数百到数百万化合物 | AUROC, RMSE | Uni-Mol/GROVER: HIV AUROC **~0.82**，BBBP **~0.91**，ClinTox **~0.94**；ESOL RMSE ~0.58 | [moleculenet.org](https://moleculenet.org/) |
| **TDC（全量）** | 2021–持续 | 66个AI就绪数据集，22个学习任务，29个公开排行榜 | 从早期发现到临床阶段 | 任务特定 | 覆盖QM性质/生物活性/临床结局；各子任务SOTA见TDC排行榜 | [tdcommons.ai](https://tdcommons.ai/) |

**任务类型**：分类（生物活性/毒性）+ 回归（物化性质）。

```python
# 输入：分子 SMILES
input_smiles = "c1ccc2c(c1)cc1ccc3cccc4ccc2c1c34"   # 苯并芘（多环芳烃）

output = {
    # 分类：HIV 逆转录酶抑制活性（MoleculeNet HIV）
    "HIV_active": True,  "HIV_prob": 0.81,    # AUROC ~0.82（Uni-Mol SOTA）
    # 分类：血脑屏障穿透（BBBP）
    "BBBP":      False,  "BBBP_prob": 0.18,
    # 回归：水溶解度 logS（ESOL）
    "logS":      -5.42,                       # RMSE ~0.58（SOTA）
    # 回归：脂水分配系数（Lipophilicity）
    "logP":       5.18,
}
```

**空白**：量子化学性质（更高精度基准）；手性/立体选择性；天然产物多样性。

---

## 4. 从头药物设计 / 分子生成

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MOSES** | 2020 | 分布学习型生成模型评测 | ~1.9M类药ZINC（训练）；~176K（测试） | Validity, Uniqueness, Novelty, FCD | LSTM-based: Validity **99.9%**，FCD **~0.07**，Novelty ~94%；Transformer: FCD ~0.09 | [Frontiers Pharmacol. 2020](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2020.565644/full) |
| **GuacaMol** | 2019 | 目标导向+分布学习；20个优化基准+5个分布测试 | ChEMBL来源 | Validity, KL散度, FCD, 基准分(0–1) | REINVENT：目标导向平均分 **~0.79**；Graph GA在多样性任务领先 | [JCIM 2019](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839) |
| **MolScore** | 2024 | 统一评分+评测框架，整合GuacaMol/MOSES+新任务 | 包装多目标 | 多目标评分 | 标准化跨架构生成模型比较；当前最优多目标综合分 **~0.72** | [J. Cheminformatics 2024](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00861-w) |
| **TOMG-Bench** | 2024 | 文本引导分子生成（LLM） | 25个LLM评测 | 自动有效性+质量评分 | Llama3.1-8B微调：**46.5%** 高于GPT-3.5；通用LLM普遍欠佳（<30%） | [IntuitionLabs](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |
| **3D扩散模型分子生成综合评测** | 2025 | 无条件/条件3D分子生成；对比MiDi/EQGAT-diff等 | ZINC类药化合物 + PDBbind | Validity, 3D RMSD, Coverage | 最优扩散模型：Validity **~99%**，3D RMSD **~0.35Å**，Coverage ~0.65 | [ACS Omega 2025](https://pubs.acs.org/doi/10.1021/acsomega.5c05077) |
| **3D结构引导分子生成基准** | 2025 | 给定蛋白口袋生成高亲和力小分子 | PDBbind子集 | Docking score, SA, QED | 最优模型：Docking score **~-8.5 kcal/mol**，SA **~0.65**，QED **~0.52** | [JCIM 2025](https://pubs.acs.org/doi/10.1021/acs.jcim.5c01020) |
| **ChemBERTa-3** | 2026 | 化学基础模型统一训练框架评测（MoleculeNet + 多任务） | MoleculeNet全套 | AUROC, RMSE | ChemBERTa-3：MoleculeNet平均 AUROC **~0.88**；系统验证对比学习优于MLM预训练 | [RSC Digital Disc. 2026](https://pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00348b) |

**任务类型**：生成类（无条件分布生成 / 靶标口袋条件生成 / 文本引导生成）。

```python
# ── 子任务① 无条件分布学习（MOSES / GuacaMol）──────────────────────────
# 输入：无（从学习的分子分布中采样）
generated = [
    "CC(C)Cc1ccc(cc1)C(C)C(=O)O",         # 布洛芬类似物
    "COc1ccc2c(c1)c(CC(=O)N3CCCC3)cn2C",  # 新生成分子
]
metrics = {
    "Validity":   0.999,   # 合法 SMILES 比例
    "Uniqueness": 0.998,
    "Novelty":    0.940,   # 不在训练集中
    "FCD":        0.07,    # Fréchet ChemNet Distance（越小越好）
}

# ── 子任务② 3D 结构引导生成（给定蛋白口袋）─────────────────────────────
# 输入：蛋白靶标口袋 PDB 坐标
input_pocket = "pocket_CDK2.pdb"

output_3d = {
    "smiles":        "C1CC(N2C=NC3=C2N=CN=C3N)OC1CO",
    "docking_score": -8.5,    # kcal/mol（越负越强）
    "SA_score":       0.65,   # 合成可及性（0–1，越高越易合成）
    "QED":            0.52,   # 类药性（0–1）
    "3D_RMSD":        0.35,   # Å，与参考配体构象对比
}
```

**空白**：蛋白质序列条件下分子生成（结构引导）；从文本描述生成具有生物活性的分子；多步合成路线可行性。
