import time
import sys

kalimat = [
    "kalau disuruh memilih 4 digit angka, aku bakal memilih angka 1467",
    "tau kah kenapa?",
    "karna kamu satu-satunya alasan aku berjuang",
    "i want to be fourever with you",
    "rasa sayangku pada mu selalu enambah terus...",
    "dan kamu adalah tujuanku di masa depan :)"
]

def ketik_per_huruf(teks, jeda=0.05):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(jeda)
    sys.stdout.write('\n')
    sys.stdout.flush()

for baris in kalimat:
    ketik_per_huruf(baris)
    time.sleep(1.5)
