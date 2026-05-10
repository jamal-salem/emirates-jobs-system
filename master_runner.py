import os

print("\nFetching Jobs...\n")

os.system("python fetch_jobs.py")

print("\nRunning Notifications...\n")

os.system("python smart_notifier.py")

print("\nSystem Cycle Complete!\n")
