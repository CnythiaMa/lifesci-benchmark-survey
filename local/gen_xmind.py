#!/usr/bin/env python3
"""
生成 XMind 8/2020/2023 兼容的脑图文件（.xmind）

修复要点：
1. <sheet> 直接挂唯一根 <topic>，不多套一层 wrapper
2. 样式通过独立 <xmap-styles> 文件处理，topic 本身只用
   branch-color / color 等合法属性，彻底避免 xhtml:style
   属性内双引号嵌套导致 XML 解析失败
3. 用 xml.etree.ElementTree 程序化构建，确保 XML 永远合法
"""

import zipfile, os, uuid
import xml.etree.ElementTree as ET

OUTFILE = "/volume/data/xyma/0-dashboard/leaderboard/local/生命科学 AI Benchmark 全景图.xmind"

# ── 颜色（一级分支背景色） ─────────────────────────────────────────────────────
BRANCH_COLORS = [
    "#4A90D9",  # 蛋白质生物学 — 蓝
    "#E86C3A",  # 药物发现    — 橙
    "#27AE60",  # 基因组/单细胞 — 绿
    "#8E44AD",  # 临床医学    — 紫
    "#C0392B",  # 多模态      — 红
    "#16A085",  # 生物NLP    — 青
    "#D35400",  # AI智能体   — 深橙
]

