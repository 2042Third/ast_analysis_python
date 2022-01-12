def main():
  a = [1,2,3,4,5,6]
  # b = [10,20,30,40,50,60]
  yield [i for i in a]
  # print("hello")
  yield [i for i in b]
  # for i in a:
  #   yield a

  return


if __name__ == '__main__':
  a , b = main()
  # print([i for i in a])
  print(a)