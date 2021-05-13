def get_list_of_stopwords():
    stopwords = []
    with open("/home/jovyan/SubFiles/stop.txt", "r") as file_:
        for line in file_:
            stopwords.append(line.rstrip())
    return stopwords
