# 多模态生物医学 Benchmarks

## 1. 医学影像 + 文本（放射科/病理/VQA）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **PathMMU** | 2024 | 病理VQA+推理，专家验证 | 33,428 QA对，24,067图像（多来源） | Accuracy | GPT-4V: ~63%；专科病理VLM: **~68%**；人类病理学家 ~90% | [arXiv 2401.16355](https://arxiv.org/abs/2401.16355) |
| **OmniMedVQA** | 2024（CVPR） | 12模态VQA（MRI/CT/X光/组织病理/皮肤镜等） | 118,010图像 | Accuracy | GPT-4V: ~76%；专科多模态模型: **~79%** | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Hu_OmniMedVQA_A_New_Large-Scale_Comprehensive_Evaluation_Benchmark_for_Medical_LVLM_CVPR_2024_paper.pdf) |
| **MIMIC-CXR VQA / EHRXQA** | 2023（NeurIPS） | 胸片+EHR多模态QA | 377,391图像-问题-答案三元组 | Accuracy | 多模态融合模型: **~80%**；仅图像模型 ~72% | [arXiv 2310.18652](https://arxiv.org/pdf/2310.18652) |
| **GEMeX** | 2025（ICCV） | 可定位、可解释的胸片VQA | 大规模CXR数据集 | Accuracy, 定位质量（IoU） | 最佳模型 Accuracy **~72%**，定位 IoU ~0.45 | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_GEMeX_A_Large-Scale_Groundable_and_Explainable_Medical_VQA_Benchmark_for_ICCV_2025_paper.pdf) |

**任务类型**：多模态 VQA 分类（医学图像 + 自然语言问题 → 文本答案 / 定位框）。

```python
# 输入：医学图像 + 自然语言问题
input_vqa = {
    "image":    "chest_xray_PA.jpg",   # 胸片（正位）
    "question": "该胸片中最显著的异常发现是什么，最可能的诊断是？",
    "modality": "CXR",
}

# 输出：文本答案 + 可选病变定位框
output_vqa = {
    "answer":   "右下肺可见大片高密度影，边界模糊，提示右下叶肺炎可能大。",
    "diagnosis": "right_lower_lobe_pneumonia",
    # GEMeX 可定位 VQA 子任务
    "localization": {
        "bbox": [312, 480, 620, 720],   # [x1, y1, x2, y2]（像素）
        "IoU":  0.45,                   # 与金标准区域重叠度
    },
    # 评测
    "accuracy":  0.72,    # GEMeX SOTA
    "PathMMU":   0.68,    # PathMMU 专科病理 VLM SOTA
    "OmniMedVQA": 0.79,   # 12模态综合 SOTA
}
```

---

## 2. 生物实验协议理解

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

## 3. 多模态生物医学基础模型评测

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **15M图像-文本生物医学基础模型** | 2024 | 对比+生成评测（图像-文本/药物-蛋白/药物-文本/蛋白-文本） | 1500万图像-文本对 | 零样本分类 Accuracy，检索 R@1 | 零样本分类 **~78%**；跨模态检索 R@1 ~65% | [ResearchGate](https://www.researchgate.net/publication/387269158_A_Multimodal_Biomedical_Foundation_Model_Trained_from_Fifteen_Million_Image-Text_Pairs) |

**任务类型**：跨模态检索（图像 ↔ 文本对齐）/ 零样本多模态分类。

```python
# 输入：文本查询 → 检索对应图像（text-to-image retrieval）
input_retrieval = {
    "query_type": "text_to_image",
    "query_text": "显示胰岛素信号通路中 IRS-1 磷酸化激活的免疫荧光图像",
    "candidate_pool_size": 10000,
}

output_retrieval = {
    "top1_image_id":    "fig_2b_pmid38291044",
    "top1_similarity":   0.87,   # 余弦相似度
    "R_at_1":   0.65,            # Recall@1（15M FM SOTA）
    "R_at_10":  0.83,

    # 零样本分类（病理图像示例）
    "zero_shot": {
        "image":    "pathology_adenocarcinoma.jpg",
        "label":    "adenocarcinoma",
        "accuracy": 0.78,   # 15M FM 零样本 SOTA
    },
}
```

---

## 4. 序列+结构多模态蛋白/分子模型

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA | 参考 |
|-----------|------|------|------|------|------|------|
| **MULAN** | 2025 | 多模态蛋白语言模型评测（序列+角度结构编码联合） | 蛋白序列+结构数据集 | 功能分类 AUC，结构对齐 TM-score | 联合模态 AUC **~0.91**，优于纯序列模型 ~3–5% | [Bioinformatics Advances 2025](https://academic.oup.com/bioinformaticsadvances/article/5/1/vbaf117/8139638) |
| **MedGemma 1.5** | 2025 | 医学图像多任务（诊断分类/病变定位/描述生成） | 内部Google标准化基准（多种影像模态） | 分类准确率，定位 AUC | 胸片分类 AUC **~0.94**；病变定位优于同期开源模型 | [Google Research Blog 2025](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/) |

**任务类型**：多模态分类（蛋白序列 + 结构角度特征 → 功能预测）/ 结构相似性回归。

```python
# 输入：蛋白质序列 + 主链二面角（MULAN 输入形式）
input_protein = {
    "sequence":  "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQ...",   # 氨基酸序列
    "structure": {
        "phi": [-60.2, -65.1, -58.4, ...],   # 主链二面角 φ（度）
        "psi": [-45.3, -40.2, -44.7, ...],   # 主链二面角 ψ
    },
}

output = {
    # EC 酶功能分类（4级层次）
    "EC_number":   "2.7.11.1",   # 蛋白激酶
    "EC_prob":      0.92,

    # 联合模态 vs 纯序列对比
    "function_AUC_joint":   0.91,   # 序列+结构联合（MULAN SOTA）
    "function_AUC_seqonly": 0.87,   # 仅序列（提升 ~3–5%）

    # MedGemma 1.5 医学影像子任务（胸片分类）
    "CXR_classification_AUC": 0.94,   # MedGemma 1.5 SOTA
}
```

## 当前空白

- **分子结构图像理解**：化学结构式图→SMILES/IUPAC，目前无标准化基准
- **蛋白质结构图像+序列联合推理**：PyMOL截图+序列+功能问答
- **多模态跨域推理**：给定基因组变异图+表型图+文献，推断致病机制
- **`<mol>/<protein>/<rna>` 序列标记的视觉呈现**：无任何已知benchmark
