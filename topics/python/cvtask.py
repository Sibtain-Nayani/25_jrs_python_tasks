# Task
#
# build a Command-Line Based Image Utility Tool
#
# 1) Accept image path input
# 2) Show a menu of operations (resize, rotate, convert to gray, blur, threshold and others that were taught)
# 3) Apply the selected operation
# 4) Save and  display the result
#
# Constraints
#
# Handle errors (invalid input, file not found, wrong image and others)
# Validate all user inputs

import cv2 as cv
import numpy as np
import os

class Imgapp:
    def __init__(self):
        end = False
        imgpath =input("Enter image path: ").strip()
        if not os.path.exists(imgpath):
            print("Error: File not found.")
            return
        
        self.img = cv.imread(imgpath)
        
        if self.img is None:
            print("Error: Invalid image file")

        self.dup = self.img.copy()

        while(not end):
            self.operation()
            cv.imshow("img",self.img)
            cv.waitKey(0)
            exeet=input("Do you wish to exit the application[y/n]:").lower()
            if(exeet=="y"):
                end= True

    def operation(self):
        print("\nSelect an operation:(Enter the corresponding number)\n")
        
        operand = int(input("1.Resize\n2.Rotate\n3.Grayscale\n4.Blur\n5.Threshold\n6.Canny Edges\n7.Erode\n8.Dilate\n9.Crop\n10.Draw\n11.Reset all Changes\n"))

        match(operand):
            case 1:
                self.resize(self.img)
            case 2:
                self.rotate(self.img)
            case 3:
                self.grayscale(self.img)
            case 4:
                self.blur(self.img)
            case 5:
                self.thres(self.img)
            case 6:
                self.canny(self.img)
            case 7:
                self.ero(self.img)
            case 8:
                self.dil(self.img)
            case 9:
                self.crop(self.img)
            case 10:
                self.draw(self.img)
            case 11:
                self.img = self.dup.copy()
            case _:
                print("Error!!, please enter a valid operation")
                self.operation()
    
    def resize(self,img):
        wid=int(input("Enter new width:"))
        hei=int(input("Enter new height:"))
        self.img =cv.resize(img,(wid,hei))
        
    def rotate(self,img):
        print("\nSelect direction of rotation:(Enter the corresponding number)\n")
        dir = int(input("1.90 deg clockwise\n2.90 deg anticlockwise\n"))
        match(dir):
            case 1:
                self.img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
            case 2:
                self.img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
            case _:
                print("Error!!, please enter a valid operation")
                self.rotate(self.img)

    def grayscale(self,img):
        self.img= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
    def blur(self,img):
        a=int(input("Enter kernel size:(enter odd integer only)"))
        if a%2==1:
            self.img= cv.GaussianBlur(img,(a,a),cv.BORDER_DEFAULT)
        else:
            print("Error!!, please enter an odd integer")
            self.blur(self.img)

    def thres(self,img):
        print("\nSelect Thresholding mode:(Enter the corresponding number)\n")
        mode = int(input("1.Binary \n2.Binary_inverse\n"))
        lt=int(input("Enter lower threshold value:"))
        ut=int(input("Enter upper threshold value:"))
        match(mode):
            case 1:
                ret,self.img = cv.threshold(img,lt,ut,cv.THRESH_BINARY)
            case 2:
                ret,self.img = cv.threshold(img,lt,ut,cv.THRESH_BINARY_INV)
            case _:
                print("Error!!, please enter a valid operation")
                self.thres(self.img)
        
        
    def canny(self,img):
        lt=int(input("Enter lower threshold value:"))
        ut=int(input("Enter upper threshold value:"))
        self.img = cv.Canny(img,lt,ut)
    
    def ero(self,img):
        a=int(input("Enter kernel size:(enter odd integer only)"))
        if a%2==1:
            self.img= cv.erode(img,(a,a),1)
        else:
            print("Error!!, please enter an odd integer")
            self.ero(self.img)
    
    def dil(self,img):
        a=int(input("Enter kernel size:(enter odd integer only)"))
        if a%2==1:
            self.img= cv.dilate(img,(a,a),1)
        else:
            print("Error!!, please enter an odd integer")
            self.dil(self.img)
    
    def crop(self,img):
        wa=int(input("Enter width range(Startpoint):"))
        wb=int(input("Enter width range(Endpoint):"))
        ha=int(input("Enter height range(Startpoint):"))
        hb=int(input("Enter height range(Endpoint):"))
        self.img = self.img[ha:hb,wa:wb]
    
    def draw(self,img):
        print("\nSelect Drawing tool:(Enter the corresponding number)\n")
        mode = int(input("1.line \n2.Rectangle\n3.Circle\n"))
        match(mode):
            case 1:
                x1=int(input("Enter x range(Startpoint):"))
                x2=int(input("Enter x range(Endpoint):"))
                y1=int(input("Enter y range(Startpoint):"))
                y2=int(input("Enter y range(Endpoint):"))
                
                th = int(input("Enter Thickness:\n"))
                print("Select a colour:\n")
                colopt= int(input("1.Red\n2.Blue\n3.Green\n4.Black\n5.White\n"))
                colorr=self.colsel(colopt)
                self.img = cv.line(img,(x1,y1),(x2,y2),colorr,th)
            
            case 2:
                x1=int(input("Enter coords of TopLeft corner (x):"))
                y1=int(input("Enter coords of TopLeft corner (y):"))
                x2=int(input("Enter coords of BottomRight corner (x):"))
                y2=int(input("Enter coords of BottomRight corner (y):"))

                th = int(input("Enter Thickness:\n"))
                print("Select a colour:\n")
                colopt= int(input("1.Red\n2.Blue\n3.Green\n4.Black\n5.White\n"))
                colorr=self.colsel(colopt)
                self.img = cv.rectangle(img,(x1,y1),(x2,y2),colorr,th)
            
            case 3:

                x1=int(input("Enter coords of Center(x):"))
                y1=int(input("Enter coords of Center(y):"))
                radi = int(input("Enter Radius(Integer):\n"))
                
                th = int(input("Enter Thickness:\n"))
                print("Select a colour:\n")
                colopt= int(input("1.Red\n2.Blue\n3.Green\n4.Black\n5.White\n"))
                colorr=self.colsel(colopt)
                self.img = cv.circle(img,(x1,y1),radi,colorr,th)
            
            case _:
                print("Error!!, please enter a valid operation")
                self.draw(self.img)
    
    def colsel(self,a):
        if a == 1:
            return (0,0,255)
        if a == 2:
            return (255,0,0)
        if a == 3:
            return (0,255,0)
        if a == 4:
            return (0,0,0)
        if a == 5:
            return (255,255,255)
        else:
            print("Enter valid option next time. Using Default option(Black)")
            return (255,255,255)
            


obj = Imgapp()

