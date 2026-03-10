# 多模态生物医学 Benchmarks

## 1. 医学影像 + 文本（放射科/病理/VQA）

| Benchmark | 年份 | 任务 | 规模 | 指标 | SOTA / 特点 | 参考 |
|-----------|------|------|------|------|------------|------|
| **PathMMU** | 2024 | 病理VQA+推理，专家验证 | 33,428 QA对，24,067图像（多来源） | Accuracy | GPT-4V辅助构建；7名病理学家验证；目前最大专家级病理基准 | [arXiv 2401.16355](https://arxiv.org/abs/2401.16355) |
| **OmniMedVQA** | 2024（CVPR） | 12模态VQA（MRI/CT/X光/组织病理/皮肤镜等） | 118,010图像 | Accuracy | 跨解剖区域、跨模态全面泛化测试 | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Hu_OmniMedVQA_A_New_Large-Scale_Comprehensive_Evaluation_Benchmark_for_Medical_LVLM_CVPR_2024_paper.pdf) |
| **MIMIC-CXR VQA / EHRXQA** | 2023（NeurIPS） | 胸片+EHR多模态QA | 377,391图像-问题-答案三元组 | Accuracy | 关联结构化EHR与放射学影像；多模态EHR QA基准 | [arXiv 2310.18652](https://arxiv.org/pdf/2310.18652) |
| **GEMeX** | 2025（ICCV） | 可定位、可解释的胸片VQA | 大规模CXR数据集 | Accuracy, 定位质量 | 支持区域定位+解释生成 | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_GEMeX_A_Large-Scale_Groundable_and_Explainable_Medical_VQA_Benchmark_for_ICCV_2025_paper.pdf) |

---

## 2. 生物实验协议理解

| Benchmark | 年份 | 任务 | 规模 | 指标 | 特点 | 参考 |
|-----------|------|------|------|------|------|------|
| **BioProBench** | 2025 | 生物实验协议理解与推理（多步实验操作） | 精心策划的协议数据集 | Accuracy, 推理步骤 | 测试LLM对实验流程的理解与执行能力 | [arXiv 2505.07889](https://arxiv.org/html/2505.07889v2) |

---

## 3. 多模态生物医学基础模型评测

| Benchmark | 年份 | 任务 | 规模 | 指标 | 特点 | 参考 |
|-----------|------|------|------|------|------|------|
| **15M图像-文本生物医学基础模型** | 2024 | 对比+生成评测（图像-文本/药物-蛋白/药物-文本/蛋白-文本） | 1500万图像-文本对 | 零样本分类, 检索 | 多域生物医学VLM全面评测框架 | [ResearchGate](https://www.researchgate.net/publication/387269158_A_Multimodal_Biomedical_Foundation_Model_Trained_from_Fifteen_Million_Image-Text_Pairs) |

---

## 3. 序列+结构多模态蛋白/分子模型

| Benchmark | 年份 | 任务 | 规模 | 指标 | 特点 | 参考 |
|-----------|------|------|------|------|------|------|
| **MULAN** | 2025 | 多模态蛋白语言模型评测（序列+角度结构编码联合） | 蛋白序列+结构 | 多任务性能 | 同时编码序列与结构模态；评测联合表示的优势 | [Bioinformatics Advances 2025](https://academic.oup.com/bioinformaticsadvances/article/5/1/vbaf117/8139638) |
| **MedGemma 1.5** | 2025 | 医学图像多任务（诊断分类/病变定位/描述生成） | 内部Google标准化基准（多种影像模态） | 分类准确率，定位AUC | 业界已有标准化内部基准体系；任务设计可参考自建开源版本 | [Google Research Blog 2025](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/) |

## 当前空白

- **分子结构图像理解**：化学结构式图→SMILES/IUPAC，目前无标准化基准
- **蛋白质结构图像+序列联合推理**：PyMOL截图+序列+功能问答
- **多模态跨域推理**：给定基因组变异图+表型图+文献，推断致病机制
- **`<mol>/<protein>/<rna>` 序列标记的视觉呈现**：无任何已知benchmark
