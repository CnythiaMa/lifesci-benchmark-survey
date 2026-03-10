# 智能体（Agents）与综合跨领域 Benchmarks

> 2025–2026年新兴类目，测试LLM/AI是否能完成真实生命科学"工作流任务"，而非单纯选择题。

## 1. 生命科学 AI 智能体 Benchmarks

| Benchmark | 年份 | 任务类型 | 规模 | 指标 | 特点 | 参考 |
|-----------|------|---------|------|------|------|------|
| **scBench** | 2026 | AI agents在单细胞RNA-seq分析工作流中的完整执行（聚类/注释/差异表达/伪时间） | 394个可验证问题；6种测序平台 | 任务成功率，步骤合理性 | 首个面向scRNA-seq完整分析流程的AI agent评测 | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **MedAgentBench** | 2025（NEJM AI） | LLM agents在虚拟EHR中执行真实任务（开医嘱/查实验室/更新记录） | 真实临床EHR任务集 | 任务完成率，临床准确性 | 首个测试LLM agents在EHR工作流中的benchmark（非MCQ） | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| **临床LLM智能体评测** | 2026 | LLM-based agent系统在临床任务中的多轮对话、决策支持 | 多轮临床场景 | 任务成功率，专家评分，安全性（错误决策比例） | Nature Digital Medicine 2026 | [Nat. Digital Medicine 2026](https://www.nature.com/articles/s41746-026-02443-6) |
| **BioAgent Bench** | 2025 | AI agents在生物信息学中的能力与生物安全风险评估（序列分析/文献检索/实验设计） | 多种agent任务 + 风险相关任务 | 能力分，安全约束通过率 | 包含生物安全维度的罕见评测框架 | [EmergentMind](https://www.emergentmind.com/topics/bioagent-bench) |

---

## 2. 综合跨领域 Benchmark 套件

| Benchmark | 年份 | 覆盖范围 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **FrontierScience** | 2025 | 跨物理/化学/生物三科的PhD级科学推理；Olympiad轨（奥赛式短答）+ Research轨（真实科研子问题）；生物学含分子生物/生化/遗传推导 | 700+题（gold set 160题）；42名国际奥赛金牌 + 45名博士科学家出题 | 逐步打分（GPT-4o评估）；Olympiad准确率；Research部分分 | GPT-5.2：Olympiad **77%** / Research **25%** | [OpenAI FrontierScience](https://openai.com/index/frontierscience/) |
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
