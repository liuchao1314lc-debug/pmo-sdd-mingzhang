# PMO 在 WorkBuddy 中使用

在仓库根目录从 [PMO 正本](../../package/skills/pmo/SKILL.md) 构建桌面端技能包。

```sh
python3 adapters/workbuddy/build.py
```

脚本打印 ZIP 的绝对路径，默认输出 `adapters/workbuddy/dist/pmo-workbuddy-0.1.0.zip`。版本号在构建脚本中维护。

1. 打开 WorkBuddy 桌面端，进入「专家·技能·连接器 → 技能 → 添加技能 → 上传技能」，选择生成的 ZIP。
2. 在「已安装」确认「PMO 项目治理」已启用。新建本地任务，选定要治理的项目目录，在对话框选择「PMO 项目治理」（`pmo-workbuddy`），例如输入「只读审核当前 PRD，列出发现」。
3. 项目启动时按 [WorkBuddy 宿主说明](../../package/skills/pmo/references/WorkBuddy宿主.md) 核验实际安装目录与宿主能力。

[WorkBuddy 桌面端技能导入说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
