from typing import List
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, Footer, Tree, Markdown
from textual.containers import Horizontal, VerticalScroll

from physics_TUI.chapters.chapter3 import Chapter3
from physics_TUI.base_chapter import PhysicsChapter

class physicsTUIApp(App):
    """
    A Textual app to manage the chapters and the information within them.
    """

    CSS_PATH = "appearance.tcss"
    BINDINGS = [
        Binding("d", "toggle_dark", "Toggle dark mode"),
    ]
    
    def __init__(self) -> None:
        super().__init__()
        self.chapters: List[PhysicsChapter] = [Chapter3()]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Horizontal():
            yield Tree("Chapters", id="chapter-tree")
            with VerticalScroll(id="content-area"):
                yield Markdown("# Select a chapter from the left panel.", id="content")
        yield Footer()

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        for chapter in self.chapters:
            tree.root.add(chapter.title)

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Update the content area when a chapter is selected."""
        selected_title = str(event.node.label)
        
        for chapter in self.chapters:
            if chapter.title == selected_title:
                self.update_content(chapter)
                break

    def update_content(self, chapter: PhysicsChapter) -> None:
        """Update the content area with chapter details."""
        content = f"# {chapter.title}\n\n"

        # Display equations
        content += "## Equations\n"
        for eq in chapter.get_equations():
            content += f"### {eq.name}\n**Formula**: `{eq.formula}`\n**Variables:**\n"
            for var, desc in eq.variables.items():
                content += f"- `{var}`: {desc}\n"
            content += "\n"

        # Display definitions
        content += "## Definitions\n"
        for defn in chapter.get_definitions():
            content += f"### {defn.term}\n{defn.meaning}\n\n"

        # Update the Markdown widget with the new content
        content_widget = self.query_one("#content", Markdown)
        content_widget.update(content)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = physicsTUIApp()
    app.run()
