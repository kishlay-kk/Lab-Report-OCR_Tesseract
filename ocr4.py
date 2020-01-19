#!/usr/bin/env python
# coding: utf-8

# In[1]:


#OCR 4 (FINAL)


"""List of parameters includes the parameters the OCR will check for in the file add more diseases 
according to the database created"""

"""This automatically detects if the file is a pdf or an image. PDF is handled by pdfocr() and image by imageocr()"""


# In[2]:


"Library Files"

from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import cv2
import os
import re


# In[3]:


"""List of parameters"""

vitals=("Sugar","(MCV)","Haemoglobin","Cholestrol","Pulse Rate","Total RBC","(PCV)","Platelet Count"," Leucocytes Count","TSH (Thyroid Stimulating Hormone)","Glucose (Random)","Bilirubin Total","PH","WBC")
kidney=("Cretin level","Protein")
stroke=("BP (diastolic)","BP (systolic)","Pulse Rate")
liver=("Bilirubin Total","Bilirubin Direct","Bilirubin Indirect")


# In[4]:


#taking the disease as input
disease=input("Enter The disease whose report you are uploading:-")


# In[12]:


def pdfocr(file,disease):
    string=""
    filexp=file.split(".")
    nm=filexp[0]
    i=1
    pages = convert_from_path(file, 500)
    for page in pages:
        name=nm+str(i)+'.jpg'
        page.save(name, 'JPEG')
        i=i+1
    
    j=1
    TEXT=""
    while j<i:
        fileimg = nm+str(j)+'.jpg'
        print(fileimg+" Scanned Successfully")
        img=cv2.imread(fileimg)
        text=pytesseract.image_to_string(img)
        TEXT=TEXT+text
        j=j+1
    
    print(TEXT)
    
    for i in vitals:
        spl_word = i
        if (TEXT.find(spl_word)!=-1):
            res=TEXT.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            if re.match('\d*\.?\d+',string):
                data.append(string)
            else:
                data.append('0')
        else:
            data.append('0')
        
    if disease=="Kidney" or disease=='kidney':
        for i in kidney:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)
        
    elif disease=="Stroke" or disease=="stroke":
        for i in stroke:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)
    elif disease=="Liver" or disease=="liver":
        for i in liver:
            #print(i)
            spl_word=i
            res=text.partition(spl_word)[-1]
            res=res.split()
            string=res[0]
            data.append(string)
    else:
        print("Vitals Only")
            
    return data
        
    


# In[9]:


def imageocr(file,disease):
    print("Image OCR")


# In[11]:


#Upload the file
file=input("Enter the file name= ")

expand=file.split(".")

data=[]

if expand[1]=="pdf":
    data=pdfocr(file,disease)
    
else:
    data=imgocr(file,disease)
    
print(data)


# In[ ]:




