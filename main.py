import tkinter as tk


#from mainfunc import main
top = tk.Tk()
#top = tk.Toplevel()
top.title("Exam-checker")
top.geometry("1024x680")
#imgicon = ImageTk.PhotoImage(file=os.path.join(r'D:\study materials\IV-I\MAJOR\codings\partOCR\imgs','nepread.ico'))
#top.tk.call('wm', 'iconphoto', top._w, imgicon)
top.resizable(0,0)
h=300
w=400
#***********************************************************
class variables:
    
    question="Your question appears here"
    qs = "Q. "+question
    key_words=[]
    mrks=0
        
    
    
    
    
    frame2 = tk.Frame(top,highlightbackground="black",
                      highlightcolor="black", highlightthickness=1,bg="white",
                      width="650", height="305", colormap="new",bd="0")
    frame2.place(x=100,y=200)
    frame2.pack_propagate(0)

    
    
    output_txt = tk.Text(frame2)
    output_txt.pack()

   
    L=tk.Label(top,fg="black",text=qs)
    L.place(x=100,y=80)
    L.pack_propagate(0)
    
    
    
    
    L12=tk.Label(top,fg="black",text="Answer:")
    L12.place(x=100,y=180)
    L12.pack_propagate(0)
    
    L20=tk.Label(top,fg="black",text="Marks:")
    L20.place(x=760,y=180)
    L20.pack_propagate(0)
    
    L2=tk.Label(top,fg="black",text=mrks)
    L2.place(x=800,y=180)
    L2.pack_propagate(0)
    #L=tk.Label(frame2,bg="white",fg="green",text="(Your image appears here)")
    #L.pack()
      
#***********************************************************
def design_fun():
    but = tk.Button(top,text ="Start",command=exam_start)#command=lambda:histogram(2))
    but.place(x=1,y=1)
    
    butt = tk.Button(top,text ="Exit",command=exit(0))
    butt.place(x=36,y=1)
        
    
    #top.config(menu=mb)
    
    but1 = tk.Button(top,text ="Next")#command=lambda:histogram(2))
    but1.place(x=680,y=510)
    
    but2 = tk.Button(top,text ="Check",command=check_marks)#command=lambda:histogram(2))
    but2.place(x=750,y=210)
    
#***********************************************************
def exam_start():
    variables.question = "Write about the Nuclear Hazard.(5 marks)"
    
    variables.qs = "Q. "+variables.question
    variables.key_words=['radiation','fusion','fission','explosion','reactor','physiological','somatic','genetic','power plant','accident']
    
    variables.L.pack_forget()
    variables.L=tk.Label(top,fg="black",text=variables.qs)
    variables.L.place(x=100,y=80)
    
    variables.L.pack_propagate(0)
    
#***********************************************************
def check_marks():
    import check_mrks
    a = variables.output_txt.get("1.0",'end-1c')
    b = variables.key_words
    if a != "" :
        variables.mrks = check_mrks.check_marks(a,b)
        variables.L2.pack_forget()
        variables.L2=tk.Label(top,fg="black",text=variables.mrks)
        variables.L2.place(x=800,y=180)
        variables.L2.pack_propagate(0)
    
    
    
    
#***********************************************************    
    
design_fun()


top.mainloop()

