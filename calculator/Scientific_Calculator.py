import tkinter as tk
from math import *
import math
import re
import copy

op_format=dict(height=1,width=4,bg='#0F0F0F',fg='white',activebackground='orange',activeforeground='black',font=('Times','10','bold'))    # format of operations' buttons // link for all colors: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
num_format=dict(height=1,width=4,bg='white',fg='black',activebackground='yellow',activeforeground='red',font=('Times','10','bold'))    # format of numbers' buttons
side_func_format=dict(bg='#FF00FF',fg='black',activebackground='orange',activeforeground='black',font=('Times','9','bold'))    # format of numbers' buttons


# Definition of Events' Handlers (or Callback) using class object
class scientific_calculator():
    def __init__(self):
        pass
    
    def close():
        reply=tk.messagebox.askquestion('Quit','Are you sure to close the window?')     # tool using tkinterface to give a message to the user and get answer based on it an action may takes place / askquestion tool gives two possible answers (yes or No)
        if reply=='yes': sci_calc.destroy()         # destroy(): it is a window method to close the window
        
    def thanks(event=None): # event=None is a must so non-clickable widgets can call this function
        if event==None: tk.messagebox.showinfo('Thanks message','Thanks for your evaluation')
        else: 
            string='x='+str(event.x)+', y='+str(event.y)+', num='+str(event.num)+', type='+event.type       #composing the response for the non-clickable widgets by showing some of the event parameters
            tk.messagebox.showinfo('click',string)
        
    def known():
        st_1='I know that not all functions are working right now.'
        st_2='Do you know that not all functions working now?'
        if checkbutton['text']== st_1: checkbutton['text']= st_2    # second wa to change widget properties: as a dictionary key.
        else: checkbutton['text']= st_1
        
    # def working():
    #     open_mess=tk.Tk()
    #     open_mess.title('Welcome message')
        
    #     open_label=tk.Label(open_mess,bg='blue',text='Welcome to my calculator')
    #     open_label.place(x=0,y=0)
        
    #     open_label.after_cancel(show_welcome)
        
    def welcome():
        wel_wind = tk.Tk()
        wel_wind.title('Welcome Window')
        wel_frame=tk.Frame(wel_wind,bg='#FF00FF',height=200,width=200)
        wel_frame.place(x=0,y=0)
        tk.Label(wel_frame,text='Welcome, Have Fun.').place(x=25,y=25)
        wel_frame.after(1500,lambda: wel_wind.destroy())    # destroy the welcome window after a specific time
        
               
    def name_validate(*arg):   # you shounld add *arg --- this function allows alphabitic only for name
        global name_str
        if name_text.get().isalpha(): name_str=name_text.get() 
        else: name_text.set(name_str)
        
    def about():
        tk.messagebox.showinfo('About Scientific Calculator','This is a scientific calculator for the AI Diploma.\nCreated by: Eng. Ayman Sayed\nSupervisor: Eng. Sara Abdelmaoty')
    
    def quit_calc(event=None):  # event=None should be added so that hotkey works
        if tk.messagebox.askyesno('Quit Scientific Calculator','Are you sure to quit scientific calculator?'):
            sci_calc.destroy()
    
    def new():
        pass
    
    
    def result():
       try:
           global counter
           global answer
           counter+=1
           text.set('# operations: '+ str(counter))
           cur_val=calc_entry.get()
           calc_entry.delete(0,tk.END)
           answer=eval(scientific_calculator.res_eq(cur_val))
           calc_entry.insert(0,answer)
       except ZeroDivisionError: calc_entry.insert(0,'Division by zero is not allowed')
       except: calc_entry.insert(0,'Error')
       
    def operation(event):
        pass
    
    def click(to_print):
        old_val=calc_entry.get()
        calc_entry.delete(0,tk.END)
        calc_entry.insert(0,old_val+to_print)
        return
    
    def res_eq(entry_val):
    
        sin_reg=re.compile(r'(.*)(sin\()(\d*)(\))(.*)')
        cos_reg=re.compile(r'(.*)(cos\()(\d*)(\))(.*)')
        tan_reg=re.compile(r'(.*)(tan\()(\d*)(\))(.*)')
        ln_reg=re.compile(r'(.*)(ln\()(.*)(\))(.*)')
        
        for i in range(entry_val.count('sin')):    
            if sin_reg.search(entry_val) :
                eq=list(sin_reg.findall(entry_val)[0])
                eq[1]='math.sin(radians('
                eq[3]='))'
                entry_val=''.join(eq)
                
        for i in range(entry_val.count('cos')):    
            if cos_reg.search(entry_val) :
                eq=list(cos_reg.findall(entry_val)[0])
                eq[1]='math.cos(radians('
                eq[3]='))'
                entry_val=''.join(eq)
        
        for i in range(entry_val.count('tan')):    
            if tan_reg.search(entry_val) :
                eq=list(tan_reg.findall(entry_val)[0])
                eq[1]='math.tan(radians('
                eq[3]='))'
                entry_val=''.join(eq)
        
        bef_ln=entry_val.replace('^','**').replace('log','log10').replace('π','(22/7)')
        
        for i in range(bef_ln.count('ln')):    
            if ln_reg.search(bef_ln) :
                eq=list(ln_reg.findall(entry_val)[0])
                eq[1]='math.log('
                eq[3]=',math.e)'
                bef_ln=''.join(eq)
        
        return bef_ln

    def A_mat_grid(*args):
        
        global A_mat_frame,A_matrix,A_col_entry,A_row_entry,A_mat_entry
      
        A_mat_frame.destroy()
        A_mat_frame=tk.Frame(sci_calc,bg='gray',width=100,height=100)
        A_mat_frame.place(x=600,y=140)
        
        A_matrix=[]
        for i in range(int(A_row_entry.get())):        
            A_matrix.append([])   
            for j in range(int(A_col_entry.get())):
                A_matrix[i].append(0)
        
        
        for i in range(int(A_row_entry.get())):           
            for j in range(int(A_col_entry.get())):
                A_mat_entry=tk.Entry(A_mat_frame,bg='white')
                A_mat_entry.grid(row=i,column=j)
                A_mat_entry.bind('<Return>',scientific_calculator.A_mat_list)
                
    
    def A_mat_list(*args):
        global switch3
        switch3.set(0)
        A_col=A_mat_entry.focus_get().grid_info()['column']
        A_row=A_mat_entry.focus_get().grid_info()['row']
        A_matrix[A_row][A_col]= int(A_mat_entry.focus_get().get())
        
        
       
        
    def B_mat_grid(*args):
        
        global B_mat_frame,B_matrix,B_col_entry,B_row_entry,B_mat_entry
      
        B_mat_frame.destroy()
        B_mat_frame=tk.Frame(sci_calc,bg='gray',width=100,height=100)
        B_mat_frame.place(x=980,y=140)
        
        B_matrix=[]
        for i in range(int(B_row_entry.get())):        
            B_matrix.append([])   
            for j in range(int(B_col_entry.get())):
                B_matrix[i].append(0)
        
        
        for i in range(int(B_row_entry.get())):           
            for j in range(int(B_col_entry.get())):
                B_mat_entry=tk.Entry(B_mat_frame,bg='white')
                B_mat_entry.grid(row=i,column=j)
                B_mat_entry.bind('<Return>',scientific_calculator.B_mat_list)
                
    
    def B_mat_list(*args):
        global switch3
        switch3.set(0)
        B_col=B_mat_entry.focus_get().grid_info()['column']
        B_row=B_mat_entry.focus_get().grid_info()['row']
        B_matrix[B_row][B_col]= int(A_mat_entry.focus_get().get())
    
    
    def show_result(result,res_row,res_col):
        global c_mat_frame
        scientific_calculator.clear_result()
        c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
        c_mat_frame.place(x=800,y=300)
        
        for i in range(res_row):           
            for j in range(res_col):
                c_mat_entry=tk.Entry(c_mat_frame,bg='white')
                c_mat_entry.grid(row=i,column=j)
                c_mat_entry.insert(0,result[i][j])
        
    def clear_result():
        try : c_mat_frame.destroy()
        except: None
        
        
    def mat_sum():
        global c_mat_frame
        if (A_row_entry.get()==B_row_entry.get() and A_col_entry.get()==B_col_entry.get()):
            c=[]
            c_row,c_col=int(A_row_entry.get()),int(A_col_entry.get())
            for i in range(c_row):
                c.append([])
                for j in range(c_col):
                    c[i].append(A_matrix[i][j]+B_matrix[i][j])
                    
            scientific_calculator.show_result(c,c_row,c_col)
            
        else:
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=300)
            tk.Label(c_mat_frame,text='A & B should be of the same size for sum.').grid(row=0,column=0)
             
    
    def mat_sub():
        global c_mat_frame
        
        if (A_row_entry.get()==B_row_entry.get() and A_col_entry.get()==B_col_entry.get()):
            c=[]
            c_row,c_col=int(A_row_entry.get()),int(A_col_entry.get())
            for i in range(c_row):
                c.append([])
                for j in range(c_col):
                    c[i].append(A_matrix[i][j]-B_matrix[i][j])
                    
            scientific_calculator.show_result(c,c_row,c_col)
            
        else:
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=300)
            tk.Label(c_mat_frame,text='A & B should be of the same size for sub.').grid(row=0,column=0)
     
    
    def mat_dot():
        if (A_col_entry.get()==B_row_entry.get()):
            c=[]
            c_row,c_col=int(A_row_entry.get()),int(B_col_entry.get())
            for i in range(c_row):
                c.append([])
                for k in range(c_col):
                    value=0
                    for j in range(int(A_col_entry.get())):
                        value+=A_matrix[i][j]*B_matrix[j][k]
                    c[i].append(value)
                    
            scientific_calculator.show_result(c,c_row,c_col)
            
        else:
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=300)
            tk.Label(c_mat_frame,text='No. of A colums should equal No. of B rows for dot product.').grid(row=0,column=0)
    
    
    def row_exchange(i):
        global A,I,B_matrix,B
        
        
        for m in range(i,int(A_row_entry.get())):
            if A[m][m]==0:
                for n in range(i+1,int(A_row_entry.get())):
                    if A[m][n] != 0 and A[n][m] != 0 :
                        A[m],A[n] =  A[n],A[m]
                        if i==0:
                            try:B[m],B[n] =  B[n],B[m]
                            except NameError: None
                        if i>0: I[m],I[n] =  I[n],I[m]
                        break
    
    
    def mat_inverse():
        global A_inverse,I,A,B
        if (scientific_calculator.det(A_matrix)==0):
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=300)
            tk.Label(c_mat_frame,text='No inverse as |A| = 0').grid(row=0,column=0)
            return
        I=[] # Identity marix
        for i in range(int(A_row_entry.get())):        
            I.append([])   
            for j in range(int(A_col_entry.get())):
                if (i==j): I[i].append(1)  
                else: I[i].append(0)
        
        A=copy.deepcopy(A_matrix)
        try: B=copy.deepcopy(B_matrix)
        except: None
        scientific_calculator.row_exchange(0)
        rows,columns=len(A),len(A[0])
        
        for i in range(rows):
            if i>0: scientific_calculator.row_exchange(i)
            pivot=A[i][i]
            for j in range(columns):
                A[i][j] /= pivot
                I[i][j] /= pivot
                
            for k in range(rows):
                if i==k: continue
                else:
                    value=A[k][i]
                    for m in range(columns):
                        A[k][m] += -1*value*A[i][m]
                        I[k][m] += -1*value*I[i][m]
        A_inverse=I.copy()

        scientific_calculator.show_result(A_inverse,rows,columns)
            
    def sys_eqs():
        global B
        if (len(A_inverse[0])==int(B_row_entry.get())):
            c=[]
            c_row,c_col=len(A_inverse),int(B_col_entry.get())
            for i in range(c_row):
                c.append([])
                for k in range(c_col):
                    value=0
                    for j in range(len(A_inverse[0])):
                        value+=A_inverse[i][j]*B[j][k]
                    c[i].append(value)
                    
            scientific_calculator.show_result(c,c_row,c_col)
            
        else:
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=300)
            tk.Label(c_mat_frame,text='No. of A colums should equal No. of B rows for dot product.').grid(row=0,column=0)
         
    def A_det():
        global A_matrix
        try: 
            determinant = scientific_calculator.det(A_matrix)
            scientific_calculator.clear_result()
            c_mat_frame=tk.Frame(sci_calc,bg='gray',width=300,height=300)
            c_mat_frame.place(x=800,y=270)
            tk.Label(c_mat_frame,text=f'Determinant of matrix A = {determinant}').grid(row=0,column=0)
        except: None
    
    def det(matrix):
        global d
        if len(matrix)==1:
            return (matrix[0][0])
        
        if len(matrix)==2:
            return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
        
        for i in range(len(matrix)):
            a=copy.deepcopy(matrix)
            a.pop(0)
            for j in range(len(a)):
                del a[j][i]
            
            d += ((-1)**i)*matrix[0][i]*scientific_calculator.det(a)
        return d
