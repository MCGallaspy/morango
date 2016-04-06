from copy import deepcopy

class Node:
	# Morango instance ID 
	instanceID = None
	# Counter position
	counter = None
	# Sync data structure	
	syncDataStructure = None

	def __init__( self, instanceID, counter, syncDataStructure ):
		self.instanceID = instanceID
		self.counter = counter
		self.syncDataStructure = deepcopy(syncDataStructure)

	def updateCounter ( self, increment ) :
		self.counter = self.counter + increment

	def calcFSIC (self, filter ) :
		#Calculate which of the filters are a superset of the filter and insert in list l
		superSetFilters = ["*"]
		fsic = []
		for i in superSetFilters :
			if len(fsic) :
				print "CalcFSIC : Reached here! Needs to be filled!"		
			else :
				fsic = deepcopy(self.syncDataStructure[i])
			return fsic

	def updateSyncDS (self, change, filter) :
		if self.syncDataStructure.has_key(filter) :
			temp = self.syncDataStructure[filter]
			for key,value in changes.items() :
				if temp.has_key(key) :
					temp[key] = value	
				else :
					temp[key] = value
		else :
			self.syncDataStructure[filter] = change


	def calcDiffFSIC ( self, fsic1, fsic2 ) :
		"""
		fsic1 : Local FSIC copy
		fsic2 : Remote FSIC copy
		Calculates changes, according to the new data which local device has
		"""
		changes = {}
		for key,value in fsic1.items() :
			if fsic2.has_key(key) and fsic2[key] < fsic1[key]:
				changes[key] = fsic1[key]
			else :
				changes[key] = value
		return changes

	def printNode ( self ) :
		"""
		Pretty-printing all the variable values residing in Node object
		"""
		print "Instance ID :" + str(self.instanceID)
		print "Counter value :" + str(self.counter)
		print "syncDataStructure :"
		for key, value in self.syncDataStructure.items() :
			print key + ":"
			print value 
			
