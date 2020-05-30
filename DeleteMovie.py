def deleteBook():
    
    bid = en1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
    except:
        messagebox.showinfo("Check Credentials","Please check Book ID")
    
    print(bid)

    en1.delete(0, END)