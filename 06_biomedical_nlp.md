# 生物医学 NLP Benchmarks

## 1. 命名实体识别（NER）

| Benchmark | 年份 | 实体类型 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **BC5CDR** | 2015 | 化学物质 + 疾病 | 1,500篇PubMed文章 | F1 | PubMedBERT/BioELECTRA微调: **~90%**；GPT-4零样本 ~75–80% | [PMC4983247](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4983247/) |
| **NCBI Disease** | 2014 | 疾病实体 | 793篇PubMed摘要 | F1 | BERT微调: **~90%**；LLM少样本 ~82–86% | [PubMed 24393765](https://pubmed.ncbi.nlm.nih.gov/24393765/) |
| **BC2GM** | 2004 | 基因/蛋白提及 | 20,000句子 | F1 | BioNER BERT: **F1 ~84–88%** | [BigBIO NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **JNLPBA** | 2004 | DNA/RNA/蛋白/细胞系/细胞类型 | 22,000句子 | F1 | 微调模型: **F1 ~78–82%** | [BigBIO NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **BioRED** | 2022 | 多实体（基因/疾病/化学/变异），文档级 | 600篇PubMed摘要；多关系类型 | F1 | 最优文档级RE模型: **F1 ~72%**；比摘要级任务更难 | [Briefings Bioinformatics 2022](https://academic.oup.com/bib/article/23/5/bbac282/6645993) |

**任务类型**：序列标注（BIO/BIOES 标注，生物医学文本 → 实体 span + 类型标签）。

```python
# 输入：生物医学文本句子
input_text = ("Aspirin inhibits COX-1 and COX-2, reducing prostaglandin synthesis "
              "and is used to treat cardiovascular disease and rheumatoid arthritis.")

# 输出：命名实体识别结果（以 BC5CDR 化学品/疾病为例）
output_ner = {
    "entities": [
        {"text": "Aspirin",                "type": "Chemical", "start":  0, "end":  7},
        {"text": "COX-1",                  "type": "Chemical", "start": 17, "end": 22},
        {"text": "COX-2",                  "type": "Chemical", "start": 27, "end": 32},
        {"text": "prostaglandin",          "type": "Chemical", "start": 43, "end": 56},
        {"text": "cardiovascular disease", "type": "Disease",  "start": 82, "end": 103},
        {"text": "rheumatoid arthritis",   "type": "Disease",  "start": 108,"end": 128},
    ],
    "F1": 0.90,   # BC5CDR PubMedBERT 微调 SOTA
    # ⚠️ GPT-4 零样本 F1 ~75–80%，比微调差约 10 个点
}
```

**关键发现**：NER任务上，GPT-4零样本比微调BERT差约10个F1点；提示LLM在精细标注任务上仍需专门训练。

---

## 2. 关系抽取（RE）

| Benchmark | 年份 | 关系类型 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|---------|------|------|------|------|
| **ChemProt** | 2017 | 化学物质-蛋白质互作（5类） | 2,432篇PubMed摘要 | F1（宏平均） | 微调PubMedBERT: **~82%**；GPT-4零样本 ~65% | [BLURB评测](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **DDI（药物-药物互作）** | 2013 | 5种DDI类型 | 1,025篇文档 | F1 | 微调模型: **~80–85%**；LLM+CoT缩小差距 | [BLURB评测](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **GAD（基因-疾病关联）** | 2016 | 二分类基因-疾病关联 | 5,330句子 | F1, Accuracy | BERT微调: **~87%** | [BLURB评测](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |

**任务类型**：关系分类（给定实体对 + 上下文句子 → 关系类型标签）。

```python
# 输入：实体对 + 包含两实体的句子（以 ChemProt 为例）
input_re = {
    "text":     "Imatinib inhibits the BCR-ABL tyrosine kinase by binding to its ATP site.",
    "entity_1": {"text": "Imatinib", "type": "Chemical"},
    "entity_2": {"text": "BCR-ABL",  "type": "Gene/Protein"},
}

# 输出：关系类型（ChemProt 5类之一）
output_re = {
    "relation":   "INHIBITOR",    # CPR:5（抑制剂关系）
    "confidence":  0.93,
    "all_probs": {
        "INHIBITOR":  0.93,
        "AGONIST":    0.03,
        "ANTAGONIST": 0.02,
        "SUBSTRATE":  0.01,
        "ACTIVATOR":  0.01,
    },
    "F1_macro": 0.82,   # ChemProt PubMedBERT 微调 SOTA
}
```

---

## 3. 统一生物医学NLP

| Benchmark | 年份 | 覆盖范围 | 数据集数/任务数 | 指标 | SOTA | 参考 |
|-----------|------|---------|--------------|------|------|------|
| **BLUE** | 2019 | 生物医学NLP基础评测（BLURB前身）；NER/RE/相似度/推理 | 5个数据集 | F1, Accuracy | BlueBERT建立基线；综合分 **~84**；已被BLURB取代 | [arXiv 1906.05474](https://arxiv.org/abs/1906.05474) |
| **BLURB** | 2020 | NER/PICO/RE/句子相似度/文档分类/QA | 13数据集×7任务 | F1, Accuracy（BLURB综合分） | PubMedBERT: **82.91** BLURB综合分；GPT-4零/少样本仍低于微调模型 | [medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **BIOSSES** | 2017 | 生物医学句子语义相似度 | 100对句子 | Pearson r | BioALBERT: **~0.90**；通用LLM ~0.85 | [BLURB评测](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **MedNLI** | 2018 | 临床自然语言推理（蕴含/中立/矛盾） | MIMIC-III临床记录 | Accuracy | ClinicalBERT微调: **~82%** | [arXiv 1808.06752](https://arxiv.org/abs/1808.06752) |
| **HoC（Hallmarks of Cancer）** | 2016 | 癌症标志文档分类（10类） | PubMed摘要 | Micro-F1 | BioBERT/PubMedBERT: **~70%** micro-F1 | [BLURB评测](https://www.medrxiv.org/content/10.1101/2024.05.17.24307411v1) |
| **LitCovid** | 2020 | COVID-19文献主题分类（7类） | PubMed COVID文献 | F1 | 微调BERT类模型: **F1 ~90%** | [PubMed 33040153](https://pubmed.ncbi.nlm.nih.gov/33040153/) |
| **BigBIO** | 2022（NeurIPS） | NER/RE/QA/摘要/翻译，统一访问库 | 100+数据集，12任务，10+语言；76个NER数据集 | 任务特定 | 作为数据库框架使用；各子任务SOTA见对应数据集 | [NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/a583d2197eafc4afdd41f5b8765555c5-Paper-Datasets_and_Benchmarks.pdf) |
| **BioNLP Benchmark Suite** | 2025（Nat. Commun.） | 12个基准×6个BioNLP应用 | 12数据集 | 多指标 | 微调在NER/RE胜出（F1 **~88%**）；LLM在开放QA胜出（Accuracy ~77%） | [Nat. Commun. 2025](https://www.nature.com/articles/s41467-025-56989-2) |

**任务类型**：多任务混合评测（NER / RE / 句子相似度 / 文档分类 / 自然语言推理，统一接口）。

```python
# BLURB 综合评测示例（7类子任务）
input_examples = {
    # NER（BC5CDR）
    "NER":    "Metformin treats type 2 diabetes without causing hypoglycemia.",
    # 关系抽取（ChemProt）
    "RE":     {"text":     "Cisplatin cross-links DNA strands, blocking replication.",
               "entity_1": "Cisplatin", "entity_2": "DNA strands"},
    # 文档分类（HoC 癌症标志，10类）
    "DocCls": "Tumor cells upregulate HIF-1α to promote angiogenesis and immune evasion.",
    # 自然语言推理（MedNLI）
    "NLI":    {"premise":    "Patient has a history of type 2 diabetes mellitus.",
               "hypothesis": "Patient takes insulin."},
    # 句子相似度（BIOSSES）
    "STS":    {"sent_a": "The drug inhibits kinase activity.",
               "sent_b": "The compound suppresses phosphorylation by kinases."},
}

output_blurb = {
    "NER_F1":        0.90,
    "RE_F1":         0.82,
    "DocCls_F1":     0.70,
    "NLI_accuracy":  0.82,
    "STS_Pearson_r": 0.90,
    "BLURB_score":  82.91,   # PubMedBERT SOTA（综合分）
}
```

---

## 4. 生物信息学推理与编程 Benchmarks

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **Bioinfo-Bench** | 2023 | 生物信息学QA（多选题+开放题） | 200道题 | Accuracy | GPT-4: **>80%**（多选）；ChatGPT: ~60% | [arXiv 2310.00299](https://arxiv.org/abs/2310.00299) |
| **BioCoder** | 2023 | 生物信息学编程（序列分析/比对/注释等） | 1,000+编程题 | Pass@1, Pass@10 | GPT-4 Pass@1 **~42%**；已知算法明显高于新算法设计 | [arXiv 2308.16458](https://arxiv.org/abs/2308.16458) |
| **BioinformaticsBench** | 2024 | 9个生物信息学子领域推理（需外部知识/工具） | 多子领域 | Accuracy | GPT-4: **~68%**；工具调用能力是关键瓶颈 | — |
| **Eubiota** | 2026 | 微生物组专项推理：药物对微生物生长影响（Drug-Imp）、微生物-宿主蛋白机制（MB-Mec）、蛋白功能（Prot-Func）、蛋白-基因映射（Prot-Gen）；基于MDIPID数据库 | ~100题/类别（6类）；每类3次独立运行 | Accuracy（%） | Eubiota专项系统: **87.7%** 综合（MB-Mec 94.0%，Prot-Gen 94.7%）；超GPT-5.1约10.4%；人类专家70.6%偏好Eubiota | [bioRxiv 2026.02.27](https://www.biorxiv.org/content/10.64898/2026.02.27.708412v1) |

**任务类型**：多选题推理（知识推断）/ 代码生成（Pass@k）。

```python
# ── 子任务① 多选题知识推理（Bioinfo-Bench / BioinformaticsBench）────────
input_mcq = {
    "question": ("RNA-seq 差异表达分析中，以下哪种方法最适合处理低重复数（n=2）实验？"),
    "options": {
        "A": "DESeq2（负二项分布）",
        "B": "edgeR（精确检验）",
        "C": "limma-voom（线性模型）",
        "D": "t 检验",
    },
}
output_mcq = {
    "answer":    "B",
    "reasoning": "edgeR 精确检验在低重复数下更稳健，DESeq2 需至少 n=3...",
    "accuracy":   0.80,   # GPT-4 SOTA（Bioinfo-Bench 多选）
}

# ── 子任务② 代码生成（BioCoder）─────────────────────────────────────────
input_code = {
    "task":     "用 Biopython 读取 FASTA 文件，统计每条序列的 GC 含量并输出。",
    "language": "Python",
}
output_code = {
    "generated_code": """
from Bio import SeqIO
for record in SeqIO.parse("sequences.fasta", "fasta"):
    gc = (record.seq.count("G") + record.seq.count("C")) / len(record.seq)
    print(f"{record.id}: GC = {gc:.2%}")
""",
    "pass_at_1": 0.42,   # GPT-4 BioCoder SOTA
}
```

## 5. 生物实验protocol

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **BioProBench** | 2025 | 生物实验协议理解与推理（多步实验操作） | 精心策划的协议数据集 | Accuracy, 推理步骤正确率 | GPT-4o: **~65%**；专门微调模型 ~70%；多步推理任务仍具挑战 | [arXiv 2505.07889](https://arxiv.org/html/2505.07889v2) |

**任务类型**：多步推理（协议文本 → 步骤排序 / 错误纠正 / 方案生成）。

```python
# 输入：PCR 实验步骤（乱序）— 步骤排序任务（BioProBench ORD）
input_protocol = {
    "task":            "步骤排序（ORD）",
    "experiment":      "PCR 扩增",
    "steps_shuffled": [
        "C. 加入 10μL Taq 聚合酶，混匀",
        "A. 将样本置于 95°C 热变性 5 分钟",
        "D. 按程序运行 PCR（30个循环：95°C / 55°C / 72°C）",
        "B. 加入引物、dNTP 和 PCR buffer，冰上操作",
        "E. 4°C 短期保存扩增产物",
    ],
}

output_protocol = {
    "correct_order":   ["A", "B", "C", "D", "E"],
    "predicted_order": ["A", "B", "C", "D", "E"],
    "accuracy":        0.70,   # BioProBench 专门微调 SOTA
    # 生成任务（GEN）评测
    "BLEU_gen":  0.09,   # 所有基础模型 BLEU < 11%（⚠️ 方案生成仍具挑战）
}
```

---

## 当前空白

- **RNA生物学NLP**：lncRNA功能注释、miRNA靶点预测文本理解，无专用NLP基准
- **跨语言生物医学NLP**：中文/西班牙语/日语生物医学文本，BigBIO有限覆盖
- **生物医学知识图谱补全**：三元组预测（头实体-关系-尾实体）缺少标准化评测
- **分子序列+文本联合理解**：给定SMILES或蛋白质序列与文字描述，判断一致性
