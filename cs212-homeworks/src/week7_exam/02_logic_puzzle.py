"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

*1. The person who arrived on Wednesday bought the laptop.
*2. The programmer is not Wilkes.
*3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
*4. The writer is not Minsky.
*5. Neither Knuth nor the person who bought the tablet is the manager.
*6. Knuth arrived the day after Simon.
*7. The person who arrived on Thursday is not the designer.
*8. The person who arrived on Friday didn't buy the tablet.
*9. The designer didn't buy the droid.
*10. Knuth arrived the day after the manager.
*11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
*12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    days_of_week = monday, tuesday, wednesday, thursday, friday = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(days_of_week))
    arrivals = next((Hamming, Knuth, Minsky, Simon, Wilkes)
                for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderings
                for (_, programmer, designer, writer, manager) in orderings
                for (laptop, iphone, tablet, droid, _) in orderings
                if laptop is wednesday and programmer is not Wilkes and ((programmer is Wilkes and droid is Hamming) or (programmer is Hamming and droid is Wilkes))
                if Knuth-manager == 1 and writer is not Minsky and Knuth is not manager and designer is not droid 
                if tablet is not manager and Knuth-Simon == 1 and designer is not thursday and tablet is not friday 
                if (Wilkes is writer and laptop is monday) or (Wilkes is monday and laptop is writer) and (iphone is tuesday or tablet is tuesday)
                )
    names = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
    arrivalsAndNames = zip(arrivals, names)
    arrivalsAndNames.sort()
    _, sortedNames = zip(*arrivalsAndNames)
    return list(sortedNames)

print logic_puzzle()