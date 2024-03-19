def myStr(*args,**kwargs):
    char1=kwargs["char1"]
    mystr= char1.join(args)
    return mystr


mylst=["@","!","$","%","&"]
print(myStr(*mylst ,char1= '-'))       
        