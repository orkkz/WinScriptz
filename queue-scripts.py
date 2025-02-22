import os

script_path = os.path.join("resources", "scripts.txt")

def collect_scripts():
    scripts = [f for f in os.listdir("scripts") if f.endswith(".py") and f != __file__]  # List all .py files except this script
    selected_scripts = []
    print("Available Scripts:")
    for idx, script in enumerate(scripts):
        print(f"{idx}. {script}")
    user_input = input("Enter the script numbers you want to run (e.g., 0 1 2): ").strip()
    script_indexes = user_input.split()
    for idx in script_indexes:
        try:
            selected_scripts.append(scripts[int(idx)])
        except (ValueError, IndexError):
            print(f"Invalid input: {idx}. Skipping.")
    if selected_scripts:
        with open(os.path.join("resources", "scripts.txt"), "w") as file:
            file.write("\n".join(selected_scripts))
        print(f"Selected scripts have been queued: {', '.join(selected_scripts)}")
    else:
        print("No scripts were selected.")

if __name__ == "__main__":
    collect_scripts()
