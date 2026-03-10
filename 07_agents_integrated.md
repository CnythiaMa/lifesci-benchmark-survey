# 智能体（Agents）与综合跨领域 Benchmarks

> 2025–2026年新兴类目，测试LLM/AI是否能完成真实生命科学"工作流任务"，而非单纯选择题。

## 1. 生命科学 AI 智能体 Benchmarks

| Benchmark | 年份 | 任务类型 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **scBench** | 2026 | AI agents在单细胞RNA-seq分析工作流中的完整执行（标准化/QC/聚类/细胞注释/差异表达）；平台差异影响与模型差异相当（最大40+百分点差距） | 394个可验证问题；6种测序平台；7类任务 | 准确率（各任务确定性评分） | Claude Opus 4.6 **52.8%** > Claude Opus 4.5 49.9% > GPT-5.2 45.2% > Claude Sonnet 4.5 44.2%；整体范围 29–53%；Normalization最易（最高83.8%），差异表达最难（最高41.4%） | [arXiv 2602.09063](https://arxiv.org/html/2602.09063v1) |
| **MedAgentBench** | 2025 | LLM agents在虚拟EHR中执行真实任务（开医嘱/查实验室/更新记录）；Query（信息检索）+ Action（操作执行）双轨评测 | 300个临床任务（10类）；100名患者档案；700,000+数据元素；FHIR标准兼容 | 总体成功率 SR；Query SR；Action SR | Claude 3.5 Sonnet v2 **69.67%**（Query 85.33% / Action 54.00%）；GPT-4o 64.00%；DeepSeek-V3 62.67%；Gemini-1.5 Pro 62.00%；Hard任务所有模型均<25% | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) · [arXiv 2501.14654](https://arxiv.org/abs/2501.14654) |
| **临床LLM智能体评测** | 2026 | LLM-based agent系统在临床任务中的多轮对话、决策支持 | 多轮临床场景 | 任务成功率，专家评分，安全性 | 暂无公开排行榜分数 | [Nat. Digital Medicine 2026](https://www.nature.com/articles/s41746-026-02443-6) |
| **BioAgent Bench** | 2025 | AI agents在生物信息学中的能力与生物安全风险评估（序列分析/文献检索/实验设计） | 多种agent任务 + 风险相关任务 | 能力分，安全约束通过率 | 包含生物安全维度的罕见评测 | [EmergentMind](https://www.emergentmind.com/topics/bioagent-bench) |
| **BixBench** | 2025 | AI Agent在真实生信分析任务上的多步骤计算推理：探索生物数据集、执行Python/R/Bash分析流程、解读研究结论 | ~205题（60个真实Jupyter notebook capsule） | LLM自动评分（开放题）；准确率（MCQ） | 开放题：Claude 3.5 Sonnet **17%** > GPT-4o 9%；MCQ（含拒答选项）：低于随机水平 ⚠️ | [arXiv 2503.00096](https://arxiv.org/abs/2503.00096) |
| **SciAgentGYM** | 2026 | LLM Agent多步骤科学工具调用：物理/化学/材料/生命科学4域，按步骤数分L1(≤3)/L2(4–7)/L3(≥8)三级难度；生命科学工具依赖性最强 | 259任务/1,134子问题；1,780种领域专属工具 | 任务成功率（%）；有/无工具对比 | GPT-5 **41.3%** > Grok-4-1 40.3% > Claude-Sonnet-4 35.9%（均含工具）；L1:60.6% / L3:30.9%（GPT-5）；生命科学平均 20.2% | [arXiv 2602.12984](https://arxiv.org/abs/2602.12984) |

**任务类型**：多步工具调用 + 推理（自然语言任务描述 → 工具序列执行 → 结构化结论）。

```python
# ── 示例① scBench：AI Agent 执行 scRNA-seq 完整分析工作流 ────────────────
input_scbench = {
    "task":     "对 10X Chromium PBMC 数据完成标准分析工作流",
    "platform": "10X_Chromium",
    "steps":    ["质控过滤", "标准化", "高变基因选择", "降维聚类", "细胞类型注释", "差异表达"],
    "data":     "raw_counts_matrix.h5ad",   # AnnData 格式
}

output_scbench = {
    "step_results": [
        {"step": "QC",             "code": "sc.pp.filter_cells(adata, min_genes=200)...",
                                   "correct": True},
        {"step": "normalization",  "code": "sc.pp.normalize_total(adata, target_sum=1e4)...",
                                   "correct": True},
        {"step": "clustering",     "code": "sc.tl.leiden(adata, resolution=0.8)...",
                                   "correct": True},
        {"step": "annotation",     "code": "# 基于marker基因注释",
                                   "correct": False,  "error": "将 NK 细胞误标为 CD8+ T"},
        {"step": "DEG",            "code": "sc.tl.rank_genes_groups(adata, 'leiden')...",
                                   "correct": True},
    ],
    "overall_accuracy": 0.528,   # Claude Opus 4.6 SOTA
    # ⚠️ 平台差异影响巨大：同一模型在不同测序平台上最大差距 >40 百分点
}

# ── 示例② MedAgentBench：LLM Agent 在虚拟 EHR 中执行临床任务 ─────────────
input_medagent = {
    "task":      "为患者 P-0042 开具华法林 5mg 口服 每日一次",
    "task_type": "Action",        # Action（操作执行）vs Query（信息检索）
    "ehr_system": "FHIR-compatible virtual EHR",
    "patient_id": "P-0042",
}

output_medagent = {
    "agent_actions": [
        {"action": "GET",  "endpoint": "/Patient/P-0042",
         "result": "患者基本信息：65岁男性，房颤病史"},
        {"action": "GET",  "endpoint": "/MedicationRequest?patient=P-0042",
         "result": "当前用药列表（检查冲突）"},
        {"action": "POST", "endpoint": "/MedicationRequest",
         "body": {"medication": "warfarin 5mg", "dosage": "PO QD", "patient": "P-0042"},
         "result": "医嘱创建成功"},
    ],
    "task_success": True,
    # Query 任务（信息检索）成功率远高于 Action 任务（操作执行）
    # Claude 3.5 Sonnet v2: Query 85.33% vs Action 54.00%
    # Hard 任务所有模型均 <25%
}

# ── 示例③ SciAgentGYM：多步骤科学工具调用（生命科学域） ───────────────────
input_sciagent = {
    "task":       "使用 Biopython 获取人类 TP53 蛋白序列，用 BLAST 搜索同源序列，统计保守残基比例",
    "domain":     "life_science",
    "difficulty": "L2",           # L1(≤3步) / L2(4–7步) / L3(≥8步)
    "available_tools": ["Biopython.Entrez", "BLAST_API", "pandas", "matplotlib"],
}

output_sciagent = {
    "tool_calls": [
        {"step": 1, "tool": "Biopython.Entrez.efetch",
         "params": {"db": "protein", "id": "NP_000537.3", "rettype": "fasta"},
         "result": "TP53 蛋白序列 393 aa"},
        {"step": 2, "tool": "BLAST_API.blastp",
         "params": {"query": "NP_000537.3", "database": "swissprot", "evalue": 1e-50},
         "result": "87 条同源序列"},
        {"step": 3, "tool": "BLAST_API.parse_alignment",
         "params": {"alignments": "..."},
         "result": "多序列比对矩阵 (87 × 393)"},
        {"step": 4, "tool": "pandas.DataFrame.apply",
         "params": {"func": "计算每列保守度"},
         "result": "保守残基（>90%一致）：218/393 = 55.5%"},
    ],
    "final_answer": "TP53 在哺乳动物中有 55.5% 的高保守残基，集中于 DNA 结合域（残基 102–292）",
    "task_success": True,
    # 生命科学域是最难领域：平均成功率仅 20.2%（全域 GPT-5 SOTA 41.3%）
}
```

---

## 2. 综合跨领域 Benchmark

| Benchmark | 年份 | 覆盖范围 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **LAB-Bench** | 2024 | 实验室生物学研究基础能力：文献检索（LitQA2）、数据库查询（DbQA）、序列操作（SeqQA）、实验方案（ProtocolQA）、分子克隆工作流（CloningScenarios） | 2,457题（8类30子任务）；FutureHouse | Precision / Coverage | Claude 3.5 Sonnet最优；整体人类 ~69% > 模型 ~40–50%（SeqQA）；翻译效率子任务模型 **88% > 人类75%** | [arXiv 2407.10362](https://arxiv.org/abs/2407.10362) |
| **FrontierScience** | 2025 | 跨物理/化学/生物三科的PhD级科学推理；Olympiad轨（奥赛式短答）+ Research轨（真实科研子问题）；生物学含分子生物/生化/遗传推导 | 700+题（gold set 160题）；42名国际奥赛金牌 + 45名博士科学家出题 | 逐步打分（GPT-4o评估）；Olympiad准确率；Research部分分 | GPT-5.2：Olympiad **77%** / Research **25%** | [OpenAI FrontierScience](https://openai.com/index/frontierscience/) |
| **BABE**（Biology Arena BEnchmark） | 2026 | 基于同行评审论文的生物实验推理；12个生物子领域；Q1→Q2→Q3三元组（强相关：顺序因果推理 ~45%；弱相关：并行检索 ~55%） | 问题三元组形式；覆盖12个生物子领域 | 平均分（0–100）；Convergence Score | GPT-5.1-high: **52.31**（强相关51.79，弱相关52.86）；人类专家基线远高于模型 | [arXiv 2602.05857](https://arxiv.org/html/2602.05857v1) |
| **ATLAS** | 2025 | 跨数学/物理/化学/生物/CS/地球/材料7大学科的博士级开放式推理；问题类型：计算推导71%/判断12%/解释10%/综合6% | ~800题（>50%含子问题）；25+机构博士专家出题；4阶段质控 | 平均准确率；mG-Pass@k（稳定性指标） | GPT-5-High: **42.9%**；大多数前沿模型 <35% | [arXiv 2511.14366](https://arxiv.org/html/2511.14366v2) |
| **GPQA**（Graduate-Level Google-Proof Q&A）<br>⚠️ *通用benchmark；本项目选取生命科学相关子集* | 2023 | **通用**跨生物/化学/物理三科的研究生级4选1选择题；设计原则：答案无法通过搜索引擎直接获取，须领域专家级深度推理；本项目选取范围：**生物全子集**（198题）+ **化学中生物化学/有机化学相关部分**，合计约占总量50% | GPQA Extended: **546题**（生物198/化学227/物理121）；GPQA Diamond（≥2位领域专家独立验证一致的最高质量子集）: **198题**；生命科学相关约 **~290题**（Extended）/ **~110题**（Diamond） | 4选1准确率（%） | o3: **87.7%**（Diamond）；Gemini 2.5 Pro: ~86%；人类领域专家: ~65%；GPT-4: ~39% ⚠️ 人类专家仍具显著优势，尚未饱和 | [arXiv 2311.12022](https://arxiv.org/abs/2311.12022) |
| **LLM Benchmarks in Life Sciences（综述）** | 2026 | 系统梳理：生物医学NLP（BioASQ/PubMedQA/MedMCQA）+药物设计（MoleculeNet/分子生成）+基因组与蛋白序列任务（DNA FM benchmarks/ProteinGym） | — | — | "目录索引"文章；帮助定位各子领域benchmark | [IntuitionLabs 2026](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview) |
| **BEACON**（计划中） | 2026 | 统一生物与药物发现领域AI benchmarking；多实验室共享实验设计的"真实实验驱动"benchmark；跨模态跨任务统一leaderboard | — | — | 社区think tank + 开放评估平台；具体数据集建设中 | [BioPharma Trend 2026](https://www.biopharmatrend.com/news/beacon-launches-to-unite-ai-benchmarking-across-biology-and-drug-discovery-1507/) |

**任务类型**：开放式科学推理（研究问题 → 多步分析推导 → 数值/文字答案）。

```python
# ── LAB-Bench 文献检索子任务（LitQA2）─────────────────────────────────
input_litqa2 = {
    "task":          "查找 BRCA1 c.5266dupC 变异的致病性证据，给出 ACMG 分级建议。",
    "allowed_tools": ["PubMed_search", "ClinVar_lookup", "OMIM_query"],
}

output_litqa2 = {
    "tool_calls": [
        {
            "tool":   "ClinVar_lookup",
            "query":  "BRCA1 c.5266dupC",
            "result": "Pathogenic (5★); 342 submissions",
        },
        {
            "tool":   "PubMed_search",
            "query":  "BRCA1 5266dupC breast cancer",
            "result": "23 papers; Ashkenazi Jewish founder mutation",
        },
        {
            "tool":   "OMIM_query",
            "query":  "BRCA1 113705",
            "result": "Hereditary breast and ovarian cancer syndrome",
        },
    ],
    "conclusion":   "该变异为已知致病截短突变（PVS1 + PS1），ACMG 分级：致病性（Pathogenic）。",
    "task_success":  True,
    # 评测
    "LAB_Bench_human_accuracy": 0.69,   # 人类研究员
    "LAB_Bench_model_accuracy": 0.45,   # Claude 3.5 Sonnet 最优
}

# ── GPQA Diamond 生物子集（研究生级 4选1）──────────────────────────────
input_gpqa = {
    "question": ("CRISPR-Cas9 导入 TP53 R248W 热点突变后，该 GOF 突变蛋白在无血清培养中"
                 "最可能通过何种机制促进肿瘤细胞存活？"),
    "options": {
        "A": "抑制 BAX 转录激活下游凋亡",
        "B": "激活 MYC 靶基因，绕过生长因子依赖",
        "C": "与 p63/p73 竞争 DNA 结合，阻断其促凋亡功能",
        "D": "激活 MDM2 E3 连接酶降解野生型 p53",
    },
}
output_gpqa = {
    "answer":     "C",
    "reasoning":  "R248W 通过显性负效应与 p63/p73 竞争结合，是经典 GOF 机制之一...",
    "confidence":  0.78,
    # 评测（GPQA Diamond 整体）
    "model_accuracy":  0.877,   # o3 SOTA
    "human_expert":    0.650,   # 领域专家
}

# ── FrontierScience Research 轨（真实科研子问题）──────────────────────
input_frontier = {
    "paper_context": "2024 Nature 文章研究 CAR-T 细胞耗竭机制...",
    "sub_question":  "图 3B 中，TOX 敲除后 CAR-T 细胞持久性提升的分子机制是什么？",
}
output_frontier = {
    "answer":     ("TOX 是 T 细胞耗竭核心转录因子，其敲除解除了 NR4A/BATF 介导的耗竭程序，"
                   "恢复效应相关基因表达..."),
    "step_score":  2.1,   # /5（GPT-5.2 Research 轨道 SOTA）
}
```

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
