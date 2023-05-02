from datetime import date

today = date.today()



print("-------------------WELCOME TO RESTURAANT--------------------------")
print ("                      MENU CARD                                 ")
print("DATE:  ",today)


list = '''
S.N     Items             price(rs)
1.      Naan              Rs.10/pie. 
2.      Chicken Tikka     RS.200/plate
3.      Butter chicken    Rs.500/plate
4.      Ice Cream         Rs.20/cup  
'''


option = str(input("To see the Menu enter, yes or y::  "))
if(option == 'yes' or option == 'y'):
    print(list)
    
   
print('-'*40)

print('-'*40)
#c = int(input("enter your choice :  "))

q1 = int(input('qty : --->naan : '))
q2 = int(input('qty: ---->chicken tikka :'))
q3 = int(input('qty: --->butter chicken :'))
q4 = int(input('qty : ---->ice cream : '))

 #for each qty   
p1 = q1 * 10   #calculating price for naan 
p2 = q1 * 200
p3 = q3 * 500
p4 = q3 * 20

total = p1 + p2 + p3 + p4
print("total is bill is Rs. ",total)  #total bill of that costumer
print("-"*40)

gst = total * 0.05 # 8% gst
total_1 = total + gst #after gst
print("Total bill after 5% gst is Rs. ",total_1)

print("-----------------Thank you---------------")
    


    

#get invoice name from user

print("\n please enter your invoice name  ")

invoice_name = str(input("Enter invoice name: "))
#make invoice name as PDF
invoice_name1 = invoice_name + '.pdf'

print("\n!!! THANK YOU || PLEASE VISIT AGAIN !!!\n")

#code for PDF generation

from fpdf import FPDF               #FPDF is a library in Python, it is used for pdf file document generation. I
class PDF(FPDF):
    def header(self):
        
        #logo
        self.image('royal.jpg',10,8,30)    
        #font
        self.set_font('times', 'B', 30)
        #padding
        self.cell(60)
        #title
        self.cell(70,25, " ROYAL RESTURANT  ", border=False, ln=False, align='C')
        #line break
        self.ln(30)
    
pdf = PDF('p', 'mm', 'letter')
pdf.add_page()   
pdf.set_auto_page_break(auto=True, margin = 15)
pdf.set_font('times', '', 20)
pdf.cell(0,10,ln=True)
#pdf.cell(0,0,'NAME: {:s}'.format(invoice_name), border = False , ln = False )



pdf.cell(0,10," S.N    ITEMS                 COSTS              qty      Total(Rs.)", border = True , ln = True)

pdf.cell(0,10," 1.     Naan                         Rs.10             {:d}          {:d}".format(q1,p1), border = True ,ln = True , )

pdf.cell(0,10," 2.     chicken tikka            Rs.200          {:d}          {:d}".format(q2,p2), border = True , ln =True)

pdf.cell(0,10," 3.     Butter Chicken         Rs.500          {:d}           {:d}".format(q3,p3), border = True , ln =True )

pdf.cell(0,10," 4.     Ice cream                  Rs.20             {:d}          {:d}".format(q4,p4), border = True , ln =True )



pdf.cell(0,10,"the total bill is :  Rs. %2d"%total,border = True , ln = True)
pdf.cell(0,10,"\nThe total bill including GST is  Rs. %2d" %total_1, border = True, ln = True )


pdf.cell(0,10,'------------THANK YOU----------------',border = False , ln = 2, align = 'C')
pdf.output(invoice_name1)    
