
# read a file that is CP-1252 encoded and print its contents as UTF-8
# with open('q-unicode-data-2/data1.csv', 'r', encoding='cp1252') as f:
#     content = f.read()
#     print(content)

# read a file that is UTF- encoded and print its contents as UTF-8
# with open('q-unicode-data-2/data2.csv', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)

# read a file that is UTF-16 encoded and print its contents as UTF-8
# with open('q-unicode-data-2/data3.txt', 'r', encoding='utf-16') as f:
#     content = f.read()
#     print(content)

#Sum up all the values where the symbol matches „ OR • OR ” across all three files.
total_sum = 0  
symbols_to_match = {'„', '•', '”'}
file_paths = [
    ('q-unicode-data-2/data1.csv', 'cp1252'),
    ('q-unicode-data-2/data2.csv', 'utf-8'),
    ('q-unicode-data-2/data3.txt', 'utf-16')
]
for file_path, encoding in file_paths:
    with open(file_path, 'r', encoding=encoding) as f:
        for line in f:
            delimiter = ','
            if "," not in line:
                delimiter = "\t"
            parts = line.strip().split(delimiter)
            if len(parts) >= 2:
                symbol = parts[0].strip()
                try:
                    value = float(parts[1].strip())
                    if symbol in symbols_to_match:
                        print(f"Matched symbol: {symbol} with value: {value}")
                        total_sum += value
                except ValueError:
                    continue
print(f'Total sum of matched symbols: {total_sum}')

