#python -m venv myvenv
#myvenv\Scripts\activate
#pip install bs4
#pip install requests

import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")


status_code=req.status_code
if status_code==200:
    #página exitosa
    print("Acceso a la página exitoso")
    html=BeautifulSoup(req.text,"html.parser")
    
    
    """
    """
    tabla=html.find('table',{'class':'rgMasterTable'})
    for c in range(6):
        moneda=tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(c)})
        lstTipoCambioDolar=moneda.find_all('td')
        #print(lstTipoCambioDolar)
        strNombreMoneda=lstTipoCambioDolar[0].text
        strValorCompra=lstTipoCambioDolar[1].text
        strValorVenta=lstTipoCambioDolar[2].text
        print(strNombreMoneda+"|"+strValorCompra+"|"+strValorVenta)
        f=open('cambio.txt','a')
        f.write(strNombreMoneda+"|"+strValorCompra+"|"+strValorVenta+"\n")
        f.close()
    
    
    
    
else:
    print("Error al acceder a la página"+str(status_code))