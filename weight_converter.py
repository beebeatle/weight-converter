from colorama import init, Fore, Style
import sys

def convert_kg_to_lb(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def convert_lb_to_kg(lb):
    """Convert pounds to kilograms"""
    return lb / 2.20462

def main():
    init()  # Initialize colorama
    
    print(f"{Fore.CYAN}Weight Converter{Style.RESET_ALL}")
    print("-" * 30)
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Exit")
    print("-" * 30)
    
    while True:
        try:
            choice = input("\nChoose conversion type (1-3): ")
            
            if choice == '1':
                kg = float(input("Enter weight in kilograms: "))
                lb = convert_kg_to_lb(kg)
                print(f"{Fore.GREEN}{kg} kilograms = {lb:.2f} pounds{Style.RESET_ALL}")
            
            elif choice == '2':
                lb = float(input("Enter weight in pounds: "))
                kg = convert_lb_to_kg(lb)
                print(f"{Fore.GREEN}{lb} pounds = {kg:.2f} kilograms{Style.RESET_ALL}")
            
            elif choice == '3':
                print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                sys.exit(0)
            
            else:
                print(f"{Fore.RED}Invalid choice! Please enter 1, 2, or 3.{Style.RESET_ALL}")
            
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
            sys.exit(0)

if __name__ == "__main__":
    main()
