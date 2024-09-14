from BS_Calculator import BS
import numpy as np
from tkinter import *

root = Tk()
root.configure(background='black')
root.title('Black_scholes_Calculator')
root.geometry('450x530')

multiplier=Label(root)

call_price=Label(root)
call_delta=Label(root)
call_gamma=Label(root)
call_vega=Label(root)
call_theta=Label(root)
call_rho=Label(root)

put_price=Label(root)
put_delta=Label(root)
put_gamma=Label(root)
put_vega=Label(root)
put_theta=Label(root)
put_rho=Label(root)



'-----------------------------------------------------------------------------'

frame1=LabelFrame(root,padx = 5,pady =5)
frame1.grid(row=7,column=1, rowspan=6)

call = Label(frame1,
              text ='Call',
              width = 5,
              font= ('Ariel',15),
              fg='white',
              bg ='purple',
              padx=3 )

call.grid(row=0,column=0)

put = Label(frame1,
             text ='Put',
             width = 5, 
             font= ('Ariel',15),
             fg='white',
             bg ='purple',
             padx=3)

put.grid(row=0,column=3)

'-----------------------------------------------------------------------------'

call_frame = LabelFrame(frame1,
                         width=160,
                         height=220,
                         bg='white')

call_frame.grid(row=1,column=0,rowspan=6)

put_frame = LabelFrame(frame1,
                        width=160,
                        height=220,
                        bg='white')

put_frame.grid(row=1,column=3,rowspan=6)

'-----------------------------------------------------------------------------'

def BS_Calculator(event=None):
    global spot, strike, rate, days, vol, multiplier, call_price,call_delta,\
           call_gamma,call_vega,call_theta,call_rho,put_price, put_delta,\
           put_gamma, put_vega, put_theta, put_rho 
    
    option = BS(float(spot.get()),
                int(strike.get()),
                float(Rf_rate.get()),
                int(days.get()),
                float(Volatility.get()),
                float(multiplier.get()))
    
    call_price.pack_forget()
    call_price = Label(call_frame, text=option.call_price(), fg='white',bg='black',font = 25, pady=5)
    call_price.pack()
    
    call_delta.pack_forget()
    call_delta = Label(call_frame, text=option.call_delta(), fg='white',bg='black',font = 25, pady=5)
    call_delta.pack()
    
    call_gamma.pack_forget()
    call_gamma = Label(call_frame, text=option.call_gamma(), fg='white',bg='black',font = 25, pady=5)
    call_gamma.pack()
    
    call_vega.pack_forget()
    call_vega = Label(call_frame, text=option.call_vega(), fg='white',bg='black', font = 25, pady=5)
    call_vega.pack()
    
    call_theta.pack_forget()
    call_theta = Label(call_frame, text=option.call_theta(), fg='white',bg='black',font= 25, pady=5)
    call_theta.pack()
    
    call_rho.pack_forget()
    call_rho = Label(call_frame, text=option.call_rho(), fg='white',bg='black', font = 25, pady=5)
    call_rho.pack()
    
    put_price.pack_forget()
    put_price = Label(put_frame, text=option.put_price(), fg='white',bg='black',font = 25, pady=5 )
    put_price.pack()
    
    put_delta.pack_forget()
    put_delta = Label(put_frame, text=option.put_delta(), fg='white',bg='black',font = 25, pady=5)
    put_delta.pack()
    
    put_gamma.pack_forget()
    put_gamma = Label(put_frame, text=option.put_gamma(), fg='white',bg='black',font = 25, pady=5)
    put_gamma.pack()
    
    put_vega.pack_forget()
    put_vega = Label(put_frame, text=option.put_vega(), fg='white',bg='black', font = 25, pady=5)
    put_vega.pack()
    
    put_theta.pack_forget()
    put_theta = Label(put_frame, text=option.put_theta(), fg='white',bg='black',font= 25, pady=5)
    put_theta.pack()
    
    put_rho.pack_forget()
    put_rho = Label(put_frame, text=option.put_rho(), fg='white',bg='black', font = 25, pady=5)
    put_rho.pack()
    
    multiplier.pack_forget()

    

