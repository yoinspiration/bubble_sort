# 用冒泡排序算法进行从小到大排序
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        is_sorted = True

        # 每一轮都把较大的数放在靠后的位置
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if is_sorted:
            break

    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))
