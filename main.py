import threading

numbers = []
input_done = threading.Event()

def input_thread():
    global numbers
    while True:
        line = input("Введіть число (або Enter для завершення): ")
        if line.strip() == "":
            break
        try:
            num = float(line)
            numbers.append(num)
        except ValueError:
            print("Будь ласка, введіть число.")
    input_done.set()

def sum_thread():
    input_done.wait()
    total = sum(numbers)
    print(f"\nСписок чисел: {numbers}")
    print(f"Сума чисел: {total}")

def avg_thread():
    input_done.wait()
    if numbers:
        avg = sum(numbers) / len(numbers)
        print(f"Середнє арифметичне: {avg}")
    else:
        print("Список порожній, неможливо обчислити середнє.")

t1 = threading.Thread(target=input_thread)
t2 = threading.Thread(target=sum_thread)
t3 = threading.Thread(target=avg_thread)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nРоботу завершено.")
