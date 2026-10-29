import json,urllib.request,urllib.error,concurrent.futures,threading
from pathlib import Path
import os, urllib.parse
root=Path.cwd(); cfg={'demoLogin':os.environ['WORKSPHERE_TEST_LOGIN'],'demoPassword':os.environ['WORKSPHERE_TEST_PASSWORD']}; base=os.environ.get('WORKSPHERE_TEST_BASE_URL','http://127.0.0.1:18080/api/v1').rstrip('/')
parsed=urllib.parse.urlsplit(base)
if parsed.scheme!='http' or parsed.hostname not in ('127.0.0.1','localhost') or parsed.username or parsed.password: raise RuntimeError('Baseline probe is restricted to local test environments')
def call(path,data=None,token=None):
 headers={'Content-Type':'application/json'}
 if token:headers['Authorization']='Bearer '+token
 req=urllib.request.Request(base+path,data=json.dumps(data).encode() if data is not None else None,headers=headers,method='POST' if data is not None else 'GET')
 try:
  with urllib.request.urlopen(req,timeout=20) as r:return r.status,json.loads(r.read() or b'{}')
 except urllib.error.HTTPError as e:
  return e.code,{}
def login():
 s,b=call('/auth/login',{'login':cfg['demoLogin'],'password':cfg['demoPassword'],'deviceName':'audit-isolated-session'})
 if s!=200:raise RuntimeError('Local audit login unavailable: '+str(s))
 return b['data']
res={}
a=login();res['before_logout_profile_http']=call('/me',token=a['accessToken'])[0];res['logout_http']=call('/auth/logout',{'refreshToken':a['refreshToken']},a['accessToken'])[0];res['after_logout_old_access_profile_http']=call('/me',token=a['accessToken'])[0]
a=login();barrier=threading.Barrier(2)
def refresh(_):
 barrier.wait(); return call('/auth/refresh',{'refreshToken':a['refreshToken']})
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: results=list(ex.map(refresh,range(2)))
res['same_refresh_two_parallel_statuses']=[x[0] for x in results]
for status,body in results:
 if status==200:
  d=body['data'];call('/auth/logout',{'refreshToken':d['refreshToken']},d['accessToken'])
output=root/'work/runtime-probes.json'; output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(res,indent=2),encoding='utf-8')
print(json.dumps(res))
