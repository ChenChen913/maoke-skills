# ChenChen913 / maoke-skills

English | [中文](./README_CN.md)

A personal collection of Claude Code skills built and refined through real workflows — covering AI image prompting, content creation, technical learning, decision-making, and skill ecosystem management.

---

## 🚀 Installation

**Option 1: Manual**

Download or clone this repository, then copy the skill folders you need into your local skills directory:
- Claude Code: `~/.claude/skills/`
- Trae: `~/.trae/skills/`

```bash
git clone https://github.com/ChenChen913/maoke-skills.git
```

**Option 2: Ask your AI assistant**

Tell Claude Code, Trae, or any compatible AI tool to install skills directly from this repository:

> "Please install the skills from https://github.com/ChenChen913/maoke-skills"

The AI will handle the download and placement automatically.

---

## 📦 Skills

### 🎨 AI Image Prompting

| Skill | Description |
|---|---|
| **aesthetic-copilot** | Translates vague ideas into professional, commercial-grade prompts for Flux, Ideogram, and Midjourney. Features a style vault, randomization engine, and 4 output templates (poster, magazine, product, surreal). |
| **city-architect** | Generates high-fidelity AI prompts for cityscapes, architecture, and urban visualization — posters, miniatures, time-lapses, and more. |
| **comic-architect** | Generates AI image prompts for comics, cartoons, infographics, and icons using the Cartoon Prompt methodology. |

### ✍️ Content Creation

| Skill | Description |
|---|---|
| **wechat-article-writer** | Full-cycle WeChat Official Account article assistant. Covers requirements clarification → research → outline → writing → 3-round review → title optimization → media resources. Supports personal style library to reduce AI-sounding text. |
| **ai-translator** | Professional EN→CN translation with smart document classification, three-layer terminology management, segmented long-document handling, and dual-format output (pure Chinese + bilingual). |

### 🧠 Learning & Thinking

| Skill | Description |
|---|---|
| **learning-assistant** | Technical learning assistant for CS, AI, ML, and Software Engineering. Generates study plans, knowledge summaries, flashcards, and deep-dives on technical topics. |
| **daily-decision-making** | Structured personal decision framework for life and career choices. Implements a Personal Decision Database to handle trade-offs and uncertainty. |
| **knowledge-distiller** | Extracts and structures tacit knowledge through Socratic questioning. Turns vague ideas into clear methodologies and documented expertise. |
| **tutorial-writer** | Complete workflow for writing high-quality technical tutorials. Supports 6 tutorial types (project, tool, installation, concept, comparison, workflow), generates 4 versions for comparison, two-round review process, and includes mental models for explaining abstract concepts. |

### 💻 Development

| Skill | Description |
|---|---|
| **project-java-init** | End-to-end Java full-stack project initializer (Spring Boot + Vue3). Handles project creation, dependency management, configuration, and base code generation. Uses a persistent `INIT_TODO.md` to track and resume progress. |

### ⚙️ Skill Ecosystem

| Skill | Description |
|---|---|
| **local-skill-manager** | The housekeeper for your local `skills/` directory. List, query, create, and delete skills. |
| **skill-evaluator** | Systematically evaluates skill files across 9 dimensions: quality, safety, structure, triggers, token efficiency, and more. |
| **skill-evolution-tracker** | Monitors skill execution in real time, logs failures, and auto-updates the failing skill's documentation to enable continuous improvement. |

---

## 📁 Repository Structure

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
    ├── knowledge-distiller
    ├── learning-assistant
    ├── local-skill-manager
    ├── project-java-init
    ├── skill-evaluator
    ├── skill-evolution-tracker
    ├── tutorial-writer
    └── wechat-article-writer
```

---

## 📄 License

[MIT](LICENSE)
