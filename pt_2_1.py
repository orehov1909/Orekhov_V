import random
colors = {"Белый","Чёрный","Синий","Красный","Жёлтый"}
print(f"Возможные цвета: {', '.join(colors.keys())}")
rand_color = random.choice(list(colors.keys()))