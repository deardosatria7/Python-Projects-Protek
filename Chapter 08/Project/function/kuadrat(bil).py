def kuadrat(bil):
    try:
        output = []
        for data in bil:
            data1 = data**2
            output.append(data1)
        print (output)
    except (TypeError):
        print("Data harus berbentuk angka (integer)")