d=0
        
        
       
    
# Window generation & configuration
sci_calc = tk.Tk()      #making the window for our application, it won't be visible untill you invoke the event controller using mainloop()
sci_calc.title('Scientific Calculator / By: Ayman Sayed / Suprvisor: Sara Abdelmoaty')      #giving a title to the window
sci_calc.geometry('1350x550')    # determine the size of the window when first shown
# sci_calc.minsize(width=580,height=550)  # setting a minimum size for the window so user can't minimize more than it
# sci_calc.maxsize(width=580,height=550)  # setting maximum size
# sci_calc.resizable(width=False,height=False) # preventing changing window size
sci_calc.protocol('WM_DELETE_WINDOW',scientific_calculator.quit_calc)   # binding closing the window using x_button to a callback

calc_canvas=tk.Canvas(sci_calc,width=260,height=530)    # canvas is like a drawing you determine its cordinate to be able to draw over it after that inside this area
calc_canvas.place(x=0,y=0)
calc_canvas.create_rectangle(3,3,260,530,outline='black',width=3,fill='yellow')     #drawing a rectangle by two corners
calc_canvas.create_line(0,95,280,95,width=3)    # drawing a line (fill,arrow,smooth) are other parameters of the line

label=tk.Label(sci_calc,bg='gray',fg='white',text='Note: Not all functions are working.')    # making a non-clickable text which is a label
label.place(x=30,y=5)        # Placing the label in a specific position inside the window

