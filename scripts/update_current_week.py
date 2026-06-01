import json
import datetime
from pathlib import Path

with open("config.json") as f:
    config = json.load(f)

start_date = datetime.datetime.strptime(config["start_date"], "%Y-%m-%d").date()
today = datetime.date.today()
total_weeks = config["total_weeks"]

delta_days = (today - start_date).days
current_week = max(1, min(total_weeks, delta_days // 7 + 1))

if today < start_date:
    status = f"🔒 Старт: {config['start_date']}"
    current_week = 1
elif delta_days >= total_weeks * 7:
    status = "🎓 Курс завершён! Переходи к портфолио."
    current_week = total_weeks
else:
    status = f"📍 Ты на неделе {current_week} из {total_weeks}"

readme_path = Path("README.md")
content = readme_path.read_text(encoding="utf-8")
import re
content = re.sub(r'!\[Текущая неделя\].*?\n', '', content)

badge = f'![Текущая неделя](https://img.shields.io/badge/📍_Сейчас-Неделя_{current_week:02d}-blue?style=for-the-badge)\n\n'
readme_path.write_text(badge + f"> {status}\n\n" + content, encoding="utf-8")

current_md = Path("CURRENT.md")
week_file = f"progress/week_{current_week:02d}.md"
current_md.write_text(
    f"# 🎯 Твоя текущая неделя: {current_week}\n\n> {status}\n\n👉 [Открыть план недели]({week_file})\n\n"
    f"---\n### Быстрые ссылки:\n- [← Назад](progress/week_{max(1, current_week-1):02d}.md)\n"
    f"- [→ Вперёд](progress/week_{min(total_weeks, current_week+1):02d}.md)\n- [📁 Все недели](progress/)",
    encoding="utf-8"
)
