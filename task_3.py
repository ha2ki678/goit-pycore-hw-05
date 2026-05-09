import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception:
        print("Помилка під час читання файлу.")

    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    filtered_logs = list(filter(lambda log: log["level"] == level, logs))
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py шлях_до_файлу [рівень]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)

        print()
        print(f"Деталі логів для рівня '{level}':")

        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
    