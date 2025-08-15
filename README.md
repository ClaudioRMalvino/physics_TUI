# Physics TUI

A comprehensive Terminal User Interface (TUI) for physics reference and calculations, providing interactive access to physics equations, definitions, and calculators organized by chapter.

![Development Status](https://img.shields.io/badge/status-stable-green)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

##  Project Status

This project is **complete and ready for use** as a comprehensive physics reference tool. It covers 12 major physics topics with over 6,800 lines of well-documented code, including extensive calculations and interactive features.

**Current Status:** Stable release - The project is feature-complete for its intended scope. While I may add enhancements like unit conversion calculators in the future, the current version provides a fully functional physics reference and calculation platform.

**Development Note:** Active development is paused as I focus on preparing for University of Cambridge (MPhil in Scientific Computing), but the project remains stable and fully usable. I may occasionally tinker with improvements during free time.

## Features

- **Interactive TUI Interface** - Clean, keyboard-driven navigation
- **12 Physics Chapters** - From basic motion to advanced fluid dynamics
- **190+ Physics Equations** - Comprehensive formula reference
- **Calculator for 58 equations** - Ability to solve for various problems
- **Interactive Calculators** - Solve for any variable in supported equations
- **Extensive Documentation** - Clear explanations and variable definitions
- **Cross-platform Support** - Works on Linux, macOS, and Windows
- **Professional Code Quality** - Type hints, error handling, and comprehensive tests

## Covered Physics Topics

1. **Motion Along a Straight Line** - Kinematics, acceleration, free fall
2. **Motion in Two and Three Dimensions** - Projectile motion, circular motion
3. **Newton's Laws of Motion** - Forces, mass, acceleration
4. **Applications of Newton's Laws** - Friction, centripetal force, drag
5. **Work and Kinetic Energy** - Energy calculations and work-energy theorem
6. **Potential Energy and Conservation of Energy** - Conservative forces, energy conservation
7. **Linear Momentum and Collisions** - Momentum conservation, elastic/inelastic collisions
8. **Fixed-Axis Rotation** - Angular motion, moment of inertia, torque
9. **Angular Momentum** - Rotational dynamics, conservation laws
10. **Static Equilibrium and Elasticity** - Force balance, material properties
11. **Gravitation** - Universal gravitation, orbital mechanics, Kepler's laws
12. **Fluid Dynamics** - Pressure, flow, Bernoulli's equation, viscosity

## Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Quick Install (Recommended)
```bash
# Utilizing pip package mananger
pip install git+https://github.com/ClaudioRMalvino/physics_tui.git
```

```bash
# Utilizing uv package manager
uv install git+https://github.com/ClaudioRMalvino/physics-tui.git
```

### Development Install
```bash
git clone https://github.com/ClaudioRMalvino/physics_tui.git
cd physics_tui
pip install -e .
```

### Using Virtual Environment (Recommended)
```bash
# Create and activate virtual environment
python -m venv physics_env
source physics_env/bin/activate  # Linux/macOS
# physics_env\Scripts\activate   # Windows

# Install physics-tui
pip install git+https://github.com/ClaudioRMalvino/physics_tui.git

```bash
# Create a project with uv
uv init physics-tui-project
cd physics-tui-project

# Add your package
uv add git+https://github.com/ClaudioRMalvino/physics_tui.git

# Run your app
uv run physics-tui
```

## Uninstall

### Quick Uninstall
```bash
# Utilizing pip package manager
pip uninstall physics-tui
```
```
```

```bash
# Utilizing uv package manager
uv remove physics-tui

# Or if you want to remove the entire uv project
rm -rf physics-tui-project/
```

### Development Uninstall
```bash
# In the cloned repo with venv activated
pip uninstall physics-tui

# Remove the cloned repository
cd ..
rm -rf physics_tui/
```

### Virtual Environment Uninstall
#### pip Package mananger
```bash
# Activate the virtual environment
source ~/venv/physics_tui/bin/activate  # or your venv path

# Uninstall
pip uninstall physics-tui

# Deactivate and optionally remove venv
deactivate
rm -rf ~/venv/physics_tui/
```

#### uv Package Manager
```bash
# If you created a uv project directory
cd physics-tui-project
uv remove physics-tui

# Or delete the entire project directory
cd ..
rm -rf physics-tui-project/
```

## Usage

After installation, launch the application:
```bash
physics-tui
```

Or run as a Python module:
```bash
python -m physics_TUI.app
```

### Navigation
- **Arrow Keys** - Navigate through chapters and options
- **Tab** - Switch between panels
- **Enter** - Select items and access calculators
- **Escape** - Go back in calculator screens
- **Q** - Quit application

### Calculator Features
- Select any equation to open its interactive calculator
- Leave one field empty to solve for that variable
- Automatic error checking and validation
- Clear variable descriptions and units

## Project Architecture

```
physics_tui/
├── src/physics_TUI/
│   ├── app.py              # Main TUI application (465 lines)
│   ├── base_chapter.py     # Chapter framework (41 lines)
│   ├── appearance.tcss     # TUI styling (100 lines)
│   └── chapters/           # Physics implementations
│       ├── chapter3.py     # Motion Along Straight Line (365 lines)
│       ├── chapter4.py     # 2D/3D Motion (325 lines)
│       ├── ...             # Additional chapters
│       └── chapter14.py    # Fluid Dynamics (525 lines)
├── tests/                  # Comprehensive test suite (1,450 lines)

```

**Total:** 6,882 lines of code with extensive documentation and testing

## Testing

The project includes comprehensive unit tests for all calculation methods:

```bash
# Install development dependencies
pip install -e .[dev]

# Run test suite
python -m pytest tests/

# Type checking
mypy src/physics_TUI/
```

## Code Quality Features

- **Type Hints** - Full type annotation throughout codebase
- **Error Handling** - Comprehensive validation and user-friendly errors
- **Documentation** - Extensive docstrings and comments (25% of codebase)
- **Testing** - Unit tests for all calculation methods
- **Professional Structure** - Modular design with clean separation of concerns

## Future Possibilities

While the current version is complete and fully functional, potential future enhancements could include:

- **Unit Conversion Calculator** - Convert between different measurement systems
- **Additional Physics Topics** - electromagnetism, modern physics


*Note: These are possibilities for future development, not commitments or current plans.*

## Educational Context

This project was developed as both a learning exercise in Python software development and a practical tool for physics education. It demonstrates:

- Advanced Python programming concepts
- TUI application development with Textual
- Professional software development practices
- Comprehensive testing and documentation

The project serves as both a useful physics reference tool and an example of well-structured scientific software.

## Platform Support

**Tested and working on:**
- ✅ Linux (Arch)
- ✅ macOS 
- I have not been able to test on a Windows environment, but as it is a Python program, it should function normally if all dependencies are installed.

**Best terminal experience:**
- Any modern terminal

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Textual](https://textual.textualize.io/) - Modern TUI framework
- Physics content referenced directly from [OpenStax](https://openstax.org/details/books/university-physics-volume-1) University Physics Volume 1 open source textbook for first year undergraduate students.
- Inspired by the need for accessible, interactive physics reference tools

## Contact

While active development is paused for academic commitments, feel free to:
- Open issues for bugs or suggestions
- Submit pull requests for improvements
- Use and adapt the code for educational purposes

**Note:** Response times may be limited due to academic commitments, but the project remains open for community contributions and use.

---
