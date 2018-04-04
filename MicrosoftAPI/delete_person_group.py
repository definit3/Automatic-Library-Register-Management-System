import cognitive_face as CF
import sys
import urllib3
urllib3.disable_warnings()

Key = 'db85583701c04bf08f8a9fb9a9290b78'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.delete(str(sys.argv[1]))
print res
