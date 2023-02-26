from tkinter import *
from tkinter import filedialog
import random
import time

root = Tk()
root.geometry('1600x700+0+0')
root.title('Mining Economic Evaluation Tool')
Tops = Frame(root, bg='light blue', width=1600, height=50, relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root, width=1300, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=('aria', 30, 'bold'), text='Mining Economic Evaluation Tool', fg='Steel Blue', bd=10,
                anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 20), text=localtime, fg='steel blue', anchor='w')
lblinfo.grid(row=1, column=0)
oreproductiongrade = {}
inputdatavalue = {}
sustaining_capexdirectCAPEX = {}
ore_production = []
average_grade = []
sustaining_capex = []
direct_indirect_capex = []
BinomialexpansionFinalvalueglobalvariable = []
NPVfinalvalueglobal = []

print(BinomialexpansionFinalvalueglobalvariable)


def Binomial_Expansion():
    class AutoScrollbar(Scrollbar):
        def set(self, low, high):
            if float(low) <= 0.0 and float(high) >= 1.0:
                self.tk.call("grid", "remove", self)
            else:
                self.grid()
            Scrollbar.set(self, low, high)

        def pack(self, **kw):
            raise (TclError, "pack cannot be used with \
                     this widget")

        def place(self, **kw):
            raise (TclError, "place cannot be used  with \
                     this widget")

    rv2 = Tk()
    rv2.geometry('1600x700+0+0')
    rv2.title('Binomial Expansion Value')

    verscrollbar = AutoScrollbar(rv2)
    verscrollbar.grid(row=0, column=1,
                      sticky=N + S)
    horiscrollbar = AutoScrollbar(rv2,
                                  orient=HORIZONTAL)
    horiscrollbar.grid(row=1, column=0,
                       sticky=E + W)
    canvas = Canvas(rv2, yscrollcommand=verscrollbar.set,
                    xscrollcommand=horiscrollbar.set)

    def on_vertical(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    def on_horizontal(event):
        canvas.xview_scroll(int(-1 * (event.delta / 120)), 'units')

    canvas.grid(row=0, column=0, sticky=N + S + E + W)

    canvas.bind_all('<MouseWheel>', on_vertical)
    canvas.bind_all('<Shift-MouseWheel>', on_horizontal)

    verscrollbar.config(command=canvas.yview)
    horiscrollbar.config(command=canvas.xview)
    rv2.grid_rowconfigure(0, weight=1)
    rv2.grid_columnconfigure(0, weight=1)
    frame = Frame(canvas)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(1, weight=1)

    def exit2():
        rv2.destroy()

    Binomial_expansion_value_odd_year = []
    Binomial_expansion_value_even_year = []

    BinomialExpansionFinalValue = []

    uf = []
    df = []
    uf_nth_expansion = []
    df_nth_expansion = []
    uf.clear()
    df.clear()

    Binomial_expansion_value_odd_year.clear()
    Binomial_expansion_value_even_year.clear()
    uf_nth_expansion.clear()
    df_nth_expansion.clear()
    m = int(Y.get())
    po = float(V.get())
    bp = float(Bp.get())
    up_factor = 2.718 ** (po / 100)
    uf.append(round(up_factor, 8))
    print(uf[0])
    Label(frame, font=('aria', 13, 'bold'), text='Upper Factor: ' + str(uf[0]), fg='steel blue', bd=10,
          anchor='w').grid(row=1, column=1)
    down_factor = 1 / up_factor
    df.append(round(down_factor, 8))
    print(df[0])
    Label(frame, font=('aria', 13, 'bold'), text='Down Factor: ' + str(df[0]), fg='steel blue', bd=10,
          anchor='w').grid(row=2, column=1)

    if m > 0:
        for k in range(0, m, 1):
            a = float(bp * up_factor ** k)
            uf_nth_expansion.append(round(a, 3))
            b = float(bp * down_factor ** k)
            df_nth_expansion.append(round(b, 3))

    print(uf_nth_expansion)
    print(df_nth_expansion)

    for q in range(len(uf_nth_expansion)):
        if q == 0:
            Binomial_expansion_value_even_year.append(uf_nth_expansion[q])
            BinomialExpansionFinalValue.append(Binomial_expansion_value_even_year[:])
        elif q == 1:
            Binomial_expansion_value_odd_year.append(uf_nth_expansion[q])
            Binomial_expansion_value_odd_year.append(df_nth_expansion[q])
            BinomialExpansionFinalValue.append(Binomial_expansion_value_odd_year[:])

        else:
            if q % 2 == 1:
                Binomial_expansion_value_odd_year.append(uf_nth_expansion[q])
                Binomial_expansion_value_odd_year.append(df_nth_expansion[q])
                BinomialExpansionFinalValue.append(Binomial_expansion_value_odd_year[:])

            else:
                Binomial_expansion_value_even_year.append(uf_nth_expansion[q])
                Binomial_expansion_value_even_year.append(df_nth_expansion[q])
                BinomialExpansionFinalValue.append(Binomial_expansion_value_even_year[:])

    print(BinomialExpansionFinalValue)
    FinalValue = []
    FinalValue.clear()
    for a in range(len(BinomialExpansionFinalValue)):
        if len(BinomialExpansionFinalValue[a]) > 0:
            FinalValue.append(BinomialExpansionFinalValue[a])
            BinomialexpansionFinalvalueglobalvariable.append(BinomialExpansionFinalValue[a])
    print(FinalValue)
    print(BinomialexpansionFinalvalueglobalvariable)
    for k in range(1, len(FinalValue) + 1, 1):
        Label(frame, font=('aria', 13, 'bold'), text='Year: ' + str(k), fg='steel blue', bd=10,
              anchor='w').grid(row=4, column=k + 1)
    for l in range(len(FinalValue)):
        for m in range(len(FinalValue[l])):
            Label(frame, font=('aria', 13, 'bold'), text=str(FinalValue[l][m]), fg='steel blue', bd=10,
                  anchor='w').grid(row=m + 5, column=l + 2)

    Button(frame, padx=16, pady=16, bd=10, fg='red', font=('ariel', 13, 'bold'), width=20, text='BACK HOME',
           bg='powder blue', command=exit2).grid(row=m + 6, column=m + 3)

    canvas.create_window(0, 0, anchor=NW, window=frame)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    rv2.mainloop()


def inputdata(index, frame, rowNo, key):
    inputvalue = []
    inputvalue.clear()
    i = 0
    for i in range(index):
        txtCri = Entry(frame, font=('ariel', 13, 'bold'), bd=6, insertwidth=3, bg='powder blue', justify='right')
        txtCri.grid(row=i + 1, column=rowNo + 1)
        inputvalue.append(txtCri)
    inputdatavalue.update({key: inputvalue})


def yearlyinputwindows():
    class AutoScrollbar(Scrollbar):
        def set(self, low, high):
            if float(low) <= 0.0 and float(high) >= 1.0:
                self.tk.call("grid", "remove", self)
            else:
                self.grid()
            Scrollbar.set(self, low, high)

        def pack(self, **kw):
            raise (TclError, "pack cannot be used with \
                     this widget")

        def place(self, **kw):
            raise (TclError, "place cannot be used  with \
                     this widget")

    rv = Tk()
    rv.geometry('1600x700+0+0')
    rv.title('Yearly Input Windows')

    verscrollbar = AutoScrollbar(rv)
    verscrollbar.grid(row=0, column=1,
                      sticky=N + S)
    horiscrollbar = AutoScrollbar(rv,
                                  orient=HORIZONTAL)
    horiscrollbar.grid(row=1, column=0,
                       sticky=E + W)
    canvas = Canvas(rv, yscrollcommand=verscrollbar.set,
                    xscrollcommand=horiscrollbar.set)

    canvas.grid(row=0, column=0, sticky=N + S + E + W)

    verscrollbar.config(command=canvas.yview)
    horiscrollbar.config(command=canvas.xview)
    rv.grid_rowconfigure(0, weight=1)
    rv.grid_columnconfigure(0, weight=1)
    frame = Frame(canvas)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(1, weight=1)

    def exit1():
        rv.destroy()

    yearvalue = []
    wastproduction = []
    oreproduction = []
    grade = []
    sustainCAPEX = []
    directindirectCAPEX = []
    directindirectCAPEX.clear()
    sustainCAPEX.clear()
    grade.clear()
    oreproduction.clear()
    wastproduction.clear()
    yearvalue.clear()
    y1 = int(Y.get())
    yearvalue.append(y1)


    keyinput = ['a', 'b', 'c', 'd', 'e']
    valueinput = [y1, y1, y1, y1, y1]
    maindictionary = dict(zip(keyinput, valueinput))
    print(maindictionary)
    rowNo = 0
    index = 0

    Label(frame, font=('aria', 13, 'bold'), text='Year ', fg='steel blue', bd=10, anchor='w').grid(row=index, column=0)
    Label(frame, font=('aria', 13, 'bold'), text='Waste Production (tonnes)', fg='steel blue', bd=10, anchor='w').grid(
        row=index, column=1)
    Label(frame, font=('aria', 13, 'bold'), text='Average Ore Production (tonnes)', fg='steel blue', bd=10,
          anchor='w').grid(row=index, column=2)
    Label(frame, font=('aria', 13, 'bold'), text='Average Grade % ', fg='steel blue', bd=10, anchor='w').grid(row=index,
                                                                                                              column=3)
    Label(frame, font=('aria', 13, 'bold'), text='Sustainable CAPEX (US$)', fg='steel blue', bd=10, anchor='w').grid(
        row=index, column=4)
    Label(frame, font=('aria', 13, 'bold'), text='Direct & Indirect CAPEX (US$) ', fg='steel blue', bd=10,
          anchor='w').grid(row=index, column=5)
    for r in range(1, yearvalue[0] + 1, 1):
        Label(frame, font=('aria', 13, 'bold'), text='Year' + str(r), fg='steel blue', bd=10, anchor='w').grid(row=r,
                                                                                                               column=0)
    for key in maindictionary:
        if maindictionary[key] > 0:
            inputdata(maindictionary[key], frame, rowNo, key)
            rowNo = rowNo + 1
    print(inputdatavalue)

    Button(frame, padx=16, pady=16, bd=10, fg='green', font=('ariel', 13, 'bold'), width=15, text='CALCULATION',
           bg='powder blue', command=lambda: npvCalculation(frame, key)).grid(row=yearvalue[0] + 4, column=1)
    Button(frame, padx=16, pady=16, bd=10, fg='green', font=('ariel', 13, 'bold'), width=15, text='RESULTS',
           bg='powder blue').grid(row=yearvalue[0] + 4, column=2)
    Button(frame, padx=16, pady=16, bd=10, fg='red', font=('ariel', 13, 'bold'), width=15, text='BACK HOME',
           bg='powder blue', command=exit1).grid(row=yearvalue[0] + 4, column=3)

    canvas.create_window(0, 0, anchor=NW, window=frame)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    rv.mainloop()


def npvCalculation(frame, key):
    class AutoScrollbar(Scrollbar):
        def set(self, low, high):
            if float(low) <= 0.0 and float(high) >= 1.0:
                self.tk.call("grid", "remove", self)
            else:
                self.grid()
            Scrollbar.set(self, low, high)

        def pack(self, **kw):
            raise (TclError, "pack cannot be used with \
                     this widget")

        def place(self, **kw):
            raise (TclError, "place cannot be used  with \
                     this widget")

    rv3 = Tk()
    rv3.geometry('1600x700+0+0')
    rv3.title('Binomial Expansion Value')

    verscrollbar = AutoScrollbar(rv3)
    verscrollbar.grid(row=0, column=1,
                      sticky=N + S)
    horiscrollbar = AutoScrollbar(rv3,
                                  orient=HORIZONTAL)
    horiscrollbar.grid(row=1, column=0,
                       sticky=E + W)
    canvas = Canvas(rv3, yscrollcommand=verscrollbar.set,
                    xscrollcommand=horiscrollbar.set)

    def on_vertical(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    def on_horizontal(event):
        canvas.xview_scroll(int(-1 * (event.delta / 120)), 'units')

    canvas.grid(row=0, column=0, sticky=N + S + E + W)

    canvas.bind_all('<MouseWheel>', on_vertical)
    canvas.bind_all('<Shift-MouseWheel>', on_horizontal)

    verscrollbar.config(command=canvas.yview)
    horiscrollbar.config(command=canvas.xview)
    rv3.grid_rowconfigure(0, weight=1)
    rv3.grid_columnconfigure(0, weight=1)
    frame = Frame(canvas)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(1, weight=1)

    def exit3():
        rv3.destroy()

    inputrankvalue = []
    revenue = []
    oreproduction = []
    averagegrade = []
    sustainableCAPEX = []
    directindirectCAPEX = []
    wasteproduction = []
    wasteproduction.clear()
    revenue.clear()
    oreproduction.clear()
    averagegrade.clear()
    sustainableCAPEX.clear()
    directindirectCAPEX.clear()
    inputrankvalue.clear()
    print(inputdatavalue)
    for v in inputdatavalue.values():
        inputrankvalue.append(v)
    print(inputrankvalue)
    print(len(inputrankvalue))
    print(len(inputrankvalue[0]))
    for i in range(1):
        for j in range(len(inputrankvalue[0])):
            wasteproduction.append(inputrankvalue[i][j])
    print(wasteproduction)
    print(len(wasteproduction))
    for a in range(1):
        for b in range(len(inputrankvalue[1])):
            oreproduction.append(inputrankvalue[a + 1][b])
    print(oreproduction)
    print(len(oreproduction))
    for c in range(1):
        for d in range(len(inputrankvalue[2])):
            averagegrade.append(inputrankvalue[c + 2][d])
    print(averagegrade)
    print(len(averagegrade))
    for e in range(1):
        for f in range(len(inputrankvalue[3])):
            sustainableCAPEX.append(inputrankvalue[e + 3][f])
    print(sustainableCAPEX)
    print(len(sustainableCAPEX))
    for l in range(1):
        for m in range(len(inputrankvalue[4])):
            directindirectCAPEX.append(inputrankvalue[l + 4][m])
    print(directindirectCAPEX)
    print(len(directindirectCAPEX))
    recovery = float(R.get())
    for m in range(len(oreproduction)):
        b = float(oreproduction[m].get()) * float(averagegrade[m].get()) * (recovery / 100) * 1000 / 100
        revenue.append(round(b, 3))
    print(revenue)
    print(len(BinomialexpansionFinalvalueglobalvariable))
    print(BinomialexpansionFinalvalueglobalvariable)
    finalrevenue = []   



    
    finalrevenue.clear()


    extraAppend = []
    

    for k in range(len(BinomialexpansionFinalvalueglobalvariable)):
        kk = 0
    
        while kk <= k:
            temptotalfr = []
            
            for a in range(len(oreproduction -k)):
                temptotalfr.extend(extraAppend)
                tempfr = (BinomialexpansionFinalvalueglobalvariable[k][kk]) * revenue[a+k]
                temptotalfr.append(round(tempfr,3))
            if kk == 0:    
                extraAppend.append(temptotalfr[k])
            finalrevenue.append(temptotalfr)
            kk =kk+1
        
    
    yesfinalrevenue = []
    exactfinalrevenue = []
    yesfinalrevenue.clear()
    exactfinalrevenue.clear()

    for q in range(len(finalrevenue)):
        if len(finalrevenue[q]) > 0:
            exactfinalrevenue.append(finalrevenue[q])
    print(exactfinalrevenue)
    print(len(exactfinalrevenue))
    operatingcost = float(Toc.get())
    finalcashflow = []
    for i in range(len(exactfinalrevenue)):
        cashflow = []
        for j in range(len(exactfinalrevenue[i])):
            cf = exactfinalrevenue[i][j] - float(oreproduction[j].get()) * operatingcost - float(
                sustainableCAPEX[j].get()) - float(directindirectCAPEX[j].get())
            cashflow.append(cf)
        finalcashflow.append(cashflow)
    print(finalcashflow)
    sumfinalcashflow = []
    for i in range(len(finalcashflow)):
        sumcashflow = []
        a = 0
        for j in range(len(finalcashflow[i])):
            a = a + finalcashflow[i][j]
            sumcashflow.append(a)
        sumfinalcashflow.append(sumcashflow)
    print(sumfinalcashflow)
    royalitiesamount = []
    royalities = float(Rt.get())
    for i in range(len(finalcashflow)):
        royalitiesamount1 = []
        for j in range(len(finalcashflow[i])):
            if finalcashflow[i][j] > 0 and sumfinalcashflow[i][j] > 0:
                a = finalcashflow[i][j - 1] * royalities / 100
                if a <= 0:
                    b = sumfinalcashflow[i][j] * royalities / 100
                    royalitiesamount1.append(round(b, 3))
                else:
                    c = finalcashflow[i][j] * royalities / 100
                    royalitiesamount1.append(round(c, 3))
            else:
                d = 0
                royalitiesamount1.append(d)
        royalitiesamount.append(royalitiesamount1)

    print(royalitiesamount)
    totaltaxes = []
    countrytaxrate = float(Ctr.get())
    statetaxrate = float(STr.get())
    for i in range(len(finalcashflow)):
        taxamount1 = []
        for j in range(len(finalcashflow[i])):
            if finalcashflow[i][j] > 0:
                if finalcashflow[i][j] > 0 and sumfinalcashflow[i][j] > 0:
                    a = sumfinalcashflow[i][j - 1] * (countrytaxrate + statetaxrate) / 100
                    if a <= 0:
                        b = sumfinalcashflow[i][j] * (countrytaxrate + statetaxrate) / 100
                        taxamount1.append(round(b, 3))
                    else:
                        c = finalcashflow[i][j] * (countrytaxrate + statetaxrate) / 100
                        taxamount1.append(round(c, 3))

            else:
                g = 0
                taxamount1.append(g)
        totaltaxes.append(taxamount1)
    print(totaltaxes)
    discountrate = float(Dr.get())
    b = discountrate / 100
    DCF = []
    for i in range(len(finalcashflow)):
        dcf = []
        for j in range(len(finalcashflow[i])):
            a = (finalcashflow[i][j] - totaltaxes[i][j] - royalitiesamount[i][j]) / (1 + b) ** (j + 1)
            dcf.append(round(a, 3))
        DCF.append(dcf)
    print(DCF)
    NPV = []
    for a in range(len(DCF)):
        sum = 0
        for b in range(len(DCF[a])):
            sum = sum + DCF[a][b]
        NPV.append(round(sum, 3))
    print(NPV)
    print(len(NPV))
    NPVfinalvalue = []
    NPVyear1 = []
    NPVyear2 = []
    NPVyear3 = []
    NPVyear4 = []
    NPVyear5 = []
    NPVfinalvalue.clear()
    NPVyear1.clear()
    NPVyear2.clear()
    NPVyear3.clear()
    NPVyear4.clear()
    NPVyear5.clear()
    for i in range(len(NPV)):
        if (i == 0):
            NPVyear1.append(NPV[0])
            NPVfinalvalue.append(NPVyear1)
        if (i == 1 & 2):
            NPVyear2.append(NPV[1])
            NPVyear2.append(NPV[2])
            NPVfinalvalue.append(NPVyear2)
        if (i == 3 & 4 & 5):
            NPVyear3.append(NPV[3])
            NPVyear3.append(NPV[4])
            NPVyear3.append(NPV[5])
            NPVfinalvalue.append(NPVyear3)
        if (i == 6 & 7 & 8 & 9):
            NPVyear4.append(NPV[6])
            NPVyear4.append(NPV[7])
            NPVyear4.append(NPV[8])
            NPVyear4.append(NPV[9])
            NPVfinalvalue.append(NPVyear4)
        if (i == 10 & 11 & 12 & 13 & 14):
            NPVyear5.append(NPV[10])
            NPVyear5.append(NPV[11])
            NPVyear5.append(NPV[12])
            NPVyear5.append(NPV[13])
            NPVyear5.append(NPV[14])
            NPVfinalvalue.append(NPVyear5)
    print(NPVfinalvalue)
    print(len(NPVfinalvalue))

    NPVFinalValue = []
    NPVFinalValue.clear()
    for a in range(len(NPVfinalvalue)):
        if len(NPVfinalvalue[a]) > 0:
            NPVFinalValue.append(NPVfinalvalue[a])
            NPVfinalvalueglobal.append(NPVFinalValue[a])
    print(NPVFinalValue)
    print(NPVfinalvalueglobal)
    for k in range(1, len(NPVFinalValue) + 1, 1):
        Label(frame, font=('aria', 13, 'bold'), text='Year: ' + str(k), fg='steel blue', bd=10,
              anchor='w').grid(row=4, column=k + 1)
    for l in range(len(NPVFinalValue)):
        for m in range(len(NPVFinalValue[l])):
            Label(frame, font=('aria', 13, 'bold'), text=str(NPVFinalValue[l][m]), fg='steel blue', bd=10,
                  anchor='w').grid(row=m + 5, column=l + 2)

    Button(frame, padx=16, pady=16, bd=10, fg='red', font=('ariel', 13, 'bold'), width=20, text='BACK HOME',
           bg='powder blue', command=exit3).grid(row=m + 6, column=m + 3)

    canvas.create_window(0, 0, anchor=NW, window=frame)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    rv3.mainloop()


Bp = StringVar()  ###basket_price
Dp = StringVar()  ###discount_price
R = StringVar()  ###recovery
Toc = StringVar()  ###total_operation_cost
Dr = StringVar()  ###discount_rate
Rt = StringVar()  ###royalties
Ctr = StringVar()  ###country_tax_rate
STr = StringVar()  ###state_tax_rate
V = StringVar()  ###volatility
Y = StringVar()  ###year

vBp = 0
vDp = 0
vR = 0
vToc = 0
vDr = 0
vRt = 0
vCtr = 0
vSTr = 0
vV = 0
vY = 0


def exit():
    root.destroy()


def resetAll():
    ore_production.clear()
    average_grade.clear()
    sustaining_capex.clear()
    direct_indirect_capex.clear()
    oreproductiongrade.clear()
    labels()


def labels():
    Label(f1, font=('aria', 16, 'bold'), text='Basket Price', fg='steel blue', bd=10, anchor='w').grid(row=2, column=1)
    txtBp = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Bp, insertwidth=4, bg='powder blue',
                  justify='right')
    txtBp.grid(row=2, column=2)
    txtBp.delete('0', 'end')
    txtBp.insert(0, vBp)
    Label(f1, font=('aria', 16, 'bold'), text='Volatility Price', fg='steel blue', bd=10, anchor='w').grid(row=2,
                                                                                                           column=3)
    txtV = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=V, insertwidth=4, bg='powder blue',
                 justify='right')
    txtV.grid(row=2, column=4)
    txtV.delete('0', 'end')
    txtV.insert(0, vV)
    Label(f1, font=('aria', 16, 'bold'), text='Year', fg='steel blue', bd=10, anchor='w').grid(row=2, column=5)
    txtY = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Y, insertwidth=4, bg='powder blue',
                 justify='right')
    txtY.grid(row=2, column=6)
    txtY.delete('0', 'end')
    txtY.insert(0, vY)
    Label(f1, font=('aria', 16, 'bold'), text='Discount Rate', fg='steel blue', bd=10, anchor='w').grid(row=3, column=1)
    txtDp = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Dp, insertwidth=4, bg='powder blue',
                  justify='right')
    txtDp.grid(row=3, column=2)
    txtDp.delete('0', 'end')
    txtDp.insert(0, vDp)
    Label(f1, font=('aria', 16, 'bold'), text='Recovery', fg='steel blue', bd=10, anchor='w').grid(row=4, column=1)
    txtR = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=R, insertwidth=4, bg='powder blue',
                 justify='right')
    txtR.grid(row=4, column=2)
    txtR.delete('0', 'end')
    txtR.insert(0, vR)
    Label(f1, font=('aria', 16, 'bold'), text='Total Operation Cost', fg='steel blue', bd=10, anchor='w').grid(row=5,
                                                                                                               column=1)
    txtToc = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Toc, insertwidth=4, bg='powder blue',
                   justify='right')
    txtToc.grid(row=5, column=2)
    txtToc.delete('0', 'end')
    txtToc.insert(0, vToc)
    Label(f1, font=('aria', 16, 'bold'), text='Discount Rate', fg='steel blue', bd=10, anchor='w').grid(row=6,
                                                                                                        column=1)
    txtDr = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Dr, insertwidth=4, bg='powder blue',
                  justify='right')
    txtDr.grid(row=6, column=2)
    txtDr.delete('0', 'end')
    txtDr.insert(0, vDr)
    Label(f1, font=('aria', 16, 'bold'), text='Royalities', fg='steel blue', bd=10, anchor='w').grid(row=7,
                                                                                                     column=1)
    txtRt = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Rt, insertwidth=4, bg='powder blue',
                  justify='right')
    txtRt.grid(row=7, column=2)
    txtRt.delete('0', 'end')
    txtRt.insert(0, vRt)
    Label(f1, font=('aria', 16, 'bold'), text='Country Tax Rate', fg='steel blue', bd=10, anchor='w').grid(row=8,
                                                                                                           column=1)
    txtCtr = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=Ctr, insertwidth=4, bg='powder blue',
                   justify='right')
    txtCtr.grid(row=8, column=2)
    txtCtr.delete('0', 'end')
    txtCtr.insert(0, vCtr)
    Label(f1, font=('aria', 16, 'bold'), text='State Tax Rate', fg='steel blue', bd=10, anchor='w').grid(row=9,
                                                                                                         column=1)
    txtSTr = Entry(f1, font=('ariel', 16, 'bold'), bd=6, textvariable=STr, insertwidth=4, bg='powder blue',
                   justify='right')
    txtSTr.grid(row=9, column=2)
    txtSTr.delete('0', 'end')
    txtSTr.insert(0, vSTr)


