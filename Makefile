all: run

split_data:
	python3 chunker.py


run:
	@start=$$(date +%s%N); \
    (python3 mapper.py chunks/chunk_1.txt | python3 combiner.py )| sort -n | python3 reducer.py