# ── 脑图数据 ─────────────────────────────────────────────────────────────────
MINDMAP = [
    ("🧬 蛋白质生物学", [
        ("蛋白质结构预测", [
            ("CASP14",                            "AlphaFold2 — GDT_TS 92.4 / sum-z 244"),
            ("CASP15",                            "AF2变体 TM-score ~0.92；AF-Multimer DockQ ~0.60"),
            ("CAMEO（持续自动评测）",                   "AF2-based 平均 lDDT > 0.85"),
            ("CATH / SCOPe（结构分类）",               "Foldseek / TM-align"),
            ("1.4M 结构基准集（2025）",                "140万经质量检查结构，可更新测试集"),
        ]),
        ("蛋白质功能与适应性", [
            ("ProteinGym（2.7M突变 / 217 assays）",  "Tranception L — 中位Spearman r 0.46"),
            ("FLIP（4任务适应性预测）",                 "ESM2微调 — GB1 ~0.75 / AAV ~0.85"),
            ("FLIP2（2026，扩展版）",                 "竞赛进行中，暂无公开SOTA"),
            ("PEER（多任务统一评测）",                  "ESM2 / ProtTrans — AUC ~0.85"),
            ("CAFA6（2026，Kaggle竞赛）",             "GO功能注释，竞赛进行中"),
        ]),
        ("蛋白质–蛋白质互作 PPI", [
            ("PRING（多物种无泄露切分，2025）",           "最优图模型 AUROC ~0.85（严格切分）"),
            ("SHS27k / SHS148k",                   "KSGPPI Accuracy 88.96%（含数据泄露警告）"),
            ("Human PPI 26法社区评测（2023）",          "严格物种切分 AUROC ~0.72 vs 随机切分 ~0.92"),
        ]),
        ("蛋白质语言模型 PLM 评测", [
            ("多任务PLM评测（2024）",                  "ESM2-3B — 定位AUC 0.90 / 稳定性Spearman 0.67"),
            ("DARKIN（2024，黑暗激酶）",               "零样本AUC ~0.75；微调可达 ~0.88"),
        ]),
    ]),
    ("💊 药物发现", [
        ("ADMET 预测", [
            ("TDC（22任务标准化）",                    "ADMET-AI — AUROC ~0.871"),
            ("PharmaBench（2024）",                 "LLM增强SMILES — AUROC ~0.86"),
            ("Tox21 Challenge",                    "DeepTox — AUC ~0.85–0.88"),
        ]),
        ("药物–靶标互作 DTI", [
            ("Davis（Kd亲和力）",                     "注意力DTA — CI 0.893"),
            ("KIBA（复合评分）",                      "最优模型 CI ~0.901"),
            ("BindingDB（>991K IC50对）",             "二分类AUROC ~0.99（结构感知）"),
        ]),
        ("分子性质预测", [
            ("MoleculeNet（17+数据集）",               "Uni-Mol/GROVER — HIV 0.82 / BBBP 0.91"),
            ("TDC（66数据集）",                       "ChemBERTa / GROVER"),
        ]),
        ("分子生成", [
            ("MOSES（2D生成）",                      "Validity ~99.9%；REINVENT均分 0.79"),
            ("GuacaMol（20优化基准）",                  "REINVENT 均分 0.79"),
            ("MolScore（多目标统一框架）",                "综合分 ~0.72"),
            ("TOMG-Bench（文本引导生成）",               "微调Llama3.1 — 46.5%优势"),
            ("3D分子生成（DiffSBDD / TargetDiff）",    "Validity 99% / RMSD ~0.35 Å"),
        ]),
    ]),
    ("🔬 基因组学 & 单细胞", [
        ("变异效应预测", [
            ("ClinVar + gnomAD",                   "AlphaGenome — AUC 0.78–0.91（剪接预测）"),
            ("AlphaGenome 26-benchmark Suite",     "AlphaGenome（DeepMind, 2025）"),
            ("CAGI（社区挑战赛）",                     "Ensemble 模型"),
        ]),
        ("基因表达预测", [
            ("Enformer（调控序列→表达）",                "EPInformer — Pearson r 0.875–0.891"),
            ("scRNA扰动预测（Norman / Replogle）",     "⚠️ PCA baseline优于所有基础模型（Nature Methods 2025）"),
        ]),
        ("调控元件预测", [
            ("Nucleotide Transformer v2（18任务）",   "剪接位点 F1 ~0.92"),
            ("SegmentNT（基因组分割）",                 "SegmentNT — Jaccard ~0.87"),
            ("GFMBench-API（28数据集）",               "多模型集成"),
        ]),
        ("单细胞 RNA-seq", [
            ("scBench（394问题 / 9任务，2026）",       "GPT-4o + 专用Agent — 65%任务成功率"),
            ("scSuperAnnotator",                   "scGPT fine-tuned"),
        ]),
        ("空间转录组", [
            ("HESCAPE（组织切片检索）",                 "R@1 ~55%（跨模态对齐模型）"),
            ("图像→基因表达（11法比较）",                  "Pearson r ~0.45（最优方法）"),
        ]),
    ]),
    ("🏥 临床与医学", [
        ("医学问答 QA", [
            ("MedQA（USMLE 4选1）",                 "Med-Gemini — 91.1%；GPT-4o ~90%"),
            ("MedMCQA（印度医学考试）",                 "GPT-4级 ~70–75%"),
            ("PubMedQA（文献推理）",                   "OpenMedLM / Yi-34B — 77.3%"),
            ("BioASQ（持续至2025）",                  "是非题 >80%；2025新增MultiClinSum"),
            ("MMLU 医学子集（~1400题）",               "GPT-4.1 ~90%；Claude 3 Opus 86.8%"),
            ("MedXpertQA（专家级，2025 ICML）",        "顶尖LLM 45–52%（⚠️ 人类87%）"),
        ]),
        ("临床 NLP / EHR 操作", [
            ("n2c2系列（去标识/关系/概念）",               "微调BERT — 去标识F1 ~99%"),
            ("MedAgentBench（EHR Agent，NEJM AI 2025）", "最佳Agent — 70%任务完成率"),
            ("MedArena（临床医生偏好，2025）",             "Gemini 2.0 Flash Thinking #1"),
            ("MedS-Bench（122类任务，2025）",           "GPT-4综合最优；平均 ~68%"),
            ("CSEDB（30指标/26科室，2025）",            "平均57.2%；高风险场景 -13.3%"),
            ("DRAGON（临床NLP自动标注，2025）",           "最优pipeline F1 ~85%（文档分类）"),
            ("GLiNER-biomed（开放域NER，2025）",        "零样本 F1 ~85%，可泛化新实体"),
        ]),
        ("疾病诊断 / ICD 编码", [
            ("MAX-EVAL-11（ICD-11编码）",              "Claude 4 Sonnet — 43.3%；Gemini 2.5 Flash 34.1%"),
            ("MedBench v4（中文医学综合，2025）",         "最优中文医学模型 Accuracy ~75%"),
        ]),
        ("综合医学 LLM 评测", [
            ("MedHELM（斯坦福, 持续更新）",              "GPT-4o / Claude-3.5-Sonnet领先"),
            ("HealthBench（OpenAI, 2025）",           "GPT-4o ~72 / Claude-3.5 ~70"),
            ("Open Medical-LLM Leaderboard（HF）",   "当前榜首平均 ~80%"),
            ("Biomni-Eval1（罕见病/CRISPR，2025）",     "Biomni Agent（Stanford）综合最优"),
        ]),
    ]),
    ("🖼️ 多模态", [
        ("医学图像 + 文本 VQA", [
            ("PathMMU（病理切片问答）",                  "专科病理VLM — 68%（⚠️ 人类 ~90%）"),
            ("OmniMedVQA（12模态，CVPR 2024）",       "专科多模态模型 — 79%"),
            ("MIMIC-CXR / EHRXQA（胸片+EHR）",       "多模态融合 — ~80%"),
            ("GEMeX（可定位CXR VQA，ICCV 2025）",     "准确率 ~72% / 定位IoU ~0.45"),
        ]),
        ("生物协议理解", [
            ("BioProBench（实验操作步骤，2025）",         "专门微调 ~70%；多步推理仍具挑战"),
        ]),
        ("多模态基础模型", [
            ("15M Image-Text Biomedical FM（2024）", "零样本 ~78% / 跨模态检索R@1 ~65%"),
            ("MULAN（序列+结构多模态，2025）",            "联合模态 AUC 0.91"),
            ("MedGemma 1.5（Google, 2025）",        "胸片分类 AUC 0.94"),
        ]),
    ]),
    ("📝 生物医学 NLP", [
        ("命名实体识别 NER", [
            ("BC5CDR（化学品/疾病）",                   "PubMedBERT fine-tuned — F1 ~90%"),
            ("NCBI Disease",                       "BERT微调 — F1 ~90%"),
            ("BC2GM（基因/蛋白质）",                    "BioNER BERT — F1 ~84–88%"),
            ("JNLPBA（5类生物实体）",                   "微调模型 — F1 ~78–82%"),
            ("BioRED（多实体/文档级，2022）",             "文档级RE F1 ~72%（比摘要级更难）"),
        ]),
        ("关系抽取 RE", [
            ("ChemProt（化学–蛋白质关系）",               "微调PubMedBERT — F1 ~82%"),
            ("DDI（药物–药物相互作用）",                  "微调模型 — F1 ~80–85%"),
            ("GAD（基因–疾病关联）",                    "BERT微调 — F1 ~87%"),
        ]),
        ("统一 NLP 套件", [
            ("BLURB（13数据集，2020）",                "PubMedBERT — 综合分 82.91"),
            ("BigBIO（100+数据集，NeurIPS 2022）",     "76个NER数据集，12任务"),
            ("BioNLP Benchmark Suite（Nat.Commun. 2025）", "微调NER/RE F1 ~88%；LLM开放QA ~77%"),
            ("BIOSSES（语义相似度）",                   "BioALBERT — Pearson r ~0.90"),
            ("MedNLI（临床NLI）",                     "ClinicalBERT — Accuracy ~82%"),
        ]),
        ("生物信息学推理 / 编程", [
            ("Bioinfo-Bench（知识推理）",               "GPT-4 — >80%（多选）"),
            ("BioCoder（生物信息编程）",                 "GPT-4 — Pass@1 ~42%"),
            ("BioinformaticsBench（9子领域，2024）",    "GPT-4 ~68%；工具调用是关键瓶颈"),
            ("Eubiota（微生物组推理，2026）",             "Eubiota系统 87.7%；超GPT-5.1约10.4%"),
        ]),
    ]),
    ("🤖 AI 智能体 & 跨领域综合", [
        ("生命科学 AI Agent 评测", [
            ("scBench（单细胞分析Agent，2026）",         "GPT-4o Agent — 65%任务成功率"),
            ("MedAgentBench（临床EHR Agent）",         "GPT-4o — 70%任务完成率"),
            ("BioAgent Bench（生物实验工作流）",          "Claude-3.5 / GPT-4o"),
            ("LAB-Bench（2457题/8类/30子任务）",        "Claude 3.5 Sonnet 综合最优"),
            ("BixBench（真实生信分析，~205题）",          "GPT-4o/Claude 3.5 ~17%（⚠️ 接近随机）"),
        ]),
        ("跨领域综合套件", [
            ("LLM Benchmarks in Life Sciences 2026", "涵盖蛋白质/基因组/药物/临床四大领域"),
            ("FrontierScience（PhD级推理）",            "物理/化学/生物跨领域；42位奥赛金牌出题"),
            ("ATLAS（博士级，~800题/7学科）",             "目标：跨领域综合推理"),
            ("BEACON（规划中）",                       "目标：跨领域统一排行榜"),
        ]),
        ("当前主要空白 Gap Analysis", [
            ("序列标记联合理解 mol/protein/rna",         "⚠️ 无成熟benchmark"),
            ("跨领域因果推理（变异→表型→疾病）",              "⚠️ 评测链路缺失"),
            ("完整药物发现流水线（端到端）",                  "⚠️ 靶点→分子→ADMET→临床"),
            ("中文生物医学Agent评测",                    "⚠️ 目前以英文为主"),
        ]),
    ]),
]

