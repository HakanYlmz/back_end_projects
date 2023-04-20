from flask.sessions import SessionMixin, SessionInterface
import uuid
import json
from itsdangerous import Signer,BadSignature,want_bytes

class myInterface(dict,SessionMixin):

    def __init__(self, initial= None,sessionId = None):
        self.initial = initial
        self.sessionId = sessionId
        super(myInterface,self).__init__(initial or ())


    def __setitem__(self,key,value):
        super(myInterface,self).__setitem__(key,value)
    

    def __getitem__(self,item):
        print("getitem")
        return super(myInterface,self).__getitem__(item)
    

    def __delitem__(self,key):
        super(myInterface,self).__delitem__(key)


class mySessionInterface(SessionInterface):
    session_class = myInterface
    salt = "yilmaz"
    container = dict()

    def __init__(self):
        pass
    
    def open_session(self, app:"Flask", request : "Request"):
        signedSession_id =  request.cookies.get(app.session_cookie_name)

        if not signedSession_id:
            session_id = str(uuid.uuid4())
            return self.session_class(sessionId=session_id)
        signer = Signer(app.secret_key,salt = self.salt)

        try:
            session_id = signer.unsign(signedSession_id).decode()
        except BadSignature:
            session_id = str(uuid.uuid4())
            return self.session_class(sessionId=session_id)
        

        initialSessionValueAsJson = self.container.get(session_id)
        try:
            initialSessionValue = json.loads(initialSessionValueAsJson)
        except:
            session_id = str(uuid.uuid4())
            return self.session_class(sessionId=session_id)
        return self.session_class(initialSessionValue,sessionId=session_id)
        
        return self.session_class(sessionId=session_id)
        
    

    def save_session(self, app, session :SessionMixin, response: "Response"):
        sessionAsJson = json.dumps(dict(session))
        self.container[session.sessionId] = sessionAsJson
        signer = Signer(app.secret_key,salt=self.salt)
        signedSessionId = signer.sign(want_bytes(session.sessionId))
        response.set_cookie(app.session_cookie_name,signedSessionId)
        