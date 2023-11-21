import matplotlib.pyplot as plt


def build_func(c1, c2, x1, y1, x2, y2):
    def wrap(x):
        term1 = (1 / c1) * ((x - x1) / ((x - x1)**2 + y1**2)**0.5)
        term2 = (1 / c2) * ((x - x2) / ((x - x2)**2 + y2**2)**0.5)
        return term1 + term2
    return wrap


def find_optimal_x(c1, c2, x1, y1, x2, y2):
    func = build_func(c1, c2, x1, y1, x2, y2)

    lv, rv = min(x1, x2), max(x1, x2)
    cur_x = (rv + lv) / 2

    while True:
        cur_v = func(cur_x)
        if abs(cur_v) < 0.0000001:
            return cur_x

        if cur_v > 0:
            rv = cur_x
        else:
            lv = cur_x

        cur_x = (rv + lv) / 2


def show_graph(x, c1, c2, x1, y1, x2, y2):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the points and lines
    ax.plot([x1, x], [y1, 0], 'bo-')  # blue line from (x1, y1) to (0, 0)
    ax.plot([x, x2], [0, y2], 'ro-')  # red line from (0, 0) to (x2, y2)

    # Annotate points
    ax.text(x1, y1, f'({x1}, {y1})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    ax.text(x2, y2, f'({x2}, {y2})', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
    ax.text(x, 0, f'({x}, 0)', fontsize=12, verticalalignment='top', horizontalalignment='right')
    ax.text(0, -0.1, f"Скорость по земле: {c1}\nСкорость по воде: {c2}", transform=ax.transAxes, ha="left", va="center")

    # Set labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Визуализация спасения')

    # Set the grid and show the plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()


def main():
    c1, c2 = 5, 1
    x1, y1 = 10, -10
    x2, y2 = 100, 50

    x = find_optimal_x(c1, c2, x1, y1, x2, y2)
    show_graph(round(x, 4), c1, c2, x1, y1, x2, y2)


if __name__ == "__main__":
    main()

