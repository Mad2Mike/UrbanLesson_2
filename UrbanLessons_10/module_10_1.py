import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(int(word_count)):
            time.sleep(0.1)
            file.write(str(f"Какое-то слово № {i+1}\n"))
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time.time()
execution_time = end_time - start_time
print(f"Работа потоков: {execution_time} секунд")

start_time = time.time()
threads = []
for i, (count, filename) in enumerate([(10, "example5.txt"),
                                        (30, "example6.txt"),
                                        (200, "example7.txt"),
                                        (100, "example8.txt")]):
    thread = threading.Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

end_time = time.time()
execution_time= end_time - start_time
print(f"Работа потоков: {execution_time} секунд")