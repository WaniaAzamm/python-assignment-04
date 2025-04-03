import time

def countdown_timer(seconds):
    """Countdown timer that displays the remaining time every second."""
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)  
            time_format = '{:02d}:{:02d}'.format(mins, secs)  
            print(time_format, end='\r')  
            time.sleep(1)  
            seconds -= 1
        
        print("Time's up! 🎉")
    
    except KeyboardInterrupt:
        print("\nTimer interrupted. Exiting...")
        return

def start_timer():
    """Function to start the countdown timer."""
    print("Welcome to the Countdown Timer!")
    
    while True:
        try:
            minutes = input("Enter the countdown time in minutes: ")
            if minutes == '': 
                print("Please enter a valid number.")
                continue
            minutes = int(minutes)  
            if minutes <= 0:
                print("Please enter a positive number.")
                continue
            break  
        except ValueError:
            print("Invalid input. Please enter a valid number in minutes.")
    
    seconds = minutes * 60  
    
    countdown_timer(seconds)

start_timer()
