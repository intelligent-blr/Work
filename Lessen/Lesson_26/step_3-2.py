import argparse

def main():
    parser = argparse.ArgumentParser(description="Читает входной файл и записывает содержимое в выходной.")
    parser.add_argument('--input', required=True, help='Path to input file')
    parser.add_argument('--output', required=True, help='Path to output file')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as in_file:
        data = in_file.read()

    with open(args.output, 'w', encoding='utf-8') as out_file:
        out_file.write(data)
    
    print(f"Содержимое файла '{args.input}' успешно скопировано в '{args.output}'.")


main()

# python copy_file.py --input path/to/input_file.txt --output path/to/output_file.txt
