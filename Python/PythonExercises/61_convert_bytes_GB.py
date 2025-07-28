# 1 GB = 1073741824 Bytes (1024 * 1024 * 1024)
bytes = 1073741824

bytes_user = int(input("Enter amount of bytes: "))

print(f"{bytes_user} bytes is {bytes_user / bytes:.2f} GB")

gigabytes = int(input("Enter amount of GB: "))

print(f"{gigabytes} GB is: {gigabytes * bytes } bytes")