#spot
spot_name = Label(root,text ='Spot', bg='white', fg='black', font=25, padx=30 ) 
spot_name.grid(row=0,column=0, padx=3,pady=3)

spot = Entry(root, fg = 'red', bg ='black', borderwidth = 5, font = 25, width = 23)
spot.grid(row =0,column=1)
spot.insert(0,1800)

#strike
strike_name = Label(root,text = 'Strike', bg='white', fg = 'black', font = 25, padx = 30 ) 
strike_name.grid(row=1,column=0, padx=3,pady=3)

strike = Entry(root, fg = 'red', bg ='black', borderwidth = 5, font = 25, width = 23)
strike.grid(row =1,column=1)
strike.insert(0,1800)

#riskfree_rate
Rf_rate_name = Label(root,text = 'Rf_rate', bg='white', fg = 'black', font = 25, padx = 30 ) 
Rf_rate_name.grid(row=2,column=0, padx=3,pady=3)

Rf_rate = Entry(root, fg = 'red', bg ='black', borderwidth = 5, font = 25, width = 23)
Rf_rate.grid(row =2,column=1)
Rf_rate.insert(0,0.10)

#days
days_name = Label(root,text = 'Days', bg='white', fg = 'black', font = 25, padx = 30 ) 
days_name.grid(row=3,column=0, padx=3,pady=3)

days = Entry(root, fg = 'red', bg ='black', borderwidth = 5, font = 25, width = 23)
days.grid(row =3,column=1)
days.insert(0,30)

#volitilty
Volatility_name = Label(root,text = 'Volatility', bg='white', fg = 'black', font = 25, padx = 30 ) 
Volatility_name.grid(row=4,column=0, padx=3,pady=3) 

Volatility = Entry(root, fg = 'red', bg ='black', borderwidth = 5, font = 25, width = 23)
Volatility.grid(row =4,column=1)
Volatility.insert(0,0.02)

#multyplier 
multiplier_name = Label(root,text = 'Multiplier', bg='white', fg = 'black', font = 25, padx = 30 ) 
multiplier_name.grid(row=5,column=0, padx=3,pady=3)

multiplier = Entry(root, fg ='red', bg ='black', borderwidth = 5, font = 25, width = 23)
multiplier.grid(row =5,column=1)
multiplier.insert(0,10)
    
root.bind('<return>',BS_Calculator())

'-----------------------------------------------------------------------------'

calculate_btn = Button(root,
                       text='Calculate', 
                       fg = 'red', 
                       bg ='orange', 
                       font = 25,
                       command=BS_Calculator) 

calculate_btn.grid(row=6,column=1,pady=6)

'-----------------------------------------------------------------------------'

price = Label(frame1,
              text = "Price", 
              font=25,
              fg='white',
              bg = 'purple')

price.grid(row=1,column=2)

delta = Label(frame1,
              text = "Delta", 
              font=25,
              fg ='white',
              bg = 'purple')

delta.grid(row=2,column=2)

gamma = Label(frame1,
              text = "Gamma", 
              font=25,
              fg ='white',
              bg = 'purple')

gamma.grid(row=3,column=2)

vega = Label(frame1,
              text = "Vega", 
              font=25,
              fg ='white',
              bg = 'purple')

vega.grid(row=4,column=2)

theta = Label(frame1,
              text = "Theta", 
              font=25,
              fg ='white',
              bg = 'purple')

theta.grid(row=5,column=2)

rho = Label(frame1,
              text = "Rho", 
              font=25,
              fg ='white',
              bg = 'purple')

rho.grid(row=6,column=2)

'-----------------------------------------------------------------------------'

root.mainloop()












