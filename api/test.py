import extenso as extenso

def test(number):
    number = extenso.converter(number)
    return number

if __name__ == '__main__':
   print(test("0"))