# Instagram Followers & Following Monitor

This project automates collecting Instagram followers and following lists through a web interface and tracks changes over time.

It consists of three main scripts:

- `For_followers.py` — collects followers
- `For_following.py` — collects following
- `monitoring.py` — compares old and new data

---

## 🚀 Features

- Collect followers usernames
- Collect following usernames
- Save results by date
- Compare two dates
- Detect:
  - New followers
  - Lost followers
  - New followings
  - Unfollowed accounts

---

## 🛠 Requirements

- Python 3.10+
- Google Chrome
- ChromeDriver (matching Chrome version)
- Selenium

Install dependencies:

```bash
pip install selenium
```
📂 Project Structure
```
project/
│
├── For_followers.py      # Collect followers
├── For_following.py      # Collect following
├── monitoring.py         # Compare changes
│
├── followers1.csv        # Example snapshot
├── following1.csv
│
├── followers2.csv
├── following2.csv
│
├── followers_changes.csv
└── following_changes.csv
```

▶️ How to Collect Followers
Run:
```
python For_followers.py
```
You will be asked:
```
nickname inst:
День просмотра:
```
Example input:
```
nickname inst: username123
День просмотра: 1
```
This creates:
```
followers1.csv
```
▶️ How to Collect Following
Run:
```
python For_following.py
```
You will be asked:
```
nickname inst:
День просмотра:
```

Example:
```
nickname inst: username123
День просмотра: 1
```

This creates:
```
following1.csv
```

🔄 How to Compare Two Dates
Run:
```
python monitoring.py
```

You will be asked:
```
Old day:
New day:
```

Example:
```
Old day: 1
New day: 2
```

## 🔄 Comparison

The script compares:

- `followers1.csv` vs `followers2.csv`
- `following1.csv` vs `following2.csv`

And creates:

- `followers_changes.csv`
- `following_changes.csv`

---

## 📊 Output Format

### followers1.csv

| username |
|----------|
| user1 |
| user2 |

### followers_changes.csv

| status  | username |
|---------|----------|
| ADDED   | new_user |
| REMOVED | old_user |

---

## ⚠️ Notes

- Make sure ChromeDriver version matches your Chrome browser
- The website may not load all users at once
- Use responsibly and follow platform rules

---

## 💡 Tips

You can track changes over time by running scripts daily:

| Day     | Files Created                         |
|--------|----------------------------------------|
| Day 1  | followers1.csv, following1.csv         |
| Day 2  | followers2.csv, following2.csv         |
| Compare | monitoring.py                        |
