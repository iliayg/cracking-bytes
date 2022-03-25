n = 0
chunksize = 32
with open("2.txt", "r") as file:
    for line in file.read().split():
        n += 1
        chunk = [line[i:i+chunksize] for i in range(0, len(line), chunksize)]
        for i, ch in enumerate(chunk):
            count = chunk.count(ch)
            if count > 1:
                print(n, i, ch)
