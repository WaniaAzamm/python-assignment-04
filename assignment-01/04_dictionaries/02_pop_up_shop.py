def main():
    fruits = {'apple': 1.5, 'peach': 50, 'orange': 80, 'kiwi': 1, 'grapes': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        while True:
            try:
                amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ")
                if amount_bought == "": 
                    break
                amount_bought = int(amount_bought)  
                total_cost += fruits[fruit_name] * amount_bought
                break
            except ValueError:
                print("Please enter a valid number.") 
    
    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
