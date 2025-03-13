import sqlite3

from flask import Flask,render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('employee.html')

@app.route('/emp',methods=['GET','POST'])
def emp_data():
    if request.method=='POST':
        no=request.form.get('eno')
        name=request.form.get('ename')
        sal=request.form.get('esal')
        ed={'eno':no,'ename':name,'esal':sal}

        con=sqlite3.connect('empdb.db')
        cursor=con.cursor()
        cursor.execute("create table if not exists emp(eno int(10),ename varchar(10),esal float(10))")
        cursor.execute("insert into emp (eno,ename,esal)values(?,?,?)",(int(no),name,float(sal)))
        con.commit()
        con.close()
        return render_template('empData.html')

@app.route('/list')
def get_all_record():
    con = sqlite3.connect('empdb.db')
    cursor = con.cursor()
    cursor.execute("select * from emp")
    data=cursor.fetchall()
    con.close()
    return render_template('emplist.html',emplist=data)

@app.route('/delete/<int:id>')
def delete_record(id):
    con = sqlite3.connect('empdb.db')
    cursor = con.cursor()
    cursor.execute("delete from emp where eno=?",(id,))
    con.commit()
    con.close()
    return redirect('/list')


@app.route('/update/<int:id>',methods=['GET','POST'])
def update_record(id):
    con = sqlite3.connect('empdb.db')
    cursor = con.cursor()
    cursor.execute("select * from emp where eno=?",(id,))
    data =cursor.fetchone()

    if request.method == 'POST':
        no = request.form.get('eno')
        name = request.form.get('ename')
        sal = request.form.get('esal')
        ed = {'eno': no, 'ename': name, 'esal': sal}

        con = sqlite3.connect('empdb.db')
        cursor = con.cursor()
        cursor.execute("update emp set ename=?,esal=? where eno=?", (name,float(sal),int(no)))
        con.commit()
        con.close()
        return redirect('/list')

    return render_template('update.html',dt=data)


app.run(debug=True)