from matplotlib import pyplot as plt

delta_t = 1  # Время шага
desired_h = 7  # Желаемая высота
total_time = 50  # Общее время полета
conditions = [
    desired_h + 7,
    desired_h - 4,
]  # Начальные состояния


# Функция принятия решения
def decision_function(_h, _desired_h):
    return 1 if _h <= _desired_h else -1


# Измененный код для построения графиков
plt.figure(figsize=(12, 6))
plt.axhline(y=desired_h, color='r', linestyle='--', label="Желаемая высота")
plt.title("Моделирование системы автоматического контроля высоты")
plt.xlabel('Time (t)')
plt.ylabel('Height (y(t))')
plt.legend()
plt.grid(True)

for h_initial in conditions:
    h = h_initial
    time_points = list(range(0, total_time+1, delta_t))  # Координаты X
    height_points = []  # Координаты Y

    for t in time_points:
        height_points.append(h)
        h += delta_t * decision_function(h, desired_h)  # Расчет новой высоты

    plt.plot(time_points, height_points)

plt.show()
