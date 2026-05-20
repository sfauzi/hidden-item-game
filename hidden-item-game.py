
# ─────────────────────────────────────────────
# 1. GRID DEFINITION  (row 0 = top)
# ─────────────────────────────────────────────
GRID = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '.', '.', '#'],  # row 2 corrected: #.###..#
    ['#', '.', '.', '.', '#', '.', '#', '#'],
    ['#', 'X', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

ROWS = len(GRID)
COLS = len(GRID[0])


def find_player(grid):
    """Return (row, col) of the player 'X'."""
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 'X':
                return r, c
    raise ValueError("Player 'X' not found in grid!")


def is_walkable(grid, r, c):
    """A cell is walkable if it is inside the grid and not an obstacle."""
    return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != '#'


def navigate(grid, start_r, start_c, steps_up, steps_right, steps_down):
    """
    Walk: Up A → Right B → Down C steps.
    At every intermediate position along each leg the cell must be walkable.
    Returns a set of (row, col) reachable final positions (on clear-path cells).
    """
    # --- Phase 1: move Up (row decreases) ---
    positions_after_up = set()
    r, c = start_r, start_c
    ok = True
    for _ in range(steps_up):
        r -= 1
        if not is_walkable(grid, r, c):
            ok = False
            break
    if ok:
        positions_after_up.add((r, c))

    # --- Phase 2: move Right (col increases) ---
    positions_after_right = set()
    for (r0, c0) in positions_after_up:
        r, c = r0, c0
        ok = True
        for _ in range(steps_right):
            c += 1
            if not is_walkable(grid, r, c):
                ok = False
                break
        if ok:
            positions_after_right.add((r, c))

    # --- Phase 3: move Down (row increases) ---
    probable_locations = set()
    for (r0, c0) in positions_after_right:
        r, c = r0, c0
        ok = True
        for _ in range(steps_down):
            r += 1
            if not is_walkable(grid, r, c):
                ok = False
                break
        if ok and grid[r][c] in ('.', 'X'):   # must land on a clear path
            probable_locations.add((r, c))

    return probable_locations


def display_grid(grid, highlights=None):
    """
    Print the grid.
    highlights : set of (row, col) to mark with '$'
    """
    if highlights is None:
        highlights = set()

    print()
    for r in range(ROWS):
        row_str = ""
        for c in range(COLS):
            if (r, c) in highlights:
                row_str += '$'
            else:
                row_str += grid[r][c]
        print("  " + row_str)
    print()


def main():
    print("=" * 45)
    print("        *** HIDDEN ITEM GAME ***")
    print("=" * 45)

    # Show original grid
    print("\n[GRID LAYOUT]")
    display_grid(GRID)

    # Find player start
    start_r, start_c = find_player(GRID)
    print(f"  Player 'X' starts at → row {start_r}, col {start_c}  (0-indexed)")

    # ── Get navigation input ──────────────────
    print("\n[NAVIGATION INPUT]")
    print("  Enter number of steps for each direction.")
    print("  (Press Enter to use example: Up=3, Right=4, Down=2)\n")

    try:
        raw_a = input("  Steps UP    (A): ").strip()
        raw_b = input("  Steps RIGHT (B): ").strip()
        raw_c = input("  Steps DOWN  (C): ").strip()

        steps_up    = int(raw_a) if raw_a else 3
        steps_right = int(raw_b) if raw_b else 4
        steps_down  = int(raw_c) if raw_c else 2
    except ValueError:
        print("\n  ⚠  Invalid input – using defaults: Up=3, Right=4, Down=2")
        steps_up, steps_right, steps_down = 3, 4, 2

    print(f"\n  Route: Up {steps_up} → Right {steps_right} → Down {steps_down}")

    # ── Navigate ─────────────────────────────
    probable = navigate(GRID, start_r, start_c, steps_up, steps_right, steps_down)

    # ── Results ──────────────────────────────
    print("\n" + "=" * 45)
    print("  PROBABLE ITEM LOCATION(S)")
    print("=" * 45)

    if probable:
        for (r, c) in sorted(probable):
            print(f"  → (row={r}, col={c})")
    else:
        print("  ✗ No reachable clear-path cell found with those steps.")
        print("    The path may be blocked by obstacles (#).")

    # ── Bonus: display grid with '$' markers ─
    print("\n[GRID WITH PROBABLE LOCATIONS MARKED AS '$']")
    display_grid(GRID, highlights=probable)

    print("=" * 45)
    print("  Good luck finding the hidden item! 🎯")
    print("=" * 45)


if __name__ == "__main__":
    main()