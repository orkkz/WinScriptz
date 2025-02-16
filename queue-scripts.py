import os

script_path = os.path.join("resources", "scripts.txt")

def collect_scripts():
    scripts = [f for f in os.listdir("scripts") if f.endswith(".py") and f != __file__]  # List all .py files except this script
    selected_scripts = []
    for script in scripts:
        choice = input(f"Do you want to queue {script}? (y/n): ").strip().lower()
        if choice == 'y':
            selected_scripts.append(script)
    if selected_scripts:
        with open(script_path, "w") as file:
            file.write("\n".join(selected_scripts))
        print("Selected scripts have been queued for the machines.")
    else:
        print("No scripts were selected.")

if __name__ == "__main__":
    collect_scripts()
