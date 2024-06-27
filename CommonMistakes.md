1) for maps always use ``x in map`` or ``x not in map``
2) for a binary search or similar algo use ``(start+end)//2``
3) ```int(int(first)/int(second))`` does return always truncate to Zero while ``(start+end)//2`` would always truncate down ``-3/2 = -2(-1.5)``
4) to check if a string is a number you can do ``i.isnumeric()``


-----
List - a mutable type
Let's try to modify the list that was passed to a method:
```
    def try_to_change_list_contents(the_list):
        print('got', the_list)
        the_list.append('four')
        print('changed to', the_list)

    outer_list = ['one', 'two', 'three']

    print('before, outer_list =', outer_list)
    try_to_change_list_contents(outer_list)
    print('after, outer_list =', outer_list)
    Output:

    before, outer_list = ['one', 'two', 'three']
    got ['one', 'two', 'three']
    changed to ['one', 'two', 'three', 'four']
    after, outer_list = ['one', 'two', 'three', 'four']
```
Since the parameter passed in is a reference to outer_list, not a copy of it, we can use the mutating list methods to change it and have the changes reflected in the outer scope.

Now let's see what happens when we try to change the reference that was passed in as a parameter:

def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)
Output:

before, outer_list = ['we', 'like', 'proper', 'English']
got ['we', 'like', 'proper', 'English']
set to ['and', 'we', 'can', 'not', 'lie']
after, outer_list = ['we', 'like', 'proper', 'English']
Since the the_list parameter was passed by value, assigning a new list to it had no effect that the code outside the method could see. The the_list was a copy of the outer_list reference, and we had the_list point to a new list, but there was no way to change where outer_list pointed.

String - an immutable type
It's immutable, so there's nothing we can do to change the contents of the string

Now, let's try to change the reference

def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)

outer_string = 'It was many and many a year ago'

print('before, outer_string =', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string =', outer_string)
Output:

before, outer_string = It was many and many a year ago
got It was many and many a year ago
set to In a kingdom by the sea
after, outer_string = It was many and many a year ago
Again, since the the_string parameter was passed by value, assigning a new string to it had no effect that the code outside the method could see. The the_string was a copy of the outer_string reference, and we had the_string point to a new string, but there was no way to change where outer_string pointed.

I hope this clears things up a little.

EDIT: It's been noted that this doesn't answer the question that @David originally asked, "Is there something I can do to pass the variable by actual reference?". Let's work on that.

How do we get around this?
As @Andrea's answer shows, you could return the new value. This doesn't change the way things are passed in, but does let you get the information you want back out:

def return_a_whole_new_string(the_string):
    new_string = something_to_do_with_the_old_string(the_string)
    return new_string

# then you could call it like
my_string = return_a_whole_new_string(my_string)
If you really wanted to avoid using a return value, you could create a class to hold your value and pass it into the function or use an existing class, like a list:

def use_a_wrapper_to_simulate_pass_by_reference(stuff_to_change):
    new_string = something_to_do_with_the_old_string(stuff_to_change[0])
    stuff_to_change[0] = new_string

# then you could call it like
wrapper = [my_string]
use_a_wrapper_to_simulate_pass_by_reference(wrapper)

do_something_with(wrapper[0])