frame=tk.Frame(sci_calc,bg='blue',height=5,width=194)    # making a nother  non-clickable text which is a frame (it's only a colored area till now)
frame.place(x=30,y=25)        # Placing the frame in a specific position inside the window

switch = tk.IntVar()        # this method is used t store an integer value and it manages communication between widgets which can't be done without this method (so regular assignment operation can't be used here for this job)
switch.set(0)       # putting the integer value using set() methid

checkbutton=tk.Checkbutton(sci_calc,side_func_format,text='Do you know that not all functions working now?',variable=switch,command=scientific_calculator.known) # making a checkbox and connect it to swich widget so when be checked the switch will be 1 and when be unchecked it will be 0
checkbutton.place(x=280,y=450)      # as the switch value set to 1, the checkbutton will be checked in the window. if switch is set to any other value checkbutton will be unchecked.

calc_entry=tk.Entry(sci_calc,width=38,borderwidth=5,relief='sunken')   # Entry widget, so user can enter data through it
calc_entry.place(x=15,y=45)
# calc_entry.bind('<Button-1>',scientific_calculator.operation)

label_2=tk.Label(sci_calc,side_func_format,text='Please rate the calculator perfarmance')    
label_2.bind("<Button-1>",scientific_calculator.thanks)      # connect/bind the non-clickable widgets to a callback
label_2.place(x=280,y=358)
switch2=tk.IntVar()
switch2.set(0)
radiobutton_1=tk.Radiobutton(sci_calc,text='well',variable=switch2,value=1,command=scientific_calculator.thanks)     # making a choices and connect them to a switch widget sochoosing them will depend on the value attribute inside the difinition
radiobutton_1.place(x=280,y=380)
radiobutton_1['cursor']='heart'  # changing the mouse pointer shape over this widget
radiobutton_2=tk.Radiobutton(sci_calc,text='accepted',variable=switch2,value=2,command=scientific_calculator.thanks)
radiobutton_2.place(x=280,y=400)
radiobutton_3=tk.Radiobutton(sci_calc,text='poor',variable=switch2,value=3,command=scientific_calculator.thanks)
radiobutton_3.place(x=280,y=420)

