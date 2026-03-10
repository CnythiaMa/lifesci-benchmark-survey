# 生命科学 AI Benchmark 全景图

> 目标：梳理现有 benchmark 的覆盖范围与水平，找到空白，为新 benchmark 的设计提供定位锚点。
> 更新时间：2026-03

## 🗺️ 交互式全景脑图

**[→ 打开可交互脑图（节点可展开/收起）](https://cnythiama.github.io/lifesci-benchmark-survey/mindmap.html)**

> 脑图覆盖全部 7 大领域 / 50+ benchmark，支持缩放、拖拽、节点折叠。需在浏览器中打开（GitHub Pages 托管）。

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

**[→ 打开可交互总览表（支持 🔬 精调专用 / 🧠 LLM·Agent 筛选）](https://cnythiama.github.io/lifesci-benchmark-survey/overview.html)**

> 收录全部 ~108 个 Benchmark，按领域分组（01–07）；同名 benchmark 仅保留首次出现的领域。

### 🧬 01 蛋白质生物学

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **CASP14** | 2020 | 蛋白质3D结构预测 | ~100 targets | GDT_TS, lDDT | AlphaFold2 GDT_TS **92.4** | [PMC9299164](https://pmc.ncbi.nlm.nih.gov/articles/PMC9299164/) |
| **CASP15** | 2022 | 单链+复合体结构预测 | 100+ targets | GDT_TS, DockQ | AF2变体 TM **~0.92**；AF-Multimer DockQ **~0.60** | [PMC10792517](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792517/) |
| **CAMEO** | 持续 | 连续自动结构评测 | ~200 targets/周 | lDDT | AF2-based 平均 lDDT **>0.85** | [cameo3d.org](https://www.cameo3d.org/) |
| **1.4M结构基准集** | 2025 | 大规模结构泛化性评估 | 140万结构 | 质量评分 | 工具集，无排行榜 | [Briefings Bioinformatics](https://academic.oup.com/bib/article/26/2/bbaf104/8069415) |
| **ProteinGym** | 2023 | 蛋白质适应性预测（零样本+监督） | 2.7M变体×217 DMS实验 | 中位Spearman ρ | Tranception L **0.46**（零样本）；监督 **~0.57** | [proteingym.org](https://proteingym.org/benchmarks) |
| **FLIP** | 2021 | 蛋白质性质预测（标准化切分） | AAV/GFP/GB1/热稳定性等 | Spearman ρ | ESM2微调 GB1 **~0.75**；AAV **~0.85** | [GitHub FLIP](https://github.com/J-SNACKKB/FLIP) |
| **PEER** | 2022 | 多任务蛋白质理解（功能/结构/互作/定位） | 15数据集×5类 | AUC, Spearman ρ | ESM2/ProtTrans 平均 AUC **~0.85** | [arXiv 2206.02096](https://arxiv.org/abs/2206.02096) |
| **ProteinGLUE** | 2022 | 自监督蛋白建模，7个下游任务 | 多任务 | 各任务独立指标 | ESM-1b 二级结构 Q3 **~84%** | [Sci. Reports](https://www.nature.com/articles/s41598-022-19608-4) |
| **FLIP2** | 2026 | 蛋白质fitness landscape基准（扩展） | 比FLIP更多蛋白+选择压力 | 中位Spearman ρ | 竞赛进行中 | [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.02.23.707496v1) |
| **CAFA6** | 2026 | 蛋白质GO功能注释预测 | 百万级未注释蛋白 | F-max | Kaggle竞赛进行中 | [Kaggle](https://www.kaggle.com/competitions/cafa-6-protein-function-prediction) |
| **PRING** | 2024 | 蛋白质-蛋白质互作预测（无泄露切分） | 21,484蛋白；186,818对 | AUROC, F1 | 最优图模型 AUROC **~0.85**（严格切分） | [arXiv 2507.05101](https://arxiv.org/html/2507.05101v1) |
| **SHS27k / SHS148k** | 2019 | 二分类PPI（STRING来源） | 27K / 148K对 | AUROC, Accuracy | KSGPPI **88.96%** ⚠️数据泄露风险 | [PMC8746451](https://pmc.ncbi.nlm.nih.gov/articles/PMC8746451/) |
| **Human PPI社区评测** | 2023 | 26方法横评，4物种 | 多物种 | AUROC | 严格切分 **~0.72**；随机切分虚高 ~0.92 ⚠️ | [Nat. Commun.](https://www.nature.com/articles/s41467-023-37079-7) |
| **多任务PLM评测** | 2024 | PLM序列理解多任务横评 | ESM2/ProtT5等6模型 | AUC, Spearman ρ | ESM2-3B 定位 AUC **~0.90**；稳定性 **~0.67** | [Nat. Commun.](https://www.nature.com/articles/s41467-024-51844-2) |
| **DARKIN** | 2024 | 零样本暗激酶磷酸化位点分类 | 暗激酶数据集 | AUC | 零样本 **~0.75**；微调 **~0.88** | [OpenReview](https://openreview.net/forum?id=a4x5tbYRYV) |

### 💊 02 药物发现

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **TDC** | 2021– | ADMET 22任务+66数据集全量评测平台 | 数千化合物/任务 | AUROC, MAE, Spearman ρ | ADMET-AI 22任务平均 AUROC **~0.871** | [tdcommons.ai](https://tdcommons.ai/) |
| **PharmaBench** | 2024 | 11个关键ADMET性质预测 | 多来源大规模化合物 | AUROC, RMSE | LLM增强SMILES AUROC **~0.86** | [Nat. Sci. Data](https://www.nature.com/articles/s41597-024-03793-0) |
| **Tox21 Challenge** | 2014– | 12个毒理学终点 | ~12,000化合物 | AUROC | Chemprop/GROVER **~0.85–0.88** | [arXiv 2511.14744](https://arxiv.org/html/2511.14744v1) |
| **Davis** | 2011 | 结合亲和力Kd预测（激酶家族） | 442蛋白×68配体 | CI, MSE | 注意力DTA CI **0.893** | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **KIBA** | 2014 | 整合生物活性评分预测 | 117,657对 | CI, MSE | 最佳DTA CI **~0.901** | [TDC DTI](https://tdcommons.ai/multi_pred_tasks/dti/) |
| **BindingDB** | 持续 | 多类型亲和力预测（Kd/IC50/Ki） | 991K+ IC50对 | AUROC, MSE | FragXsiteDTI AUROC **~0.99**（二分类） | [Briefings Bioinformatics](https://academic.oup.com/bib/article/26/5/bbaf491/8260789) |
| **Structure-based DTI** | 2024 | 3D结构感知DTI 30+方法横评 | Davis/KIBA/BindingDB | CI, AUROC | Transformer+GNN CI **~0.91**（Davis） | [arXiv 2407.04055](https://arxiv.org/html/2407.04055v1) |
| **MoleculeNet** | 2018 | 分子性质预测（17+数据集） | 数百~数百万化合物 | AUROC, RMSE | Uni-Mol HIV **~0.82**；BBBP **~0.91** | [moleculenet.org](https://moleculenet.org/) |
| **MOSES** | 2020 | 分子生成分布学习评测 | ~1.9M类药ZINC | Validity, FCD | LSTM Validity **99.9%**；FCD **~0.07** | [Frontiers Pharmacol.](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2020.565644/full) |
| **GuacaMol** | 2019 | 目标导向+分布学习分子生成 | ChEMBL来源 | 基准分(0–1), FCD | REINVENT目标导向 **~0.79** | [JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00839) |
| **MolScore** | 2024 | 统一多目标分子生成评测框架 | 包装GuacaMol/MOSES | 多目标综合分 | 最优多目标综合 **~0.72** | [J. Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00861-w) |
| **TOMG-Bench** | 2024 | 文本引导分子生成（LLM评测） | 25个LLM评测 | 有效性+质量评分 | Llama3.1-8B微调 **46.5%** | [IntuitionLabs](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |
| **3D扩散模型分子生成评测** | 2025 | 无条件/条件3D分子生成方法比较 | ZINC + PDBbind | Validity, RMSD | 最优Validity **~99%**；RMSD **~0.35Å** | [ACS Omega](https://pubs.acs.org/doi/10.1021/acsomega.5c05077) |
| **3D结构引导分子生成基准** | 2025 | 蛋白口袋条件分子生成 | PDBbind子集 | Docking score, QED | 最优Docking **~-8.5 kcal/mol** | [JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.5c01020) |
| **ChemBERTa-3** | 2026 | 化学基础模型统一训练框架评测 | MoleculeNet全套 | AUROC, RMSE | MoleculeNet平均 AUROC **~0.88** | [RSC Digital Disc.](https://pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00348b) |

### 🔬 03 基因组学

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **ClinVar致病变异基准** | 2024 | 致病SNP vs常见SNP分类（零样本） | ClinVar+gnomAD | AUC | AlphaGenome **~0.78**；NT-v2 0.73 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **QTL预测基准** | 2024 | 因果QTL变异效应预测 | GTEx等QTL数据集 | AUC | AlphaGenome sQTL **0.80**；ipaQTL **0.86** | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65823-8) |
| **DNA基础模型5模型横评** | 2024 | 序列分类/表达/变异/TAD识别 | 多基因组任务 | AUC, Spearman ρ | NT-v2表观 **~0.89**；Caduceus-Ph表达 **~0.62** | [bioRxiv 2024.08.16](https://www.biorxiv.org/content/10.1101/2024.08.16.608288v2) |
| **AlphaGenome 26-benchmark suite** | 2025 | 26任务变异效应综合评测 | 多数据库整合 | AUC, Spearman ρ | 剪接 **~0.91**；基因表达 **~0.68** | [PMC12851941](https://pmc.ncbi.nlm.nih.gov/articles/PMC12851941/) |
| **Enformer基准** | 2021 | DNA序列→基因表达预测 | ENCODE/Roadmap表观基因组 | Pearson r | EPInformer **0.875–0.891**；Enformer ~0.85 | [Nat. Methods](https://www.nature.com/articles/s41592-021-01252-x) |
| **scRNA-seq扰动预测基准** | 2024 | 基因扰动后转录组变化预测 | Replogle/Norman Perturb-seq | Pearson r | ⚠️ PCA baseline **~0.35** > 所有FM（scGPT ~0.22） | [Nat. Methods 2025](https://www.nature.com/articles/s41592-025-02772-6) |
| **scGPT/Geneformer评测** | 2023 | 细胞注释/批次校正/表达重建 | 多scRNA-seq atlas | ARI, AUROC | Geneformer ARI 0.11；scGPT 0.18；均输给标准基线 ⚠️ | — |
| **Nucleotide Transformer (NT)基准** | 2024 | 18个基因组下游任务 | ENCODE, RefSeq | MCC, F1, AUC | NT-v2 剪接 MCC **~0.73**；染色质 AUC **~0.89** | [Nat. Methods](https://www.nature.com/articles/s41592-024-02523-z) |
| **SegmentNT** | 2024 | 单核苷酸分辨率14类基因组注释 | 人类参考基因组 | F1 | 剪接位点 **~0.92**；启动子 **~0.85**；lncRNA **~0.71** | [bioRxiv 2024.03.14](https://www.biorxiv.org/content/10.1101/2024.03.14.584712v3.full) |
| **调控变异因果预测** | 2024 | GWAS因果非编码调控变异预测 | ENCODE精细定位变体 | AUC | AlphaGenome **~0.83**；Enformer微调 ~0.79 | [PMC11844472](https://pmc.ncbi.nlm.nih.gov/articles/PMC11844472/) |
| **长程DNA预测基准套件** | 2025 | 多实验信号轨迹长程预测 | ENCODE公共资源 | Pearson r, R² | Borzoi **~0.79**（256kb）；Enformer ~0.75 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-65077-4) |
| **GFMBench-API** | 2026 | 基因组基础模型统一接口评测 | DNA/表观多种任务 | 多指标 | NT-v2/DNABERT-2综合最优 | [bioRxiv 2026.02.19](https://www.biorxiv.org/content/10.64898/2026.02.19.706811v1.full.pdf) |
| **DNA Long Bench / Genomics LRB** | 2025 | 长程DNA预测（最长1M bp上下文） | 多任务 | Pearson r, AUC | DNABERT-2 AUC **~0.85**；NT-v2 **~0.89** | [arXiv 2409.12641](https://arxiv.org/abs/2409.12641) |
| **scBench** | 2026 | AI智能体执行scRNA-seq完整分析工作流 | 394题；6测序平台；7类任务 | 准确率 | Claude Opus 4.6 **52.8%**；整体范围29–53% | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **scSuperAnnotator** | 2025 | 细胞类型注释方法大规模横评 | 多数据集平台 | 注释准确率, Jaccard | 监督方法 **~90%**；零样本迁移 ~75% | [NAR 2025](https://academic.oup.com/nar/article/54/1/gkaf1470/8415836) |
| **sc-HeurekaBench** | 2026 | 从论文半自动构建单细胞Agent评测 | 50 OEQ+50 MCQ；41 insights；13篇Nature/Cell | OEQ(1–5分)；MCQ准确率 | Biomni Agent OEQ **2.31/5**；MCQ **50%** | [arXiv 2601.01678](https://arxiv.org/abs/2601.01678) |
| **Biomni-Eval1** | 2025 | 罕见病诊断/GWAS因果基因/CRISPR靶点/基因检测 | 433题（多子任务） | 准确率 | Biomni Agent（Stanford）综合最优 | [HuggingFace](https://huggingface.co/datasets/biomni/Eval1) |
| **空间基因表达预测基准** | 2025 | H&E图像→空间基因表达预测，11方法比较 | 多组织切片 | Pearson r | 最优 **~0.45**；高变基因 ~0.60 | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-56618-y) |
| **HESCAPE** | 2025 | 视觉-基因组对齐，空间转录组跨模态检索 | 空间转录组+图像对 | R@1 | 最优 R@1 **~55%** | [preprint 2025](https://www.linkedin.com/pulse/hescape-benchmark-visiongenomics-alignment-spatial-rushin-gindra-rfrsf) |

### 🏥 04 临床医学

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MedQA (USMLE)** | 2021 | 执照医师考试风格MCQ | 12,723题（美版） | Accuracy | Med-Gemini **91.1%**；人类通过率 ~60% | [paperswithcode](https://paperswithcode.com/sota/question-answering-on-medqa-usmle) |
| **MedMCQA** | 2022 | 印度医学入学考试MCQ（4选项） | 194,000题 | Accuracy | GPT-4级 **~70–75%** | [arXiv 2203.14371](https://arxiv.org/abs/2203.14371) |
| **PubMedQA** | 2019 | 生物医学是/否/也许QA | 1,000专家标注题 | Accuracy | Yi-34B + OpenMedLM **77.3%** | [PMC10935498](https://pmc.ncbi.nlm.nih.gov/articles/PMC10935498/) |
| **BioASQ** | 2013– | 生物医学语义索引+多类型QA | 5,000+ QA对 | F1, MAP | 是非题 **>80%**；事实类 ~0.55–0.62 | [bioasq.org](https://bioasq.org/) |
| **MMLU 医学/生物子集** | 2021 | 医学遗传/解剖/临床知识MCQ | ~1,400题 | Accuracy | GPT-4.1 **~90%**；Claude 3 Opus 86.8% | [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) |
| **MedXpertQA** | 2025 | 专家级医学推理（文本+多模态） | 精心策划专家级题目 | Accuracy | 顶尖LLM **~45–52%**；人类专家 ~87% ⚠️ | [GitHub](https://github.com/TsinghuaC3I/MedXpertQA) |
| **n2c2 / i2b2** | 2006– | 临床去标识化/NER/关系抽取（年度轨道） | 去标识MIMIC记录 | F1 | 去标识化 **~99%**；临床NER ~90–93% | [n2c2](https://n2c2.dbmi.hms.harvard.edu/) |
| **MedAgentBench** | 2025 | LLM智能体虚拟EHR任务执行 | 300任务（10类）；100患者档案；FHIR | SR, Query SR, Action SR | Claude 3.5 Sonnet v2 **69.67%**；GPT-4o 64.00% | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| **MedArena** | 2025 | 临床医生偏好评估（80+亚专科） | 1,200+偏好；300+临床医生 | Elo / 偏好率 | Gemini 2.0 Flash Thinking **#1** | [Stanford HAI](https://hai.stanford.edu/news/medarena-comparing-llms-for-medicine-in-the-wild) |
| **MedS-Bench** | 2024 | 11类高级临床任务，122种任务类型 | 500万条指令（58语料库） | 多指标 | GPT-4综合最优；平均 **~68%** | [npj Digital Medicine](https://www.nature.com/articles/s41746-024-01390-4) |
| **CSEDB** | 2025 | 临床安全+效能（30指标，26科室） | 2,069道开放QA | 综合分 | 平均 **57.2%**；高风险场景 -13.3% | [npj Digital Medicine](https://www.nature.com/articles/s41746-025-02277-8) |
| **DRAGON** | 2025 | 临床NLP自动化标注pipeline评测 | 多种临床NLP任务 | F1 | 最优pipeline **~85%**（文档分类） | [npj Digital Medicine](https://www.nature.com/articles/s41746-025-01626-x) |
| **GLiNER-biomed** | 2025 | 开放域生物医学NER（零样本） | BC5CDR/NCBI Disease等标准集 | F1 | 零样本 **~85%**；可泛化新实体 | [arXiv 2504.00676](https://arxiv.org/html/2504.00676v1) |
| **CL4Health CT-DEB'26** | 2026 | 临床试验剂量错误检测 | 临床试验文档 | Precision, F1 | 竞赛进行中 | [bionlp.nlm.nih.gov](https://bionlp.nlm.nih.gov/cl4health2026/) |
| **LLM医疗文本信息抽取基准** | 2026 | LLM信息抽取工具在医疗文本上的对比 | 多种医疗文本格式 | F1, ROUGE | GPT-4 **~82%**；传统NER微调 ~88% | [medRxiv 2026](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full-text) |
| **MAX-EVAL-11** | 2025 | ICD-11临床编码 | 含ICD-11标签的临床记录 | 加权分 | Claude 4 Sonnet **43.3%** | [medRxiv](https://www.medrxiv.org/content/10.1101/2025.10.30.25339130v1.full.pdf) |
| **MedBench v4（中文）** | 2024 | 中文医学MCQ+开放题+Agent任务 | 700,000+任务（500+机构） | Accuracy | 最优中文医学模型 **~75%** | [arXiv 2511.14439](https://arxiv.org/abs/2511.14439) |
| **MedHELM** | 2024– | 多维度临床综合评测 | 多临床场景 | 综合分 | GPT-4o/Claude-3.5-Sonnet领先 | [HELM Medical](https://crfm.stanford.edu/helm/medical/latest/) |
| **HealthBench** | 2025 | 真实临床对话5维度评测 | 5,000+医患对话 | 综合分(0–100) | GPT-4o **~72**；Claude-3.5 ~70 | [OpenAI](https://openai.com/index/healthbench/) |
| **Open Medical-LLM Leaderboard** | 2023– | 6项医学数据集综合评测排行榜 | 多数据集合并 | Accuracy | 榜首平均 **~80%** | [HuggingFace](https://huggingface.co/blog/leaderboard-medicalllm) |

### 🖼️ 05 多模态

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **PathMMU** | 2024 | 病理VQA+推理 | 33,428 QA对；24,067图像 | Accuracy | 专科病理VLM **~68%**；人类 ~90% ⚠️ | [arXiv 2401.16355](https://arxiv.org/abs/2401.16355) |
| **OmniMedVQA** | 2024 | 12模态医学VQA（MRI/CT/X光/病理等） | 118,010图像 | Accuracy | 专科多模态模型 **~79%** | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Hu_OmniMedVQA_A_New_Large-Scale_Comprehensive_Evaluation_Benchmark_for_Medical_LVLM_CVPR_2024_paper.pdf) |
| **MIMIC-CXR VQA / EHRXQA** | 2023 | 胸片+EHR多模态QA | 377,391图像-问题-答案三元组 | Accuracy | 多模态融合 **~80%** | [arXiv 2310.18652](https://arxiv.org/pdf/2310.18652) |
| **GEMeX** | 2025 | 可定位、可解释的胸片VQA | 大规模CXR数据集 | Accuracy, IoU | Accuracy **~72%**；定位 IoU **~0.45** | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_GEMeX_A_Large-Scale_Groundable_and_Explainable_Medical_VQA_Benchmark_for_ICCV_2025_paper.pdf) |
| **15M生物医学图像-文本基础模型** | 2024 | 跨模态检索+零样本分类 | 1,500万图像-文本对 | Accuracy, R@1 | 零样本 **~78%**；检索 R@1 **~65%** | [ResearchGate](https://www.researchgate.net/publication/387269158_A_Multimodal_Biomedical_Foundation_Model_Trained_from_Fifteen_Million_Image-Text_Pairs) |
| **MULAN** | 2025 | 蛋白序列+结构多模态评测 | 蛋白序列+结构数据集 | AUC, TM-score | 联合模态 AUC **~0.91**；优于纯序列 ~3–5% | [Bioinformatics Advances](https://academic.oup.com/bioinformaticsadvances/article/5/1/vbaf117/8139638) |
| **MedGemma 1.5** | 2025 | 医学图像多任务（诊断/定位/生成） | Google内部标准化基准 | 分类准确率, AUC | 胸片分类 AUC **~0.94** | [Google Research Blog](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/) |

### 📝 06 生物医学NLP

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **BC5CDR** | 2015 | 化学品+疾病NER | 1,500篇PubMed | F1 | PubMedBERT **~90%**；GPT-4零样本 ~75–80% | [PMC4983247](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4983247/) |
| **NCBI Disease** | 2014 | 疾病实体NER | 793篇PubMed摘要 | F1 | BERT微调 **~90%** | [PubMed 24393765](https://pubmed.ncbi.nlm.nih.gov/24393765/) |
| **BC2GM** | 2004 | 基因/蛋白质NER | 20,000句子 | F1 | BioNER BERT **~84–88%** | [BigBIO NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **JNLPBA** | 2004 | DNA/RNA/蛋白/细胞NER（5类） | 22,000句子 | F1 | 微调模型 **~78–82%** | [BigBIO NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **BioRED** | 2022 | 多实体文档级NER | 600篇PubMed摘要 | F1 | 文档级 **~72%** | [Briefings Bioinformatics](https://academic.oup.com/bib/article/23/5/bbac282/6645993) |
| **ChemProt** | 2017 | 化学-蛋白质关系抽取 | 2,432篇PubMed摘要 | F1（宏平均） | PubMedBERT **~82%** | [BLURB](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **DDI** | 2013 | 药物-药物互作关系抽取 | 1,025篇文档 | F1 | 微调模型 **~80–85%** | [BLURB](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **GAD** | 2016 | 基因-疾病关联关系抽取 | 5,330句子 | F1 | BERT微调 **~87%** | [BLURB](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **BLUE** | 2019 | 生物医学NLP基础评测（BLURB前身） | 5个数据集 | F1, Accuracy | BlueBERT综合分 **~84**（已被BLURB取代） | [arXiv 1906.05474](https://arxiv.org/abs/1906.05474) |
| **BLURB** | 2020 | NER/RE/相似度/分类/QA综合套件 | 13数据集×7任务 | BLURB综合分 | PubMedBERT **82.91**；GPT-4零样本仍低 | [medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **BIOSSES** | 2017 | 生物医学句子语义相似度 | 100对句子 | Pearson r | BioALBERT **~0.90** | [BLURB](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **MedNLI** | 2018 | 临床自然语言推理（蕴含/中立/矛盾） | MIMIC-III临床记录 | Accuracy | ClinicalBERT **~82%** | [arXiv 1808.06752](https://arxiv.org/abs/1808.06752) |
| **HoC（Hallmarks of Cancer）** | 2016 | 癌症标志文档分类（10类） | PubMed摘要 | Micro-F1 | BioBERT/PubMedBERT **~70%** | [BLURB](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **LitCovid** | 2020 | COVID-19文献主题分类（7类） | PubMed COVID文献 | F1 | 微调BERT **~90%** | [PubMed 33040153](https://pubmed.ncbi.nlm.nih.gov/33040153/) |
| **BigBIO** | 2022 | 统一生物医学NLP访问框架 | 100+数据集；12任务；76个NER集 | 任务特定 | 数据框架；各子任务SOTA见对应数据集 | [NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **BioNLP Benchmark Suite** | 2025 | 12基准×6个BioNLP应用综合评测 | 12数据集 | 多指标 | 微调NER/RE **~88%**；LLM开放QA **~77%** | [Nat. Commun.](https://www.nature.com/articles/s41467-025-56989-2) |
| **Bioinfo-Bench** | 2023 | 生物信息学QA（多选+开放题） | 200道题 | Accuracy | GPT-4 **>80%**（多选）；ChatGPT ~60% | [arXiv 2310.00299](https://arxiv.org/abs/2310.00299) |
| **BioCoder** | 2023 | 生物信息学编程（序列分析/比对/注释） | 1,000+编程题 | Pass@1, Pass@10 | GPT-4 Pass@1 **~42%** | [arXiv 2308.16458](https://arxiv.org/abs/2308.16458) |
| **BioinformaticsBench** | 2024 | 9个生物信息学子领域推理 | 多子领域 | Accuracy | GPT-4 **~68%** | — |
| **Eubiota** | 2026 | 微生物组专项推理（药物/机制/蛋白/基因） | ~100题/类（6类）；MDIPID数据库 | Accuracy | Eubiota系统 **87.7%**；超GPT-5.1约10.4% | [bioRxiv 2026.02.27](https://www.biorxiv.org/content/10.64898/2026.02.27.708412v1) |
| **BioProBench** | 2025 | 生物实验protocol理解（PQA/ORD/ERR/GEN/REA） | 556,171题；26,933个协议；16子领域 | Accuracy, F1, BLEU | PQA: Gemini-2.5-pro **70.27%**；ERR: DeepSeek-R1 F1 **64.03%** | [arXiv 2505.07889](https://arxiv.org/abs/2505.07889) |

### 🤖 07 智能体 & 跨领域综合

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **临床LLM智能体评测** | 2026 | 临床Agent多轮对话+决策支持 | 多轮临床场景 | 成功率，专家评分，安全性 | 暂无公开分数 | [Nat. Digital Medicine](https://www.nature.com/articles/s41746-026-02443-6) |
| **BioAgent Bench** | 2025 | 生物信息学Agent+生物安全风险评估 | 多Agent任务+风险任务 | 能力分，安全通过率 | 含生物安全维度的罕见评测 | [EmergentMind](https://www.emergentmind.com/topics/bioagent-bench) |
| **BixBench** | 2025 | 真实生信分析多步骤计算推理 | ~205题（60个Jupyter capsule） | LLM自动评分，MCQ准确率 | 开放题：Claude 3.5 Sonnet **17%** > GPT-4o 9%；MCQ低于随机 ⚠️ | [arXiv 2503.00096](https://arxiv.org/abs/2503.00096) |
| **SciAgentGYM** | 2026 | 多步骤科学工具调用（物理/化学/材料/生命科学） | 259任务；1,780种工具 | 任务成功率 SR | GPT-5 **41.3%**；Grok-4-1 40.3%；生命科学平均 20.2% | [arXiv 2602.12984](https://arxiv.org/abs/2602.12984) |
| **LAB-Bench** | 2024 | 实验室生物学研究基础能力（LitQA2/DbQA/SeqQA/ProtocolQA/CloningScenarios） | 2,457题（8类30子任务）；FutureHouse | Precision / Coverage | Claude 3.5 Sonnet最优；人类 ~69% > 模型 ~40–50% | [arXiv 2407.10362](https://arxiv.org/abs/2407.10362) |
| **FrontierScience** | 2025 | PhD级跨学科推理（Olympiad+Research轨） | 700+题；42奥赛金牌+45博士出题 | Olympiad准确率，Research部分分 | GPT-5.2: Olympiad **77%** / Research **25%** | [OpenAI](https://openai.com/index/frontierscience/) |
| **BABE** | 2026 | 基于论文的生物实验推理（Q1→Q2→Q3三元组） | 12生物子领域三元组 | 平均分(0–100)，Convergence Score | GPT-5.1-high **52.31** | [arXiv 2602.05857](https://arxiv.org/html/2602.05857v1) |
| **ATLAS** | 2025 | 博士级跨学科开放式推理（7大学科） | ~800题；25+机构博士出题；4阶段质控 | 平均准确率，mG-Pass@k | GPT-5-High **42.9%**；大多数模型 <35% | [arXiv 2511.14366](https://arxiv.org/html/2511.14366v2) |
| **GPQA** | 2023 | 研究生级跨学科Google-Proof QA（生物/化学/物理） | Extended 546题；Diamond 198题 | 4选1准确率 | o3 Diamond **87.7%**；人类专家 ~65% | [arXiv 2311.12022](https://arxiv.org/abs/2311.12022) |
| **LLM Benchmarks in Life Sciences（综述）** | 2026 | 生命科学AI benchmark系统梳理综述 | — | — | 索引文章，非评测 | [IntuitionLabs](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |
| **BEACON** | 2026 | 统一生物/药物发现AI benchmarking（计划中） | — | — | 社区平台建设中 | [BioPharma Trend](https://www.biopharmatrend.com/news/beacon-launches-to-unite-ai-benchmarking-across-biology-and-drug-discovery-1507/) |

## 核心发现（定位新 Benchmark 的关键依据）

1. **结构化任务上，微调 >> 零样本**：NER/RE/DTI/蛋白质适应性预测中，专门微调的小模型持续优于 GPT-4 零样本。
2. **scRNA 扰动预测：所有基础模型都输给 PCA baseline**（Nature Methods 2025 重磅结论）。
3. **数据泄露是系统性问题**：PPI、DTI benchmark 普遍存在随机切分导致的性能虚高。
4. **临床 benchmark 正从选择题转向真实任务**：MedAgentBench、MedArena 测的是 EHR 操作而非知识记忆。
5. **分子生物学没有统一跨领域排行榜**：ProteinGym/CASP/TDC 各管一段，无整合视角。
6. **当前 benchmark 极少涵盖序列标记（`<mol>`, `<protein>`, `<rna>`）的理解与生成**。
