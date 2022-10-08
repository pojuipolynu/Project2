class Read:
    def __init__(self, filename):
        self.text = filename

    def letters_num(self):
        count = 0
        self.text.seek(0)
        for line in self.text:
            count += len(line)
        return count

    def words_num(self):
        count = 0
        self.text.seek(0)
        for line in self.text:
            k = line.split(' ')
            count += len(k)
        return count

    def sent_num(self):
        count = 0
        self.text.seek(0)
        for line in self.text:
            k = line.split('.')
            count += len(k)
        return count


text = open('data.txt')
file = Read(text)
print('Letters count:', file.letters_num(), '\nWords count:', file.words_num(), '\nSentences count:', file.sent_num())
text.close()
