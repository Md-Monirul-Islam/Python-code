''''
3. Do the same with the third program from exercise 2.
'''
import logging
def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        logging.info("Created %s." % listname)
    else:
        logging.info("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        logging.info("Added %s to %s." % (element, listname))