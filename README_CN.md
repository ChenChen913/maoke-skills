# ChenChen913 / maoke-skills

个人 Claude Code 技能库，涵盖 AI 图像提示词生成、内容创作、技术学习、决策辅助和技能生态管理等场景，均来自真实工作流的打磨与沉淀。

---

## 🚀 安装

**方式一：手动安装**

下载或克隆本仓库，将需要的 Skill 文件夹复制到本地技能目录：
- Claude Code 用户：`~/.claude/skills/`
- Trae 用户：`~/.trae/skills/`

```bash
git clone https://github.com/ChenChen913/maoke-skills.git
```

**方式二：让 AI 帮你安装**

直接告诉 Claude Code、Trae 等 AI 工具，把仓库地址发给它，让它自动完成下载和安装：

> "请帮我安装这个 Skills 仓库：https://github.com/ChenChen913/maoke-skills"

---

## 📦 技能列表

### 🎨 AI 图像提示词

| 技能 | 描述 |
|---|---|
| **aesthetic-copilot** | 将模糊的想法转化为专业的商业级图像生成提示词，支持 Flux、Ideogram、Midjourney。内置风格库、随机混合引擎和 4 种输出模板（海报、杂志、产品、超现实）。 |
| **city-architect** | 专为城市景观、建筑设计、城市可视化生成高质量 AI 提示词，支持海报、微缩模型、时间流逝等多种形式。 |
| **comic-architect** | 基于漫画提示词方法论，为漫画、卡通、信息图表和图标生成 AI 图像提示词。 |

### ✍️ 内容创作

| 技能 | 描述 |
|---|---|
| **wechat-article-writer** | 微信公众号文章全流程创作助手。覆盖需求澄清 → 市场调研 → 大纲共创 → AI 写作 → 三轮结构化审稿 → 标题优化 → 配图配视频资源。支持个人素材库与写作风格学习，有效降低 AI 感。 |
| **ai-translator** | 专业英译中翻译助手，具备智能文档分类、三层术语管理、长文档分段翻译、语气检测优化，输出纯中文与双语对照两种格式。 |

### 🧠 学习与思考

| 技能 | 描述 |
|---|---|
| **learning-assistant** | 计算机科学、AI、机器学习和软件工程技术学习助手。可生成学习计划、知识总结、抽认卡，支持深度技术话题探究。 |
| **daily-decision-making** | 个人生活与职业决策结构化框架。建立个人决策数据库，系统处理不确定性与多方权衡。 |
| **knowledge-distiller** | 通过苏格拉底式追问提取和结构化隐性知识，将模糊想法转化为清晰方法论，帮助记录个人专业经验。 |

### 🏥 健康与健身

| 技能 | 描述 |
|---|---|
| **healthfit** | 个人全维度健康管理系统，中西医融合。提供四位独立顾问（Coach Alex 运动教练、Dr. Mei 营养师、Analyst Ray 数据分析师、Dr. Chen 中医体质顾问），支持性别差异化训练（M1-M5/F1-F6）、中医体质辨识与舌诊追踪、二十四节气养生、性健康隐私记录。内置 48 条术语知识库、成就系统、三层数据存储架构（JSON/TXT/SQLite）。综合评分 4.9/5，达到发布就绪标准。 |

### 💻 开发工程

| 技能 | 描述 |
|---|---|
| **project-java-init** | Java 全栈项目端到端初始化工具（Spring Boot + Vue3）。处理项目创建、依赖管理、配置和基础代码生成，使用持久化 `INIT_TODO.md` 文件跟踪和恢复初始化进度。 |

### ⚙️ 技能生态管理

| 技能 | 描述 |
|---|---|
| **local-skill-manager** | 本地技能目录的管家。支持查询、创建、删除技能，快速了解本地已安装的所有技能。 |
| **skill-evaluator** | 从 9 个维度对技能文件进行系统评估，包括质量、安全性、结构、触发词、Token 效率等，提供详细可操作的改进建议。 |
| **skill-evolution-tracker** | 实时监控技能执行情况，记录失败案例，并自动更新相关技能文档，实现持续自我进化。 |

---

## 📁 仓库结构

```
maoke-skills/
├── README.md
├── README_CN.md
└── skills/
    ├── aesthetic-copilot
    ├── ai-translator
    ├── city-architect
    ├── comic-architect
    ├── daily-decision-making
    ├── healthfit
    ├── knowledge-distiller
    ├── learning-assistant
    ├── local-skill-manager
    ├── project-java-init
    ├── skill-evaluator
    ├── skill-evolution-tracker
    └── wechat-article-writer
```

---

## 📄 开源协议

[MIT](LICENSE)
