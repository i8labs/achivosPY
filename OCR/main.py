from PIL import Image 
import pytesseract
outfile = "out_text.txt"

f = open(outfile, "a") 
  
filename = "sample.png"

# Recognize the text as string in image using pytesserct 
text = str(((pytesseract.image_to_string(Image.open(filename))))) 

# In many PDFs, at line ending, if a word can't 
# be written fully, a 'hyphen' is added. 
# To remove this, we replace every '-\n' to ''. 
text = text.replace('-\n', '')     

# Finally, write the processed text to the file. 
f.write(text) 
  
# Close the file after writing all the text. 
f.close() 