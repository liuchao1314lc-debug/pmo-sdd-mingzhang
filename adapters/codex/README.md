# PMO 在 Codex 中使用

PMO 的方法正本在 [package/skills/pmo](../../package/skills/pmo/SKILL.md)。从已选定的提交或快照安装，指定产品项目的根目录：

```sh
python3 adapters/codex/install.py '/绝对路径/产品项目'
```

安装器在目标项目生成 `.agents/skills/pmo/` 独立副本，并逐文件核对内容。重复运行会校验相同的实例。目标已有不同内容时会报错，由项目按版本治理处理迁移。从目标项目根目录打开 Codex，在对话中使用 `$pmo`。如果技能列表未刷新，重新打开 Codex。 [Codex Skills 文档](https://developers.openai.com/codex/skills)

本仓库的开发入口 `.agents/skills/pmo` 指向方法正本，适合检查当前改动。产品项目的部署回执登记实际副本路径、宿主版本、来源提交或快照及文件校验结果。已批准的项目实例按权-01 只读使用，更新时先修改源并同步。启动时核对 OO 指引随包安装、流程卷动作处的指针可读。

安装后按 [Codex 宿主说明](../../package/skills/pmo/references/Codex宿主.md) 核对项目的宿主能力与降级，并安排独立检查者。
