# PROGRESS · hello-flask-sz 〔本项目活记忆 · 状态机〕

> **作用**:这是项目的"存档点"。任意 AI、任意重启会话,读它即可知道当前做到哪、下一步做什么、踩过什么坑。
> **更新时机**:每完成一个有意义步骤、每次会话结束前。
> **格式要求**:时间倒序,最新在上;短、准、可接力。

---

## 当前状态 (最后更新: 2026-06-06 · by AI)

- **阶段**: `初始化`
- **上一步完成**: 已读取并理解全部规范模板
- **下一步 (TODO 第一条)**: 等待用户确认 `00-project-context.md` 和 `01-requirements.md` 内容
- **阻塞项**: 无(待用户确认)

---

## 待办清单 (TODO,按优先级)

- [ ] 用户确认 `00-project-context.md` 内容无误
- [ ] 用户确认 `01-requirements.md` 用户故事和验收标准
- [ ] 从 `main` 开第一条 feature 分支: `feature/1-init-project`
- [ ] 创建基础文件: `app.py`, `test_app.py`, `requirements.txt`, `requirements-dev.txt`, `Dockerfile`
- [ ] 实现欢迎接口 (`GET /`)
- [ ] 实现健康检查接口 (`GET /health`)
- [ ] 编写单元测试(覆盖率 >= 80%)
- [ ] 本地自检: `ruff format --check .` + `ruff check .` + `pytest`
- [ ] 创建 CI workflow (`.github/workflows/ci.yml`)
- [ ] 创建 CD workflow (`.github/workflows/cd.yml`)
- [ ] 提交并推送 feature 分支
- [ ] 创建 PR,等待 CI 绿
- [ ] 合并 main,触发 CD 验证部署
- [ ] 验证部署后 `http://<服务器>:8003/health` 可访问
- [ ] 更新 `PROGRESS.md` 记录完成状态

---

## 关键决策记录 (ADR)

| 日期 | 决策 | 理由 |
|---|---|---|
| - | - | - |

---

## 已知坑 (GOTCHAS)

- - | - | - |

---

## 里程碑 (DONE)

- [ ] US-1 初始化项目工程化与 CI/CD
- [ ] US-2 实现欢迎接口
- [ ] US-3 实现健康检查接口
- [ ] US-4 容器化部署
