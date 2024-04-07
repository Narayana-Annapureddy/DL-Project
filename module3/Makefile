all: module3.1.3

extract_data:
	python3 task3.py;
    
scrap:
	python3 task1.py;

module3.1.2:
	python3 task3_2.py;

module3.1.3:
	@start=$$(date +%s%N); \
    python3 mapper.py ../data/worldometers_countrylist.txt | python3 combiner.py | sort -n | python3 reducer.py