from help import is_prime

primes = [p for p in range(10000) if is_prime(p)]

for p1 in primes:
    if p1 == 2:
        continue
    for p2 in primes:
        if p2 <= p1:
            continue
        if not (is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))):
            continue
        for p3 in primes:
            if p3 <= p2:
                continue
            if not (
                is_prime(int(str(p1) + str(p3)))
                and is_prime(int(str(p3) + str(p1)))
                and is_prime(int(str(p2) + str(p3)))
                and is_prime(int(str(p3) + str(p2)))
            ):
                continue
            for p4 in primes:
                if p4 <= p3:
                    continue
                if not (
                    is_prime(int(str(p1) + str(p4)))
                    and is_prime(int(str(p4) + str(p1)))
                    and is_prime(int(str(p2) + str(p4)))
                    and is_prime(int(str(p4) + str(p2)))
                    and is_prime(int(str(p3) + str(p4)))
                    and is_prime(int(str(p4) + str(p3)))
                ):
                    continue
                for p5 in primes:
                    if p5 <= p4:
                        continue
                    if not (
                        is_prime(int(str(p1) + str(p5)))
                        and is_prime(int(str(p5) + str(p1)))
                        and is_prime(int(str(p2) + str(p5)))
                        and is_prime(int(str(p5) + str(p2)))
                        and is_prime(int(str(p3) + str(p5)))
                        and is_prime(int(str(p5) + str(p3)))
                        and is_prime(int(str(p4) + str(p5)))
                        and is_prime(int(str(p5) + str(p4)))
                    ):
                        continue
                    print(p1, p2, p3, p4, p5)
                    print(p1 + p2 + p3 + p4 + p5)
                    exit()