close=tk.Button(sci_calc,side_func_format,text='Close the calculator',command=scientific_calculator.close,bg='#FF00FF',fg='black',activebackground='orange',activeforeground='black')
close.place(x=280,y=500)
close['borderwidth']=5      # some widget parameter (there are other parameters in the pdf)
close['cursor']='clock'
# close.config(command=lambda:None,text='new text')  # changing any value of the widget properties using config() method
# close.cget('text')    # get the value of any widget property using cget('name of the property')
# label_2.unbind("<Button-1>")         # unbind the non-clickable widget
# sci_calc.bind_all(event,callback)    # bind all the existing widgets to the same callback 
# sci_calc.unbind_all(event,callback)  # unbind all the existing widgets to the same callback  

note_label_frame=tk.LabelFrame(sci_calc,bg='#FF00FF',width=185,height=40,text='Note:',labelanchor='nw')  # making a labelframe (it is a frame with border and title)
note_label_frame.place(x=280,y=10)
tk.Label(note_label_frame,bg='#0F0F0F',fg='white',text='Take a look on the below column.',font=('Times','9','bold')).place(x=0,y=0)

info_label_frame=tk.LabelFrame(sci_calc,bg='#FF00FF',width=185,height=40,text='Personal info.:',labelanchor='nw')
info_label_frame.place(x=280,y=70)
tk.Label(info_label_frame,bg='#FF00FF',fg='black',text='Name:',font=('Times','9','bold')).place(x=0,y=0)
name_text=tk.StringVar()
name_entry=tk.Entry(info_label_frame,textvariable=name_text,width=20)   
name_entry.place(x=40,y=0)
name_text.trace('w',scientific_calculator.name_validate)
name_str=''
name_text.set(name_str)

