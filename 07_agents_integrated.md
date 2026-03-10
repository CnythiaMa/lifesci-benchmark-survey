# 智能体（Agents）与综合跨领域 Benchmarks

> 2025–2026年新兴类目，测试LLM/AI是否能完成真实生命科学"工作流任务"，而非单纯选择题。

## 1. 生命科学 AI 智能体 Benchmarks

| Benchmark | 年份 | 任务类型 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **scBench** | 2026 | AI agents在单细胞RNA-seq分析工作流中的完整执行（聚类/注释/差异表达/伪时间） | 394个可验证问题；6种测序平台 | 任务成功率，步骤合理性 | 暂无公开排行榜分数 | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **MedAgentBench** | 2025 | LLM agents在虚拟EHR中执行真实任务（开医嘱/查实验室/更新记录） | 真实临床EHR任务集 | 任务完成率，临床准确性 | 暂无公开排行榜分数 | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| **临床LLM智能体评测** | 2026 | LLM-based agent系统在临床任务中的多轮对话、决策支持 | 多轮临床场景 | 任务成功率，专家评分，安全性 | 暂无公开排行榜分数 | [Nat. Digital Medicine 2026](https://www.nature.com/articles/s41746-026-02443-6) |
| **BioAgent Bench** | 2025 | AI agents在生物信息学中的能力与生物安全风险评估（序列分析/文献检索/实验设计） | 多种agent任务 + 风险相关任务 | 能力分，安全约束通过率 | 包含生物安全维度的罕见评测 | [EmergentMind](https://www.emergentmind.com/topics/bioagent-bench) |
| **LAB-Bench** | 2024 | 实验室生物学研究基础能力：文献检索（LitQA2）、数据库查询（DbQA）、序列操作（SeqQA）、实验方案（ProtocolQA）、分子克隆工作流（CloningScenarios） | 2,457题（8类30子任务）；FutureHouse | Precision / Coverage | Claude 3.5 Sonnet最优；整体人类 ~69% > 模型 ~40–50%（SeqQA）；翻译效率子任务模型 **88% > 人类75%** | [arXiv 2407.10362](https://arxiv.org/abs/2407.10362) |
| **BixBench** | 2025 | AI Agent在真实生信分析任务上的多步骤计算推理：探索生物数据集、执行Python/R/Bash分析流程、解读研究结论 | ~205题（60个真实Jupyter notebook capsule） | LLM自动评分（开放题）；准确率（MCQ） | GPT-4o / Claude 3.5 Sonnet均 **~17%**；MCQ与随机水平相当 ⚠️ | [arXiv 2503.00096](https://arxiv.org/abs/2503.00096) |
| **BioProBench** | 2025 | 生物实验Protocol理解与生成：方案问答（PQA）、步骤排序（ORD）、错误纠正（ERR）、Protocol生成（GEN）、链式推理（REA）；16个生物子领域 | 556,171题（26,933个人工协议） | PQA/ORD: Accuracy；ERR: F1；GEN: BLEU/Step Recall | PQA: Gemini-2.5-pro **70.27%**（ProAgent 85%）；ERR: DeepSeek-R1 F1 **64.03%**；GEN: BLEU<11%，所有基础模型 | [arXiv 2505.07889](https://arxiv.org/abs/2505.07889) |
| **SciAgentGYM** | 2026 | LLM Agent多步骤科学工具调用：物理/化学/材料/生命科学4域，按步骤数分L1(≤3)/L2(4–7)/L3(≥8)三级难度 | 259任务/1,134子问题；1,780种领域专属工具 | 任务成功率（%） | GPT-5: **41.3%**（L1:60.6%, L3:30.9%）；Claude-Sonnet-4: 35.9% | [arXiv 2602.12984](https://arxiv.org/abs/2602.12984) |

---

## 2. 综合跨领域 Benchmark 套件

| Benchmark | 年份 | 覆盖范围 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **FrontierScience** | 2025 | 跨物理/化学/生物三科的PhD级科学推理；Olympiad轨（奥赛式短答）+ Research轨（真实科研子问题）；生物学含分子生物/生化/遗传推导 | 700+题（gold set 160题）；42名国际奥赛金牌 + 45名博士科学家出题 | 逐步打分（GPT-4o评估）；Olympiad准确率；Research部分分 | GPT-5.2：Olympiad **77%** / Research **25%** | [OpenAI FrontierScience](https://openai.com/index/frontierscience/) |
| **BABE**（Biology Arena BEnchmark） | 2026 | 基于同行评审论文的生物实验推理；12个生物子领域；Q1→Q2→Q3三元组（强相关：顺序因果推理 ~45%；弱相关：并行检索 ~55%） | 问题三元组形式；覆盖12个生物子领域 | 平均分（0–100）；Convergence Score | GPT-5.1-high: **52.31**（强相关51.79，弱相关52.86）；人类专家基线远高于模型 | [arXiv 2602.05857](https://arxiv.org/html/2602.05857v1) |
| **ATLAS** | 2025 | 跨数学/物理/化学/生物/CS/地球/材料7大学科的博士级开放式推理；问题类型：计算推导71%/判断12%/解释10%/综合6% | ~800题（>50%含子问题）；25+机构博士专家出题；4阶段质控 | 平均准确率；mG-Pass@k（稳定性指标） | GPT-5-High: **42.9%**；大多数前沿模型 <35% | [arXiv 2511.14366](https://arxiv.org/html/2511.14366v2) |
| **GPQA**（Graduate-Level Google-Proof Q&A）<br>⚠️ *通用benchmark；本项目选取生命科学相关子集* | 2023 | **通用**跨生物/化学/物理三科的研究生级4选1选择题；设计原则：答案无法通过搜索引擎直接获取，须领域专家级深度推理；本项目选取范围：**生物全子集**（198题）+ **化学中生物化学/有机化学相关部分**，合计约占总量50% | GPQA Extended: **546题**（生物198/化学227/物理121）；GPQA Diamond（≥2位领域专家独立验证一致的最高质量子集）: **198题**；生命科学相关约 **~290题**（Extended）/ **~110题**（Diamond） | 4选1准确率（%） | o3: **87.7%**（Diamond）；Gemini 2.5 Pro: ~86%；人类领域专家: ~65%；GPT-4: ~39% ⚠️ 人类专家仍具显著优势，尚未饱和 | [arXiv 2311.12022](https://arxiv.org/abs/2311.12022) |
| **LLM Benchmarks in Life Sciences（综述）** | 2026 | 系统梳理：生物医学NLP（BioASQ/PubMedQA/MedMCQA）+药物设计（MoleculeNet/分子生成）+基因组与蛋白序列任务（DNA FM benchmarks/ProteinGym） | — | — | "目录索引"文章；帮助定位各子领域benchmark | [IntuitionLabs 2026](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |
| **BEACON**（计划中） | 2026 | 统一生物与药物发现领域AI benchmarking；多实验室共享实验设计的"真实实验驱动"benchmark；跨模态跨任务统一leaderboard | — | — | 社区think tank + 开放评估平台；具体数据集建设中 | [BioPharma Trend 2026](https://www.biopharmatrend.com/news/beacon-launches-to-unite-ai-benchmarking-across-biology-and-drug-discovery-1507/) |

---

## 3. 已有综合评测的组合方式

AI综述建议的"全栈 life science benchmark"结构（可作为新benchmark参考）：

```
蛋白结构与功能   → CASP + ProteinGym + CAFA + PPI benchmarks
小分子与药物     → MoleculeNet + 3D生成benchmark + DTI(Human/C.elegans)
基因组与调控     → DNA FM benchmark suite + 长程调控预测 + 变异效应26benchmark
单细胞与空间     → scBench + 单细胞注释benchmark + 空间表达预测benchmark
文本与LLM        → BioASQ + Biomedical-NLP-Benchmarks + DRAGON + CL4Health
多模态与智能体   → HESCAPE + MULAN + 多模态临床图像文本基准 + scBench agents
```

---

## 4. 当前空白

- **跨领域推理agent**：给定基因变异+相关文献，自动查阅数据库后生成诊断解释（无标准benchmark）
- **生物实验设计agent**：给定研究目标，规划实验步骤、试剂、分析方法（仅BioProBench初步探索）
- **药物发现完整流程agent**：从靶标到候选分子到ADMET预测的端到端工作流评测
- **中文生命科学agent任务**：目前所有agent benchmark均为英文
- **序列操作agent**：给定文本指令，正确操作 `<mol>/<protein>/<rna>` 序列标记（全空白）
