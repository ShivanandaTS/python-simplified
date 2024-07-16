# Generator: It is used for creating sequences, without the actual collection of elements.
# Lazy execution: It yields the next item in the sequence 'on-demand' basis.
# No matter the size of elements to be yielded from the generator, the size of the generator remains constant.
# generators can be used to create a infinite sequences as well

def gen_z():
    '''This function returns years starting from 2000'''
    year = 2000
    while True:
        yield year
        year += 1

gen_z_years = gen_z()
for i in range(5):
    print(next(gen_z_years))

# Printing sizes of two generators with huge difference in their range.
import sys
print(sys.getsizeof(range(10)))
print(sys.getsizeof(range(999999999999999999999999))) # both of these generators will be of same bytes.
# By the way range() is an in-built python generator

# Checking my custom made infinite sequence generator size; out of curiosity :D
print(sys.getsizeof(gen_z_years))