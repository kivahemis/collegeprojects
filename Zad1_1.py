for i in range(100, 1000):
    digs = [int(j) for j in str(i)]
    if digs[2] > digs[1] and digs[1] > digs[0]:
        print(i)


#Program zwraca liczby od 100 do 999. Zwraca tylko te liczby w których cyfry posortowane są rosnąco