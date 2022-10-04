class Read:
    def __init__(self, filename):
        with open(filename, 'r') as textfile:
            self.text = textfile.read()

    def letters_num(self):
        count = 0
        for char in self.text:
            if char.isalpha():
                count += 1
        return count

    def words_num(self):
        count = self.text.count(' ')
        if count == 0 and self.text[1].isalpha():
            count = 1
        return count + 1

    def sent_num(self):
        count = self.text.count('.')
        if count == 0 and self.text[1].isalpha():
            count = 1
        return count


file = Read('data.txt')
print('Letters count:', file.letters_num(), '\nWords count:', file.words_num(), '\nSentences count:', file.sent_num())
