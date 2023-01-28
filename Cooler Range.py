def cooler_range(first, *args, **kwargs):
    answer = [i for i in range(first)]
    try:
        end = args[0]
        answer = [i for i in range(first, end)]
        
        step = args[1]
        answer = [i for i in range(first, end, step)]
        
        skip = args[2]
        answer = [el for el in answer if el not in skip]
    finally:
        return answer


print(cooler_range(5))
print(cooler_range(3, 10))
print(cooler_range(0, 10, 2))
print(cooler_range(0, 10, 1, [1, 5, 7]))
