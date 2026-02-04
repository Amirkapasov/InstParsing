import csv

def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            return set(row[0] for row in reader if row)
    except FileNotFoundError:
        return set()

def save_changes(filename, added, removed):
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["status", "username"])
        for u in added:
            writer.writerow(["ADDED", u])
        for u in removed:
            writer.writerow(["REMOVED", u])

day_old = input("Old day:")
day_new = input("New day:")


old_followers = read_csv(f"followers{day_old}.csv")
new_followers = read_csv(f"followers{day_new}.csv")

added_followers = new_followers - old_followers
removed_followers = old_followers - new_followers

save_changes("followers_changes.csv", added_followers, removed_followers)

print("Подписчики:")
print("Добавились:", added_followers)
print("Удалились:", removed_followers)

old_following = read_csv(f"following{day_old}.csv")
new_following = read_csv(f"following{day_new}.csv")

added_following = new_following - old_following
removed_following = old_following - new_following

save_changes("following_changes.csv", added_following, removed_following)

print("\nПодписки:")
print("Добавились:", added_following)
print("Удалились:", removed_following)
