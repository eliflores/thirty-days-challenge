class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0

    def compute_difference(self):
        number_of_elements = len(self.__elements)
        if number_of_elements == 0:
            return 0

        if number_of_elements == 1:
            return 0

        min_number = self.__elements[0]
        max_number = self.__elements[0]
        for i in self.__elements[1:]:
            if i < min_number:
                min_number = i
            if i > max_number:
                max_number = i
        self.maximum_difference = abs(max_number - min_number)


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.compute_difference()
print(d.maximum_difference)
