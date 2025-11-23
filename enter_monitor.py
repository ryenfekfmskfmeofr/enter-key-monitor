
---

## 📄 enter_monitor.py
```python
count = 0

print("Press ENTER to count (CTRL + C to exit)")

try:
    while True:
        input()
        count += 1
        print(f"Enter pressed: {count} times")
except KeyboardInterrupt:
    print(f"\nTotal presses: {count}")
