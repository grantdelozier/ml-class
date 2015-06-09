import os
import sys
import csv


if 'MLCLASS' in os.environ:
	print "MLCLASS variable set to ", os.environ['MLCLASS']
else:
	print >> sys.stderr, "WARNING: $MLCLASS environment variable not set"

class FeatureMatrix:

	x_names = None
	y_names = None
	X = []
	Y = []

	def __init__(self):
		self.X = []
		self.Y = []

	def add_csv(self, csv_path, delimiter=',', headers=True, labeled=False):
		with open(csv_path, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=delimiter)
			if headers == True:
				header_line = reader.next()
				x_names = header_line
			else:
				header_line = []
			if labeled == False:
				self.X = [row for row in reader]
			else:
				for row in reader:
					Y.append(row[0])
					X.append(row[1:])





def main():
	"blah"

if __name__ == "__main__":
	main()