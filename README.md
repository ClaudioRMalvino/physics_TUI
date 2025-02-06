# Physics TUI Project Structure

## WORK IN PROGRESS

## Project Overview
- **Name**: physics_tui
- **Description**: A Terminal User Interface (TUI) for physics reference and calculations
- **Purpose**: Educational tool for physics students
- **Main Features**:
  - Interactive TUI
  - Physics equations and definitions
  - Calculators for various physics problems
  - Chapter-based organization

## Directory Structure
```
physics_tui/
├── src/
│   └── physics_tui/
│       ├── __init__.py
│       ├── app.py                # Main TUI application
│       ├── base_chapter.py       # Base class for chapters
│       └── chapters/             # Individual chapter modules
│           ├── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_chapters/
├── setup.py
├── README.md
└── LICENSE
```

## Core Components

### 1. Base Chapter Class
- Location: `src/physics_tui/base_chapter.py`
- Purpose: Template for all physics chapters
- Key Features:
  - Equation storage
  - Definition storage
  - Basic calculation methods

### 2. Chapters
1. One Dimensional Motion
2. Two Dimensional Motion
3. Newton's Laws of Motion 
4. Work and Kinetic Energy
5. Potential Energy and Conservation of Energy
6. Linear Momentum & Collisions
7. Fixed Axis Rotation
8. Angular Momentum 
9. Static Equilibrium and Elasticity 
10. Gravitation
11. Fluid Mechanics
12. Oscillations
13. Waves
14. Sounds

### 3. TUI Components
- Location: `src/physics_tui/app.py`
- Screens:
  - Main menu
  - Chapter view
  - Calculator view
- Navigation:
  - Chapter selection
  - Topic browsing
  - Calculator access

## Dependencies
```python
# setup.py dependencies
install_requires=[
    "textual>=0.38.1",    # TUI framework
    "numpy>=1.24.0",      # Numerical computations
    "scipy>=1.10.0"       # Scientific computations
]
```