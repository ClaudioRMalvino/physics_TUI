from typing import List, Dict, Any, Optional
import re

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Header, Footer, Tree, Button, Static, Input, OptionList
from textual.containers import Horizontal, VerticalScroll, Vertical
from textual.screen import Screen

from physics_TUI.chapters.chapter3 import Chapter3
from physics_TUI.chapters.chapter4 import Chapter4
from physics_TUI.chapters.chapter5 import Chapter5
from physics_TUI.chapters.chapter6 import Chapter6
from physics_TUI.chapters.chapter7 import Chapter7
from physics_TUI.chapters.chapter8 import Chapter8
from physics_TUI.chapters.chapter9 import Chapter9
from physics_TUI.chapters.chapter10 import Chapter10
from physics_TUI.chapters.chapter11 import Chapter11
from physics_TUI.chapters.chapter12 import Chapter12
from physics_TUI.chapters.chapter13 import Chapter13
from physics_TUI.chapters.chapter14 import Chapter14

from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class CalculatorScreen(Screen):
    """Screen for displaying calculator form for an equation"""

    BINDINGS = [
        Binding("escape", "go_back", "Back")
    ]

    def __init__(self, equation: Equation, current_chapter: Optional[PhysicsChapter]=None) -> None:
        super().__init__()
        self.equation = equation
        self.calc_inputs: Dict[str, Input] = {}
        self.current_chapter = current_chapter

    def compose(self) -> ComposeResult:
        """Create the calculator form layout"""
        yield Header()

        # Single scrollable container
        with VerticalScroll(id="calc-scroll-container"):
            yield Static(f"Calculator: {self.equation.name}", id="calc-title")
            yield Static(f"Formula: {self.equation.formula}", id="calc-formula")
            yield Static("Enter values (leave one field blank to solve for it):", id="calc-instructions")

            # Input fields in the same scrollable container
            for var, desc in self.equation.variables.items():
                # Skip variables marked as constants in their description
                if '(constant)' in desc:
                    continue

                yield Static(f"{var}: {desc}", classes="input-label")
                input_field = Input(placeholder=f"Enter value for {var}")

                # Properly sanitize variable name for ID
                sanitized_var = re.sub(r'[^\x00-\x7F]', '_', var)
                sanitized_var = re.sub(r'[^a-zA-Z0-9\-_]', '_', sanitized_var)

                input_field.id = f"input-{sanitized_var}"
                self.calc_inputs[var] = input_field
                yield input_field

            yield Button("Calculate", id="calc-button", variant="primary")
            yield Static("", id="calc-result")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle calculate button press"""
        
        if event.button.id == "calc-button":
            try:
                # Get values from input fields
                input_values = {}
                empty_field = None
                
                for var, input_widget in self.calc_inputs.items():
                    value_str = input_widget.value.strip()
                    if value_str:
                        try:
                            input_values[var] = float(value_str)
                        except ValueError:
                            self.query_one("#calc-result", Static).update(
                                f"[red]Error: '{value_str}' is not a valid number for {var}[/]"
                            )
                            return
                    else:
                        if empty_field is None:
                            empty_field = var
                        else:
                            self.query_one("#calc-result", Static).update(
                                "[red]Error: Leave exactly one field empty to solve for it[/]"
                            )
                            return
                
                # Check if we have exactly one empty field
                if empty_field is None:
                    self.query_one("#calc-result", Static).update(
                        "[red]Error: Leave one field empty to solve for it[/]"
                    )
                    return
                
                # Map display variables to calculation function parameters
                if self.current_chapter:
                    mapped_values = {}
                    for display_var, value in input_values.items():
                        # Use the variable mapping if available
                        if hasattr(self.current_chapter, 'var_mapping') and display_var in self.current_chapter.var_mapping:
                            calc_var = self.current_chapter.var_mapping[display_var]
                        else:
                            calc_var = display_var
                        mapped_values[calc_var] = value
                    
                    # Map the empty field too
                    if hasattr(self.current_chapter, 'var_mapping') and empty_field in self.current_chapter.var_mapping:
                        empty_calc_var = self.current_chapter.var_mapping[empty_field]
                    else:
                        empty_calc_var = empty_field
                
                    mapped_values[empty_calc_var] = None
                    
                    # Call the calculation function
                    if self.equation.calculation:
                        result = self.equation.calculation(**mapped_values)
                          
                        result_text = f"[green]✓ {empty_field} = {result}[/]"
                        
                        # Add units if available in variable description
                        if empty_field in self.equation.variables:
                            var_desc = self.equation.variables[empty_field]
                            # Try to extract units from description 
                            if '(' in var_desc and ')' in var_desc:
                                units = var_desc[var_desc.find('(')+1:var_desc.find(')')]
                                result_text = f"[green]✓ {empty_field} = {result} {units} [/]"
                        
                        self.query_one("#calc-result", Static).update(result_text)
                    else:
                        self.query_one("#calc-result", Static).update(
                            "[red]Error: No calculation function available for this equation[/]"
                        )
                else:
                    self.query_one("#calc-result", Static).update(
                        "[red]Error: No chapter context available[/]"
                    )
                    
            except Exception as e:
                # Handle calculation errors
                error_msg = str(e)
                self.query_one("#calc-result", Static).update(f"[red]Error: {error_msg}[/]")

    def action_go_back(self) -> None:
        """Go back to the previous screen"""
        self.app.pop_screen()


class physicsTUIApp(App):
    """
    A Textual app to manage the chapters and the information within them.
    """

    CSS_PATH = "appearance.tcss"
    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.chapters: List[PhysicsChapter] = [
            Chapter3(),
            Chapter4(),
            Chapter5(),
            Chapter6(),
            Chapter7(),
            Chapter8(),
            Chapter9(),
            Chapter10(),
            Chapter11(),
            Chapter12(),
            Chapter13(),
            Chapter14()
        ]
        self.current_chapter: Optional[PhysicsChapter] = None
        self.showing_equation_list = False
        self.calculable_equations: List[Equation] = []

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Horizontal():
            yield Tree("Chapters", id="chapter-tree")
            with VerticalScroll(id="content-area"):
                yield Static("", id="content", markup=True)
                yield Static("", id="welcome_content", markup=True)
                yield OptionList(id="equation-list", classes="hidden")
        yield Footer()

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        for chapter in self.chapters:
            chapter_branch = tree.root.add(chapter.title)

            if chapter.equations:
                chapter_branch.add_leaf("Equations")

            if chapter.definitions:
                chapter_branch.add_leaf("Definitions")

            # Add Calculations leaf only if the chapter has equations with calculation functions
            if any(hasattr(eq, 'calculation') and eq.calculation is not None for eq in chapter.equations):
                chapter_branch.add_leaf("Calculations")

        # Set initial content
        welcome_content_widget = self.query_one("#welcome_content", Static)

        welcome_content = """
