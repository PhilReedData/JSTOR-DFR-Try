class DfR(object):
	"""A bundle of data downloaded from JSTOR Data for Research
	"""

	OK = "OK"

	def __init__(self, dataPath):
		self.dataPath = dataPath

	def getDataPath(self):
		return self.dataPath