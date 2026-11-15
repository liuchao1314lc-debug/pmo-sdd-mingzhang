# PMO 在 DeepSeek Harness 中使用

在仓库根目录从 PMO 正本构建插件，再安装到实际使用的 DSH profile（以 `web` 为例）：

```sh
pmo_dsh_package=$(python3 adapters/dsh/build.py)
dsh plugin --profile web add "$pmo_dsh_package"
```

构建输出为 `adapters/dsh/dist/dsh-plugin-pmo-0.1.0.tgz`，可整体分发。安装需要 DSH 与 `pnpm`，插件包无第三方依赖或安装脚本。`0.1.0` 是插件包版本，制作后续版本时在插件清单升版后重新构建。

从目标项目目录启动对应 profile，在会话输入 `/pmo-dsh 只读审核当前 PRD，列出发现`，或用 `skill` 工具加载 `pmo-dsh`。若已有会话未刷新，重启对应 profile。宿主核验与检查者安排见 [DSH 宿主说明](../../package/skills/pmo/references/DSH宿主.md)。 [DSH 插件打包与安装文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.zh.md)