main_menu=tk.Menu(sci_calc)     # creating a main menu
sci_calc.configure(menu=main_menu)  # adding the main menu to the application
sub_menu_file=tk.Menu(main_menu,tearoff=0)    # creating a sub-menu for a specific main menu   & tearoff=0 to hide the dashed line appears on the submenu
main_menu.add_cascade(label='File',menu=sub_menu_file,underline=0)  # adding the sub-menu to the main menu the underline value sets a shortcut for this menu and its sub menus by the character with this index (Alt + this character)
sub_menu_about=tk.Menu(main_menu)
main_menu.add_command(label='About',command=scientific_calculator.about) # adding a sub-menu to the main menu but as a command
# file_menu=tk.Menu(sub_menu_file)    # components of file menu this if you want to add a nother sub-menu to the sub-menu
sub_menu_file.add_command(label='New',command=scientific_calculator.new,underline=0)   # adding the components of the file menu
sub_menu_file.add_separator()   # add a separator line here in the sub-menu
sub_menu_file.add_command(label='Quit',underline=0,command=scientific_calculator.quit_calc,accelerator='Ctrl-Q')  # accelerated property shows the hotkey for this command beside it in the menu
sci_calc.bind_all("<Control-q>",scientific_calculator.quit_calc)    # binding the hotkey to a specific funnction

counter=0
text=tk.StringVar()
no_result=tk.Message(sci_calc,bg='#FF00FF',fg='black',textvariable=text,width=100,font=('Times','9','bold')).place(x=280,y=320)    # make a string obsevable variable  and use it to show dynamic text on screen by connecting it to textvariable property of label (not text property) -- message method when reach the width it will wrap the ext automaticlly this is the different from the lebel widget
text.set('# operations: '+ str(counter))


