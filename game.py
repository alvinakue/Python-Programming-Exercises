import time

# Define a function to print a colored message
def print_color(text, color):
    print(f"\033[{color}m{text}\033[0m")

# Print a colored welcoming message
print_color("**********************************************", "38")
print_color("*                                            *", "32")
print_color("*                                            *", "32")
print_color("*              WELCOME TO PUBG RPG            *", "33")
print_color("*                                            *", "32")
print_color("*                                            *", "32")
print_color("**********************************************", "39")
print_color("\nSurvive the battle and become the last player standing!\n", "36")
time.sleep(1)

# ANSI color codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"
# Example text
text = "Hello, world!"
print(RED + text + RESET) 