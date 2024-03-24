import math
import os

def read_input_file(file_path):
    with open(file_path, 'r') as fp: data = fp.readlines()
    return data

def divide_data_into_chunks(data, k):
    chunks = []
    size = math.ceil(len(data) / k)
    for i in range(k):
        start = i * size
        end_index = (i + 1) * size if i < k - 1 else len(data)
        chunk = data[start:end_index]
        chunks.append(chunk)
    return chunks

def write_chunk_to_file(chunk, output_file):
    with open(output_file, 'w') as f:
        f.writelines(chunk)

def processData(chunks, k):
    for i, chunk in enumerate(chunks):
        output_file = f"chunks/chunk_{i + 1}.txt"
        write_chunk_to_file(chunk, output_file)

def main(input_file, K):
    data = read_input_file(input_file)
    chunks = divide_data_into_chunks(data, K)
    processData(chunks, K)

if __name__ == "__main__":
    input_file = 'data.txt'
    main(input_file, 20)
