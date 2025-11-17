player_one = str(input("Player One; Enter rock, paper or scissors: "))

player_two = str(input("Player Two; Enter rock, paper or scissors: "))

rock =  "rock"

paper = "paper"

scissors = "scissors"

if (player_one == rock and player_two == paper):
    print(player_two, "beats", player_one, "Player 2 wins")

elif (player_one == paper and player_two == rock):
    print(player_one, "beats", player_two, "Player 1 wins")

elif (player_one == rock and player_two == scissors):
    print(player_two, "beats", player_one, "Player 2 wins")

elif (player_one == scissors and player_two == rock):
    print(player_one, "beats", player_two, "Player 1 wins")

elif (player_one == scissors and player_two == paper):
    print(player_one, "beats", player_two, "Player 1 wins")

elif (player_one == paper and player_two == scissors):
    print(player_two, "beats", player_one, "Player 2 wins")

elif (player_one == rock and player_two == rock):
    print(player_one, "=", player_two, "This is a Tie!")

elif (player_one == paper and player_two == paper):
    print(player_one, "=", player_two, "This is a Tie!")

elif (player_one == scissors and player_two == scissors):
    print(player_one, "=", player_two, "This is a Tie!")

else:
    print("invalid option. TRY AGAIN!")
