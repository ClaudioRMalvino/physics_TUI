from typing import Dict, List
from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Header, Footer, Tree, Static, Input, Button, Markdown
from textual.screen import Screen
from physics_TUI.chapters.chapter3 import Chapter3
from physics_TUI.base_chapter import PhysicsChapter

class ChapterView(Screen):
    """Screen for viewing chapter content"""
    
    def __init__(self, chapter: PhysicsChapter):
        super().__init__()
        self.chapter = chapter

    def compose(self) -> ComposeResult:
        yield Header(self.chapter.title)
        
        # Display equations
        yield Static("# Equations", classes="section-title")
        for eq in self.chapter.get_equations():
            yield Static(f"## {eq.name}")
            yield Static(f"Formula: {eq.formula}")
            yield Static("Variables:")
            for var, desc in eq.variables.items():
                yield Static(f"- {var}: {desc}")
        
        # Display definitions
        yield Static("# Definitions", classes="section-title")
        for defn in self.chapter.get_definitions():
            yield Static(f"## {defn.term}")
            yield Static(defn.meaning)
            
        yield Footer()

class physicsTUIApp(App):
    """
    A Textual app to manage the chapters and the information within them.

    """

    CSS_PATH = "appearance.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def __init__(self) -> None:
        super().__init__()
        self.chapters: List[PhysicsChapter] =  [Chapter3()]


    def compose(self) -> ComposeResult:
        """Create Child widgets for the app."""
        yield Header()
        yield Tree("Chapters", id="chapter-tree")
        yield Footer()

    # def on_mount(self) -> None:
    #     tree = self.query_one(Tree)
    #     for title, chapter in self.chapters.items():
    #         tree.root.add(title)
    
    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        for chapter in self.chapters:
            tree.root.add(chapter.title)
            
    # def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
    #     node_label = str(event.node.label)
    #     chapter = self.chapters.get(event.node.label)
    #     if chapter:
    #         self.push_screen(ChapterView(chapter))
    
    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        selected_title = str(event.node.label)
        
        for chapter in self.chapters:
            if chapter.title == selected_title:
                self.push_screen(ChapterView(chapter))
                break

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mopde."""

        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = physicsTUIApp()
    app.run()