# Non-working Buttons
shift=tk.Button(sci_calc,op_format,text='shift',state='disabled')    #making button object but it won't be visible untill you use a window method to determine where to place it inside the window
shift.place(x=15,y=100)     #make the button object visible inside the window at specific location / there are two other methods (pack & grid) to put the buttoon inside the window...but ONLY one method of the three should be used for all widgets' objects in one application
alpha=tk.Button(sci_calc,op_format,text='alpha',state='disabled')   # state property making the button inactive 
alpha.place(x=55,y=100)
Replay=tk.Button(sci_calc,op_format,text='Replay',height=5,width=9,state='disabled')
Replay.place(x=95,y=100)
# Replay['anchor']='n'      # position of the text inside the widget (center by default)
mode=tk.Button(sci_calc,op_format,text='mode',state='disabled')
mode.place(x=175,y=100)
calc=tk.Button(sci_calc,op_format,text='calc',state='disabled')
calc.place(x=15,y=150)
integration=tk.Button(sci_calc,op_format,text='int',state='disabled')
integration.place(x=55,y=150)
div=tk.Button(sci_calc,op_format,text='(/)',state='disabled')
div.place(x=15,y=200)
dash=tk.Button(sci_calc,op_format,text='(--)',state='disabled')
dash.place(x=175,y=200)
hyp=tk.Button(sci_calc,op_format,text='hyp',state='disabled')
hyp.place(x=175,y=150)
RCL=tk.Button(sci_calc,op_format,text='RCL',state='disabled')
RCL.place(x=95,y=200)
ENG=tk.Button(sci_calc,op_format,text='ENG',state='disabled')
ENG.place(x=135,y=200)
M_=tk.Button(sci_calc,op_format,text='M+',state='disabled')
M_.place(x=55,y=200)
log_x_base=tk.Button(sci_calc,op_format,text='log_b',state='disabled')
log_x_base.place(x=215,y=150)


# higher operations & Constants
sin=tk.Button(sci_calc,op_format,text='sin',command=lambda: scientific_calculator.click('sin('))
sin.place(x=135,y=250)
cos=tk.Button(sci_calc,op_format,text='cos',command=lambda: scientific_calculator.click('cos('))
cos.place(x=175,y=250)
tan=tk.Button(sci_calc,op_format,text='tan',command=lambda: scientific_calculator.click('tan('))
tan.place(x=215,y=250)
mul_10_to_power=tk.Button(sci_calc,op_format,text='*10^',command=lambda: scientific_calculator.click('*10^'))
mul_10_to_power.place(x=115,y=500)
left_arc=tk.Button(sci_calc,op_format,text='(',command=lambda: scientific_calculator.click('('))
left_arc.place(x=95,y=300)
right_arc=tk.Button(sci_calc,op_format,text=')',command=lambda: scientific_calculator.click(')'))
right_arc.place(x=135,y=300)
x_1=tk.Button(sci_calc,op_format,text='x-¹',command=lambda: scientific_calculator.click('^-1'))
x_1.place(x=95,y=250)
root=tk.Button(sci_calc,op_format,text='√',command=lambda: scientific_calculator.click('^0.5'))
root.place(x=215,y=300)
square=tk.Button(sci_calc,op_format,text='x²',command=lambda: scientific_calculator.click('^2'))
square.place(x=15,y=300)
power=tk.Button(sci_calc,op_format,text='xⁿ',command=lambda: scientific_calculator.click('^'))
power.place(x=55,y=300)
log=tk.Button(sci_calc,op_format,text='log',command=lambda: scientific_calculator.click('log('))
log.place(x=15,y=250)
ln=tk.Button(sci_calc,op_format,text='ln',command=lambda: scientific_calculator.click('ln('))
ln.place(x=55,y=250)
pi=tk.Button(sci_calc,op_format,text='π',command=lambda: scientific_calculator.click('π'))
pi.place(x=175,y=300)
e_val=tk.Button(sci_calc,op_format,text='e',command=lambda: scientific_calculator.click('e'))
e_val.place(x=215,y=200)


# control buttons (AC,DEL,Ans,on,=)
AC=tk.Button(sci_calc,op_format,text='AC',bg='#00FFFF',fg='black',command=lambda: calc_entry.delete(0,tk.END) )
AC.place(x=215,y=350)
delete=tk.Button(sci_calc,op_format,text='DEL',bg='#00FFFF',fg='black',command=lambda: calc_entry.delete(len(calc_entry.get())-1,tk.END))
delete.place(x=165,y=350)
Ans=tk.Button(sci_calc,op_format,text='Ans',command=lambda: calc_entry.insert(0,answer))
Ans.place(x=165,y=500)
equal=tk.Button(sci_calc,op_format,text='=',command=scientific_calculator.result)
equal.place(x=215,y=500)
on=tk.Button(sci_calc,op_format,state='active',text='on',bg='orange',fg='black',command=scientific_calculator.welcome)#,command=scientific_calculator.working)
on.place(x=215,y=100)
# show_welcome=on.after(100,scientific_calculator.working)    # this to apply a specific function after a specific time from implementing this widget property.
# on.after_cancel(show)  # to cancel the after object created before 


