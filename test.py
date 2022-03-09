from tabnanny import check
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pygame
from os import walk
import os
import cv2
import numpy as np
import random
def page_number(s):
    global page_count
    page_count+=1
    my_canvas.setFont("Courier", 40)
    if(s==1):
        my_canvas.setFillColorRGB(255, 255, 255)
    else:
        my_canvas.setFillColorRGB(0, 0, 0)
    my_canvas.drawString(30, 30, str(page_count))
if __name__ == "__main__":
    x='gabe'
    check = 0
    initial_count = 6
    img_width = 600
    img_height = 1200
    print_size = str(int(img_width/10))+'*'+str(int(img_height/10))+'cm'
    if(img_width == img_height):
        sq_width_size = 200
        sq_height_size = 200
    elif(img_width==300 and img_height==600):
        sq_width_size = 100
        sq_height_size = 200
    elif(img_width==300 and img_height==900):
        sq_width_size = 100
        sq_height_size = 300
    elif(img_width==600 and img_height==1200):
        sq_width_size = 100
        sq_height_size = 200
    elif(img_width==1200 and img_height==1800):
        sq_width_size = 200
        sq_height_size = 300
    elif(img_width==800 and img_height==1200):
        sq_width_size = 130
        sq_height_size = 200
    elif(img_width==200 and img_height==1200):
        sq_width_size = 130
        sq_height_size = 200 
    canvas_width = 845
    canvas_height = 1192
    page_count = 0
    mono_print_size_width = str(int(img_width/10))+'cm'
    mono_print_size_height = str(int(img_height/10))+'cm'
    os.system("taskkill /f /im "+"Acrobat.exe") 
    my_canvas = canvas.Canvas("canvas_image.pdf", pagesize=A3)
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
    filenames = 'aaaa'
    if(check == 0):
        chap = x
        print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",x)
        img = pygame.image.load(x+"/1.jpg")
        aspect = img.get_width() / img.get_height()

        my_canvas.drawImage(x+"/1.jpg",0, 0, width=845, height=1200)  
        
        img = cv2.imread(x+"/pru/1.jpg")
        avg_color_per_row = np.average(img, axis=0)
        avg_colors = np.average(avg_color_per_row, axis=0)
        int_averages = np.array(avg_colors, dtype=np.uint8)
        if(int_averages[2] > 127):
            page_number(1) 
        else:
            page_number(0)
        my_canvas.showPage()
    
        my_canvas.drawImage(x+"/2.jpg",0, 0, width=720, height=720)
        img = cv2.imread(x+"/pru/2.jpg")
        avg_color_per_row = np.average(img, axis=0)
        avg_colors = np.average(avg_color_per_row, axis=0)
        int_averages = np.array(avg_colors, dtype=np.uint8)
        if(int_averages[2] > 127):
            page_number(1) 
        else:
            page_number(0)
            y_canvas.setFillColorRGB(255,255, 255)
        my_canvas.roundRect(30, 980, 280, 100, 10, stroke=0, fill=1)    
        my_canvas.setFont("Courier", 102)
        my_canvas.setFillColorRGB(0, 0, 0)
        my_canvas.drawString(50, 1000, x.upper())     
        my_canvas.showPage()            
    my_canvas.save()
    os.startfile('canvas_image.pdf')
