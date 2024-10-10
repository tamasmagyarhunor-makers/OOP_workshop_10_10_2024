# OOP workshop 10 10 2024


## Exercise 1:
###### Refactor this code in the link using the OOP principles: https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/python

## Exercise 2:
###### Please write a paragraph listing some positives and some negatives about the following code. Then refactor this to apply the OOP Principles. Once you're done, send me a DM with a link to your repo and I will review it and give you feedback on it.
```python
    # type should be either of the following: "ball pen", "ink pen", "pencil"
    class WriteObject():
        def __init__(self, type):
            self.type = type

    class Notebook():
        def __init__(self, write_object):
            self.write_object = write_object
        
        def write(self, text):
            if self.write_object.type == "ball pen":
                self.__turn_on(self.write_object)
                return text
            elif self.write_object.type == "ink pen":
                if self.__has_enough_ink(self.write_object):
                    return text
                else:
                    self.__refill_ink(self.write_object)
                    return text
            elif self.write_object.type == 'pencil':
                if self.__sharp_enough(self.write_object):
                    return text
                else:
                    self.__sharpen(self.write_object)
                    return text
            else:
                raise Exception("need some write object to write")
                
        # private methods
        def __sharpen(write_object):
            # sharpen the pencil
            pass

        def __refill_ink(write_object):
            # refill ink
            pass

        def __sharp_enough(write_object):
            # check if pencil is sharp enough
            pass


        def __has_enough_ink(write_object):
            # check if ink pen it has enough ink
            pass

        def __turn_on(write_object):
            #press the top of the ball pen to turn it on
            pass
    
    pencil = WriteObject('pencil')

    notebook = Notebook(pencil)
    notebook.write('hi my dear calendar')
```