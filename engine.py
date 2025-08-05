"""
engine.py

Manages the logic of saving and recalling stories.
"""

class StoryEngine:
    def __init__(self, storage):
        self.storage = storage

    def save_story(self, title, content):
        self.storage.save(title, content)

    def recall_story(self, title):
        return self.storage.load(title)

    def list_stories(self):
        return self.storage.list_titles()
