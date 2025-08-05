"""
main.py

Entry point for the GPT Story Archive system.
"""

from storage import LocalStorage
from engine import StoryEngine

def main():
    storage = LocalStorage("stories.db")
    engine = StoryEngine(storage)

    print("GPT Story Archive System Initialized.")
    while True:
        command = input("\nEnter a command (new, recall, list, exit): ").strip().lower()
        if command == "new":
            title = input("Story title: ")
            content = input("Story content: ")
            engine.save_story(title, content)
        elif command == "recall":
            title = input("Title to recall: ")
            story = engine.recall_story(title)
            print(f"\n--- {title} ---\n{story}")
        elif command == "list":
            stories = engine.list_stories()
            print("\nSaved Stories:")
            for s in stories:
                print(f"- {s}")
        elif command == "exit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
