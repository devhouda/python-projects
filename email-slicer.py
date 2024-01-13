# username, domain, extension
print("Welcome to my email slicer")
email = input("Enter your Email please: ")

print(email.split("@"))
(username, domain) = email.split("@")
(domain, extension) = domain.split(".")
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Extension: .{extension}")
