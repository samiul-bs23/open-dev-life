nums = ['id1', 'id4', 'id2', 'id10', 'id3', 'id20']

nums = sorted(nums, key=lambda x: int(x[2:]))
print(nums)
