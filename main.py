string = input("Введите слова в строку для изменений 1-ого и последнего символа через пробел: ") # Получаем строку слов от пользователя через ввод

lines = string.split(' ') # Разбиваем строку на слова, используя пробелы как разделители
modified_lines = [] # Создаем пустой список для хранения модифицированных слов

for line in lines: # Перебираем каждое слово в списке lines
    
    if len(line) > 1: # Если длина слова больше 1 символа (чтобы избежать изменения однобуквенных слов)
        
        modified_line = line[-1] + line[1:-1] + line[0] # Меняем первый и последний символы местами
        
    else: # Если условие не верно, выполняется блок_инструкций ниже
        
        modified_line = line # Приравниваем к modified_line, оставляя его как есть
        
    modified_lines.append(modified_line) # Добавляем модифицированное слово в список modified_lines
    
modified_text = ' '.join(modified_lines) # Объединяем модифицированные слова в строку, разделяя их пробелами

print(f"Измененный текст: {modified_text}") # Выводим модифицированную строку
