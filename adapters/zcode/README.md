# PMO 在 ZCode 中使用

在仓库根目录生成可导入的本地插件市场：

```sh
python3 adapters/zcode/build.py
```

脚本打印市场的绝对路径，默认是 `adapters/zcode/dist/local-marketplace/`。输出包含市场清单、插件清单和完整的 PMO 技能副本，可以整体移动。若默认目录已有不同版本，给脚本传入新的输出目录。

1. 在 ZCode 打开工作区，进入「设置 → 插件」，点「创建 → 添加插件市场」，选择上一步的市场根目录。
2. 在「个人」分组找到 `pmo-local`，安装并启用「PMO 项目治理」。到「设置 → 技能 → Plugin 技能」确认 `pmo-zcode` 已显示。
3. 在目标项目的对话输入 `/`，从「技能」分组选择 `pmo-zcode`，例如接着写「只读审核 PRD，只给发现」。插件限定名是 `pmo:pmo-zcode`。这个入口名让 ZCode 能在同一仓库里同时列出 Codex 的 `pmo` 和插件技能。

更多入口见 [ZCode 插件文档](https://zcode.z.ai/cn/docs/plugin)。产品项目的宿主核验、降级与检查者安排见 [ZCode 宿主说明](../../package/skills/pmo/references/ZCode宿主.md)。

`0.1.0` 是插件包版本。更新已登记的市场时，先同步提升插件清单和市场条目的 `version`，把旧的生成目录移到备份位置，再生成到已登记的原路径。在 ZCode 刷新该市场并更新插件，项目部署回执记录实际版本与源提交或快照。
