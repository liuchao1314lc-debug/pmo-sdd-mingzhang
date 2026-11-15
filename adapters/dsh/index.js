import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import manifest from './package.json' with { type: 'json' }

export const name = 'pmo-dsh'
export const inject = ['skills']

const resourceBase = {
  kind: 'directory',
  path: fileURLToPath(new URL('./skills/pmo-dsh/', import.meta.url)),
}
const entry = new URL('./skills/pmo-dsh/SKILL.md', import.meta.url)

export async function apply(ctx) {
  const markdown = await readFile(entry, 'utf8')
  const content = markdown.replace(/^---\n[\s\S]*?\n---\n/, '').trim()
  ctx.skills.register({
    name,
    description: manifest.description,
    source: 'bundled',
    provider: name,
    resourceBase,
    path: fileURLToPath(entry),
    content,
  })
}
