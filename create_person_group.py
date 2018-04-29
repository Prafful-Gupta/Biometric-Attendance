import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = '302c3ee94b5a4a2896c7d2baecb035bb'
CF.Key.set(Key)
CF.util.DEFAULT_BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print personGroupId + " already exists."
        sys.exit()

res = CF.person_group.create(personGroupId)
print res
