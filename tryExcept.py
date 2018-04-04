while True:
    try:
        num = int(input("whats your fav num?\n"))
        print(num/num)
        break
    except ValueError:
        print("make sure you enter number")
    except ZeroDivisionError:
        print("devide by zero")
    except:
        break
    finally:
        print("loop complete")