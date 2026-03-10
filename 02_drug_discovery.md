# 药物发现 Benchmarks

## 1. ADMET 预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **TDC ADMET Benchmark Group** | 2021–持续 | 22个ADMET任务（吸收/分布/代谢/排泄/毒性），分类+回归 | 每个数据集数千个化合物 | AUROC（分类），MAE/Spearman ρ（回归） | ADMET-AI（Chemprop-RDKit GNN），22个数据集全面领先 | [tdcommons.ai](https://tdcommons.ai/benchmark/admet_group/overview/) |
| **PharmaBench** | 2024 | 11个关键ADMET性质，比TDC更大更多样 | >22性质，化合物数量实质更大 | AUROC, RMSE | LLM增强的SMILES表示竞争力强 | [Nat. Sci. Data 2024](https://www.nature.com/articles/s41597-024-03793-0) |
| **Tox21 Challenge** | 2014–持续 | 12个毒理学终点 | ~12,000化合物×12实验 | AUROC | 图模型+Transformer（Chemprop, GROVER）领先；2024年建立可复现排行榜 | [arXiv 2511.14744](https://arxiv.org/html/2511.14744v1) |

**空白**：多目标ADMET联合建模（非独立任务）；稀有毒性（hERG以外）；跨物种代谢差异。

---

## 2. 药物-靶标互作（DTI）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Davis** | 2011 | 结合亲和力Kd，激酶家族 | 442蛋白 × 68配体 | MSE, CI | 注意力DTA > GCN/序列法；CI > 0.90 | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **KIBA** | 2014 | 整合生物活性评分（IC50/Ki/Kd） | 117,657对；2,068药物；229蛋白 | MSE, CI | 最佳DTA模型 CI ~0.88–0.90 | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **BindingDB** | 持续 | 多亲和力类型（Kd/IC50/Ki） | 991K+ IC50对；375K+ Ki对 | AUROC, MSE | FragXsiteDTI / SSCPA-DTI / GraphsformerCPI: AUROC **~0.99** | [Briefings Bioinformatics 2025](https://academic.oup.com/bib/article/26/5/bbaf491/8260789) |
| **Structure-based DTI** | 2024 | 3D结构感知DTI，30+模型横评 | Davis/KIBA/BindingDB_Kd | MSE, CI, AUROC | Transformer+GNN混合最强；标准化实验条件 | [arXiv 2407.04055](https://arxiv.org/html/2407.04055v1) |

**空白**：共价结合药物、变构位点、选择性预测（vs. 整个激酶组）。

---

## 3. 分子性质预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MoleculeNet** | 2018 | 17+数据集（QM7/9, ESOL, FreeSolv, Lipophilicity, HIV, BACE, BBBP, Tox21, SIDER, ClinTox等） | 数百到数百万化合物 | AUROC, RMSE | Graph Transformer（Uni-Mol, GROVER, ChemBERTa-2）领先 | [moleculenet.org](https://moleculenet.org/) |
| **TDC（全量）** | 2021–持续 | 66个AI就绪数据集，22个学习任务，29个公开排行榜 | 从早期发现到临床阶段 | 任务特定 | 覆盖QM性质/生物活性/临床结局 | [tdcommons.ai](https://tdcommons.ai/) |

**空白**：量子化学性质（更高精度基准）；手性/立体选择性；天然产物多样性。

---

## 4. 从头药物设计 / 分子生成

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MOSES** | 2020 | 分布学习型生成模型评测 | ~1.9M类药ZINC（训练）；~176K（测试） | Validity, Uniqueness, Novelty, FCD, Fragment/Scaffold相似度, 内部多样性 | FCD < 0.5为最佳 | [Frontiers Pharmacol. 2020](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2020.565644/full) |
| **GuacaMol** | 2019 | 目标导向+分布学习；20个优化基准+5个分布测试 | ChEMBL来源 | Validity, KL散度, FCD, 基准分(0–1) | REINVENT, Graph GA, LSTM HC在目标导向任务领先 | [JCIM 2019](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839) |
| **MolScore** | 2024 | 统一评分+评测框架，整合GuacaMol/MOSES+新任务 | 包装多目标 | 多目标评分 | 标准化跨架构生成模型比较 | [J. Cheminformatics 2024](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00861-w) |
| **TOMG-Bench** | 2024 | 文本引导分子生成（LLM） | 25个LLM评测 | 自动有效性+质量评分 | Llama3.1-8B微调比GPT-3.5高 **+46.5%**；通用LLM普遍欠佳 | [IntuitionLabs](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |

| **3D扩散模型分子生成综合评测** | 2025 | 无条件/条件3D分子生成（ZINC系列+PDBbind子集）；对比MiDi/EQGAT-diff等 | ZINC类药化合物 + PDBbind | Validity, Uniqueness, 3D RMSD, Coverage, 性质分布匹配 | 2024–2025多篇扩散模型论文采用统一benchmark设计 | [ACS Omega 2025](https://pubs.acs.org/doi/10.1021/acsomega.5c05077) |
| **3D结构引导分子生成基准** | 2025 | 给定蛋白口袋生成高亲和力小分子 | PDBbind子集 | Docking score, SA（合成可及性）, QED（类药性） | 系统性对比structure-based生成模型 | [JCIM 2025](https://pubs.acs.org/doi/10.1021/acs.jcim.5c01020) |
| **ChemBERTa-3** | 2026 | 化学基础模型统一训练框架评测（MoleculeNet + 多任务） | MoleculeNet全套 | AUROC, RMSE | 开源训练框架；系统比较预训练策略（对比学习/自监督）的影响 | [RSC Digital Disc. 2026](https://pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00348b) |

**空白**：蛋白质序列条件下分子生成（结构引导）；从文本描述生成具有生物活性的分子；多步合成路线可行性。
