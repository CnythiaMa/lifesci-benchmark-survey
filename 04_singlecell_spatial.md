# 单细胞与空间组学 Benchmarks

## 1. 单细胞 RNA-seq 分析 Benchmarks

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **scBench** | 2026 | AI智能体执行scRNA-seq分析工作流（聚类/注释/差异表达/伪时间等） | 394个可验证问题；6种测序平台；多个真实分析步骤 | 任务正确率，分析步骤合理性 | 最优AI agent任务正确率 **~65%**；复合步骤任务显著下降 | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **scSuperAnnotator** | 2025 | 细胞类型注释方法大规模横向比较 | 大规模多数据集平台 | 注释准确率，跨数据集一致性（Jaccard） | 最优监督方法准确率 **~90%**；零样本迁移 ~75% | [NAR 2025](https://academic.oup.com/nar/article/54/1/gkaf1470/8415836) |
| **scRNA扰动预测基准** | 2024–2025 | 预测基因敲除/过表达后转录组变化 | Replogle Perturb-seq；Norman等 | Pearson r（delta表达） | ⚠️ **重磅（Nature Methods 2025）：所有FM均输给PCA/scVI基线（r ~0.35）；scGPT/Geneformer r ~0.22–0.28** | [Nat. Methods 2025](https://www.nature.com/articles/s41592-025-02772-6) |

**已知任务类型**：细胞聚类与类型注释 / 批次效应校正 / 差异基因表达分析 / 伪时间/轨迹推断 / 基因扰动效应预测 / 细胞通讯预测

**核心教训**：单细胞基础模型（scGPT/Geneformer）在扰动预测上不及传统方法，提示规模化预训练对单细胞数据的适用性仍有根本性问题。

---

## 2. 空间转录组 Benchmarks

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **空间基因表达预测基准** | 2025 | 从组织病理图像（H&E染色）预测空间基因表达；11种方法横向比较 | 多组织切片数据集 | Pearson r（per-gene平均） | 最优方法（Hist2ST类）平均 Pearson r **~0.45**；高变基因 ~0.60 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-56618-y) |
| **HESCAPE** | 2025 | Vision–Genomics alignment在空间转录组中的评估 | 空间转录组数据+组织切片图像对 | 对齐精度，跨模态检索 R@1 | 当前最优跨模态检索 R@1 **~55%**；benchmark仍处建立阶段 | [LinkedIn/preprint 2025](https://www.linkedin.com/pulse/hescape-benchmark-visiongenomics-alignment-spatial-rushin-gindra-rfrsf) |

---

## 3. 当前空白

- **空间多组学整合**：空间转录组+蛋白质组+代谢组联合预测，无标准benchmark
- **单细胞时序数据**：跨时间点细胞命运预测（如胚胎发育）
- **跨模态单细胞翻译**：从ATAC-seq预测RNA表达（单细胞多组学翻译）
- **空间分辨率增强**：低分辨率空间组学数据的超分辨率预测
- **细胞-细胞通讯（CCC）定量评测**：现有CCC方法缺乏统一gold standard benchmark
