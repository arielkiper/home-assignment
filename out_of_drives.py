"""
@Author: Ariel Kipervasser
@Purpose: This program should implement the OutOfDrives assignment which
receives an input file containing drives in CSV format and prints the
information of the ones in offline state
@Date: 29/05/19
@Version: 1.0
@file: out_of_drives.py
"""

import csv
import re

# My local path of the input.txt file
INPUT_FILE = r"C:\Users\User\Desktop\outbrain\input.txt"
OFFLINE = " Offline"


class Drive:
	"""
	A class used to represent a drive
	"""
	def __init__(self, name, state, size, free_space, path, log_size, port,
				 guid, cluster_uuid, disks, dare):
		"""
		:param name: The name of the drive
		:type: C{str}
		:param state: The state of the drive - offline/online
		:type: C{str}
		:param size: The size of the drive (in MB)
		:type: C{str}
		:param free_space: The free space of the drive (in MB)
		:type: C{str}
		:param path: The path of the drive
		:type: C{str}
		:param log_size: The size of the log (in MB)
		:type: C{str}
		:param port: The port of the drive
		:type: C{str}
		:param guid: The guid of the drive
		:type: C{str}
		:param cluster_uuid: The cluster_uuid of the drive
		:type: C{str}
		:param disks: The paths of the disks
		:type: C{str}
		:param dare: The dare of the drive
		:type: C{str}
		"""
		self.name = name
		self.state = state
		self.size = size
		self.free_space = free_space
		self.path = path
		self.log_size = log_size
		self.port = port
		self.guid = guid
		self.cluster_uuid = cluster_uuid
		self.disks = disks
		self.dare = dare


def out_of_drives():
	"""
	Read from an input file all the drives information, and print the offline
	drives information in a human readable manner
	"""
	with open(INPUT_FILE) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		offline_drives = []
		line_number = 1
		# Adding the offline drives info to a offline drives list
		for row in csv_reader:
			if row[1] == OFFLINE:
				# Extracting the information with regex
				try:
					drive_name = re.findall(r".+name (\w+)", row[0])[0]
					drive_state = re.findall(r"\S+", row[1])[0]
					drive_size = re.findall(r" size (\d+ .+)", row[2])[0]
					drive_free_space = re.findall(r" free (\d+ .+)", row[3])[0]
					drive_path = re.findall(r" path (.+)", row[4])[0]
					drive_log_size = re.findall(r" log (\d+ .+)", row[5])[0]
					drive_port = re.findall(r" port (\d+)", row[6])[0]
					drive_guid = re.findall(r" guid (.+)", row[7])[0]
					drive_cluster_uuid = re.findall(r" clusterUuid (.+)", row[8])[0]
					drive_disks = re.findall(r" disks (.+)", row[9])[0]
					drive_dare = re.findall(r"\d", row[10])[0]
				# One of the fields does not match the regex pattern
				except IndexError:
					print("One of the fields in the input file in line {} is not "
						  "in the correct pattern. This drive will not be printed"
						  " and you should check it manually".format(line_number))
				else:
					offline_drives.append(Drive(
						drive_name, drive_state, drive_size, drive_free_space,
						drive_path, drive_log_size, drive_port, drive_guid,
						drive_cluster_uuid, drive_disks, drive_dare))
			line_number += 1

		print("Found ({}) offline drives:".format(len(offline_drives)))
		for drive in offline_drives:
			drive_info = (
				drive.name, drive.size, drive.free_space, drive.path,
				drive.log_size, drive.port, drive.guid, drive.cluster_uuid,
				drive.disks, drive.dare
			)
			print("""
	name: {}
	\t size: {}
	\t free: {}
	\t path: {}
	\t log: {}
	\t port: {}
	\t guid: {}
	\t clusterUuid: {}
	\t disks: {}
	\t dare: {}
			""".format(*drive_info))


if __name__ == "__main__":
	out_of_drives()
