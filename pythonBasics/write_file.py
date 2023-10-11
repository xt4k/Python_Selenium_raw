with open("new_file.txt",'r') as file_reader:
    content = file_reader.readlines()
    reversed(content)
    file_reader.close()

    with open("new_file.txt",'w') as file_writer:
        for line in reversed(content):
            file_writer.write(line)

        file_writer.close()
