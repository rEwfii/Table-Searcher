from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# 示例表格数据库（你可以加载外部 JSON 文件）
EXISTING_TABLES = [
    {"id": "table_001", "markdown": "| Name | Age |\n|------|-----|\n| Tom  | 21 |"},
    {"id": "table_002", "markdown": "| Product | Price |\n|---------|-------|\n| Apple   | 1.2   |"}
]

# 你需要实现的函数
def search_similar_tables(input_markdown):
    # 👉 你自己写相似度匹配逻辑
    # 暂时直接返回所有示例表格
    return EXISTING_TABLES

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    markdown_input = data.get("markdown", "")
    results = search_similar_tables(markdown_input)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
