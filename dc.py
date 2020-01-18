# File Number 2
import time
from datetime import timedelta
start_time = time.time()
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import sys
from PIL import Image, ImageTk
import os
from combined import root,sequence,  create_dir, find_good_metaphases, f2, make_gui_before, info_dialogue_box, red_cross, VerticalScrolledFrame, fileout
import tkMessageBox
import cv2
from os.path import basename
import numpy as np  
import shutil
import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage
import skimage.color
import os
from scipy.stats import gaussian_kde
from scipy.interpolate import spline

from skimage.io import imread
import openpyxl
from ranking import score



def run():
    global threshold_value , min_score
    # global threshold_value
    threshold_value = threshold_entry.get() 
    min_score = threshold_value
    # print "Run algorithm with threshold value = " + str(threshold_value)
    # print "File\t\tNumber of segments"

    root.destroy()
    global number_of_segments, good_metaphases_list, good_metaphases_list_with_coordinates, file_with_good_metaphases, actual_contours_path
    number_of_segments,good_metaphases_list, good_metaphases_list_with_coordinates,segpath = find_good_metaphases(25)
    # print good_metaphases_list
    global originalPath,scoredImages,scoredImagesList, pres_time, rankPlot
    originalPath,scoredImages, pres_time, scoredImagesList, rankPlot = score(segpath)

