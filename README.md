# PMO SDD · 项目与流程治理技能

PMO SDD 给 AI 编程助手一套可执行的项目协作流程。从需求澄清到交付和迭代，每个阶段都有明确的产物、检查依据和决策记录。团队可以沿需求 ID 和图出处追溯规格、设计、实现与验收证据。

## 可以用来做什么

- **启动或接续项目。** 登记项目事实与约束，从状态板定位当前阶段和待决事项。
- **评审阶段产物。** 核对 PRD、架构图等产物是否承接上游需求，列出缺口和依据。
- **处理需求变更。** 沿追溯链找出受影响的规格、图、实现和测试，完成变更后的复核。

流程覆盖启动、MRD、PRD、架构、模块、组件、UI、开发、联调测试和迭代。仓库提供[技能入口](package/skills/pmo/SKILL.md)、[流程卷](package/skills/pmo/references/流程卷.md)、[通则卷](package/skills/pmo/references/通则卷.md)、[项目卷](package/skills/pmo/references/项目卷.md)和[配套模板](package/skills/pmo/assets/)。涉及多个功能的业务状态和规则时，可参考[面向对象方法指引](package/skills/pmo/references/OO方法指引.md)。

## 安装

克隆仓库后，按使用的宿主选择安装方式。安装和构建命令均从仓库根目录运行。

```sh
git clone https://github.com/liuchao1314lc-debug/pmo-sdd-mingzhang.git
cd pmo-sdd-mingzhang
```

| 宿主 | 安装方式 | 调用入口 |
| --- | --- | --- |
| [Codex](adapters/codex/README.md) | 项目级技能 | `$pmo` |
| [ZCode](adapters/zcode/README.md) | 从本地市场安装插件 | `pmo-zcode` |
| [DeepSeek Harness](adapters/dsh/README.md) | 安装 DSH 插件包 | `/pmo-dsh` |
| [WorkBuddy](adapters/workbuddy/README.md) | 导入技能 ZIP | 「PMO 项目治理」 |
| [Claude Code](adapters/claude-code/README.md) | 项目级技能 | `/pmo` |

## 试用

安装后在目标项目目录开启会话，调用 PMO，再说明本次要做的事。

> 只读审核当前 PRD，检查每条需求是否有功能承接和可执行的验收口径。列出缺口及其出处。
