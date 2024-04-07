import os

def run_commands():
    os.system("python3 link_generator.py")
    os.system("python3 get_data_timeline.py")
    os.system("python3 get_data_response.py")
    os.system("python3 country_info.py")

def main():
    run_commands()

if __name__ == "__main__":
    main()
