# Claude Code 宿主绑定

Claude Code 从目标项目的 `.claude/skills/pmo/` 加载 PMO。在项目根目录启动会话，从 `/` 菜单选择 `/pmo` 并附上当前动作。卷册、OO 指引和模板从已安装的技能目录定位，状态板和交付物从目标项目根目录定位。

启动卡核对 `/pmo` 指向目标项目的副本，并确认同一副本的卷册、模板、OO 指引和流程卷中的引用可读。部署回执登记实际技能路径、Claude Code 版本、约束包版本、来源提交或快照及文件核验结果。已批准的项目副本按权-01 只读使用。

按 [通则卷 #20／#21](通则卷.md) 核对状态板续接、写入边界、产出物头部、图出处及覆盖、生效记录和裁定写入通道。回执按实际登记宿主具备的执法及手工替代，涉及承重执法的降级按 #7 显式裁定。

检查者另开会话，只接收待核产物、适用判据和必要上游证据。Claude Code CLI 可用 `claude --permission-mode plan --tools 'Read,Glob,Grep,Skill' --disallowedTools 'mcp__*'` 限定检查会话。安排时仍须核实会话和可用工具均无项目写入权，或由独立人工承担；检查结论交用户裁定。 [Claude Code 权限与沙箱](https://code.claude.com/docs/en/permissions)
