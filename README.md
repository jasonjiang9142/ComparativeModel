# Comparative Model

**Description:** This is a Comparative model program that calculates the similarities between 2 sources of text using the Naïve Bayes Probability Model 

**1. Overview:**

This program will consist: 
- A `Parameter` section that includes functions to modify words 
- The `TextModel` class blueprint for objects that model a body of text
- A `Testing` sections that serves to test the program
--- 

**2. Program Specifications:**

- **Input Format:** A set of TXT files, each TXT file will include a sample excerpt from a book written by a specific author 

- **Output Format:** The program will print out a sentence referencing which author the sample source is most likely to have come from 
---

#### **Code Specifications:**
A `Parameter` section that includes functions to modify words 
- **compare_dictionaries(d1, d2):** This method compares two dictionary of texts
  
- **clean_text(txt):** This method remove the punctuations in a string of text
  
- **remove_prefix(s):** This method remove the prefix of the word

- **remove_suffix(s):** This method removes the suffix of the word
  
- **stem(s):** This method returns the stem of s

The `TextModel` class blueprint for objects that model a body of text
- **__init__(self, model_name):** This method constructs a new TextModel object by accepting
        a string model_name as a parameter and
        initializing the following three attributes:
  
- **__repr__(self):** This method adds a string of text s to the model by augmenting the feature
        dictionaries defined in the constructor.
  
- **add_file(self, filename):** This method adds all of the text in the file identified by filename to the model.

- **save_model(self):** This method saves the TextModel object self by writing its various feature dictionaries to files
  
- **read_model(self):** This method reads the stored dictionaries for the called TextModel object from their files
        and assigns them to the attributes of the called TextModel
  
- **similarity_scores(self, other):** This method computes and returns a list of log similarity scores measuring the similarity of self and other – one score for each type of feature
  
- **classify(self, source1, source2):** This method compares the called TextModel object (self) to two other “source”
        TextModel objects (source1 and source2) and determines which
        of these other TextModels
        is the more likely source of the called TextModel.
---

**4. Example:**

Below is an example testing the program: 
Function name: `def test():`
```
def test():
  source1 = TextModel('rowling')
    source1.add_file('jkrowlingbook1.txt')

    source2 = TextModel('shakespear')
    source2.add_file('williamss.txt')

    mystery = TextModel('mystery')
    mystery.add_file('textmodel.txt')
    mystery.classify(source1, source2)

```

**5. Usage/Installation:**

- **1: Clone Repository:** 
  ```
  git clone https://github.com/jasonjiang9142/ComparativeModel.git
  ```

- **2: In terminal, try running the command** 
  ```
  test()
  ```


