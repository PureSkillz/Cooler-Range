def cooler_range(first, *args, **kwargs):
    answer = [i for i in range(first)]
    try:
        answer = [i for i in range(first, args[0])]
        answer = [i for i in range(first, args[0], kwargs["step"])]
        answer = [el for el in answer if el not in kwargs["skip"]]
    finally:
        return answer


print(cooler_range(5))
print(cooler_range(3, 10))
print(cooler_range(0, 10, step=2))
print(cooler_range(0, 10, step=1, skip=[1, 5, 7]))
