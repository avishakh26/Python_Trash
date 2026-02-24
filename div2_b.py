import sys
input = sys.stdin.buffer.read

def main():
    data = input().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        X = data[idx].decode(); idx += 1

        # Bitmask: bit0 = parity-0 reachable, bit1 = parity-1 reachable
        # Parity = (number of chars taken from left) % 2
        # char from left  = 'a' if parity==0, 'b' if parity==1
        # char from right = 'a' if (n-1-i+parity)%2==0, else 'b'
        possible = 1  # start: l=0, parity=0

        for i in range(n):
            xi = X[i]
            new_possible = 0

            if possible & 1:  # parity 0 reachable
                cl = 'a'
                cr = 'a' if (n - 1 - i) % 2 == 0 else 'b'
                if xi == '?' or xi == cl: new_possible |= 2  # take left -> parity flips to 1
                if xi == '?' or xi == cr: new_possible |= 1  # take right -> parity stays 0

            if possible & 2:  # parity 1 reachable
                cl = 'b'
                cr = 'a' if (n - i) % 2 == 0 else 'b'
                if xi == '?' or xi == cl: new_possible |= 1  # take left -> parity flips to 0
                if xi == '?' or xi == cr: new_possible |= 2  # take right -> parity stays 1

            possible = new_possible
            if not possible:
                break

        out.append("YES" if possible else "NO")

    sys.stdout.write("\n".join(out) + "\n")

main()