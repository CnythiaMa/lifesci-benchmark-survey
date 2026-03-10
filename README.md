# 生命科学 AI Benchmark 全景图

> 目标：梳理现有 benchmark 的覆盖范围与水平，找到空白，为新 benchmark 的设计提供定位锚点。
> 更新时间：2026-03

## 🗺️ 交互式全景脑图

**[→ 打开可交互脑图（节点可展开/收起）](https://cnythiama.github.io/lifesci-benchmark-survey/mindmap.html)**

> 脑图覆盖全部 6 大领域 / 50+ benchmark，支持缩放、拖拽、节点折叠。需在浏览器中打开（GitHub Pages 托管）。

## 文件结构

```
leaderboard/
├── README.md                      # 本文件：总览与导航
├── 01_protein_biology.md          # 蛋白质结构/功能(CASP/ProteinGym/CAFA/FLIP2)/PPI/PLM
├── 02_drug_discovery.md           # ADMET / DTI / 分子性质 / 2D+3D分子生成
├── 03_genomics_singlecell.md      # 变异效应 / 基因表达 / 调控元件 / 单细胞RNA-seq / 空间转录组
├── 04_clinical_medical.md         # 医学QA / 临床NLP / 诊断 / EHR / ICD编码 / DRAGON / GLiNER
├── 05_multimodal.md               # 医学影像VQA / MULAN / MedGemma / 多模态基础模型
├── 06_biomedical_nlp.md           # NER / RE / BLURB / BigBIO / 生物信息学编程
├── 07_agents_integrated.md        # AI智能体评测 / BEACON / 跨领域综合套件
└── 08_gap_analysis.md             # Gap分析：现有空白 → 新benchmark定位
```

## 快速总览



| 领域 | 代表性 Benchmark | 当前 SOTA | 主要短板 |
|------|-----------------|-----------|---------|
| 蛋白质结构 | CASP14/15, CAMEO | AlphaFold2 GDT 92.4 | 复合体、共折叠 |
| 蛋白质功能/适应性 | ProteinGym (217 assays) | EVE/ESM-1v | 零样本多任务 |
| PPI | PRING, SHS148k | KSGPPI 88.96% | 数据泄露问题普遍 |
| ADMET | TDC (22 tasks) | ADMET-AI | 多任务联合建模 |
| 药物-靶标结合 | Davis, KIBA, BindingDB | CI >0.90 | 3D结构感知 |
| 分子生成 | MOSES, GuacaMol | FCD <0.5 | 多目标优化 |
| 基因组变异效应 | ClinVar+gnomAD | AlphaGenome AUC 0.86 | 非编码区机制解释 |
| 基因表达预测 | Enformer | Pearson r 0.875 | scRNA扰动预测 ⚠️ |
| 医学QA | MedQA(USMLE) | Med-Gemini 91.1% | 推理过程可解释性 |
| 临床NLP | BLURB, n2c2 | Fine-tuned BERT F1 90% | 零样本LLM仍差 |
| 医学影像VQA | PathMMU, OmniMedVQA | GPT-4V级别 | 跨模态推理 |
| 生物医学NLP | BigBIO (100+ datasets) | PubMedBERT | 多语言覆盖 |
| 单细胞RNA-seq | scBench (394问题) | scRNA扰动：基线>所有FM ⚠️ | 智能体工作流评测 |
| 空间转录组 | HESCAPE, 11方法比较 | Pearson r ~0.7–0.8 | 视觉-基因组对齐 |
| AI智能体 | scBench, MedAgentBench, BioAgent Bench | MedArena: Gemini 2.0 Flash #1 | 完整工作流评测 |

## 核心发现（定位新 Benchmark 的关键依据）

1. **结构化任务上，微调 >> 零样本**：NER/RE/DTI/蛋白质适应性预测中，专门微调的小模型持续优于 GPT-4 零样本。
2. **scRNA 扰动预测：所有基础模型都输给 PCA baseline**（Nature Methods 2025 重磅结论）。
3. **数据泄露是系统性问题**：PPI、DTI benchmark 普遍存在随机切分导致的性能虚高。
4. **临床 benchmark 正从选择题转向真实任务**：MedAgentBench、MedArena 测的是 EHR 操作而非知识记忆。
5. **分子生物学没有统一跨领域排行榜**：ProteinGym/CASP/TDC 各管一段，无整合视角。
6. **当前 benchmark 极少涵盖序列标记（`<mol>`, `<protein>`, `<rna>`）的理解与生成**。