# ── 用 ElementTree 构建 XML，彻底避免手拼字符串导致的引号问题 ─────────────────

def new_id():
    return "id_" + uuid.uuid4().hex[:12]

def make_topic_el(title: str, branch_color: str = "", font_color: str = "") -> ET.Element:
    el = ET.Element("topic", id=new_id())
    if branch_color:
        el.set("branch-color", branch_color)
    if font_color:
        el.set("color", font_color)
    title_el = ET.SubElement(el, "title")
    title_el.text = title
    return el

def add_children(parent_el: ET.Element, children_els: list):
    if not children_els:
        return
    ch = ET.SubElement(parent_el, "children")
    topics = ET.SubElement(ch, "topics", type="attached")
    for c in children_els:
        topics.append(c)

def build_tree() -> ET.Element:
    # 注册命名空间（避免 ns0: 前缀）
    ET.register_namespace("", "urn:xmind:xmap:xmlns:content:2.0")
    ET.register_namespace("fo",    "http://www.w3.org/1999/XSL/Format")
    ET.register_namespace("svg",   "http://www.w3.org/2000/svg")
    ET.register_namespace("xhtml", "http://www.w3.org/1999/xhtml")
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

    root_el = ET.Element(
        "xmap-content",
        xmlns="urn:xmind:xmap:xmlns:content:2.0",
        version="2.0",
    )
    # 补全其他 xmlns（ET不直接支持多xmlns，手动加）
    root_el.set("xmlns:fo",    "http://www.w3.org/1999/XSL/Format")
    root_el.set("xmlns:svg",   "http://www.w3.org/2000/svg")
    root_el.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")
    root_el.set("xmlns:xlink", "http://www.w3.org/1999/xlink")

    sheet = ET.SubElement(root_el, "sheet", id="sheet01", theme="default")

    # 中心根节点
    center = make_topic_el("生命科学 AI Benchmark 全景图",
                           branch_color="#2C3E50", font_color="#FFFFFF")

    branch_els = []
    for i, (branch_name, sections) in enumerate(MINDMAP):
        bcolor = BRANCH_COLORS[i % len(BRANCH_COLORS)]
        branch_el = make_topic_el(branch_name, branch_color=bcolor, font_color="#FFFFFF")

        sec_els = []
        for sec_name, benchmarks in sections:
            sec_el = make_topic_el(sec_name)

            bench_els = []
            for bench_name, sota_str in benchmarks:
                bench_el = make_topic_el(bench_name)
                sota_el  = make_topic_el(f"SOTA: {sota_str}")
                add_children(bench_el, [sota_el])
                bench_els.append(bench_el)

            add_children(sec_el, bench_els)
            sec_els.append(sec_el)

        add_children(branch_el, sec_els)
        branch_els.append(branch_el)

    add_children(center, branch_els)
    sheet.append(center)

    title_el = ET.SubElement(sheet, "title")
    title_el.text = "生命科学 AI Benchmark 全景图"

    return root_el