[bold #bb9af7]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            WELCOME TO PHYSICS TUI!               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛[/]

[bold #7aa2f7]╔══════════════════════════════════════════════════╗
║  Physics Reference & Calculator                  ║
╚══════════════════════════════════════════════════╝[/]

[bold #9ece6a]▸[/] [#c0caf5]Select a chapter from the left panel[/]
[bold #9ece6a]▸[/] [#c0caf5]Navigate with arrow keys or mouse[/]
[bold #9ece6a]▸[/] [#c0caf5]Navigate between window panels with [bold #e0af68]Tab[/]
[bold #9ece6a]▸[/] [#c0caf5]Press [bold #e0af68]Enter[/] to select[/]
[bold #9ece6a]▸[/] [#c0caf5]Press [bold #e0af68]Ctrl + p[/] to open the palette[/]
[bold #9ece6a]▸[/] [#c0caf5]Press [bold #e0af68]Q[/] to quit[/]

[bold #2ac3de]━━━ Features ━━━[/]
[#ff9e64]✦[/] [#c0caf5]Physics equations and definitions[/]
[#ff9e64]✦[/] [#c0caf5]Interactive calculators[/]
[#ff9e64]✦[/] [#c0caf5]Chapter-based organization[/]

[#565f89]─────────────────────────────────────────────────────[/]
[italic #7aa2f7]
“I... a universe of atoms, an atom in the universe.” [/]
[italic #565f89]- Richard Feynman[/]"""

        welcome_content_widget.update(welcome_content)

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Update the content area when a node is selected."""
        selected_path = []
        node = event.node

        # Traverse the tree to get the full path of the selected node
        while node:
            selected_path.insert(0, str(node.label))
            node = node.parent

        # Ensure the path has at least two levels (chapter + leaf)
        if len(selected_path) == 3:
            parent, chapter_title, leaf_type = selected_path

            # Find the selected chapter
            for chapter in self.chapters:
                if chapter.title == chapter_title:
                    self.current_chapter = chapter  # Set current chapter

                    if leaf_type == "Equations":
                        self.update_content_equations(chapter)
                    elif leaf_type == "Definitions":
                        self.update_content_definitions(chapter)
                    elif leaf_type == "Calculations":
                        self.show_calculations_list(chapter)
                    break

    def update_content_equations(self, chapter: PhysicsChapter) -> None:
        """Update the content area with chapter equations."""
        self.showing_equation_list = False

        # Hide equation list and show content
        equation_list = self.query_one("#equation-list")
        equation_list.add_class("hidden")

        content_widget = self.query_one("#content", Static)
        content_widget.remove_class("hidden")

        # Build content string
        title_length = len(chapter.title)
        padding = max(0, (50 - title_length) // 2)

        content = f"""[bold #bb9af7 on #24283b]┏━{'━' * 50}━┓
┃{' ' * padding}{chapter.title.upper()}{' ' * (50 - title_length - padding)}┃
┗━{'━' * 50}━┛[/]

[bold #7aa2f7]╔══════════════════════════════════════════════════╗
║{'EQUATIONS'.center(50)}║
╚══════════════════════════════════════════════════╝[/]\n"""

        for eq in chapter.get_equations():
            name_padding = max(0, 45 - len(eq.name))
            content += f"\n[bold #2ac3de]┌─ {eq.name} {'─' * name_padding}┐[/]\n"
            content += f"[#c0caf5]│ Formula:[/] [#e0af68]{eq.formula}[/]\n"

            if eq.variables:
                content += f"[#c0caf5]│[/]\n"
                content += f"[#c0caf5]│ Variables:[/]\n"
                for var, desc in eq.variables.items():
                    content += f"[#c0caf5]│[/]   [#9ece6a]◆[/] [bold #ff9e64]{var}[/]: [#c0caf5]{desc}[/]\n"

            content += f"[bold #2ac3de]└{'─' * 48}┘[/]"

        content_widget.update(content)

    def update_content_definitions(self, chapter: PhysicsChapter) -> None:
        """Update the content area with chapter definitions"""
        self.showing_equation_list = False

        equation_list = self.query_one("#equation-list")
        equation_list.add_class("hidden")

        content_widget = self.query_one("#content", Static)
        content_widget.remove_class("hidden")

        title_length = len(chapter.title)
        padding = max(0, (50 - title_length) // 2)

        content = f"""[bold #bb9af7 on #24283b]┏━{'━' * 50}━┓
┃{' ' * padding}{chapter.title.upper()}{' ' * (50 - title_length - padding)}┃
┗━{'━' * 50}━┛[/]

[bold #7aa2f7]╔══════════════════════════════════════════════════╗
║{'DEFINITIONS'.center(50)}║
╚══════════════════════════════════════════════════╝[/]\n"""

        for defn in chapter.get_definitions():
            term_padding = max(0, 45 - len(defn.term))
            content += f"\n[bold #2ac3de]╭─ {defn.term} {'─' * term_padding}╮[/]\n"

            words = defn.meaning.split()
            lines = []
            current_line = ""

            for word in words:
                if len(current_line) + len(word) + 1 <= 46:
                    current_line += (" " + word) if current_line else word
                else:
                    lines.append(current_line)
                    current_line = word 

            if current_line:
                lines.append(current_line)

            for line in lines:
                content += f"[#c0caf5]│ {line:<47}│[/]\n"

            content += f"[bold #2ac3de]╰{'─' * 48}╯[/]"

        content_widget.update(content)

    def show_calculations_list(self, chapter: PhysicsChapter) -> None:
        """Show list of calculable equations using OptionList"""
        self.showing_equation_list = True
        self.current_chapter = chapter

        # Get equations with calculation functions
        self.calculable_equations = [
            eq for eq in chapter.equations if hasattr(eq, 'calculation') and eq.calculation is not None
        ]

        if not self.calculable_equations:

            equation_list = self.query_one("#equation-list")
            equation_list.add_class("hidden")

            content_widget = self.query_one("#content", Static)
            content_widget.remove_class("hidden")

            content = f"""[bold #bb9af7 on #24283b]{chapter.title}[/]

[bold #f7768e]No calculators available for this chapter.[/]"""
            content_widget.update(content)
            return

        # Hide content and show equation list
        content_widget = self.query_one("#content")
        content_widget.add_class("hidden")

        equation_list = self.query_one("#equation-list", OptionList)
        equation_list.remove_class("hidden")

        # Configure the option list
        equation_list.can_focus = True

        # Clear and populate the option list
        equation_list.clear_options()

        calc_header = self.query_one("#content-area").query_one("#calc-header", Static) if self.query_one("#content-area").query("#calc-header") else None

        if calc_header:
            calc_header.update(f"Calculable Equations for {chapter.title}")
        else:
            header = Static(f"Calculable Equations for {chapter.title}", id="calc-header")
            self.query_one("#content-area").mount(header, before=equation_list)


        equation_names = []

        for eq in self.calculable_equations:
            option_text = f"{eq.name}: {eq.formula} \n"
            equation_names.append(option_text)

        equation_list.add_options(equation_names)
        equation_list.focus()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle equation selection from OptionList"""
        # Make sure we're in equation list mode and have a chapter
        if not self.showing_equation_list or not self.current_chapter:
            return

        # Get the selected index
        selected_index = event.option_index

        # Check if we have calculable equations and the index is valid
        if not self.calculable_equations:
            return

        if 0 <= selected_index < len(self.calculable_equations):
            selected_equation = self.calculable_equations[selected_index]
            # Push to the calculator screen instead of modifying the current screen
            self.push_screen(CalculatorScreen(selected_equation, self.current_chapter))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

def main() -> None:
    """Main entry point for the physics TUI application."""
    app = physicsTUIApp()
    app.run()

if __name__ == "__main__":
    main()
