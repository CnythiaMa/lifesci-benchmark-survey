# 基因组学 Benchmarks

## 1. 变异效应预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **ClinVar致病变异基准** | 2024 | 区分致病SNP与常见SNP（零样本） | ClinVar致病变体 + gnomAD常见变体 | AUC | NT-v2: AUC **0.73**；Caduceus-Ph相当 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **QTL预测基准** | 2024 | 因果QTL变异效应（sQTL/ipaQTL/eQTL/pQTL） | GTEx及相关QTL数据集 | AUC, Cohen's d | AlphaGenome最佳：sQTL AUC **0.80**，ipaQTL **0.86** | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **DNA基础模型5模型横评** | 2024–2025 | 序列分类/基因表达/变异效应/TAD识别 | 多基因组任务 | AUC, Spearman ρ | DNABERT-2, NT-v2, HyenaDNA, Caduceus-Ph, GROVER横向比较；任务依赖性差异大 | [bioRxiv 2024.08.16](https://www.biorxiv.org/content/10.1101/2024.08.16.608288v2) |
| **AlphaGenome 26-benchmark suite** | 2025 | 26个变异效应预测任务（基因表达改变/剪接/polyA/增强子-基因作用等） | 多数据库整合 | AUC, Spearman ρ | AlphaGenome综合最优；最全面的单模型变异效应横评 | [PMC12851941](https://pmc.ncbi.nlm.nih.gov/articles/PMC12851941/) |

**空白**：罕见变异功能效应（频率<0.001%）；RNA剪接变异机制解释；多变体协同效应。

---

## 2. 基因表达预测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA / 关键发现 | 参考 |
|-----------|------|------|------|------|----------------|------|
| **Enformer基准** | 2021 | 序列→基因表达（CAGE/ATAC/ChIP），200kb上下文 | ENCODE/Roadmap表观基因组 | Pearson r, Spearman ρ | Enformer Pearson r ~0.85；EPInformer提升至 **0.875–0.891** | [Nat. Methods 2021](https://www.nature.com/articles/s41592-021-01252-x) |
| **scRNA-seq扰动预测基准** | 2024 | 预测基因扰动后转录组变化 | Replogle等 Perturb-seq；Norman等 | Pearson r（delta表达） | ⚠️ **重磅：所有基础模型（scGPT/Geneformer等）均输给PCA/scVI基线** | [Nat. Methods 2025](https://www.nature.com/articles/s41592-025-02772-6) |
| **scGPT/Geneformer评测** | 2023–2024 | 细胞类型注释/批次校正/基因表达重建 | 多个scRNA-seq atlas数据集 | ARI, AUROC | Geneformer ARI 0.11，scGPT ARI 0.18；零样本均输给标准批次校正 | — |

**关键教训**：scRNA-seq基础模型在扰动预测上表现不如简单基线，提示现有模型缺乏真正的"因果机制"理解。

---

## 3. 调控元件预测与基因组注释

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Nucleotide Transformer (NT)基准** | 2024 | 18个下游基因组任务（调控元件/剪接位点/染色质） | ENCODE, RefSeq注释 | MCC, F1, AUC | NT-v2 250M在调控任务强；SegmentNT在剪接位点和基因注释SOTA | [Nat. Methods 2024](https://www.nature.com/articles/s41592-024-02523-z) |
| **SegmentNT / 核苷酸分辨率基因组注释** | 2024–2025 | 单核苷酸分辨率14类基因/调控区域注释 | 人类参考基因组 | 每类F1 | SegmentEnformer/SegmentBorzoi改善lncRNA/CTCF/启动子/增强子分割 | [bioRxiv 2024.03.14](https://www.biorxiv.org/content/10.1101/2024.03.14.584712v3.full) |
| **调控变异因果预测** | 2024–2025 | 预测GWAS中因果非编码调控变异 | ENCODE精细定位变体 | AUC | Enformer衍生嵌入+微调竞争力强；AlphaGenome最优 | [PMC11844472](https://pmc.ncbi.nlm.nih.gov/articles/PMC11844472/) |
| **长程DNA预测基准套件** | 2025 | 人/小鼠基因组多种实验信号轨迹（染色质可及性/组蛋白修饰），长程上下文 | ENCODE公共资源 | Pearson r, R² | 专为长程上下文模型（Enformer类）设计的标准化测试集 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65077-4) |
| **GFMBench-API** | 2026 | 基因组基础模型统一接口评测（监督+零样本） | DNA/表观基因组多种任务 | 多指标 | 首个为基因组FM提供标准化API接口的评测框架 | [bioRxiv 2026.02.19](https://www.biorxiv.org/content/10.64898/2026.02.19.706811v1.full.pdf) | 
| **DNA Long Bench / Genomics LRB** | 2025 | 长程DNA预测（最长1M bp上下文）；染色质/表观信号 | 多任务 | Pearson r, AUC | DNABERT-2最稳定；NT-v2在表观遗传检测最优；专为超长上下文模型设计 | [arXiv 2409.12641](https://arxiv.org/abs/2409.12641) |

**空白**：3D基因组（Hi-C/TAD/loop）与调控变异整合预测；跨细胞类型增强子活性差异；非人物种基因组功能注释。
