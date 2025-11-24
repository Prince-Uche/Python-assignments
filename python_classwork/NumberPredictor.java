import java.util.Scanner;
public class NumberPredictor{
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int fixedValue = 50;
    System.out.println("Enter a number: ");
    int userInput = input.nextInt();
    while (userInput != fixedValue){
    if (userInput > fixedValue){
    System.out.println("Too high");
}
    else{
    System.out.println("Too low");
}
    System.out.println("Enter a number: ");
    userInput = input.nextInt();
    if (userInput == fixedValue){
    System.out.printf("%d is the correct number %n", userInput);
}
}
}
}
