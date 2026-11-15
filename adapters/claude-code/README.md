# PMO 在 Claude Code 中使用

从仓库根目录运行安装器，指定目标项目根目录。

```sh
python3 adapters/install_project_skill.py claude-code '/绝对路径/产品项目'
```

安装器将 [PMO 正本](../../package/skills/pmo/SKILL.md) 复制到项目的 `.claude/skills/pmo/` 并逐文件核对。重复执行会复核相同的副本，遇到已有不同内容则提示按项目版本规则迁移。

从目标项目根目录启动 Claude Code。在会话输入 `/pmo 只读审核当前 PRD，列出发现`。启动卡的宿主核验与检查者安排见 [Claude Code 宿主说明](../../package/skills/pmo/references/ClaudeCode宿主.md)。

[Claude Code 项目技能文档](https://code.claude.com/docs/en/skills#choose-where-skills-load)
