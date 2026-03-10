# 临床医学 Benchmarks

## 1. 医学问答（Medical QA）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MedQA (USMLE)** | 2021 | 美国执照医师考试风格MCQ（4选项） | 12,723题（美版）；多语言版本 | Accuracy | Med-Gemini: **91.1%**；GPT-4o: ~90%；人类通过率 ~60% | [paperswithcode](https://paperswithcode.com/sota/question-answering-on-medqa-usmle) |
| **MedMCQA** | 2022 | 印度医学入学考试（AIIMS/NEET-PG），4选项 | 194,000题 | Accuracy | GPT-4级模型 ~70–75%；专门微调更高 | [arXiv 2203.14371](https://arxiv.org/abs/2203.14371) |
| **PubMedQA** | 2019 | 生物医学是/否/也许QA（PubMed摘要） | 1,000专家标注；61.2K未标注 | Accuracy | ~79%；Yi-34B + OpenMedLM: **77.3%** | [PMC10935498](https://pmc.ncbi.nlm.nih.gov/articles/PMC10935498/) |
| **BioASQ**（第13届，持续） | 2013–2025 | 生物医学语义索引+QA（是非/事实/列表/摘要） | 5,000+ QA对（PubMed来源） | MAP, MRR, F1 | 2025：83支队伍，1,000+提交；新增MultiClinSum, GutBrainIE任务 | [bioasq.org](https://bioasq.org/) |
| **MMLU 医学/生物子集** | 2021 | 医学遗传学/解剖学/临床知识/学院医学/专业医学 | ~1,400题（医学子集） | Accuracy | GPT-4.1: **~90%**；GPT-4o: 88.7%；Claude 3 Opus: 86.8%；人类专家 ~90% | [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) |
| **MedXpertQA** | 2025（ICML） | 专家级医学推理；文本+多模态子集 | 精心策划的专家级；多样图像 | Accuracy | 目前同类中最难；顶尖模型距人类专家仍有差距 | [GitHub TsinghuaC3I](https://github.com/TsinghuaC3I/MedXpertQA) |

**趋势**：通用LLM在USMLE级MCQ已接近/超过人类通过率，但专家级推理题（MedXpertQA）仍有明显差距。

---

## 2. 临床NLP / EHR

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **n2c2 / i2b2 Shared Tasks** | 2006–持续 | 去识别化/NER/关系抽取/时序/共指/临床编码（年度轨道） | 每任务数百条去标识MIMIC/Partners记录 | F1, Precision, Recall | 最新2022：进展记录评估计划推理；BERT微调模型主导 | [n2c2.dbmi.hms.harvard.edu](https://n2c2.dbmi.hms.harvard.edu/) |
| **MedAgentBench** | 2025（NEJM AI） | LLM智能体在虚拟EHR中执行任务（开医嘱/查实验室/更新记录） | 真实临床EHR任务 | 任务完成率, Accuracy | 首个测试LLM智能体在EHR工作流中的基准（非MCQ） | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| **MedArena** | 2025 | 临床医生偏好评估11个LLM，80+亚专科 | 1,200+临床医生偏好（300+临床医生） | Elo / 偏好率 | Gemini 2.0 Flash Thinking #1；GPT-4o #2 | [Stanford HAI](https://hai.stanford.edu/news/medarena-comparing-llms-for-medicine-in-the-wild) |
| **MedS-Bench** | 2024–2025 | 11类高级临床任务，122种任务类型 | 500万条指令（58个医学语料库） | 多指标 | GPT-4/Claude-3.5/MEDITRON评测；专科模型在复杂任务上更强 | [npj Digital Medicine 2025](https://www.nature.com/articles/s41746-024-01390-4) |
| **CSEDB** | 2025 | 临床安全+效能（30指标，26个科室） | 2,069道开放式QA | 综合分 | 平均57.2%；高风险场景下降13.3%；专科LLM > 通用LLM | [npj Digital Medicine 2025](https://www.nature.com/articles/s41746-025-02277-8) |
| **Open Medical-LLM Leaderboard** | 2023–持续（HuggingFace） | MedQA/MedMCQA/PubMedQA/MMLU医学等综合分 | 多数据集合并 | Accuracy | 持续更新；公开可访问 | [HuggingFace Blog](https://huggingface.co/blog/leaderboard-medicalllm) |

---

## 3. 疾病诊断 / ICD编码

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MAX-EVAL-11** | 2025 | ICD-11临床编码 | 含ICD-11标签的临床记录 | 加权分, 临床精确率 | Claude 4 Sonnet: **0.433**（43.3%精确率）；Gemini 2.5 Flash: 0.341 | [medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.10.30.25339130v1.full.pdf) |
| **MedBench v4**（中文） | 2024–2025 | 24个主科+91个副科；MCQ+开放题+智能体任务 | 700,000+专家策划任务（500+机构） | Accuracy, 专家评级 | 云端动态评测防刷榜；防快捷学习 | [arXiv 2511.14439](https://arxiv.org/abs/2511.14439) |

## 4. 整体医学LLM评估框架

| Benchmark | 年份 | 覆盖范围 | 特点 | 参考 |
|-----------|------|---------|------|------|
| **MedHELM** | 2024–持续 | 整体医学LLM评估框架；多维度临床任务 | Stanford Health Care + Microsoft合作；超越单一MCQ；关注安全性和临床实用性 | [HELM Medical](https://crfm.stanford.edu/helm/medical/latest/) |
| **HealthBench** | 2025 | 真实临床对话评估；多维度（准确性/安全/沟通） | 超越传统benchmark的多维框架；强调医患对话真实场景 | [OpenAI HealthBench](https://openai.com/index/healthbench/) |
| **Open Medical-LLM Leaderboard** | 2023–持续 | MedQA/MedMCQA/PubMedQA/MMLU医学等综合分 | HuggingFace持续更新；公开可访问 | [HuggingFace Blog](https://huggingface.co/blog/leaderboard-medicalllm) |

**当前水平小结**：医学MCQ已趋近饱和（USMLE ~91%）；真实工作流任务（EHR操作、ICD编码）仍有大量提升空间；中文医学评测体系相对独立。
