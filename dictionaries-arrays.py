def dictionary_basics():
    phonebook = {'Chris': '555-1111',
                 'Katie': '555-2222',
                 'Joanne': '555-333'}


    print(phonebook['Chris'])

    if 'Katie' in phonebook:
        print("Katie's number:", phonebook['Katie'])

    print(phonebook.get('Andy', 'Entry not found'))
dictionary_basics()


def dictionary_modification():
    pb= phonebook = {'Chris': '555-1111',
                 'Katie': '555-2222',
                 'Joanne': '555-333'}

    pb['Sarah']= '555-444'
    pb['Chris']= '555-999'


    if 'Katie' in pb:
        del pb['Katie']

    print(pb)

dictionary_modification()


def dictionary_iteration():
    pb = {'Chris': '555-1111',
                 'Katie': '555-2222',
                 'Joanne': '555-333'}

    for key in pb:
        print(key)

        for key, value in pb.items():
            print(f{key}: {value})

dictionary_iteration()



def dictionary_methods_demo():
     pb = {'Chris': '555-1111',
                 'Katie': '555-2222',
                 'Joanne': '555-333'}
     print(pb.get('Tom', 'Not found'))

     print(len(pb))

     pb.clear()
     print(pb)
dictionary_methods_demo():




def dictionary_with_lists():
    test_scores={'Kayla': [88,92,100],
                 'Luis': [95, 74, 81],
                 'Sophie': [72, 88, 91]}

    print("Kayla's scores:", test_scores['Kayla'])

    for student, scores in test_scores.item():
        avg= sum(scores)/ len (scores)
        print(f'{student}: Avg= {avg:.2f}')
dictionary_with_lists()





def sets_basics():
    colors = {'red', 'green', 'blue'}
    colors.add ('yellow')
    colors.remove('green')

    set1= {1,2,3}
    set2={3,4,5,}

    print("Union:", set1|set2)
    print("Intersection:", set1 & set2)
    print("Difference:", set1-set2)

sets_basics()

import pickle


def save_data():
    data= {'name': 'Alice', 'age':30}
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

def load_data():
    with open('data.pkl', 'rb') as file:
        data= pickle.load(file)
        print(data)

save_data()
load_data()



    
