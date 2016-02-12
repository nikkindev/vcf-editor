import glob,os
os.chdir(os.path.expanduser('~/Desktop/vcf_editor/contacts'))

dumpfile=open('dump.DAT','r+')
fnum_res=dumpfile.read()
fnum=0
for file in glob.glob('*'):
    fnum=fnum+1
    dumpfile.seek(0)
    dumpfile.truncate()
    dumpfile.write(str(fnum))
    if fnum<int(fnum_res):
        continue    

    fhand=open(file)
    print fhand.read()
    fname=raw_input('\nFirst name : ')
    lname=raw_input('Last name : ')
    if (len(lname)!=0):
        name=fname+' '+lname
    else:
        name=fname
    newfile='new/'+name+'.vcf'
    fnew=open(newfile,'w+')
    fnew.write('\nBEGIN:VCARD\nVERSION:2.1\nN:')
    fnew.write(lname+';')
    fnew.write(fname+';;;\n')
    fnew.write('FN:'+fname+' '+lname+'\n')
    while True:
        choice=raw_input('Enter your choice\n1. Cell\n2. Home\n3. Work\n')
        if choice=='1':
            num=raw_input('Enter Cell no. : ')
            fnew.write('TEL;CELL:'+num+'\n')
        elif choice=='2':
            num=raw_input('Enter Home no. : ')
            fnew.write('TEL;HOME:'+num+'\n')
        elif choice=='3':
            num=raw_input('Enter Work no. : ')
            fnew.write('TEL;WORK:'+num+'\n')
        else:
            break

    email=raw_input('Email : ')
    if len(email)!=0:
        fnew.write('EMAIL;PREF;HOME:'+email+'\n')
    fnew.write('END:VCARD')
    fhand.close()
    fnew.close()

dumpfile.close()
