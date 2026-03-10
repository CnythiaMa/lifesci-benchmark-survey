# 基因组学 & 单细胞/空间组学 Benchmarks

## 1. 变异效应预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **ClinVar致病变异基准** | 2024 | 区分致病SNP与常见SNP（零样本） | ClinVar致病变体 + gnomAD常见变体 | AUC | NT-v2: AUC **0.73**；Caduceus-Ph相当；AlphaGenome ~0.78 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **QTL预测基准** | 2024 | 因果QTL变异效应（sQTL/ipaQTL/eQTL/pQTL） | GTEx及相关QTL数据集 | AUC, Cohen's d | AlphaGenome: sQTL AUC **0.80**，ipaQTL **0.86**；Enformer: sQTL ~0.73 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **DNA基础模型5模型横评** | 2024–2025 | 序列分类/基因表达/变异效应/TAD识别 | 多基因组任务 | AUC, Spearman ρ | 表观遗传分类：NT-v2 AUC **~0.89**；基因表达：Caduceus-Ph Spearman **~0.62**；任务依赖性强 | [bioRxiv 2024.08.16](https://www.biorxiv.org/content/10.1101/2024.08.16.608288v2) |
| **AlphaGenome 26-benchmark suite** | 2025 | 26个变异效应预测任务（基因表达改变/剪接/polyA/增强子-基因作用等） | 多数据库整合 | AUC, Spearman ρ | AlphaGenome综合最优：剪接 AUC **~0.91**，基因表达 Spearman **~0.68**；26任务全面领先 | [PMC12851941](https://pmc.ncbi.nlm.nih.gov/articles/PMC12851941/) |

**空白**：罕见变异功能效应（频率<0.001%）；RNA剪接变异机制解释；多变体协同效应。

---

## 2. 基因表达预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Enformer基准** | 2021 | 序列→基因表达（CAGE/ATAC/ChIP），200kb上下文 | ENCODE/Roadmap表观基因组 | Pearson r, Spearman ρ | Enformer Pearson r ~0.85；EPInformer提升至 **0.875–0.891**；Borzoi ~0.79 | [Nat. Methods 2021](https://www.nature.com/articles/s41592-021-01252-x) |
| **scRNA-seq扰动预测基准** | 2024 | 预测基因扰动后转录组变化 | Replogle等 Perturb-seq；Norman等 | Pearson r（delta表达） | ⚠️ **重磅（Nature Methods 2025）：PCA/scVI基线 r ~0.35；scGPT/Geneformer r ~0.22–0.28，全面落后基线** | [Nat. Methods 2025](https://www.nature.com/articles/s41592-025-02772-6) |
| **scGPT/Geneformer评测** | 2023–2024 | 细胞类型注释/批次校正/基因表达重建 | 多个scRNA-seq atlas数据集 | ARI, AUROC | Geneformer ARI **0.11**，scGPT ARI **0.18**；零样本均输给标准批次校正（ARI ~0.35） | — |

**关键教训**：scRNA-seq基础模型在扰动预测上表现不如简单基线，提示现有模型缺乏真正的"因果机制"理解。

---

## 3. 调控元件预测与基因组注释

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Nucleotide Transformer (NT)基准** | 2024 | 18个下游基因组任务（调控元件/剪接位点/染色质） | ENCODE, RefSeq注释 | MCC, F1, AUC | NT-v2 250M: 剪接位点 MCC **~0.73**，染色质 AUC **~0.89**；SegmentNT在基因注释SOTA | [Nat. Methods 2024](https://www.nature.com/articles/s41592-024-02523-z) |
| **SegmentNT / 核苷酸分辨率基因组注释** | 2024–2025 | 单核苷酸分辨率14类基因/调控区域注释 | 人类参考基因组 | 每类F1 | SegmentNT: 剪接位点 F1 **~0.92**，启动子 **~0.85**，lncRNA **~0.71** | [bioRxiv 2024.03.14](https://www.biorxiv.org/content/10.1101/2024.03.14.584712v3.full) |
| **调控变异因果预测** | 2024–2025 | 预测GWAS中因果非编码调控变异 | ENCODE精细定位变体 | AUC | AlphaGenome最优: AUC **~0.83**；Enformer微调 ~0.79 | [PMC11844472](https://pmc.ncbi.nlm.nih.gov/articles/PMC11844472/) |
| **长程DNA预测基准套件** | 2025 | 人/小鼠基因组多种实验信号轨迹（染色质可及性/组蛋白修饰），长程上下文 | ENCODE公共资源 | Pearson r, R² | Borzoi（256kb上下文）: 平均 Pearson r **~0.79**；Enformer（200kb）: ~0.75 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65077-4) |
| **GFMBench-API** | 2026 | 基因组基础模型统一接口评测（监督+零样本） | DNA/表观基因组多种任务 | 多指标 | 首个标准化接口框架；NT-v2/DNABERT-2综合最优；竞赛持续更新 | [bioRxiv 2026.02.19](https://www.biorxiv.org/content/10.64898/2026.02.19.706811v1.full.pdf) |
| **DNA Long Bench / Genomics LRB** | 2025 | 长程DNA预测（最长1M bp上下文）；染色质/表观信号 | 多任务 | Pearson r, AUC | DNABERT-2最稳定：平均 AUC **~0.85**；NT-v2表观遗传检测 AUC **~0.89** | [arXiv 2409.12641](https://arxiv.org/abs/2409.12641) |

**空白**：3D基因组（Hi-C/TAD/loop）与调控变异整合预测；跨细胞类型增强子活性差异；非人物种基因组功能注释。

---

## 4. 单细胞 RNA-seq 分析

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **scBench** | 2026 | AI智能体执行scRNA-seq分析工作流（聚类/注释/差异表达/伪时间等） | 394个可验证问题；6种测序平台；多个真实分析步骤 | 任务正确率，分析步骤合理性 | 最优AI agent任务正确率 **~65%**；复合步骤任务显著下降 | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **scSuperAnnotator** | 2025 | 细胞类型注释方法大规模横向比较 | 大规模多数据集平台 | 注释准确率，跨数据集一致性（Jaccard） | 最优监督方法准确率 **~90%**；零样本迁移 ~75% | [NAR 2025](https://academic.oup.com/nar/article/54/1/gkaf1470/8415836) |
| **scRNA扰动预测基准** | 2024–2025 | 预测基因敲除/过表达后转录组变化 | Replogle Perturb-seq；Norman等 | Pearson r（delta表达） | ⚠️ **重磅（Nature Methods 2025）：所有FM均输给PCA/scVI基线（r ~0.35）；scGPT/Geneformer r ~0.22–0.28** | [Nat. Methods 2025](https://www.nature.com/articles/s41592-025-02772-6) |
| **sc-HeurekaBench** | 2026 | 从13篇Nature/Cell单细胞论文（2024–2025）半自动构建的Agent评测；要求模型复现论文核心分析结论；50道开放题+50道MCQ；ICLR 2026 | 100题（50 OEQ + 50 MCQ）；来自41个论文insight | OEQ: 1–5分（GPT-4o评分）；MCQ: 准确率/召回率 | Biomni Agent: OEQ **2.31/5**，MCQ **50%**；BixBench-Agent: OEQ 2.34/5；CritiqAgent模块可提升开源模型 +22% | [arXiv 2601.01678](https://arxiv.org/abs/2601.01678) |
| **Biomni-Eval1**（单细胞/基因组部分） | 2025 | GWAS因果基因识别（3数据源变体）、GWAS变异优先级排序、CRISPR靶点筛选基因检索；由Stanford Biomni团队构建 | 433题总计（GWAS相关子集：~1500训练/50测试） | 准确率（基因符号匹配） | Biomni Agent（Stanford）综合最优；具体分数未公开 | [HuggingFace biomni/Eval1](https://huggingface.co/datasets/biomni/Eval1) |

**已知任务类型**：细胞聚类与类型注释 / 批次效应校正 / 差异基因表达分析 / 伪时间/轨迹推断 / 基因扰动效应预测 / 细胞通讯预测

**核心教训**：单细胞基础模型在扰动预测上不及传统方法，提示规模化预训练对单细胞数据的适用性仍有根本性问题。

---

## 5. 空间转录组

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **空间基因表达预测基准** | 2025 | 从组织病理图像（H&E染色）预测空间基因表达；11种方法横向比较 | 多组织切片数据集 | Pearson r（per-gene平均） | 最优方法（Hist2ST类）平均 Pearson r **~0.45**；高变基因 ~0.60 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-56618-y) |
| **HESCAPE** | 2025 | Vision–Genomics alignment在空间转录组中的评估 | 空间转录组数据+组织切片图像对 | 对齐精度，跨模态检索 R@1 | 当前最优跨模态检索 R@1 **~55%**；benchmark仍处建立阶段 | [LinkedIn/preprint 2025](https://www.linkedin.com/pulse/hescape-benchmark-visiongenomics-alignment-spatial-rushin-gindra-rfrsf) |

---

## 6. 当前空白

- **空间多组学整合**：空间转录组+蛋白质组+代谢组联合预测，无标准benchmark
- **单细胞时序数据**：跨时间点细胞命运预测（如胚胎发育）
- **跨模态单细胞翻译**：从ATAC-seq预测RNA表达
- **细胞-细胞通讯（CCC）定量评测**：现有CCC方法缺乏统一gold standard benchmark
- **3D基因组与调控**：Hi-C/TAD/loop与调控变异整合预测
