length = int(input())
width = int(input())
height = int(input())
filled_volume_percent = float(input())

volume = length * width * height / 1000
free_volume = volume * (1 - filled_volume_percent / 100)
print(free_volume)