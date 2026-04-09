import json, urllib.request
u = "https://pjxynrqzydcxstnpsbtg.supabase.co"
v = u + "/storage/v1/object/public/video-matting/"
v += "temp/bc175e3e-dd17-42e2-81b1-dd92b200173f/input.webm"
k = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
k += "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBqeH"
k += "lucnF6eWRjeHN0bnBzYnRnIiwicm9sZSI6InNlcn"
k += "ZpY2Vfcm9sZSIsImlhdCI6MTczMTk4MTYyNiwiZXh"
k += "wIjoyMDQ3NTU3NjI2fQ.S1v0czmrqPqSKx7LYMB"
k += "cmRBXnEFmmiaKz2tXJOHPXtI"
d = json.dumps({"video_url": v, "bg_mode": "blur", "supabase_url": u, "supabase_key": k}).encode()
req = urllib.request.Request("http://localhost:18000/", data=d, headers={"Content-Type": "application/json"})
print(urllib.request.urlopen(req, timeout=600).read().decode())
