"""A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams"""


def grams_to_ounces(grams):
    return grams * 28.3495231

x = float(input("Enter the value:"))
print(x , "grams are equal to", grams_to_ounces(x) , "ounces")