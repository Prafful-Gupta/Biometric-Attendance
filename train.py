import cognitive_face as CF
from global_variables import personGroupId

Key = '302c3ee94b5a4a2896c7d2baecb035bb'
CF.Key.set(Key)
CF.util.DEFAULT_BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'


res = CF.person_group.train(personGroupId)
print res
