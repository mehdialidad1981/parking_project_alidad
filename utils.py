def format_car_list(cars):
    lines = []
    for i, c in enumerate(cars):
        entry = c[4] if c[4] else "نامشخص"
        exit_ = c[5] if c[5] else "در پارکینگ"
        lines.append(f"{i+1}. {c[0]} - {c[1]} - {c[2]} - {c[3]} | ورود: {entry} | خروج: {exit_}")
    return "\n".join(lines)
