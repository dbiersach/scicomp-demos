# measure_sample.py

from lab_utils import TriadSensor, DataFile

sensor = TriadSensor()

file_name = "UnknownSample"
dataFile = DataFile(file_name)

readings = sensor.get_spectra()
dataFile.save(readings)
