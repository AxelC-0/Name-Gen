import math
import random
import time





def main():
    
    version = ".2"
    print (f"Hello! Welcome to the Name GEN v{version}")
    print ("----====----====----====----====----====")
    ask = input ("Would you like to randomly GENERATE a name, or CONSTRUCT one? >> ").strip().lower()

    if ask == "generate":

        Generate.from_the_letters()
    elif ask == "construct":

        secask = input ("Cool! There are a few opitons when it  comes to starting. \n \nYou can start with a NOUN-VERB, or an ADJ-NOUN base?"
                        "Which would you like to start with? " 
                        "NV or AN? >> ")

        if secask == "nv":
            Construct.age(Construct.noun_verb()) 


class Generate():

    def from_the_letters():

        """Will generate names based on vowel and consonant relationships letter by letter,
           without using existing or provided words

            :param name: the list holding letters while name is constructed
            :type name: str
            
            :return from_letters_name: The generated name
            :rtype: str
        """

        # TO DO: Need to define which letters are allowed to appear near eachother
            # Vowels that can appear together: A:I, A:E, A:U | E:A, E:E, E:I, E:O, E:U | 
            #                                  I:A, I:E, I:O, I:U | O:A, O:I, O:O, O:U | 
            #                                  U:A, U:E, U:I, U:O, U:U
            # Consonant inclusions: B:H, B:J, B:K, B:L, B:M, B:N, B:R, B:V, B:Y, B:Z
            # Consonant exclusions:
            #                      B:C, B:D, B:G, B:P, B:Q, B:S, B:T, B:W, B:X, 
            # General Rules: Use double letters springly (less weight)
            #                Y and H add flavor (less weight)

        Vowels = ["A", "E", "I", "O", "U"]
        Consonants = ["B", "C", "D", "F", "G", "J", "H", "K", "L", "M", "N", "P", "Q", "R", "S", "T", 
                      "V", "W",  "X", "Y", "Z"]
        Holding = []
        Length = random.randint(2, 8)
        print (Length)
        print (random.randrange(2, 8))

        # random number to determine positioning of vowels and consonants, 
        # then random number deciding which letters its going to place there
        randomlength = random.randrange(2, 8)
        word_skel = []
        for idx in range(randomlength):
            word_skel.append(random.randrange(1, 10))
            print (word_skel)
        for idx in range(len(word_skel)):
            if idx % 2 != 0:
                word_skel[idx] = Consonants[random.randrange(1, 21)]
            else:
                word_skel[idx] = Vowels[random.randrange(1, 5)]
        
        word = "".join(word_skel)
        print (word)



class Construct():

    def noun_verb():
        
        
        """Will construct names based on a noun-verb relationship
        
        :param noun: nouns that will be used for the ocnstruction
        :type noun: list
        
        :param verb: verbs that will be used for the construction
        :type verb: list
        """


        nouns = ["house", "tree", "book", "computer", "phone", "table", "chair",
    "man", "woman", "child", "friend", "teacher", "student", "city", "country", "school", "job",
    "water", "food", "music", "movie", "game", "apple", "banana", "shirt", "shoe", "bag",
    "money", "time", "day", "night", "year", "road", "river", "mountain", "ocean", "sun",
    "moon", "star", "door", "window", "room", "family", "team", "store", "train", "plane", 
    "fall", "helm", "reach", "mere", "forge", "rock", "holdt", "run", "watch", "march",
    "shade", "wood", "vale", "water", "haven", "field", "rest", "hold", "pine", "moor",
    "deep", "port", "vale", "watch", "hollow", "spear", "shade", "gate", "mere", "spire",
    "moor", "reach", "watch", "mere", "wrath", "top", "rest", "stone", "reach", "field", "Wyrm", "Sky", "Crow", "Blight"]
        
        verbs = ["run", "walk", "eat", "drink", "sleep", "write", "read", "speak", "listen", "see",
    "hear", "make", "do", "go", "come", "have", "be", "know", "think", "take",
    "give", "work", "play", "study", "learn", "drive", "ride", "buy", "sell", "build",
    "cook", "clean", "watch", "open", "close", "start", "stop", "jump", "sit", "stand",
    "grow", "draw", "paint", "sing", "dance", "teach", "help", "move", "throw", "catch", 
    "Dagger", "Wind", "Storm", "Shadow", "Iron", "Raven", "Frost",
    "Red", "Moon", "Drift", "Bright", "Gold", "Thorn", "Hollow",
    "Dark", "Ember", "Skull", "Mist", "Rime", "Fall", "Sun", "Brim", "Night", "Gren",
    "Oak", "Steel", "Fallow", "Howl", "Crag", "Fire", "Dust",
    "Ice", "Thunder"]
        
        #chosenNoun = nouns[random.randrange()]
        #chosenVerb = verbs[random.randrange()]
        chosenNoun = random.choice(nouns)
        chosenVerb = random.choice(verbs)
        print(chosenVerb)
        constructedWord = chosenNoun + chosenVerb
        print (constructedWord)
        return constructedWord


    def adj_noun():

        """Will construct names based on an adjective-noun relationship
        
        :param adj: adjectives that will be used for the ocnstruction
        :type adj: list
        
        :param noun: nouns that will be used for the construction
        :type noun: list
        """

    nouns = ["house", ]

    adjectives = []

    def age(constructedWord):

        """Will apply a multitude of aging effects to the name generated by previous functions 
        Changes include: 
            Conflation: Melding of similar sounds
            Simplification: Hard to pronounce sounds are removed
            Elaboration: Modifier words added to names to distinguish them from other similar names, 
                        or to add distinction in the form of adjectives
            """
        
        # Conflation:
            #if certain number:
        # planning
                    # run rng -> if certain number: it will run a letter change and select random letter combo next to eachother
        suffixes = ["hold", "moor", "mere", "heim", "dale", "burg", "stead", "wick", "thorpe",
    "by", "ford", "fell", "holm", "hurst", "ley", "combe", "den", "ton",
    "ham", "worth", "beck", "croft", "clough", "shaw", "wold", "thwaite",
    "rigg", "gate", "gill", "hollow", "kirk", "lough", "ness", "toft", "sike"]
        selection = random.randrange(0, 2)

        if selection == 0:
            modification = random.randrange(0, 3)
            index = random.randrange(len(constructedWord))
            secondIndex = index + 1
            print (index)
            print (secondIndex)
            modification = 0 # don't forget to delete this
            if modification == 0:
                # conflate

                for idx in range(len(constructedWord)):
                    if idx < len(constructedWord) - 1:
                        if constructedWord[idx] == "n" and constructedWord[idx + 1] == "b"
                        or constructedWord[idx + 1] == "p" 
                        or constructedWord[idx + 1] == "f" 
                        or constructedWord[idx + 1] == "v":
                        modifiedWord = constructedWord.replace("n", "m")
                # if similar sound?
                print ("conflate")
                print (modifiedWord)
            elif modification == 1:
            # simplifyc
                print ("Simplify")
            elif modification == 2:
            # remove
                print ("remove")
        elif selection == 1:
            suffix = random.choice(suffixes)
            constructedWord += suffix
            
            print (constructedWord)
            # elaboration            # nested if second rng run: it will decide whether it will conflate, or simplify, or remove
                    # else: it will be elaboration

            #    conflate
            #elseif different number:
            #    simplify
            #else: 
            #elaborate
        # simplification:
        # Elaboraton: Heim, Hold, Gard, Mere, Moor, etc. 

        #constructedWord = 



if __name__ == "__main__":
    main()
