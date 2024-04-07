import os

def run_commands():

    cwdi = os.getcwd()
    os.system(f"python3 {cwdi}/module2/link_generator.py")
    os.system(f"python3 {cwdi}/module2/timeline_info.py")
    os.system(f"python3 {cwdi}/module2/response_info.py")
    os.system(f"python3 {cwdi}/module2/country_generator.py")
    os.system(f"python3 {cwdi}/module2/info_country.py")

def main():
    run_commands()

if __name__ == "__main__":
    main()
