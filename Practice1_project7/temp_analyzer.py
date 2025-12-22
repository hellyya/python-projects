def parse_temps(raw): 
    parts= raw.split(",")
    temps = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        try:
            temps.append(float(p))
        except ValueError:
            print(f"skipping invalid value: {p}")
    return temps

def c_to_f(c):
    return c * 9 / 5 + 32