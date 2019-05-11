#!/usr/bin/python
import json, sys, hashlib
from fractions import gcd


def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

#TODO -- n1 and n2 share p or q?
def is_waldo(n1, n2):

    print "###############################################"
    result = False

    #your code start here
    p = 0
    p = gcd(n1, n2)
    if p > 1:
        result = True

    #your code ends here

    return result



def euclid_algorithm(x,y):
    if y == 0:
        return 1,0,x
    else:
        a,b,q = euclid_algorithm(y,x%y)
        a,b = b,(a - x/y*b)
        return a,b,q



#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0
    p = 0
    q = 0
    #your code starts here

    if is_waldo(n1,n2):
        p = gcd(n1,n2)
        q = n1/p
                
        print 1./float(e)

        tmp = (p - 1) * (q -1)
        print tmp


        d = (1./float(e) % (tmp))
        d,x,y = euclid_algorithm(e,(p-1) * (q-1))
        if d < 0:
            d = ( p - 1 ) * ( q - 1) + d
    print d

    #your code ends here

    return d

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys4student.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
