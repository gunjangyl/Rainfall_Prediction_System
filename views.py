from django.shortcuts import render
import pickle
import os


# Create your views here.
def index(req):
    res=''
    if req.method=='POST':
        pn=float(req.POST['pn'])
        maxt=float(req.POST['maxt'])
        mint=float(req.POST['mint'])
        ws=float(req.POST['ws'])
        path=os.path.dirname(__file__)
        model=pickle.load(open(os.path.join(path,'rfp.pkl'),'rb'))
        X=[pn,maxt,mint,ws]
        res=str(model.predict([X])[0])
    return render(req,"index.html",{'res':res})

def predict(req):
    return index(req)