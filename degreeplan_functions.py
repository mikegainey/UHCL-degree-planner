from degreeplan_data import * # imports coursecatalog, corereq, and majorreq

coursestaken = {"MATH 2413"} # why do I need this?

def prerequisites_met(course, coursestaken=coursestaken): # coursestaken could be removed because it is global
    '''Given a proposed course and a list of courses taken, 
       return True if the course's prerequisites have been met.
       prerequisites_met(course : str, coursestaken : set) -> bool
       * Informally tested: seems to work
    '''
    prerequisites = coursecatalog[course][1]     # get the set of prerequisites for the course

    for p in prerequisites:       # check each prerequistite
        if p not in coursestaken: # if a prerequisite is not in coursestaken
            return False          # return False

    return True                   # all prerequisites were in coursestaken


def LLCcomplete(coursestaken=coursestaken, LLC=LLC):
    '''Given a set of coursestaken and the set of LLC, return True if the LLC is complete.
       LLCcomplete(coursestaken : set, LLC : set) -> bool
    '''
    return LLC <= coursestaken # True if every element of LLC issubset of coursestaken


def possibilities(coursestaken=coursestaken,
                  corereq=corereq, majorreq=majorreq,CSelectives=CSelectives,
                  langPhilCulture=langPhilCulture, creativeArts=creativeArts,
                  socialScience=socialScience):

    # possibilities will eventually be all possible courses that can be taken
    # start with: corereq | majorreq | langPhilCulture | creativeArts | socialScience | CSelectives
    possibilities = corereq | majorreq | langPhilCulture | creativeArts | socialScience | CSelectives

    # remove coursestaken from possibilities
    possibilities -= coursestaken

    # remove courses if prerequisitives have not been met
    possibilities = { p for p in possibilities if prerequisites_met(p)}
    
    # remove ULC if LLC not complete
    if not LLCcomplete:      # if LLC is not complete
        possibilities -= ULC # remove ULC

    # if langPhilCulture requirement met (3 hours), remove all langPhilCulture courses from possibilities
    if len(langPhilCulture & coursestaken) > 0: # if the intersection of langPhilCulture and coursestaken is greater than zero
        possibilities -= langPhilCulture        # remove all langPhilCulture courses from the possibilities list

    # if creativeArts requirement met (3 hours), remove all creativeArts courses from possibilities
    if len(creativeArts & coursestaken) > 0: # if the intersection of creativeArts and coursestaken is greater than zero
        possibilities -= creativeArts        # remove all creativeArts courses from the possibilities list
    
    # if socialScience requirement met (3 hours), remove all socialScience courses from possibilities
    if len(socialScience & coursestaken) > 0: # if the intersection of socialScience and coursestaken is greater than zero
        possibilities -= socialScience        # remove all socialScience courses from the possibilities list

    return possibilities

