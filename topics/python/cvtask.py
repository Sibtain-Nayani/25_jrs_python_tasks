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
        operand = int(input("1.Resize\n2.Rotate\n3.Grayscale\n4.Blur\n5.Threshold\n6.Canny Edges\n7.Reset all Changes\n"))
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
                self.rotate()

    def grayscale(self,img):
        self.img= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
    def blur(self,img):
        a=int(input("Enter kernel size:(enter odd integer only)"))
        if a%2==1:
            self.img= cv.GaussianBlur(img,(a,a),cv.BORDER_DEFAULT)
        else:
            print("Error!!, please enter an odd integer")
            self.blur()

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
                self.thres()
        
        
    def canny(self,img):
        lt=int(input("Enter lower threshold value:"))
        ut=int(input("Enter upper threshold value:"))
        self.img = cv.Canny(img,lt,ut)
    

obj = Imgapp()

