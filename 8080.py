from multiprocessing import Condition
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import pygame
from os import walk , path
import os 
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
    img_width = 200
    img_height = 1200 
    canvas_width = 845
    canvas_height = 1192
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Bold.ttf'))
    os.system("taskkill /f /im "+"Acrobat.exe")
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
    elif(img_width==800 and img_height==1200):
        sq_width_size = 130
        sq_height_size = 200
    elif(img_width==200 and img_height==1200):
        sq_width_size = 33
        sq_height_size = 200
    page_count = 0
    initial_count = 0
    print_size = str(int(img_width/10))+'*'+str(int(img_height/10))+'cm'
    mono_print_size_width = str(int(img_width/10))+'cm'
    mono_print_size_height = str(int(img_height/10))+'cm'
    header_cat = str(int(img_width/10))+'cm'+' X '+str(int(img_height/10))+'cm'
    pdf_name = header_cat+".pdf"
    my_canvas = canvas.Canvas(pdf_name, pagesize=A3)
    my_canvas.drawImage('12.jpg', 100, 0, width=1000, height=1000)
    my_canvas.setFillColorRGB(0, 0, 0)
    my_canvas.rect(0, 0, 120, 1500, stroke=0, fill=1)
    my_canvas.rect(725, 0, 120, 1500, stroke=0, fill=1)
    my_canvas.rect(0, 1000, 1500, 900, stroke=0, fill=1)
    my_canvas.rect(0, 0, 1500, 150, stroke=0, fill=1)
    my_canvas.setFont("Roboto", 70)
    my_canvas.drawString(200, 800, 'CATALOGUE')
    my_canvas.setFont("Courier", 40)
    my_canvas.drawString(340, 770, header_cat)
    my_canvas.setFillColorRGB(255, 255, 255)
    my_canvas.setStrokeColorRGB(0,0,0)
    my_canvas.setFillColorRGB(255, 255, 255)
    my_canvas.rect(50, 70, 3, 1030, stroke=0, fill=1)
    my_canvas.rect(50, 1100, 740, 3, stroke=0, fill=1)
    my_canvas.rect(790, 70, 3, 1031, stroke=0, fill=1)
    my_canvas.rect(50, 70, 740, 3, stroke=0, fill=1)
    my_canvas.showPage()
    my_list = os.listdir('A:\Site Pics - Copy')
    for x in my_list:
        initial_count = 0
        for (dirpath, dirnames, filenames) in walk(x +"/pru/"):
            for j in filenames:
                if(j !='Thumbs.db'):
                    img = pygame.image.load(x+"/pru/"+j)
                    if (img.get_width() == img_width and img.get_height() == img_height):
                        initial_count += 1
            if (initial_count == 1):
                check = random.randrange(0, 3)
                #11
                if(check == 0):
                    my_canvas.drawImage(x +'/3.jpg', 0, 0, width=2098, height=1202)
                    my_canvas.setFont("Courier", 40)
                    page_number(1)
                    my_canvas.showPage()
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height):
                                my_canvas.drawImage(x +'/2.jpg', 0, 0, width=1280, height=720)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0,500,1300,785,stroke=0, fill=1)
                                my_canvas.drawImage(x+"/pru/"+cd, 90, 900, width=sq_width_size, height=sq_height_size)
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.drawImage('detail.png', 400, 1020, width=295, height=75)
                                my_canvas.setFont("Courier", 20)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(90, 880, chap)
                                my_canvas.setFont("Courier", 40)        
                                my_canvas.drawString(400, 1000, x.upper())
                                my_canvas.drawString(400, 950, print_size)
                                page_number(1)
                                my_canvas.showPage()
                #12
                if(check == 1):
                    my_canvas.setStrokeColorRGB(0, 0, 0)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.rect(0, 295, 2098, 1204, stroke=0, fill=1)
                    my_canvas.drawImage(x +'/2.jpg', -30, 300, width=2098, height=1202)
                    my_canvas.setStrokeColorRGB(0, 0, 0)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.rect(440, 190, sq_width_size+20, sq_height_size+20, stroke=0, fill=1) 
                    my_canvas.setFillColorRGB(255, 255, 255)
                    my_canvas.rect(430, 100, sq_width_size+40, 194, stroke=0, fill=1)
                    my_canvas.rect(445, 195, sq_width_size+10, sq_height_size+10, stroke=0, fill=1)
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height):
                                my_canvas.drawImage(x+"/pru/"+cd, 450, 200, width=sq_width_size, height=sq_height_size)
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)   
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(450, 180, chap)
                                my_canvas.setFont("Courier", 40)  
                                my_canvas.drawString(500, 50, print_size)
                                page_number(0)
                                my_canvas.showPage()
                                my_canvas.drawImage(x+"/pru/"+cd, 100, 300, width=sq_width_size*7, height=sq_height_size*7)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0, 0, 900, 320, stroke=0, fill=1)
                                my_canvas.rect(0, 0, 120, 1500, stroke=0, fill=1)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.setFont('Times-Bold',24)
                                img = cv2.imread(x+"/pru/"+cd)
                                avg_color_per_row = np.average(img, axis=0)
                                avg_colors = np.average(avg_color_per_row, axis=0)
                                int_averages = np.array(avg_colors, dtype=np.uint8)

                                if(int_averages[2] > 127):
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(500, -180, mono_print_size_width)
                                    my_canvas.restoreState()
                                    my_canvas.setFont('Times-Bold',24)
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(200, 720, mono_print_size_height)
                                    my_canvas.setFont("Courier", 102)
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(130, 340, x.upper())
                                    my_canvas.setLineWidth(4)
                                    my_canvas.setStrokeColorRGB(0,0,0)
                                    if(img_width == img_height):
                                        my_canvas.setStrokeColorRGB(0,0,0)
                                        my_canvas.rect(200, 500 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                    if(img_width == 300 and img_height == 600):
                                        my_canvas.setStrokeColorRGB(0,0,0)
                                        my_canvas.rect(200, 500 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                    if(img_width == 600 and img_height == 1200):
                                        my_canvas.setStrokeColorRGB(0,0,0)
                                        my_canvas.rect(200, 500 ,sq_width_size, sq_height_size, stroke=1, fill=0) 
                                    if(img_width == 800 and img_height == 1200):
                                        my_canvas.setStrokeColorRGB(0,0,0)  
                                        my_canvas.rect(200, 500 ,sq_width_size, sq_height_size, stroke=1, fill=0)    
                                    if(img_width == 200 and img_height == 1200):
                                        my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                    if(img_width == 300 and img_height == 900):
                                        my_canvas.setStrokeColorRGB(0,0,0)
                                        my_canvas.rect(200, 500 ,67, 200, stroke=1, fill=0)
                                else:
                                    my_canvas.setFillColorRGB(255, 255, 255)
                                    my_canvas.drawString(500, -180, mono_print_size_width)
                                    my_canvas.restoreState()
                                    my_canvas.setFont('Times-Bold',24)
                                    my_canvas.drawString(200, 720, mono_print_size_height)
                                    my_canvas.setFont("Courier", 102)
                                    my_canvas.drawString(130, 340, x.upper())
                                    my_canvas.setLineWidth(4)
                                    my_canvas.setStrokeColorRGB(255,255,255)
                                    my_canvas.rect(200, 500, sq_width_size, 200, stroke=1, fill=0)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.rect(50, 300, 3, 900, stroke=0, fill=1)
                                my_canvas.drawImage('detail - Copy.png', 20, 70, width=75, height=295)
                                page_number(0)
                                my_canvas.showPage()
                #13
                if(check == 2):
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height):    
                                my_canvas.drawImage(x +'/2.jpg', -50, 0, width=1280, height=720)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0, 500, 2098, 1202, stroke=0, fill=1)
                                my_canvas.drawImage(x+"/pru/"+cd, 90, 800, width=sq_width_size, height=sq_height_size)
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFont("Courier", 20)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(90, 770, chap)
                                img_color = cv2.imread(x+"/pru/"+cd)
                                avg_color_per_row = np.average(img_color, axis=0)
                                avg_colors = np.average(avg_color_per_row, axis=0)
                                int_averages = np.array(avg_colors, dtype=np.uint8)
                                if(int_averages[2] > 127):
                                    page_number(1)
                                else:
                                    page_number(0)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(920, -580, mono_print_size_height )
                                my_canvas.restoreState()
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(600, 870, mono_print_size_width)
                                my_canvas.setLineWidth(4)
                                my_canvas.setStrokeColorRGB(0,0,0)
                                if(img_width == img_height):
                                    my_canvas.rect(600, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 300 and img_height == 600):
                                    my_canvas.rect(600, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 600 and img_height == 1200):
                                    my_canvas.rect(600, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0) 
                                if(img_width == 800 and img_height == 1200):
                                    my_canvas.rect(600, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 200 and img_height == 1200):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 300 and img_height == 900):
                                    my_canvas.rect(600,  900 ,67, 200, stroke=1, fill=0)
                                my_canvas.showPage()
                                my_canvas.drawImage(x+"/pru/"+cd, -700, -30, width=1300, height=1300) 
                                if(int_averages[2] > 127):
                                    my_canvas.setStrokeColorRGB(0,0,0)
                                    my_canvas.setLineWidth(10)
                                    my_canvas.rect(50, 200 ,600, 800, stroke=1, fill=0)
                                    page_number(0)
                                else:
                                    my_canvas.setStrokeColorRGB(255,255,255)
                                    my_canvas.setLineWidth(10)
                                    my_canvas.rect(50, 200 ,600, 800, stroke=1, fill=0)
                                    page_number(1)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(490, 000 ,600, 1200, stroke=0, fill=1)
                                my_canvas.drawImage('detail.png', 530, 50, width=295, height=75)
                                my_canvas.showPage()
            if (initial_count == 2):
                check = random.randrange(0, 3)
                #21
                if(check == 0):
                    if(os.path.exists(x +'/w1.jpg')):
                        my_canvas.drawImage(x +'/w1.jpg', 0, 0, width=2098, height=1202)
                    else:
                        my_canvas.drawImage(x +'/2.jpg', 0, 0, width=2098, height=1202)
                    page_number(1)
                    my_canvas.showPage()
                    first_pic = 1
                    Condition_page = 1
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 0): 
                                my_canvas.drawImage(x+"/pru/"+cd, 500, 130, width=sq_width_size+sq_width_size/2, height=sq_height_size+sq_height_size/2) 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFont("Courier", 20)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(500, 90, chap)  
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 1):
                                my_canvas.drawImage(x+"/pru/"+cd, 90, 130, width=sq_width_size+sq_width_size/2, height=sq_height_size+sq_height_size/2)
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.drawImage('detail - Copy.png', 700, 720, width=75, height=295)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.drawString(720, -80, mono_print_size_height )
                                my_canvas.restoreState()
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(100, 680, mono_print_size_width)
                                my_canvas.setLineWidth(4)
                                if(img_width == img_height):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 300 and img_height == 600):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 600 and img_height == 1200):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0) 
                                if(img_width == 800 and img_height == 1200):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 200 and img_height == 1200):
                                    my_canvas.rect(90, 700 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                if(img_width == 300 and img_height == 900):
                                    my_canvas.rect(90, 700 ,67, 200, stroke=1, fill=0)
                                my_canvas.setFont("Courier", 20)
                                my_canvas.drawString(90, 90, chap)  
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 50)      
                                my_canvas.drawString(90, 1000, x.upper())
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 40)
                                my_canvas.drawString(90, 950, print_size)
                                page_number(0)
                                first_pic = 0
                                Condition_page = 0
                #22
                if(check == 1):
                    first_pic = 1
                    Condition_page = 1
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height and  first_pic == 0):     
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setStrokeColorRGB(00, 0, 0)
                                my_canvas.rect(240, 190, sq_width_size+20, sq_height_size+20, stroke=0, fill=1) 
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0, 100, 545, 195, stroke=0, fill=1)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(245, 195, sq_width_size+10, sq_height_size+10, stroke=0, fill=1)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(250, 180, chap)
                                my_canvas.drawImage(x+"/pru/"+cd, 250, 200, width=sq_width_size, height=sq_height_size)
                                my_canvas.drawImage('detail.png', 350, 53, width=295, height=75)
                                my_canvas.showPage()
                                my_canvas.drawImage(x+"/pru/"+cd, 100, 0, width=sq_width_size*7, height=sq_height_size*7)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0, 0, 120, 1500, stroke=0, fill=1)
                                my_canvas.rect(725, 0, 120, 1500, stroke=0, fill=1)
                                my_canvas.rect(0, 995, 1500, 900, stroke=0, fill=1)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.setLineWidth(4)
                                my_canvas.setStrokeColorRGB(0,0,0)
                                my_canvas.rect(845/2-sq_width_size/2, 200 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(200, -(845/2-sq_width_size/2)+30, mono_print_size_height)
                                my_canvas.restoreState() 
                                my_canvas.setFont("Courier", 70)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(320, 780, mono_print_size_width)
                                my_canvas.drawString(390, 680, 'X')
                                my_canvas.drawString(320, 580, mono_print_size_height)
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.drawString(845/2-sq_width_size/2, 170, mono_print_size_width)
                                my_canvas.setLineWidth(2)
                                my_canvas.rect(50, 100, 3, 1000, stroke=0, fill=1)
                                my_canvas.rect(50, 1100, 740, 3, stroke=0, fill=1)
                                my_canvas.rect(790, 70, 3, 1031, stroke=0, fill=1)
                                my_canvas.rect(790, 70, 100, 3, stroke=0, fill=1)
                                page_number(0)
                                my_canvas.showPage()
                                first_pic = 1
                                Condition_page = 0
                            if (img.get_width() == img_width and img.get_height() == img_height and  Condition_page == 1): 
                                my_canvas.setStrokeColorRGB(00, 0, 0)
                                my_canvas.rect(0, 295, 2098, 1204, stroke=0, fill=1)
                                if(os.path.exists(x +'/w1.jpg')):
                                    my_canvas.drawImage(x +'/w1.jpg', 0, 300, width=2098, height=1202)
                                else:
                                    my_canvas.drawImage(x +'/2.jpg', 0, 300, width=2098, height=1202)
                                my_canvas.setStrokeColorRGB(00, 0, 0)
                                my_canvas.rect(540, 190, sq_width_size+20, sq_height_size+20, stroke=0, fill=1) 
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(0, 100, 1202, 195, stroke=0, fill=1)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(545, 195, sq_width_size+10, sq_height_size+10, stroke=0, fill=1)
                                my_canvas.setStrokeColorRGB(0.2, 0.5, 0.3)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.rect(545, 195, sq_width_size+10, sq_height_size+10, stroke=0, fill=1)

                                my_canvas.drawImage(x+"/pru/"+cd, 550, 200, width=sq_width_size, height=sq_height_size) 
                                my_canvas.rect(245, 195, sq_width_size+10, sq_height_size+10, stroke=0, fill=1)  
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.drawString(550, 180, chap)

                                my_canvas.rect(00, 70, 600, 3, stroke=0, fill=1) 
                                my_canvas.setLineWidth(4)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.setStrokeColorRGB(0, 0, 0)
                                my_canvas.rect(400, 870, 500, 100, stroke=1, fill=1)
                                my_canvas.setFont("Courier", 72)
                                my_canvas.setFont("Courier", 70)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(422, 900, x.upper())
                                my_canvas.setFillColorRGB(0, 0, 0)
                                page_number(0)
                                Condition_page = 0
                                first_pic = 0
                #23
                if(check == 2):
                    my_canvas.drawImage(x +'/2.jpg', -50, 0, width=1280, height=720)
                    my_canvas.setFillColorRGB(255, 255, 255)
                    my_canvas.rect(0, canvas_height/2, 2098, 1202, stroke=0, fill=1)
                    my_canvas.saveState()
                    my_canvas.rotate(90)
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.drawString(800, -80, mono_print_size_height)
                    my_canvas.restoreState()
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.drawString(100, 820+sq_height_size, mono_print_size_width )
                    my_canvas.setLineWidth(4) 
                    my_canvas.setStrokeColorRGB(0,0,0)
                    my_canvas.rect(100, 800 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                    img_color = cv2.imread(x+"/2.jpg")
                    avg_color_per_row = np.average(img_color, axis=0)
                    avg_colors = np.average(avg_color_per_row, axis=0)
                    int_averages = np.array(avg_colors, dtype=np.uint8)
                    if(int_averages[2] > 127):
                        page_number(1)
                    else:
                        page_number(0)
                    my_canvas.showPage()
                    first_pic = 1
                    Condition_page = 1
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)    
                            if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 0): 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/2+110, -(canvas_width+sq_height_size)/2, width=sq_width_size*1.25, height=sq_height_size*1.25) 
                                my_canvas.restoreState()
                                my_canvas.drawString((canvas_width-sq_height_size*1.25)/2, canvas_height/2+80, chap)
                                my_canvas.setFont("Courier", 40)        
                                my_canvas.drawString(100, 1050, x.upper())
                                my_canvas.drawString(100, 1000, print_size)
                                my_canvas.drawImage('detail.png', 330, 50, width=295, height=75)
                                my_canvas.setFillColorRGB(0,0,0)
                                my_canvas.rect(50, 80 ,3, 1000, stroke=0, fill=1)
                                page_number(0)
                                Condition_page = 1
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 1):  
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/2-sq_width_size-10, -(canvas_width+sq_height_size)/2, width=sq_width_size*1.25, height=sq_height_size*1.25) 
                                my_canvas.restoreState()
                                my_canvas.drawString((canvas_width-sq_height_size*1.25)/2, canvas_height/2-sq_width_size*1.25-20, chap)
                                first_pic = 0
                                Condition_page = 0            
            if (initial_count == 3):
                #31
                check = random.randrange(0, 2)
                if(check == 0):
                    first_pic = 0
                    sec_pic = 0
                    Condition_page = 0
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 1): 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height*2/3+sq_width_size*1.5, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height*2/3+sq_width_size*1.5-20, chap) 
                                Condition_page = 0
                                forth_pic = 1
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and sec_pic == 1):
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/2, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5)  
                                my_canvas.restoreState()
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height/2-30, chap)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                Condition_page = 1
                                sec_pic = 0
                            if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 0):
                                my_canvas.setFillColorRGB(0,0,0)
                                my_canvas.drawImage('detail.png', canvas_width/2-295/2, 21, width=295, height=75) 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/3-sq_width_size*1.5-10, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height/3-sq_width_size*1.5-30, chap)

                                page_number(0)
                                first_pic = 1
                                sec_pic = 1

                    my_canvas.drawImage(x +'/2.jpg', -30, 0, width=1280, height=720)
                    page_number(0)
                    my_canvas.setFont("Courier", 40)        
                    my_canvas.drawString(90, 1000, x.upper())
                    my_canvas.drawString(90, 950, print_size)
                    my_canvas.showPage()
                #32
                if(check == 1):
                    my_canvas.drawImage(x +'/2.jpg', -380, 0, width=1280, height=720)
                    my_canvas.setFillColorRGB(255, 255, 255)
                    my_canvas.saveState()
                    my_canvas.rotate(90)
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.drawString(900, -480, mono_print_size_height)
                    my_canvas.restoreState()
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.drawString(500, 870, mono_print_size_width )
                    my_canvas.setLineWidth(4) 
                    my_canvas.setStrokeColorRGB(0,0,0)
                    my_canvas.rect(500, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                    my_canvas.setFont("Courier", 40)        
                    my_canvas.drawString(100, 1050, x.upper())
                    my_canvas.drawString(100, 1000, print_size)
                    my_canvas.setLineWidth(4) 
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.line(x1=0, y1=1060, x2=70, y2=1060)
                    page_number(1)
                    my_canvas.showPage()
                    my_canvas.drawImage(x +'/2.jpg', canvas_width-380, 0, width=1280, height=720) 
                    my_canvas.setLineWidth(4) 
                    my_canvas.line(x1=30, y1=1060, x2=canvas_height, y2=1060)
                    my_canvas.line(x1=40, y1=70, x2=30, y2=1062)
                    first_pic = 0
                    sec_pic = 0
                    Condition_page = 0
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 1): 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height*2/3+sq_width_size, -(canvas_width/3+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/3-sq_height_size/2), canvas_height*2/3+sq_width_size-20, chap) 
                                Condition_page = 0 
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and sec_pic == 1):
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/2, -(canvas_width/3+sq_height_size/2), width=sq_width_size, height=sq_height_size)  
                                my_canvas.restoreState()
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.drawString((canvas_width/3-sq_height_size/2), canvas_height/2-30, chap)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                Condition_page = 1
                                sec_pic = 0
                            if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 0):
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/3-sq_width_size-10, -(canvas_width/3+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/3-sq_height_size/2), canvas_height/3-sq_width_size-30, chap)
                                my_canvas.drawImage('detail.png', 500, 900, width=295, height=75) 
                                page_number(0)
                                first_pic = 1
                                sec_pic = 1

            if (initial_count == 4):
                check=random.randrange(0, 2)
                #41
                if(check == 0):
                    my_canvas.drawImage(x +'/2.jpg', 0, 0, width=2098, height=1202)
                    my_canvas.setFont("Courier", 40)
                    my_canvas.saveState()
                    my_canvas.rotate(90)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.drawString(950, -480, mono_print_size_height )
                    my_canvas.restoreState()
                    my_canvas.setFont('Times-Bold',24)
                    my_canvas.setFillColorRGB(0, 0, 0)
                    my_canvas.drawString(500, 900, mono_print_size_width)
                    my_canvas.setLineWidth(4)                  
                    page_number(0)
                    my_canvas.setStrokeColorRGB(0,0,0)
                    my_canvas.rect(500, 930 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                    my_canvas.showPage()
                    forth_pic = 0
                    first_pic = 0
                    sec_pic = 0
                    Condition_page = 0
                    if(sq_height_size == sq_width_size):
                        for cd in filenames:
                            if(cd !='Thumbs.db'):
                                img = pygame.image.load(x+"/pru/"+cd)
                                if (img.get_width() == img_width and img.get_height() == img_height and forth_pic == 1): 
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.setFont("Courier", 15)
                                    my_canvas.drawImage(x+"/pru/"+cd, 420, 460, width=sq_width_size, height=sq_height_size) 
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(420, 440, chap)
                                    forth_pic = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 1): 
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    my_canvas.setFont("Courier", 15)
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.drawImage(x+"/pru/"+cd, 180, 460, width=sq_width_size, height=sq_height_size) 
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(180, 440, chap)
                                    forth_pic = 1
                                    Condition_page = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and sec_pic == 1):
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    my_canvas.setFont("Courier", 15)
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.drawImage(x+"/pru/"+cd, 420, 700, width=sq_width_size, height=sq_height_size) 
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(420, 680, chap) 
                                    Condition_page = 1
                                    sec_pic = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 0):
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.drawImage(x+"/pru/"+cd, 180, 700, width=sq_width_size, height=sq_height_size) 
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.setFont("Courier", 15)
                                    my_canvas.drawString(180, 680, chap) 
                                    my_canvas.drawImage('detail.png', 270, 150, width=295, height=75) 
                                    page_number(0)
                                    my_canvas.setFont("Courier", 40)        
                                    my_canvas.drawString(90, 1100, x.upper())
                                    my_canvas.drawString(90, 1050, print_size) 
                                     

                                    first_pic = 1
                                    sec_pic = 1
                    if(sq_height_size != sq_width_size):
                        for cd in filenames:
                            if(cd !='Thumbs.db'):
                                img = pygame.image.load(x+"/pru/"+cd)
                                if (img.get_width() == img_width and img.get_height() == img_height and forth_pic == 1): 
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.setFont("Courier", 15)
                                    my_canvas.saveState()
                                    my_canvas.rotate(90)
                                    my_canvas.drawImage(x+"/pru/"+cd, canvas_height*4/5-sq_width_size/2, -(canvas_width/2+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                    my_canvas.restoreState()
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(canvas_width/2-sq_height_size/2, canvas_height*4/5-sq_width_size/2-20, chap) 
                                    forth_pic = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 1): 
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    my_canvas.setFont("Courier", 15)
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.saveState()
                                    my_canvas.rotate(90)
                                    my_canvas.drawImage(x+"/pru/"+cd, canvas_height*3/5-sq_width_size/2, -(canvas_width/2+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                    my_canvas.restoreState()
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(canvas_width/2-sq_height_size/2, canvas_height*3/5-sq_width_size/2-20, chap) 
                                    forth_pic = 1
                                    Condition_page = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and sec_pic == 1):
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    my_canvas.setFont("Courier", 15)
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.saveState()
                                    my_canvas.rotate(90)
                                    my_canvas.drawImage(x+"/pru/"+cd, canvas_height*2/5-sq_width_size/2, -(canvas_width/2+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                    my_canvas.restoreState()
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.drawString(canvas_width/2-sq_height_size/2, canvas_height*2/5-sq_width_size/2-20, chap) 
                                    Condition_page = 1
                                    sec_pic = 0
                                if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 0):
                                    file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                    all_lines_variable = file.readlines()
                                    num_line = int(cd.replace(".jpg",""))
                                    chap = all_lines_variable[num_line-1].replace("\n"," ")
                                    print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                    my_canvas.saveState()
                                    my_canvas.rotate(90)
                                    my_canvas.drawImage(x+"/pru/"+cd, canvas_height/5-sq_width_size/2, -(canvas_width/2+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                    my_canvas.restoreState()
                                    my_canvas.setFillColorRGB(0, 0, 0)
                                    my_canvas.setFont("Courier", 15)
                                    my_canvas.drawString(canvas_width/2-sq_height_size/2, canvas_height/5-sq_width_size/2-20, chap) 
                                    my_canvas.drawImage('detail.png', 270, 50, width=295, height=75) 
                                    page_number(0)
                                    my_canvas.setFont("Courier", 40)        
                                    my_canvas.drawString(90, 1100, x.upper())
                                    my_canvas.drawString(90, 1050, print_size) 
                                    
                                    first_pic = 1
                                    sec_pic = 1
                    my_canvas.showPage()
                #42
                if(check == 1):
                    first_pic = 0
                    sec_pic = 0
                    Condition_page = 0
                    forth_pic = 0
                    for cd in filenames:
                        if(cd !='Thumbs.db'):
                            img = pygame.image.load(x+"/pru/"+cd)
                            if (img.get_width() == img_width and img.get_height() == img_height and forth_pic == 1): 
                                my_canvas.drawImage(x +'/2.jpg', -420, 0, width=1280, height=720)
                                my_canvas.setFillColorRGB(255, 255, 255)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(900, -480, mono_print_size_height)
                                my_canvas.restoreState()
                                my_canvas.setFont('Times-Bold',24)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString(500, 870, mono_print_size_width )
                                my_canvas.setLineWidth(4) 
                                my_canvas.setStrokeColorRGB(0,0,0)
                                my_canvas.rect(500, 900 ,sq_width_size, sq_height_size, stroke=1, fill=0)
                                my_canvas.setFillColorRGB(0,0,0)
                                my_canvas.setFont("Courier", 40)        
                                my_canvas.drawString(80, 1080, x.upper())
                                my_canvas.drawString(80, 1030, print_size)
                                my_canvas.setLineWidth(4) 
                                my_canvas.setFillColorRGB(0, 0, 0)
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height*3/5+sq_width_size, -(canvas_width/3+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/3-sq_height_size/2), canvas_height*3/5+sq_width_size-20, chap) 
                                Condition_page = 0 
                                page_number(1)
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and Condition_page == 1): 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height*2/3+sq_width_size*1.5, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height*2/3+sq_width_size*1.5-20, chap) 
                                Condition_page = 0
                                forth_pic = 1
                                my_canvas.showPage()
                            if (img.get_width() == img_width and img.get_height() == img_height and sec_pic == 1):
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/2, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5)  
                                my_canvas.restoreState()
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.setFont("Courier", 15)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height/2-30, chap)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                Condition_page = 1
                                sec_pic = 0
                            if (img.get_width() == img_width and img.get_height() == img_height and first_pic == 0):
                                my_canvas.setLineWidth(4)
                                my_canvas.rect(40, 40 ,canvas_width-40-50, canvas_height-40-50, stroke=1, fill=0)
                                my_canvas.setFillColorRGB(255,255,255)
                                my_canvas.rect(0, 0 ,60, 90, stroke=0, fill=1)
                                my_canvas.setFillColorRGB(0,0,0)
                                my_canvas.drawImage('detail.png', canvas_width/2-295/2, 21, width=295, height=75) 
                                file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
                                all_lines_variable = file.readlines()
                                num_line = int(cd.replace(".jpg",""))
                                chap = all_lines_variable[num_line-1].replace("\n"," ")
                                print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
                                my_canvas.saveState()
                                my_canvas.rotate(90)
                                my_canvas.drawImage(x+"/pru/"+cd,canvas_height/3-sq_width_size*1.5-10, -(canvas_width+sq_height_size*1.5)/2, width=sq_width_size*1.5, height=sq_height_size*1.5) 
                                my_canvas.restoreState()
                                my_canvas.setFont("Courier", 15)
                                my_canvas.setFillColorRGB(0, 0, 0)
                                my_canvas.drawString((canvas_width/2-sq_height_size*1.5/2), canvas_height/3-sq_width_size*1.5-30, chap)

                                page_number(0)
                                first_pic = 1
                                sec_pic = 1
        if (initial_count == 8):
            file = open("A:\Site Pics - Copy\\"+x+"\\infoen.txt", "r")
            all_lines_variable = file.readlines()
            chap = all_lines_variable[0].replace("\n"," ")
            print("pg: ",page_count, "item: ",initial_count,check+1,"\tname:",chap)
            img = pygame.image.load(x+"/pru/1.jpg")


            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/2.jpg",canvas_height/4+sq_width_size/2, -(canvas_width/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width/4-sq_height_size/2), canvas_height/4+sq_width_size/2-20, chap) 

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/1.jpg",canvas_height/4+sq_width_size/2, -(canvas_width*3/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width*3/4-sq_height_size/2), canvas_height/4+sq_width_size/2-20, chap) 

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/3.jpg",canvas_height*2/4+sq_width_size/2, -(canvas_width/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width/4-sq_height_size/2), canvas_height*2/4+sq_width_size/2-20, chap)     

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/4.jpg",canvas_height*2/4+sq_width_size/2, -(canvas_width*3/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width*3/4-sq_height_size/2), canvas_height*2/4+sq_width_size/2-20, chap)             

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/5.jpg",canvas_height*3/4+sq_width_size/2, -(canvas_width/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width/4-sq_height_size/2), canvas_height*3/4+sq_width_size/2-20, chap)        

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/6.jpg",canvas_height*3/4+sq_width_size/2, -(canvas_width*3/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width*3/4-sq_height_size/2), canvas_height*3/4+sq_width_size/2-20, chap)        
            page_number(0)  
            
            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.setFont('Times-Bold',24)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString(80, -680, mono_print_size_height)
            my_canvas.restoreState()
            my_canvas.setFont('Times-Bold',24)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString(700, 50, mono_print_size_width )
            my_canvas.setLineWidth(4) 
            my_canvas.setStrokeColorRGB(0,0,0)     
            my_canvas.rect(700, 80 ,sq_width_size/2, sq_height_size/2, stroke=1, fill=0)
            my_canvas.drawImage('detail.png', canvas_width/2-295/2, 50, width=295, height=75)
            my_canvas.showPage()
            
            my_canvas.saveState()
            my_canvas.rotate(90) 
            my_canvas.drawImage(x+"/pru/8.jpg",canvas_height*3/4+sq_width_size/2, -(canvas_width/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width/4-sq_height_size/2), canvas_height*3/4+sq_width_size/2-20, chap)        

            my_canvas.saveState()
            my_canvas.rotate(90)
            my_canvas.drawImage(x+"/pru/7.jpg",canvas_height*3/4+sq_width_size/2, -(canvas_width*3/4+sq_height_size/2), width=sq_width_size, height=sq_height_size) 
            my_canvas.restoreState()
            my_canvas.setFont("Courier", 15)
            my_canvas.setFillColorRGB(0, 0, 0)
            my_canvas.drawString((canvas_width*3/4-sq_height_size/2), canvas_height*3/4+sq_width_size/2-20, chap)   

            my_canvas.drawImage(x +'/2.jpg', -50, 0, width=1280, height=720)
            my_canvas.setFillColorRGB(255, 255, 255)
            page_number(1)     
            my_canvas.showPage()
    my_canvas.save()           
    os.startfile(pdf_name)                