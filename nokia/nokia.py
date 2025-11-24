menu = """
***** Nokia menu map *****

>> List of menu functions <<

    1. Phone book 📗

    2. Messages 📨
    
    3. Chat 💬

    4. Call register 📖
    
    5. Tones 🎶

    6. Settings ⚙️

    7. Call divert 📵

    8. Games 🎮

    9. Calculator 🖩
    
    10. Reminders ⏰

    11. Clock

    12. Profiles 👤

    13. Sim services 🟨
    
    0. EXIT 
"""
print(menu)

while(True):
    select_option = input("Enter a number to select an option: ")
    match select_option:
        case 1:
            menu_one = """        
***PHONE BOOK 📗***
    1. Search
    2. Service Nos.
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7 Send b'card
    8. Options
    9. Speed dials
    10. Voice tags
    0. Back to Main Menu
""" 
phone_book = input("Enter a number to select an option: ")
match phone_book:
            case 1:
                print("Searching....")
                match searching:
                    case 0:
                        searching = input("press 0 to go back: ")
                        print(phone_book)
                        break
            case 2:
                        print("Pending...")
                        match service_nos:
                            case 0:
                                pending = input("press 0 to go back: ")
                                print(phone_book)
                                break
            case 3:
                            print("Pending...")
                            match add_name:
                                case 0:
                                    pending = input("press 0 to go back: ")
                                    print(phone_book)
                                    break
            case 4:
                              print("Pending...")
                              match erase:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
            case 5:
                              print("Pending...")
                              match edit:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
            case 6:
                               print("Pending...")
                               match assign_tone:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
            case 7:
                                        print("Pending...")
                                        match send_bcard:
                                            case 0:
                                                pending = input("press 0 to go back: ")
                                                print(phone_book)
                                                break
            case 8:
                                print("1. Type of view")
                                print("2. Memory status")
                                options = input("Enter a number to select an option:")
                                match options:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
                                        match type_of_view:
                                            case 1:
                                                print("Pending...")
                                                match type_of_view:
                                                    case 0:
                                                        pending = input("press 0 to go back: ")
                                                        print(options)
                                                        break
                                                        match memory_status:
                                                            case 2:
                                                                print("Pending...")
                                                                match memory_staus:
                                                                    case 0:
                                                                        pending = input("press 0 to go back: ")
                                                                        print(options)
                                                                        break
                                                                        default
                                                                        print("Invalid option")
                                                                        match phone_book:
                                                                            case 0:
                                                                                pending = input("press 0 to go back: ")
                                                                                print(phone_book) 
                                                                                break
            case 9:
                                print("Pending...")
                                match phone_book:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
            case 10:
                                print("Pending...")
                                match phone_book:
                                    case 0:
                                        pending = input("press 0 to go back: ")
                                        print(phone_book)
                                        break
                                        default
                                        print("Invalid option")
                                        match select_option:
                                            case 0:
                                                pending = input("press 0 to go back: ")
                                                print(select_option)         
                                                break

    
