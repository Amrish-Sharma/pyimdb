def bookRegister():
    
    bid = en1.get()
    title = en2.get()
    subject = en3.get()
    author = en4.get()
    status = en5.get()
    status = status.lower()
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+subject+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)