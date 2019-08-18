nums = collections.defaultdict(list)
for i in range(2):
 j = input(f'Введите {i + 1}-е hex число: ')
 nums[i + 1] = list(j)
summ = [int(''.join(i), 16) for i in nums.values()]
print(f'Сумма введенных чисел: {list(hex(sum(summ)).upper())}')
nums2 = [int(''.join(i), 16) for i in nums.values()]
print(f'Произведение введенных чисел : {list(hex(nums2[0] * nums2[1]).upper())}')