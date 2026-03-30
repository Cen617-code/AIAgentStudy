"""
Flask 学习笔记应用 - Day 6 多文件项目练习
"""
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
NOTES_FILE = "notes.txt"


def load_notes():
    """从文件加载笔记"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return []


def save_note(content):
    """保存笔记到文件"""
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(content + "\n")


@app.route("/")
def index():
    """首页 - 显示所有笔记"""
    notes = load_notes()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    """添加笔记"""
    content = request.form.get("content", "").strip()
    if content:
        save_note(content)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
