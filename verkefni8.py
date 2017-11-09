#Sighvatur Sveinsson
import os
from bottle import route, run, template, request, response, redirect


#Local storage og Session storage eru geymslur fyrir gögn á vefsíðum t.d myndir og texti.
#Session storage getur geymt allt að 5MB af gögnum og eyðir þeim þegar vefsíðunni er lokað.
#Local storage getur geymt allt að 10MB af gögnum og er ekki með expiration date.
#WebSQL er API notað til að fá og senda upplýsingar á gagnagrunn sem notar SQL
#IndexedDB er API fyrir client-side geymslu fyrir mikið af skipulögðum gögnum
#Cache er tímabundin geymsla gagna á vefsíðum til að flýta fyrir.
#Cookies eru merktir textastrengir sem koma frá serverinum og eru geymdir í browserinum hjá notanda.


@route('/')
def root():
    username = request.get_cookie("account")
    if username:
        return template('template2.tpl')
    else:
        return template('template.tpl')

@route('/login', method = 'POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'admin' and password == 'admin':
        response.set_cookie("account", username)
        return redirect('/')
    else:
        return "Login failed."

@route('/logout', method = 'POST')
def logout():
    response.set_cookie("account","",expires=0)
    return redirect('/')

run(host='0.0.0.0', port=os.environ.get("PORT"))