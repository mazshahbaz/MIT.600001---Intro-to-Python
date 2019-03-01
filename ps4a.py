# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    n=len(sequence)
    out = []
    step = 1
#    for car in sequence:
#        seq_list.append(car)
    if len(sequence)==1:
        out=sequence
        print('this is out', out)
        return out
    else:
        for letter in sequence:
            new_seq = sequence[step:]
            print('new seq  ' + new_seq)
            for car in new_seq:
                perm = car + str(get_permutations(new_seq))
                print('this is a perm for letter:  ' , car, ' for sequence:  ', new_seq, 'perm ----> ', perm)
                output = [perm]
                print (output)
            step+= 1
    
get_permutations('abc')    


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

