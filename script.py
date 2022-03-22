import json
import os
import time
from modified_simulation import *

def main(abr):
	BUFFLENS = [2, 4, 6, 8, 10]
	traces = os.listdir('./synthetic_trace_for_configmap')
	
	abr_dict = {}
	abr_dict["mpc"] = False
	abr_dict["hyb"] = False
	abr_dict["bola"] = False
	abr_dict[abr] = True

	result_arr = []
	
	for trace in traces:
		print("Doing trace: " + trace)
		for bufflen in BUFFLENS:
			try:
				print("Bufflen: " + str(bufflen))

				result = simulation(trace, bufflen, abr_dict["mpc"], abr_dict["hyb"], abr_dict["bola"])

				if (result["buftime"] == 0):
					result["bufflen"] = bufflen
					result_arr.append(result)
					break

				if (bufflen == 10):
					print("BUFFLENS ARRAY EXCEEDED")
			except Exception as e:
				print(e)
				continue

	result_file_name = abr + "_" + "result" + ".json"

	with open(result_file_name, 'w') as fout:
		json.dump(result_arr, fout)

main("mpc")
main("hyb")
main("bola")