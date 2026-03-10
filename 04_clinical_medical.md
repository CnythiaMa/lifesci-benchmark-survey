# 临床医学 Benchmarks

## 1. 医学问答（Medical QA）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MedQA (USMLE)** | 2021 | 美国执照医师考试风格MCQ（4选项） | 12,723题（美版）；多语言版本 | Accuracy | Med-Gemini: **91.1%**；GPT-4o: ~90%；人类通过率 ~60% | [paperswithcode](https://paperswithcode.com/sota/question-answering-on-medqa-usmle) |
| **MedMCQA** | 2022 | 印度医学入学考试（AIIMS/NEET-PG），4选项 | 194,000题 | Accuracy | GPT-4级模型 ~70–75%；专门微调更高 | [arXiv 2203.14371](https://arxiv.org/abs/2203.14371) |
| **PubMedQA** | 2019 | 生物医学是/否/也许QA（PubMed摘要） | 1,000专家标注；61.2K未标注 | Accuracy | Yi-34B + OpenMedLM: **77.3%**；GPT-4零样本 ~75% | [PMC10935498](https://pmc.ncbi.nlm.nih.gov/articles/PMC10935498/) |
| **BioASQ**（第13届，持续） | 2013–2025 | 生物医学语义索引+QA（是非/事实/列表/摘要） | 5,000+ QA对（PubMed来源） | MAP, MRR, F1 | 是非题准确率 **>80%**；事实类 F1 ~0.55–0.62；2025新增MultiClinSum任务 | [bioasq.org](https://bioasq.org/) |
| **MMLU 医学/生物子集** | 2021 | 医学遗传学/解剖学/临床知识/学院医学/专业医学 | ~1,400题（医学子集） | Accuracy | GPT-4.1: **~90%**；GPT-4o: 88.7%；Claude 3 Opus: 86.8%；人类专家 ~90% | [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) |
| **MedXpertQA** | 2025（ICML） | 专家级医学推理；文本+多模态子集 | 精心策划的专家级；多样图像 | Accuracy | 顶尖LLM ~45–52%；人类专家 ~87%；差距仍显著 | [GitHub TsinghuaC3I](https://github.com/TsinghuaC3I/MedXpertQA) |

**任务类型**：多选题分类（题干 + 选项 → 正确选项字母）。

```python
# 输入：题干 + 4个选项
input_question = {
    "question": "一名 52 岁男性出现胸痛、大汗、左臂放射痛，心电图 V1–V4 导联 ST 段抬高。最可能的诊断是？",
    "options": {
        "A": "稳定型心绞痛",
        "B": "急性前壁心肌梗死（STEMI）",
        "C": "主动脉夹层",
        "D": "肺栓塞",
    },
    "source": "USMLE Step 2 CK 风格",
}

# 输出：预测选项 + 推理链
output = {
    "answer":     "B",
    "confidence": 0.96,
    "reasoning":  "ST 段抬高 + 胸痛 + V1–V4 导联受累提示 LAD 供血区 STEMI，需立即 PCI。",
    # 评测（MedQA USMLE）
    "benchmark_accuracy": 0.911,   # Med-Gemini SOTA
}
```

**趋势**：通用LLM在USMLE级MCQ已接近/超过人类通过率，但专家级推理题（MedXpertQA）仍有明显差距（~40个百分点）。

---

## 2. 临床NLP / EHR

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **n2c2 / i2b2 Shared Tasks** | 2006–持续 | 去识别化/NER/关系抽取/时序/共指/临床编码（年度轨道） | 每任务数百条去标识MIMIC/Partners记录 | F1, Precision, Recall | 去识别化 F1 **~99%**；临床NER F1 ~90–93%；BERT微调模型主导 | [n2c2.dbmi.hms.harvard.edu](https://n2c2.dbmi.hms.harvard.edu/) |
| **MedAgentBench** | 2025（NEJM AI） | LLM智能体在虚拟EHR中执行任务（开医嘱/查实验室/更新记录） | 真实临床EHR任务 | 任务完成率, Accuracy | 最佳agent任务完成率 **~70%**；复合任务显著下降 | [NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144) |
| **MedArena** | 2025 | 临床医生偏好评估11个LLM，80+亚专科 | 1,200+临床医生偏好（300+临床医生） | Elo / 偏好率 | Gemini 2.0 Flash Thinking **#1**；GPT-4o #2 | [Stanford HAI](https://hai.stanford.edu/news/medarena-comparing-llms-for-medicine-in-the-wild) |
| **MedS-Bench** | 2024–2025 | 11类高级临床任务，122种任务类型 | 500万条指令（58个医学语料库） | 多指标 | GPT-4综合最优；专科模型在复杂任务上更强；平均得分 **~68%** | [npj Digital Medicine 2025](https://www.nature.com/articles/s41746-024-01390-4) |
| **CSEDB** | 2025 | 临床安全+效能（30指标，26个科室） | 2,069道开放式QA | 综合分 | 平均 **57.2%**；高风险场景下降13.3%；**专科LLM > 通用LLM** | [npj Digital Medicine 2025](https://www.nature.com/articles/s41746-025-02277-8) |
| **DRAGON** | 2025 | 临床NLP自动化标注pipeline评测（文档分类/信息抽取/临床事件检测） | 多种临床NLP任务 | F1, Precision | 最优pipeline F1 **~85%**（文档分类）；事件检测 ~78% | [npj Digital Medicine 2025](https://www.nature.com/articles/s41746-025-01626-x) |
| **GLiNER-biomed** | 2025 | 开放域生物医学NER（无需为每个实体类型微调） | BC5CDR/NCBI Disease等标准NER集 | F1 | GLiNER-biomed: **F1 ~85%**（零样本）；可泛化到新实体类型 | [arXiv 2504.00676](https://arxiv.org/html/2504.00676v1) |
| **CL4Health CT-DEB'26** | 2026 | 临床试验剂量错误检测 shared task | 临床试验文档 | Precision, Recall, F1 | 竞赛进行中；暂无公开SOTA | [bionlp.nlm.nih.gov](https://bionlp.nlm.nih.gov/cl4health2026/) |
| **LLM医疗文本信息抽取基准** | 2026 | LLM-based信息抽取工具在医疗文本上的对比 | 多种医疗文本格式 | F1, ROUGE | GPT-4: **F1 ~82%**；传统NER微调 ~88%；LLM仍落后约6% | [medRxiv 2026](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full-text) |

**任务类型**：① 序列标注（临床文本 → 命名实体/关系）；② 智能体多步操作（自然语言任务 → EHR 工作流执行）。

```python
# ── 子任务① 临床 NER / 去标识化（n2c2 / DRAGON）───────────────────────
input_text = ("患者 John Smith，生于1978-03-15，就诊于 Mass General Hospital。"
              "诊断：2型糖尿病（E11.9），服用二甲双胍 500mg bid。")

output_ner = {
    "entities": [
        {"text": "John Smith",            "label": "PATIENT",    "start":  3, "end": 13},
        {"text": "1978-03-15",            "label": "DATE",       "start": 18, "end": 28},
        {"text": "Mass General Hospital", "label": "HOSPITAL",   "start": 34, "end": 55},
        {"text": "2型糖尿病",              "label": "CONDITION",  "start": 60, "end": 65},
        {"text": "E11.9",                "label": "ICD_CODE",   "start": 66, "end": 71},
        {"text": "二甲双胍 500mg bid",    "label": "MEDICATION", "start": 76, "end": 89},
    ],
    "F1_deid": 0.99,   # n2c2 去标识化 SOTA
}

# ── 子任务② EHR 智能体操作（MedAgentBench）─────────────────────────────
input_task = "为该患者开具空腹血糖检查医嘱，结果回报后更新糖化血红蛋白控制目标。"

output_agent = {
    "actions": [
        {"step": 1, "action": "order_lab",    "params": {"test": "FBG", "priority": "routine"}},
        {"step": 2, "action": "await_result", "params": {"test": "FBG"}},
        {"step": 3, "action": "update_goal",  "params": {"field": "HbA1c_target", "value": "<7%"}},
    ],
    "task_success":    True,
    "completion_rate": 0.70,   # MedAgentBench 最佳 agent SOTA
}
```

---

## 3. 疾病诊断 / ICD编码

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MAX-EVAL-11** | 2025 | ICD-11临床编码 | 含ICD-11标签的临床记录 | 加权分, 临床精确率 | Claude 4 Sonnet: **0.433**（43.3%精确率）；Gemini 2.5 Flash: 0.341 | [medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.10.30.25339130v1.full.pdf) |
| **MedBench v4**（中文） | 2024–2025 | 24个主科+91个副科；MCQ+开放题+智能体任务 | 700,000+专家策划任务（500+机构） | Accuracy, 专家评级 | 云端动态评测防刷榜；最优中文医学模型 Accuracy **~75%** | [arXiv 2511.14439](https://arxiv.org/abs/2511.14439) |

**任务类型**：多分类（临床记录全文 → ICD 编码列表）。

```python
# 输入：出院小结文本
input_note = """
出院小结：患者男，67岁，因"反复胸闷气促3年，加重1周"入院。
查体：双肺底湿啰音，下肢凹陷性水肿。BNP 2,840 pg/mL。
超声心动图：EF 35%，左室扩大。
诊断：慢性心力衰竭急性发作（HFrEF）；高血压3级；2型糖尿病。
"""

# 输出：主要诊断 + 附加诊断 ICD 编码
output_icd = {
    "primary_code":    "I50.1",    # 左心室衰竭（ICD-10-CM）
    "secondary_codes": ["I10", "E11.9"],
    "confidence": {
        "I50.1": 0.93,
        "I10":   0.88,
        "E11.9": 0.79,
    },
    # 评测（MAX-EVAL-11 ICD-11 benchmark）
    "weighted_score": 0.433,   # Claude 4 Sonnet SOTA
}
```

---

## 4. 整体医学LLM评估框架

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MedHELM** | 2024–持续 | 多维度临床任务（问答/摘要/诊断/安全性） | Stanford Health Care + Microsoft合作；覆盖多个临床场景 | 任务加权综合分 | GPT-4o/Claude-3.5-Sonnet领先；具体分数随版本更新 | [HELM Medical](https://crfm.stanford.edu/helm/medical/latest/) |
| **HealthBench** | 2025 | 真实临床对话评估；5个维度（准确性/安全/沟通/推理/拒绝） | 5,000+医患对话；多维度评分 | 综合评分(0–100) | GPT-4o: **~72**；Claude-3.5: ~70；Gemini 1.5 Pro: ~68 | [OpenAI HealthBench](https://openai.com/index/healthbench/) |
| **Open Medical-LLM Leaderboard** | 2023–持续 | MedQA/MedMCQA/PubMedQA/MMLU医学等六项综合分 | 多数据集合并评测 | Accuracy加权平均 | 持续更新；当前榜首平均 **~80%** | [HuggingFace Blog](https://huggingface.co/blog/leaderboard-medicalllm) |
| **Biomni-Eval1**（临床/诊断部分） | 2025 | 罕见病诊断（给定表型+候选基因推断OMIM诊断）、患者因果基因检测（MyGene2数据集）、CRISPR递送方式选择 | 433题总计（罕见病116题/患者基因检测400题/CRISPR递送40题） | 准确率（OMIM ID匹配）；加权专家评分 | Biomni Agent（Stanford）综合最优；具体分数未公开披露 | [HuggingFace biomni/Eval1](https://huggingface.co/datasets/biomni/Eval1) |

**任务类型**：综合多维度评测（问答准确性 / 安全性 / 沟通 / 推理 / 拒绝行为），无单一固定输入格式。

```python
# 以 HealthBench 单次医患对话评估为例
input_dialog = {
    "role":    "patient",
    "message": "我头痛三天了，要不要服用阿司匹林？我正在吃华法林。",
}

output_eval = {
    "model_response": ("不建议在服用华法林期间自行使用阿司匹林，"
                       "两者合用显著增加出血风险。请立即联系您的医生或药剂师。"),
    "dimensions": {
        "accuracy":      4.5,    # /5：信息正确（华法林+阿司匹林禁忌）
        "safety":        5.0,    # /5：正确提示出血风险
        "communication": 4.0,    # /5：表达清晰、无过多医学术语
        "refusal":      "N/A",   # 本题无需拒绝
    },
    "composite_score": 72,   # HealthBench 综合分（0–100），GPT-4o SOTA
}
```

**当前水平小结**：医学MCQ已趋近饱和（USMLE ~91%）；专家级推理题差距显著（~45% vs 人类87%）；真实工作流任务（EHR操作、ICD编码）仍有大量提升空间；中文医学评测体系相对独立。
