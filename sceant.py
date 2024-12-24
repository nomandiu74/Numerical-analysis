def f(x):
    return x**3-x-1

e=0.001

def sceant(a,b):

    if f(a)*f(b)>0:
        print("Invalid input.")
    else:
        iter=1

        c=a-(f(a)*(b-a))/(f(b)-f(a))

        while abs(f(c))>e:

            c=c=a-(f(a)*(b-a))/(f(b)-f(a))
            print("n={};a={:.4f};b={:.4f};c={:.4f};f(c)={:.4f}".format(iter,a,b,c,f(c)))

            if abs(f(c))<e:
                break
            else:
                a=b
                b=c
            iter+=1
        print("Approx. root is:{:.4f}".format(c))
    
a=float(input("Enter the values of a:"))
b=float(input("Enter the values of b:"))

sceant(a,b)