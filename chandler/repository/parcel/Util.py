"""
Utility functions for displaying repository contents
"""

__revision__  = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2003 Open Source Applications Foundation"
__license__   = "http://osafoundation.org/Chandler_0.1_license_terms.htm"

import repository

def PrintItem(uri, rep, level=0):
    """
    Given a uri, display its info along with all its children recursively

    Example:  PrintItem("//Schema", rep)

    """
    for i in range(level):
        print " ",
    item = rep.find(uri)
    print "%s (Kind: %s)" % (uri, item.kind.getItemPath() )

    # For Kinds, display their attributes (except for the internal ones
    # like notFoundAttributes:
    if "//Schema/Core/Kind" == str(item.kind.getItemPath()):
        for i in range(level+2):
            print " ",
        print "attributes:"

        displayedAttrs = { }
        for (name,attr) in item.kind.iterAttributes():
            if name == "attributes" or \
               name == "notFoundAttributes" or \
               name == "inheritedAttributes":
                continue
            displayedAttrs[name] = attr

        keys = displayedAttrs.keys()
        keys.sort()
        for key in keys:
            for k in range(level+4):
                print " ",
            print "%s %s" % ( key, displayedAttrs[key].getItemPath() )

    displayedAttrs = { }
    for (name, value) in item.iterAttributeValues():
        displayedAttrs[name] = value

    keys = displayedAttrs.keys()
    keys.sort()
    for name in keys:
        value = displayedAttrs[name]
        t = type(value)

        if name == "attributes" or \
           name == "notFoundAttributes" or \
           name == "inheritedAttributes" or \
           name == "kind":
            pass

        elif t == list \
         or t == repository.item.PersistentCollections.PersistentList:
            for i in range(level+2):
                print " ",

            print "%s: (list)" % name
            for j in value:
                for k in range(level+4):
                    print " ",
                print j

        elif t == repository.item.PersistentCollections.PersistentDict:
            for i in range(level+2):
                print " ",

            print "%s: (dict)" % name
            for key in value.keys():
                for k in range(level+4):
                    print " ",
                print "%s:" % key, value[key]

        elif t == repository.persistence.XMLRepositoryView.XMLRefDict \
         or t == repository.item.ItemRef.TransientRefDict:
            for i in range(level+2):
                print " ",

            print "%s: (dict)" % name
            for j in value:
                for k in range(level+4):
                    print " ",
                print j.getItemPath()

        else:
            for i in range(level+2):
                print " ",

            print "%s:" % name,
            try:
                print value.getItemPath()
            except:
                print value, type(value)

    print

    for child in item:
        childuri = child.getItemPath()
        PrintItem(childuri, rep, level+1)

