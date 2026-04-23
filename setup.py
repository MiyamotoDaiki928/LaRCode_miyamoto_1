# ============================================
# コンテスト番号を3桁で指定してください（例: 012）
# ============================================
CONTEST_NUMBER = "012"


# ============================
# 必要なライブラリのインストール
# ============================
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import time
import sys


# =========================
# 共通ログ関数
# =========================
def log(msg):
    print(f"[INFO] {msg}")

def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


# =========================
# URL読み込み
# =========================
CONTEST_URL = f"https://atcoder.jp/contests/abc{int(CONTEST_NUMBER):03d}"


# =========================
# HTML取得
# =========================
def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    log(f"GET {url} -> {res.status_code}")

    if res.status_code != 200:
        error(f"HTTPエラー: {res.status_code}")

    return res.text


# =========================
# tasks URL生成
# =========================
def get_tasks_url(contest_url):
    return contest_url.rstrip("/") + "/tasks"


# =========================
# 問題URL抽出
# =========================
def extract_problem_urls(tasks_html):
    soup = BeautifulSoup(tasks_html, "html.parser")

    urls = []
    for a in soup.select('a[href*="/tasks/"]'):
        href = a.get("href")

        if href and href.count("/") == 4:
            full_url = "https://atcoder.jp" + href
            if full_url not in urls:
                urls.append(full_url)

    if not urls:
        error("問題URL取得失敗")

    log(f"問題数: {len(urls)}")
    return urls


# =========================
# 問題データ抽出
# =========================
def extract_problem_data(html, url):
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("span", class_="h2")
    if not title_tag:
        error("タイトル取得失敗")

    for unwanted in title_tag.find_all(["a", "span"]):
        unwanted.extract()

    title = title_tag.get_text(strip=True)

    statement = soup.find("div", id="task-statement")
    if not statement:
        error("問題文取得失敗")

    samples = []
    sections = statement.find_all("section")

    current_input = None

    for sec in sections:
        h3 = sec.find("h3")
        if not h3:
            continue

        text = h3.text

        if "入力例" in text:
            pre = sec.find("pre")
            current_input = pre.text.strip() if pre else ""

        elif "出力例" in text and current_input is not None:
            pre = sec.find("pre")
            output = pre.text.strip() if pre else ""

            samples.append({
                "input": current_input,
                "output": output
            })

            current_input = None

    return {
        "url": url,
        "title": title,
        "samples": samples
    }


# =========================
# ファイル生成
# =========================
def generate_files(all_data, contest_url):
    contest_name = contest_url.rstrip("/").split("/")[-1].upper()

    base_dir = Path(f"{contest_name}")
    base_dir.mkdir(parents=True, exist_ok=True)

    log(f"作成ディレクトリ: {base_dir}")

    for i, data in enumerate(all_data):
        problem_letter = chr(ord('A') + i)

        problem_dir = base_dir / f"Problem {problem_letter}"
        problem_dir.mkdir(exist_ok=True)

        # =========================
        # Solutionファイル
        # =========================
        solution_path = problem_dir / f"Solution {problem_letter}.py"

        solution_code = f"""# {data['title']}
# {data['url']}

# =======================================================
# 以下に解答を記入してください
# コードテストはTesterファイルをターミナルで実行してください
# =======================================================


"""

        solution_path.write_text(solution_code, encoding="utf-8")

        # =========================
        # Testerファイル
        # =========================
        tester_path = problem_dir / f"Tester {problem_letter}.py"

        samples_str = repr(data["samples"])

        tester_code = f"""import subprocess
import sys
import os

SAMPLES = {samples_str}

print("=== TEST START ===")

for i, sample in enumerate(SAMPLES):
    print(f"[TEST {{i+1}}]")
    
    solution_path = os.path.join(os.path.dirname(__file__), "Solution {problem_letter}.py")
    
    result = subprocess.run(
        [sys.executable, solution_path],
        input=sample["input"].replace("\\r\\n", "\\n") + "\\n",
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()
    expected = sample["output"].strip()

    print("Input:")
    print(sample["input"])
    print("Output:", output)
    print("Expected:", expected)

    print("OK" if output == expected else "NG")
    print("-" * 20)
"""

        tester_path.write_text(tester_code, encoding="utf-8")

        log(f"作成: Problem {problem_letter}")


# =========================
# メイン処理
# =========================
def main():
    log("=== START ===")

    contest_url = CONTEST_URL.strip()

    tasks_url = get_tasks_url(contest_url)
    tasks_html = fetch_html(tasks_url)

    problem_urls = extract_problem_urls(tasks_html)

    all_data = []

    for url in problem_urls:
        html = fetch_html(url)
        data = extract_problem_data(html, url)
        all_data.append(data)
        time.sleep(1)

    generate_files(all_data, contest_url)

    log("=== DONE ===")


if __name__ == "__main__":
    main()
