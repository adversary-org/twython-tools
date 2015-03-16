if l >=2:
    user = sys.argv[1]
else:
    user = input("Enter the username or ID (do not include the @ symbol): ")

try:
    target = int(user)
except:
    target = user
