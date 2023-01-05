import math

""" ------------------------------------------------------------ Parameters ------------------------------------------------------------ """
def compare_dictionaries(d1, d2):
    if d1 == {}:
        return -50
    else:
        score = 0
        total = 0
        for i in d1:
            total += d1[i]
        for items in d2:
            if items in d1:
                score += math.log(d1[items] / total) * d2[items]
            else:
                score += math.log(0.5 / total) * d2[items]
        return score


def clean_text(txt):
    '''takes a string of text txt as a parameter and returns a
    list containing the words in txt after it has been “cleaned”.'''

    for symbols in """.,?"'!;:""":
        txt = txt.replace(symbols, '')

    txt = txt.lower().split()

    return txt


# Part 3
# 2
# remove the prefix of the word
def remove_prefix(s):
    prefix = ['pre', 'dis', 'in', 'mis', 'anti', 'de', 'em', 'im', 'sub', 'trans', 'semi']

    for x in prefix:
        length = len(x)
        if s[:length] == x:
            s = s[length:]
            break
    return s


# removes the suffix of the word
def remove_suffix(s):
    suffix = ['ed', 'ie', 'ing', 'ion', 'ly', 'ful', 'y', 'ly', 'ic', 'ally', 'ness', 'ier']

    for x in suffix:
        length = len(x) * -1
        if s[length:] == x:
            s = s[:length]
            break
    return s


def stem(s):
    '''accepts a string as a parameter. The function should then return the stem of s'''
    if s[-1] == 's':
        s = s[:-1]
        s = remove_prefix(s)
        s = remove_suffix(s)
        if len(s) > 2:
            if s[-1] == s[-2]:
                s = s[:-1]
    else:
        s = remove_prefix(s)
        s = remove_suffix(s)
        if len(s) > 2:
            if s[-1] == s[-2]:
                s = s[:-1]

    return s




""" ------------------------------------------------------------ MOdel ------------------------------------------------------------ """

class TextModel():
    '''serve as a blueprint for objects that model a body of text
    (i.e., a collection of one or more text documents).'''

    # 1
    def __init__(self, model_name):
        '''constructs a new TextModel object by accepting
        a string model_name as a parameter and
        initializing the following three attributes:'''

        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuations = {}

        # 2

    def __repr__(self):
        '''returns a string that includes the name of the model as
        well as the sizes of the dictionaries for each feature of the text.'''

        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations)) + '\n'
        return s

    # 4
    def add_string(self, s):
        '''adds a string of text s to the model by augmenting the feature
        dictionaries defined in the constructor.'''

        # new code, take a look
        sentence_lengths_count = 0
        y = s.split(' ')
        for i in y:
            if '.' in i or '?' in i or '!' in i:
                if sentence_lengths_count in self.sentence_lengths:
                    self.sentence_lengths[sentence_lengths_count] += 1
                    sentence_lengths_count = 0
                else:
                    self.sentence_lengths[sentence_lengths_count] = 1
                    sentence_lengths_count = 0
            else:
                sentence_lengths_count += 1
        ##########################
        for i in s:
            if i in """.,?"'!;:""":
                if i not in self.punctuations:
                    self.punctuations[i] = 1
                else:
                    self.punctuations[i] += 1

        word_list = clean_text(s)

        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1

            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1

            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1

                # 5

    def add_file(self, filename):
        '''adds all of the text in the file identified by filename to the model. '''

        f = open(filename, 'r', encoding='utf8', errors='ignore')
        # f.read()
        self.add_string(f.read())
        f.close()

    # Part 2 - allow you to save and retrieve a text model in this way.
    # 1
    def save_model(self):
        ''' saves the TextModel object self by writing its various feature dictionaries to files'''

        # save the dictionaries to a file. The name should be "self.name" + "_ ..."

        f = open(str(self.name + '_' + 'words'), 'w')  # creates a new file and names it
        f.write(str(self.words))  # writes within the created file
        f.close()  # closes the file

        f = open(str(self.name + '_' + 'word_lengths'), 'w')
        f.write(str(self.word_lengths))
        f.close()

        f = open(str(self.name + '_' + 'stems'), 'w')
        f.write(str(self.stems))
        f.close()

        f = open(str(self.name + '_' + 'sentence_lengths'), 'w')
        f.write(str(self.sentence_lengths))
        f.close()

        f = open(str(self.name + '_' + 'punctuations'), 'w')
        f.write(str(self.punctuations))
        f.close()
        # 2

    def read_model(self):
        '''reads the stored dictionaries for the called TextModel object from their files
        and assigns them to the attributes of the called TextModel'''

        w = open(str(self.name + '_' + 'words'), 'r')  # opens word file
        wl = open(str(self.name + '_' + 'word_lengths'), 'r')  # open word_length file
        s = open(str(self.name + '_' + 'stems'), 'r')
        sl = open(str(self.name + '_' + 'sentence_lengths'), 'r')
        p = open(str(self.name + '_' + 'punctuations'), 'p')

        # self.words= f.read() #read Word file and assign it to variable
        w_str = w.read()  # i changed it so it doesnt call the class
        wl_str = wl.read()
        s_str = s.read()
        sl_str = sl.read()
        p_str = p.read()

        w.close()  # close both file)
        wl.close()
        s.close()
        sl.close()
        p.close()

        self.words = dict(eval(w_str))  # input variable to self.word
        self.word_lengths = dict(eval(wl_str))  # input variable to self.word
        self.stems = dict(eval(s_str))
        self.sentence_lengths = dict(eval(sl_str))
        self.punctuations = dict(eval(p_str))

    # Part 3

    def similarity_scores(self, other):
        '''computes and returns a list of log similarity scores measuring the similarity of self and other – one score for each type of feature'''

        list = []

        word_score = compare_dictionaries(other.words, self.words)
        list += [word_score]

        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        list += [word_lengths_score]

        stems_score = compare_dictionaries(other.stems, self.stems)
        list += [stems_score]

        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        list += [sentence_lengths_score]

        punctuations_score = compare_dictionaries(other.punctuations, self.punctuations)
        list += [punctuations_score]

        return list

    def classify(self, source1, source2):
        '''compares the called TextModel object (self) to two other “source”
        TextModel objects (source1 and source2) and determines which
        of these other TextModels
        is the more likely source of the called TextModel.'''

        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print('scores for', source1.name, ':', scores1)
        print('scores for', source2.name, ':', scores2)

        count1 = 0
        count2 = 0
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]:
                count1 += 1
            elif scores1[x] < scores2[x]:
                count2 += 1

        if count1 > count2:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)



""" ------------------------------------------------------------ Testing ------------------------------------------------------------ """

def test():
    """ your docstring goes here """
    source1 = TextModel('rowling')
    source1.add_file('jkrowlingbook1.txt')

    source2 = TextModel('shakespear')
    source2.add_file('williamss.txt')

    mystery = TextModel('mystery')
    mystery.add_file('textmodel.txt')
    mystery.classify(source1, source2)

test()

