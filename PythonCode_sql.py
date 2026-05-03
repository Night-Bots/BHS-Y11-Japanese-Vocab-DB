import sqlite3
DATABASE = 'Y11 Japanese Vocab.db'
space = " "
UnderScore = "_"

def Print_result():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    while True:
        try:
            Word = input("Word: ")
            if Word.lower() == "all":
                c.execute(f"""
                          SELECT *
                          FROM Vocab
                          order by Vocab.English desc;
                          """)
                print(f"{space*1}{UnderScore*55}")
                print(f"|ID{space*3}|English{space*20}|Japanese{space*18}|")
                print(f"|{UnderScore*5}|{UnderScore*25}|{UnderScore*26}|")
                for result in c.fetchall():
                    print(f"|{result[0]:<3}|{result[1]:<30}|{result[2]:<15}")
                    print(f"|{UnderScore*3}|{UnderScore*30}|{UnderScore*30}|")
            else:
                c.execute(f"""
                          SELECT *
                          FROM Vocab
                          WHERE Vocab.English LIKE '%{Word}%'
                          OR Vocab.Japanese LIKE '%{Word}%'
                          Or Vocab.Vocab_ID Like '%{Word}%'
                          order by Vocab.English desc;
                        """)
                print(f"{space*1}{UnderScore*57}")
                print(f"|ID{space*2}|English{space*18}|Japanese{space*18}|")
                print(f"|{UnderScore*4}|{UnderScore*25}|{UnderScore*26}|")
                for result in c.fetchall():
                    print(f"|{result[0]:<4}|{result[1]:<25}|{result[2]:<30}")
                    print(f"|{UnderScore*4}|{UnderScore*25}|{UnderScore*30}|")
        except:
            print("Error")

if __name__ == "__main__":
    Print_result()