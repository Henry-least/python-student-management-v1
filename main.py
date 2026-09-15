import json
from pathlib import Path


# __file__ 表示当前代码文件，with_name() 会把文件名替换为 students.json。
# 这样无论从哪个目录运行程序，数据都会保存在 main.py 旁边。
DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """从 JSON 文件读取全部学生；文件不存在时返回空列表。"""
    if not DATA_FILE.exists():
        return []

    # encoding="utf-8" 可以正确读取中文姓名。
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_students(students):
    """把全部学生写入 JSON 文件。"""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        # ensure_ascii=False 让中文直接显示；indent=4 让文件更易阅读。
        json.dump(students, file, ensure_ascii=False, indent=4)


def input_student():
    """接收用户输入，返回一名学生的信息。"""
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    score = float(input("请输入学生成绩："))

    student = {
        "name": name,
        "age": age,
        "score": score,
    }
    return student


def show_students(students):
    """在终端中显示全部学生的信息。"""
    if not students:
        print("\n暂时没有学生信息。")
        return

    print("\n--- 全部学生信息 ---")
    # enumerate(..., start=1) 会从 1 开始为学生编号。
    for number, student in enumerate(students, start=1):
        print(
            f"{number}. 姓名：{student['name']}，"
            f"年龄：{student['age']}，"
            f"成绩：{student['score']}"
        )


def main():
    """程序的主入口。"""
    print("=== Python 学生信息管理系统 v1.0 ===")

    # 先读取以前保存的数据，再录入一名新学生。
    students = load_students()
    show_students(students)

    print("\n--- 录入新学生 ---")
    student = input_student()
    students.append(student)

    # 把包含新学生的完整列表保存到磁盘。
    save_students(students)
    print("\n保存成功！")
    show_students(students)


if __name__ == "__main__":
    main()