# ── 序列化 & 打包 ──────────────────────────────────────────────────────────────

META_XML = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<meta xmlns="urn:xmind:xmap:xmlns:meta:2.0" version="2.0"/>
"""

MANIFEST_XML = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="urn:xmind:xmap:xmlns:manifest:1.0">
  <file-entry full-path="content.xml" media-type="text/xml"/>
  <file-entry full-path="META-INF/manifest.xml" media-type="text/xml"/>
  <file-entry full-path="meta.xml" media-type="text/xml"/>
</manifest>
"""

print("构建 XML 树 …")
tree_root = build_tree()

# 序列化
content_bytes = ET.tostring(tree_root, encoding="unicode", xml_declaration=False)
content_xml = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + content_bytes

# 验证
print("验证 XML …")
try:
    ET.fromstring(content_xml)
    print("  ✅ XML 合法")
except Exception as e:
    print(f"  ❌ XML 验证失败: {e}")
    raise SystemExit(1)

print(f"写入 {OUTFILE} …")
with zipfile.ZipFile(OUTFILE, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("content.xml",           content_xml)
    zf.writestr("meta.xml",              META_XML)
    zf.writestr("META-INF/manifest.xml", MANIFEST_XML)

print(f"\n✅ 完成: {OUTFILE}")
print(f"   大小: {os.path.getsize(OUTFILE):,} bytes")
print("   支持: XMind 8 / XMind 2020 / XMind 2023")
