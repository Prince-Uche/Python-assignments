correct_password = "codex28"

password = (input("Enter your password: ")).lower()

while correct_password != password:
    print("Invalid password")
    password = (input("Enter your password: ")).lower()
    
print("Login confirmed")
    
    


