# Python 学生信息管理系统 v1.0

这是一个用于学习 Python 基础、JSON 数据保存和 Git 工作流的命令行项目。

## 当前功能

- 录入学生姓名、年龄和成绩
- 显示全部学生信息
- 使用 JSON 文件永久保存数据
- 再次运行时自动读取历史数据

## 运行环境

- Python 3.14 或更高版本
- Windows PowerShell 或其他终端

## 使用方法

进入项目目录：

```powershell
cd D:\codex\Codex\2026-09-14\python-v1-0
```

运行程序：

```powershell
python main.py
```

根据终端提示输入学生姓名、年龄和成绩。程序会把数据保存到
`students.json` 中。

## 项目文件

| 文件 | 作用 |
| --- | --- |
| `main.py` | 程序入口和主要功能代码 |
| `students.json` | 保存学生数据，由程序自动生成 |
| `README.md` | 项目介绍和使用说明 |

## JSON 数据示例

```json
[
    {
        "name": "张三",
        "age": 18,
        "score": 92.5
    }
]
```

## 学习进度

- [x] 认识项目文件夹和终端
- [x] 创建 `main.py`
- [x] 编写第一个小程序
- [x] 将代码拆成多个函数
- [x] 使用 JSON 永久保存数据
- [x] 创建 `README.md`，学习 Markdown
- [ ] 从零学习 Git
- [ ] 创建 GitHub 仓库并第一次推送
- [ ] 学习 `status`、`diff` 和 `log`
- [ ] 学习 `.gitignore`
- [ ] 增加新功能
- [ ] 提交并推送第二个版本

## 后续计划

下一阶段将使用 Git 记录项目的每次修改，并把项目发布到 GitHub。