def after_path_selection(): # after selecting the path
    Label(f2, text=" ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    global threshold_entry
    threshold_entry = Entry(f2, bd =5)
    threshold_entry.insert(1, 10)
    threshold_entry.pack(fill = X)
    b = Button(f2, text = "Run algorithm",command=run)
    b.pack(fill=X)
    info_dialogue_box()
    root.mainloop()

def delete_dialogue_box(text):
    msg = "Are you sure to delete " + os.path.basename(text) + " ?"
    result = tkMessageBox.askquestion("Delete", msg, icon='warning')
    return result

def info_dialogue_box():
    msg = "Please select a score upto which you want to run the algorithm. Default score is set to 10."
    result = tkMessageBox.showinfo("Select a Threshold Value", msg, icon='warning')
    return result

def removekey(d, key):
    r = dict(d)
    if key in r :
        del r[key]
    return r

single = False
def test(event, segments, text, extra=None):
    global single
    if extra == 1:
        single = True
        root.after(500, single_click, event, segments, text)
    elif extra == 101:
        single = False
        click('double click', event, segments, text)

def single_click(event, segments, text):
    global single
    if single:
        single = False
        click('single click', event, segments, text)

# def create(root):
#   frm1 = Frame(root,bg = "black", height = 900,width = 40)
#   frm1.pack(side = RIGHT, fill=Y)
#   frm2 = Frame(root,bg = "black", height = 900,width = 40)
#   frm2.pack(side = RIGHT, fill=Y)
#   frm3 = Frame(root,bg = "black", height = 900,width = 40)
#   frm3.pack(side = RIGHT, fill=Y)
#   frm4 = Frame(root,bg = "black", height = 900,width = 40)
#   frm4.pack(side = RIGHT, fill=Y)
#   frm5 = Frame(root,bg = "black", height = 900,width = 40)
#   frm5.pack(side = RIGHT, fill=Y)
#   frm6 = Frame(root,bg = "black", height = 900,width = 40)
#   frm6.pack(side = RIGHT, fill=Y)
class disp_segment:

    def __init__(self,root,image,i):
        if 0<=i<15:
            self.c = Canvas(frm1, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        if 15<=i<30:
            self.c = Canvas(frm2, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        if 30<=i<45:
            self.c = Canvas(frm3, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        if 45<=i<60:
            self.c = Canvas(frm4, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        if 60<=i<75:
            self.c = Canvas(frm5, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        if 75<=i<90:
            self.c = Canvas(frm6, height=60, width = 60)
            self.c.pack(fill=Y,expand=0)
            self.c.pack(fill=Y,expand=0)
            self.c.create_image(0,0,anchor = NW, image = image)
            self.c.image = image
        # self.canvas.pack(fill=X, expand=2)
        # self.canvas.create_image(0,0,anchor = NW, image = image)
        # self.canvas.image = image
def destroy(root):
    for widget in frm1.winfo_children():
        widget.destroy()
    for widget in frm2.winfo_children():
        widget.destroy()
    for widget in frm3.winfo_children():
        widget.destroy()
    for widget in frm4.winfo_children():
        widget.destroy()
    for widget in frm5.winfo_children():
        widget.destroy()
    for widget in frm6.winfo_children():
        widget.destroy()
def show_segments(histPath):
    # root2 = Tkinter.Tk()
    photos = []
    destroy(root)
    i=0
    print histPath
    for file in os.listdir(histPath):
        if file.endswith('.jpg'):
            # print file
            # img = cv2.imread(file)
            img = ImageTk.PhotoImage(Image.open(histPath+file))  # PIL solution
            # canvas2.create_image(20*i, 60*j, anchor=NW, image=img)
            # canvas2.photo = img
      #         frm1.destroy()
            # frm2.destroy()
            # frm3.destroy()
            # frm4.destroy()
            # frm5.destroy()
            # frm6.destroy()
            # create(root)
            
            disp_segment(root,img,i)
            # photos.append(img)
            i+=1
            # if i==8:
            #   j+=1
            #   i=0
    # root2.mainloop()
    # i,j=10,10
    # # # print len(photos)
    # # # canvas2.delete("all")
    # # # canvas2.pack(fill=X, expand=0) # expand
    # for photo in photos:
    #   # print type(photo)
    #   canvas2.create_image(20*i, 60*j, anchor=NW, image=photo)
    #   canvas2.photo = photo
    #   break
    #   i+=1
    #   if i==8:
    #       j+=1
    #       i=0




def click(msg, event, segments, text):
    global path
    if msg == 'single click':

        dir = os.path.dirname(text)
        segment_path = dir+'/segments/'
        print os.path.basename(text), msg
        global histPath
        # histPath = path

        filename_ext = os.path.splitext(basename(text))[0]
        histPath = dir + "/results_" + filename_ext + '/actual/'
        # print histPath
 

        show_segments(histPath)
        # photos = []
        # i,j=0,0
        # for file in os.listdir(histPath):
        #   if file.endswith('.jpg'):
        #       photos.append(file)
        # n = len(photos)
        # for x in xrange(n):
        #   print photos[x]
        #   image = Image.open(histPath+photos[x])
        #   image = ImageTk.PhotoImage(image)
        #   canvas2.create_image(30*i,30*j,image = image, anchor = NW)
        #   canvas2.image = image
        #   j+=1
        #   if j==8:
        #       j=0
        #       i+=1
        # ''''''

        canvas.delete("all")
        # print text
        path = text
        canvas.pack(fill=Tkinter.BOTH, expand=2) # expand
        image = Image.open(segment_path+os.path.basename(text))
        
        width, height = image.size
        topleft = (600,500)
        bottomright = (2000,1600)
        cropped = image.crop((topleft[0], topleft[1], bottomright[0], bottomright[1]))
        width = bottomright[0] - topleft[0]
        height = bottomright[1] - topleft[1]
        image = cropped.resize((int(width/1.4), int(height/1.4)), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        # print type(photo)
        canvas.create_image(0, 0, image = photo, anchor = NW)
        canvas.photo = photo
        image_name_entry.delete(0, 'end')
        image_name_entry.insert(0, os.path.basename(text))
        class1_entry.delete(0, 'end')
        class1_entry.insert(0, segments[0])
        class2_entry.delete(0, 'end')
        class2_entry.insert(0, segments[0])
        class3_entry.delete(0, 'end')
        class3_entry.insert(0, segments[0])
        class4_entry.delete(0, 'end')
        class4_entry.insert(0, segments[0])
        number.delete(0, 'end')
        number.insert(0, int(segments))
        metaphaseScore.delete(0, 'end')
        metaphaseScore.insert(0,str(scoredImages[filename_ext][0])+ " out of 10")
        rank.delete(0, 'end')
        rank.insert(0, str(scoredImagesList.index(filename_ext)+1) + " out of " + str(len(scoredImages)))   
        # canvas2.delete_dialogue_boxe("all")
        # 
        
        


    elif msg == 'double click':
        result = delete_dialogue_box(text)
        if result == 'yes':
            image = Image.open(text)
            width, height = image.size
            topleft = (600,500)
            bottomright = (2000,1600)
            cropped = image.crop((topleft[0], topleft[1], bottomright[0], bottomright[1]))
            width = bottomright[0] - topleft[0]
            height = bottomright[1] - topleft[1]
            image = cropped.resize((int(width/1.4), int(height/1.4)), Image.ANTIALIAS)
            # photo = ImageTk.PhotoImage(image)
            image.paste(red_cross, (100, 100), red_cross)
            image = image.resize((100,100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            event.widget.config(image=photo,width="100",height="100")
            images.append(photo)
            print "DELETING " + os.path.basename(text)
            global good_metaphases_list, good_metaphases_list_with_coordinates
            good_metaphases_list = removekey(good_metaphases_list, text)
            good_metaphases_list_with_coordinates = removekey(good_metaphases_list_with_coordinates, text) 
            # good_metaphases_entry.delete(0, 'end')
            # good_metaphases_entry.insert(0, len(good_metaphases_list))

            dir = os.path.dirname(text)
            filename_ext = os.path.splitext(basename(text))[0]
            newpath = dir + "/results_" + filename_ext
            # print newpath
            shutil.rmtree(newpath)
    elif msg == 'display original':
        # image.close()
        dir = os.path.dirname(text)
        segment_path = dir+'/segments/'
        print path, msg
        canvas.delete("all")
        print text
        # path = text
        canvas.pack(fill=Tkinter.BOTH, expand=2) # expand
        image = Image.open(path)
        # canvas2.delete("all")
        print text
        path = text
        
        # global histPath
        # histPath = path

        filename_ext = os.path.splitext(basename(text))[0]
        histPath = dir + "/results_" + filename_ext + '/actual/'
        width, height = image.size
        topleft = (600,500)
        bottomright = (2000,1600)
        cropped = image.crop((topleft[0], topleft[1], bottomright[0], bottomright[1]))
        width = bottomright[0] - topleft[0]
        height = bottomright[1] - topleft[1]
        image = cropped.resize((int(width/1.4), int(height/1.4)), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image = photo, anchor = NW)
        canvas.photo = photo
        canvas.bind("<B1-Motion>", paint)
        # image_name_entry.delete(0, 'end')
        # image_name_entry.insert(0, os.path.basename(text))
        # class1_entry.delete(0, 'end')
        # class1_entry.insert(0, segments[0])
        # class2_entry.delete(0, 'end')
        # class2_entry.insert(0, segments[1])
        # class3_entry.delete(0, 'end')
        # class3_entry.insert(0, segments[2])
        # class4_entry.delete(0, 'end')
        # class4_entry.insert(0, segments[3])
        number.delete(0, 'end')
        # number.insert(0, int(segments[0])+int(segments[1])+int(segments[2])+int(segments[3]))   
    elif msg=='display ranks':
        plt.bar(range(1,len(rankPlot)+1),rankPlot)
        plt.title('Rank Statistics')
        plt.ylabel('Number of metaphases')
        plt.xlabel('Score of metaphase')
        plt.grid(True,color='k')
        plt.show()
        # os.system("libreoffice scoredData_%s.xlsx"%pres_time)



    return histPath
def paint( event ):
    print "draw"
    python_green = "#476042"
    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
    canvas.create_oval( x1, y1, x2, y2, fill = python_green )
# def pathforhist():
#     global histPath
#     histPath = click('single click', event, segments, text)
#     return histPath

def dicentric_info_dialogue_box():
    msg = "no. of Dicentric Chromosomes found = 25."
    result = tkMessageBox.showinfo("Dicentric Chromosomes", msg, icon='warning')
    return result

def make_widgets_and_labels(f2, f3):
    # widgets in f2
    Label(f2, text=" ", bg="gray", fg="black", width = 50).pack(fill=X, pady=10)
    good_metaphases_entry = Entry(f2, bd =5)
    good_metaphases_entry.insert(0, no_of_good_metaphases)
    good_metaphases_entry.pack(fill = X)
    def rerun():
        print "Rerun! Algorithm."
        root.destroy()
        print os.getcwd()
        os.chdir('..')
        os.chdir('..')
        os.system('python test_combining.py')


    b = Button(f2, text = "Re-run the algorithm for refined score",command=rerun)
    b.pack(fill=X)

    # widgets in f3
    Label(f3, text="Selected Image : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    image_name_entry = Entry(f3, bd =5)
    image_name_entry.pack(fill = X)
    # Label(f3, text="Objects in Class 1 : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    class1_entry = Entry(f3, bd =5)
    # class1_entry.pack(fill = X)
    # Label(f3, text="Objects in Class 2 : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    class2_entry = Entry(f3, bd =5)
    # class2_entry.pack(fill = X)
    # Label(f3, text="Objects in Class 3 : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    class3_entry = Entry(f3, bd =5)
    # class3_entry.pack(fill = X)
    # Label(f3, text="Objects in Class 4 : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    class4_entry = Entry(f3, bd =5)
    # class4_entry.pack(fill = X)
    Label(f3, text="Total segments : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    number = Entry(f3, bd =5)
    number.pack(fill = X)

    Label(f3, text="Score : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    metaphaseScore = Entry(f3, bd =5)
    metaphaseScore.pack(fill = X)

    Label(f3, text="Rank : ", bg="gray", fg="black", width = 25).pack(fill=X, pady=10)
    rank = Entry(f3, bd =5)
    rank.pack(fill = X)
    def refine():

        print "Detection of Dicentrics Initiated"
        # p = os.system('python hist.py')
        # print histPath
        # root.destroy()
        resultdc = histPath + 'dc/'
        # create_dir(resultdc)
        result = histPath + 'mc/'
        # create_dir(result)
        for file in os.listdir(histPath):
            # DCcount=0
            if file.endswith('.jpg'):
            # print file
                image = skimage.color.rgb2gray(skimage.io.imread(histPath+file))

                fig, axs = plt.subplots(2,1, figsize=(12, 8), frameon = False)
                total=[]
                h=image.shape[0]
                w=image.shape[1]
                a=6
                for x in xrange(min(10,h/a),h-min(10,h/a)):
                    s=0
                    for y in xrange(w):
                        s+=image[x][y]
                    total.append(s)

                
                # temp = total
                avg = [sum(total)/len(total)]*len(total)
                # print file,avg
                # avg = [np.median(total)]*len(total)
                T = list(range(len(total)))
                t = np.array(T)
                power = np.array(total)
                totalnew = np.linspace(t.min(),t.max(),10000)
                power_smooth = spline(t,power,totalnew)
                ax = axs[1]
                plt.plot(totalnew,power_smooth)
                ax.plot(t,avg)
                # plt.show()
                # mx = [max(total)]*len(total)
                # plt.plot(t,mx)
                

                index = []
                temp=0
                for i in xrange(1,len(total)-1):
                    if total[i]>total[i-1] and total[i]>total[i+1]:
                        index.append(i)
                # print index
                if len(index)==0:
                    continue
                for x in xrange(len(index)):
                    plt.scatter(index[x],total[index[x]])


                cm = []

                for x in xrange(1,len(index)):
                    for y in xrange(x):
                        if total[index[y]]<total[index[x]]:
                            temp = index[y]
                            index[y] = index[x]
                            index[x] = temp

                mx = [total[index[0]]]*len(total)
                plt.plot(t,mx)
                cent1 = index[0]
                ax=axs[0]
                cm1 = (w/2,min(10,h/a)+cent1)
                cv2.circle(image,cm1,3,(0,1,0),-1)
                cm.append(cm1)
                DCcount=0
                # if len(index)>1:
                   #  print file
                   #  # print total[index[1]],avg[0]
                   #  print cent1,index[1],min(10,h/a)
                   #  print total[cent1],total[index[1]],avg[0]
                if len(index)>1 and total[index[1]]>avg[0] and abs(cent1-index[1])>max(10,h/a) and abs(total[cent1]-total[index[1]])<abs(total[index[1]]-avg[0]):
                    mx2 = [total[index[1]]]*len(total)
                    plt.plot(t,mx2)
                    cent2 = index[1]
                    cm2 = (w/2,min(10,h/a)+cent2)
                    cv2.circle(image,cm2,3,(0,1,0),-1)
                    cm.append(cm2)
                    DCcount+=1     
                                
                ax.imshow(image)
                # # print file,index
                if len(cm)==2:
                    print file
                    DCcount+=1
                    plt.savefig(resultdc+file)
                
                else:
                #   print file
                    plt.savefig(result+file)
                plt.close()
        print "Over"
        root.mainloop()

        # print "We are back in test_combining.py"
        # lines = [line.rstrip('\n') for line in open('results.txt')]
        # # print lines
        # # fo = open("metaphases_with_dicentrics.txt", "w")
        # for x in xrange(len(lines)):
        #     temp = lines[x].split(' ')
        #     print temp
        #     dicentrics = []
        #     metaphase_name = temp[0]
        #     for y in xrange(len(temp)):
        #         if y != 0:
        #           dicentrics.append(temp[y])

        #     print metaphase_name, dicentrics
        #     coordinates_list = good_metaphases_list_with_coordinates[fileout()]
        #     # print filename_ext 
        #     actual_image = cv2.imread(fileout())
        #     for m in xrange(len(dicentrics)):
        #         # dicentric_chromosome = os.path.splitext(basename(dicentrics[m]))[0]
        #         dicentric_chromosome = dicentrics[m]
        #         dicentric_chromosome_index = int(dicentric_chromosome)-1
        #         rect = cv2.minAreaRect(coordinates_list[dicentric_chromosome_index])
        #         box = cv2.cv.BoxPoints(rect)
        #         box = np.int0(box)
        #         cv2.drawContours(actual_image,[box],0,(0,0,255),2)
        #         # print x 
        #     filename = metaphase_name + '_actual_image.png'
        #     cv2.imwrite(filename,actual_image)
        #     fo = open(filename,"w")
        #     fo.write(filename)
        #     fo.write("\n")
        #     fo.close()
        #     # print "Written in file"
        # p = os.system('python show_metaphases_containing_dicentrics.py')

        
    b = Button(f3, text = "Detect Dicentrics", command=refine)
    b.pack(fill=X, pady = 30)



    return  image_name_entry, class1_entry, class2_entry, class3_entry, class4_entry, number, metaphaseScore, rank
single = False
def manual_count(event, segments, text, extra=None):
    global single
    if extra == 1:
        single = True
        click('display original', event, segments, text) 
def ranks(event, segments, text, extra=None):
    global single
    if extra == 1:
        single = True
        click('display ranks', event, segments, text) 

    # elif extra == 101:
    #     single = False
    #     click('double click', event, segments, text) 

# global pathforhist
# pathforhist = click('single click', event, segments, text)

if __name__ == "__main__": 
    after_path_selection()

 #    soft_data = openpyxl.load_workbook('SoftDataUpload.xlsx')
    # softsheet = soft_data['SampleSoftData']

    no_of_good_metaphases = len(good_metaphases_list)
    root, f2, f3, scframe, canvas, f4, canvas2, frm1,frm2,frm3,frm4,frm5,frm6 = make_gui_before()
    image_name_entry, class1_entry, class2_entry, class3_entry, class4_entry, number, metaphaseScore, rank = make_widgets_and_labels(f2,f3)
    images = []
    buttons = []
    row_number = 0
    iteration = 0
    for k, v in originalPath.items():
        # print v[0],min_score
        if v[0]>=int(min_score):
        # break
            for x in xrange(len(v)):
                v[x] = str(v[x])
            text = k
            segments = v[1]
            image = Image.open(text)
            image = image.resize((100,100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            btn = Tkinter.Button(scframe.interior, height=1, width=20, relief=Tkinter.FLAT, bg="gray99", fg="purple3",font="Dosis")
            btn.config(image=photo,width="100",height="100")
            btn.grid(row=row_number/2, column=iteration)
            images.append(photo)
            buttons.append(btn)
            iteration = 1-iteration
            row_number+=1
            btn.bind('<Button-1>', lambda event, segments = segments, text=text :test(event,segments,text,1))
            btn.bind('<Double-Button-1>', lambda event, segments = segments, text=text :test(event,segments,text,101))
      


    try:
        b=Button(f3, text = "Count manually")
        b.pack(fill=X, pady = 30)
        b.bind('<Button-1>', lambda event, segments = segments, text=text :manual_count(event,segments,text,1))

        b=Button(f3, text = "Show Rank Statistics")
        b.pack(fill=X, pady = 30)
        b.bind('<Button-1>', lambda event, segments = segments, text=text :ranks(event,segments,text,1))

    except Exception as NameError:
        print "Invalid score threshold"

    

    elapsed_time_secs = time.time() - start_time
    root.mainloop()

    msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    print(msg) 
