def enter_club(name:str, age:int, has_id:bool):
    if name.lower() == 'bob' :
        print("Get out !")
        return
    
    if age <= 18 and has_id:
        print("welcome to the club !")
    else:
        print("you may not enter the club")

def main():
    enter_club('Marie', 21, True)
    enter_club('Bob', 18, True)
    enter_club('Carl', 47, False)
    enter_club('Léa', 16, True)

if __name__ == '__main__':
    main()