labels()

Button(f1, padx=5, pady=5, bd=5, fg='black', font=('ariel', 15, 'bold'), width=15, text='Binomial Expansion',
       bg='powder blue', command=Binomial_Expansion).grid(row=4, column=4)
Button(f1, padx=5, pady=5, bd=5, fg='black', font=('ariel', 15, 'bold'), width=15, text='Yearly Input',
       bg='powder blue', command=yearlyinputwindows).grid(row=4, column=6)
Button(f1, padx=5, pady=5, bd=5, fg='black', font=('ariel', 15, 'bold'), width=15, text='Result',
       bg='powder blue').grid(row=11, column=1)
Button(f1, padx=5, pady=5, bd=5, fg='black', font=('ariel', 15, 'bold'), width=15, text='Reset',
       bg='powder blue', command=resetAll).grid(row=11, column=2)
Button(f1, padx=5, pady=5, bd=5, fg='black', font=('ariel', 15, 'bold'), width=15, text='Exit',
       bg='powder blue', command=exit).grid(row=11, column=3)

Label(f1, font=('aria', 16, 'bold'), text='      ', fg='steel blue', bd=10, anchor='w').grid(row=3, column=3)
Label(f1, font=('aria', 16, 'bold'), text='      ', fg='steel blue', bd=10, anchor='w').grid(row=3, column=3)
Label(f1, font=('aria', 16, 'bold'), text='      ', fg='steel blue', bd=10, anchor='w').grid(row=3, column=6)
Label(f1, font=('aria', 16, 'bold'), text='      ', fg='steel blue', bd=10, anchor='w').grid(row=3, column=8)
Label(f1, font=('aria', 16, 'bold'), text='      ', fg='steel blue', bd=10, anchor='w').grid(row=6, column=9)
Label(f1, font=('aria', 16, 'bold'), text='  .   ', fg='white', bd=10, anchor='w').grid(row=6, column=4)

root.mainloop()


