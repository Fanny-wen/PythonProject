from datetime import timedelta

"""只有 days, seconds 和 microseconds 会存储在内部"""
delta = timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, microseconds=1, milliseconds=1)
print(delta)  # 8 days, 1:01:01.001001
print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print("=" * 100)
print(delta + timedelta(days=1))
print(delta - timedelta(days=1))
print(delta * 3)  # t1 = t2 * i or t1 = i * t2
print(delta / timedelta(seconds=1))  # f = t2 / t3
print(delta // 3)  # t1 = t2 // i or t1 = t2 // t3
print(delta % timedelta(days=3))
print("=" * 100)
print(delta.total_seconds())  # 返回时间间隔包含了多少秒
print("=" * 100)

year = timedelta(days=365)
print(year)
