
from ali_miao.persister import hist_data_persister

def run():
    hist = hist_data_persister.HistDataPersister()
    while True:
        hist.persist()

if __name__ == "__main__":
    run()