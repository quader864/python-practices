import math

def get_func(ls):
    def square(a):
        return a * a

    def circle(r):
        return math.pi * (r ** 2)

    def rectangle(a, b):
        return a * b

    def triangle(h, b):
        return (h * b) / 2

    # دیکشنری برای نگاشت اسم شکل به تابع مربوطه
    func_map = {
        'square': square,
        'circle': circle,
        'rectangle': rectangle,
        'triangle': triangle
    }

    # ساخت لیست از توابع مورد نیاز به ترتیب ورودی
    return [func_map[name] for name in ls]