# simple operations(+,-,*,/)
add=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('+'),text='+')
add.place(x=165,y=450)
sub=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('-'),text='-')
sub.place(x=215,y=450)
mul=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('*'),text='x')
mul.place(x=165,y=400)
div=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('/'),text='/')
div.place(x=215,y=400)


# Numbers & decimal point
zero=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('0'),text='0',activebackground='yellow',activeforeground='red')
zero.place(x=15,y=500)
one=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('1'),text='1')
one.place(x=15,y=450)
two=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('2'),text='2')
two.place(x=65,y=450)
three=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('3'),text='3')
three.place(x=115,y=450)
four=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('4'),text='4')
four.place(x=15,y=400)
five=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('5'),text='5')
five.place(x=65,y=400)
six=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('6'),text='6')
six.place(x=115,y=400)
seven=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('7'),text='7')
seven.place(x=15,y=350)
eight=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('8'),text='8')
eight.place(x=65,y=350)
nine=tk.Button(sci_calc,num_format,command=lambda: scientific_calculator.click('9'),text='9')
nine.place(x=115,y=350)
dot=tk.Button(sci_calc,op_format,command=lambda: scientific_calculator.click('.'),text='.',activebackground='yellow',activeforeground='red')
dot.place(x=65,y=500)


# Matrices

switch3=tk.IntVar()
switch3.set(0)


tk.Radiobutton(sci_calc,text='|A|',variable=switch3,value=6,command=scientific_calculator.A_det).place(x=600,y=280)
tk.Radiobutton(sci_calc,text='A + B',variable=switch3,value=1,command=scientific_calculator.mat_sum).place(x=600,y=300)
tk.Radiobutton(sci_calc,text='A - B',variable=switch3,value=2,command=scientific_calculator.mat_sub).place(x=600,y=320)
tk.Radiobutton(sci_calc,text='A.B',variable=switch3,value=3,command=scientific_calculator.mat_dot).place(x=600,y=340)
tk.Radiobutton(sci_calc,text='Inverse(A)',variable=switch3,value=4,command=scientific_calculator.mat_inverse).place(x=600,y=360)
tk.Radiobutton(sci_calc,text='Inverse(A).B\nsystem of eqs',variable=switch3,value=5,command=scientific_calculator.sys_eqs).place(x=600,y=380)
tk.Label(sci_calc,text='for solving system of equations use (Inverse(A).B) ').place(x=600,y=420)


A_mat_frame=tk.Frame(sci_calc,bg='gray',width=100,height=100)
A_mat_frame.place(x=600,y=140)
A_row_entry=tk.Entry(sci_calc,width=10)
A_row_entry.place(x=670,y=5)
tk.Label(sci_calc,text='A_rows:').place(x=600,y=5)
A_col_entry=tk.Entry(sci_calc,width=10)
A_col_entry.place(x=670,y=30)
tk.Label(sci_calc,text='A_columns:').place(x=600,y=30)
tk.Label(sci_calc,text='after writing each cell value using KEYBOARD, \nyou MUST press ENTER before leaving the call').place(x=600,y=90)
A_button=tk.Button(sci_calc,text='Create Matrix A',command=scientific_calculator.A_mat_grid)
A_button.place(x=600,y=60)


B_mat_frame=tk.Frame(sci_calc,bg='gray',width=100,height=100)
B_mat_frame.place(x=980,y=140)
B_row_entry=tk.Entry(sci_calc,width=10)
B_row_entry.place(x=1052,y=10)
tk.Label(sci_calc,text='B_rows:').place(x=980,y=10)
B_col_entry=tk.Entry(sci_calc,width=10)
B_col_entry.place(x=1052,y=35)
tk.Label(sci_calc,text='B_columns:').place(x=980,y=35)
tk.Label(sci_calc,text='after writing each cell value using KEYBOARD, \nyou MUST press ENTER before leaving the call' ).place(x=980,y=90)
B_button=tk.Button(sci_calc,text='Create Matrix B',command=scientific_calculator.B_mat_grid)
B_button.place(x=980,y=60)












# sci_calc.focus_get()  # get the activated widget right now
on.focus_set()

sci_calc.mainloop()     #all your code must between the window creation and the mainloop(), exiting this means exiting the program GUI










































