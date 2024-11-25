from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
class Sorting_app:
    def __init__(self,root):
        self.root=root
        self.root.title("Sorting Apllication | Developed by MAnn Soni")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="images/folder.png")
        title=Label(self.root,text="Files Sorting Application",padx=10 ,image=self.logo_icon,compound=LEFT,font=("impact",40),bg="#023458",fg="white",anchor="w").place(x=0,y=0,relwidth=1)


        #---------------Section 1----------------------
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=100,height=40,width=600)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=900,y=95,height=45,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=150,height=2,width=1250)

        #--------------Section 2------------------------
        #--------------All Extensions-------------------
        self.image_extensions=["Image Extensions",".png",".jpg",".JPG",".JPEG",".jpeg","jfif"]
        self.audio_extensions=["Audio Extensions",".amr",".mp3"]
        self.video_extensions=["Video Extensions",".mp4",".avi",",mpeg4",".3gp",".mpg",".MPG"]
        self.doc_extensions=["Document Extensions",".doc",".xlsx",".ppt",",pptx",".xls",".pdf",".zip",".rar",".csv",".docx",".txt",".stl",".art",".dxf",".cdr",".rlf",".jdp",".eps",".STL",".RLF",".7z"]
        
        
        self.folders={
            'video':self.video_extensions,
            'audio':self.audio_extensions,
            'images':self.image_extensions,
            'documents':self.doc_extensions,  
        }

        lbl_support_ext=Label(self.root,text="Various Supported Extensions",font=("times new roman",25),bg="white").place(x=50,y=170)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.image_box.place(x=60,y=230,width=270,height=35)
        self.image_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.audio_box.place(x=360,y=230,width=270,height=35)
        self.audio_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.video_box.place(x=700,y=230,width=270,height=35)
        self.video_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15),state="readonly",justify=CENTER)
        self.doc_box.place(x=1010,y=230,width=270,height=35)
        self.doc_box.current(0)
        #-----------------Section 3--------------------
        #-----------------All Images-------------------
        self.image_icon=PhotoImage(file="images/im.png")
        self.audio_icon=PhotoImage(file="images/audio.png")
        self.video_icon=PhotoImage(file="images/videos.png")
        self.document_icon=PhotoImage(file="images/doc.png")
        self.other_icon=PhotoImage(file="images/other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
        self.lbl_total_files=Label(Frame1,text="Total files: ",font=("times new roman",18),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image=Label(Frame1,bd=2,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_image.place(x=20,y=60,width=230,height=200)

        self.lbl_total_audio=Label(Frame1,bd=2,relief=RAISED,image=self.audio_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
        self.lbl_total_audio.place(x=260,y=60,width=230,height=200)

        self.lbl_total_video=Label(Frame1,bd=2,relief=RAISED,image=self.video_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
        self.lbl_total_video.place(x=500,y=60,width=230,height=200)

        self.lbl_total_document=Label(Frame1,bd=2,relief=RAISED,image=self.document_icon,compound=TOP,font=("times new roman",20,"bold"),bg="#DFF02A",fg="white")
        self.lbl_total_document.place(x=740,y=60,width=230,height=200)

        self.lbl_total_other=Label(Frame1,bd=2,relief=RAISED,image=self.other_icon,compound=TOP,font=("times new roman",20,"bold"),bg="GRAY",fg="white")
        self.lbl_total_other.place(x=980,y=60,width=230,height=200)

        #-------------Section 3-------------------
        lbl_status=Label(self.root,text="STATUS",font=("times new roman",25),bg="white").place(x=50,y=620)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=620)
        
        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=620)
        
        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18),bg="white",fg="orange")
        self.lbl_st_left.place(x=700,y=620)

        #----------------Buttons
        self.btn_clear=Button(self.root,text="CLEAR",command=self.clear,bd=4,font=("times new roman",15,"bold"),bg="#607d8b",fg="white",activebackground="#607d8b",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=880,y=610,height=45,width=200)
        
        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="START",bd=4,font=("times new roman",15,"bold"),bg="#ff5722",fg="white",activebackground="#ff5722",cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1100,y=610,height=45,width=200)
        
    def Total_count(self):
        images=0
        audio=0
        video=0
        document=0
        others=0
        self.count=0
        cmbine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name[1]:
                        cmbine_list.append(x)

                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="audio":
                        audio+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="video":
                        video+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="document":
                        document+=1
        #This is for Calculating other files only 
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                ext="."+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audio))        
        self.lbl_total_video.config(text="Total Videos\n"+str(video))
        self.lbl_total_document.config(text="Total Documents\n"+str(document))
        self.lbl_total_other.config(text="Total Others\n"+str(others))
        self.lbl_total_files.config(text="Total File: "+str(self.count))
    
    def browse_function(self):
        op=filedialog.askdirectory(title="Select folder for Sorting")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directry)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            #print(self.all_files)
           
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

            messagebox.showinfo("Success","All Files Has Moved Succesfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please select folder")


    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")        
        self.lbl_total_video.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files")


 
    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder))


    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,self.other_name))


root=Tk()
obj=Sorting_app(root)
root.mainloop()
